"""Helpers for tracing an area from a source map, and for drawing a hatched area.

    deg = fit([((px, py), (lon, lat)), ...])   # an affine fit from source-map pixels to degrees
    pts = deg([(px, py), ...])
    hatched(m, pts, minus=[core_pts], colour="red")   # a lightly filled, hatched area
"""
import numpy as np
from shapely.geometry import Polygon
from matplotlib.patches import Polygon as MplPoly
import lib
from lib import smooth, FILL


def fit(pairs, show=True, quad=False):
    """Least-squares fit from pixels to degrees: affine, or quadratic (quad=True, for a source map
    in a curved projection; needs at least eight points). Prints the worst error, in degrees."""
    def terms(x, y):
        x, y = x / 1000.0, y / 1000.0
        return [x, y, 1.0, x * x, x * y, y * y] if quad else [x, y, 1.0]
    P = np.array([terms(x, y) for (x, y), _ in pairs])
    L = np.array([ll for _, ll in pairs], float)
    A, *_ = np.linalg.lstsq(P, L, rcond=None)
    if show:
        err = np.hypot(*(P @ A - L).T)
        print(f"fit: worst error {err.max():.2f} deg, mean {err.mean():.2f} deg")

    def deg(px):
        return [tuple(np.array(terms(x, y)) @ A) for x, y in px]
    return deg


def hatched(m, pts, minus=(), colour="red", alpha=0.16, hatch="//", edge=True):
    """An area drawn faintly and hatched, less any core areas given in minus, clipped to land."""
    poly = Polygon(smooth(pts, n=14, closed=True)).buffer(0)
    for c in minus:
        poly = poly.difference(Polygon(smooth(c, n=14, closed=True)).buffer(0))
    poly = poly.intersection(lib._land)
    fc = FILL.get(colour, colour)
    for p in getattr(poly, "geoms", [poly]):
        if p.is_empty or p.geom_type != "Polygon":
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
        m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=0, alpha=0.8, zorder=2.05, hatch=hatch))
        if edge:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=1.4, alpha=0.9, zorder=2.1))


def states(m, items, alpha=0.45, smooth_n=8):
    """Neighbouring areas that must not overlap: items is [(pts, colour), ...]; each is smoothed and
    clipped to the land, and any part already taken by an earlier item is cut away."""
    taken = None
    for pts, colour in items:
        poly = Polygon(smooth(pts, n=smooth_n, closed=True)).buffer(0).intersection(lib._land)
        if taken is not None:
            poly = poly.difference(taken)
        taken = poly if taken is None else taken.union(poly)
        fc = FILL.get(colour, colour)
        for p in getattr(poly, "geoms", [poly]):
            if p.is_empty or p.geom_type != "Polygon" or p.area < 1e-3:
                continue
            xy = np.array(p.exterior.coords)
            m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=1.8, alpha=0.95, zorder=2.1))
