"""A map in a true projection (for example a Lambert conic), for areas too large for the plain latitude and
longitude frame of lib.Map, such as the whole of the Soviet Union. Same house style as lib.Map. Every
method takes longitude and latitude; label offsets (dx, dy) are in kilometres.

    m = ProjMap("+proj=lcc +lat_1=52 +lat_2=68 +lon_0=92 +units=km", (x0, x1, y0, y1))   # frame in km
    m.region(geom_in_lonlat, "red")
    m.city(37.6, 55.8, "Moscow", dx=60, dy=40)
"""
import numpy as np
import pyproj
from shapely.geometry import box, Polygon
from shapely.ops import transform, unary_union
from matplotlib.patches import Polygon as MplPoly
import matplotlib.pyplot as plt
import lib
from lib import INK, PAPER, FILL, LAND, SEA, SHORE, WATER, SIZE, HALO, smooth


class ProjMap(lib.Map):
    def __init__(self, crs, frame, lonlat_box=(-180, 180, -90, 90), width=16.0):
        lib._load()
        self.T = pyproj.Transformer.from_crs("EPSG:4326", crs, always_xy=True)
        x0, x1, y0, y1 = frame
        self.ext = frame
        self.fig = plt.figure(figsize=(width, width * (y1 - y0) / (x1 - x0)), dpi=100)
        ax = self.ax = self.fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(x0, x1); ax.set_ylim(y0, y1)
        ax.set_facecolor(SEA); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_edgecolor(INK); s.set_linewidth(1.8)
        if hasattr(lonlat_box, "geom_type"):                  # a geometry: the part of the world to draw
            self.llclip = lonlat_box
        else:
            w, e, s_, n = lonlat_box
            self.llclip = box(w, s_, e, n)
        self.offs = [0]
        self.land = self.proj(lib._land.intersection(self.llclip))
        self.clip = box(x0 - 500, y0 - 500, x1 + 500, y1 + 500)
        for p in getattr(self.land, "geoms", [self.land]):
            if p.is_empty or p.geom_type != "Polygon":
                continue
            ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=LAND, ec=SHORE, lw=0.8, zorder=1))
            for hole in p.interiors:
                ax.add_patch(MplPoly(np.array(hole.coords), closed=True, fc=SEA, ec=SHORE, lw=0.8, zorder=1.1))
        for _, r in lib._lakes.iterrows():
            if (r.get("scalerank", 0) or 0) > 1:
                continue
            g = self.proj(r.geometry.intersection(self.llclip))
            for p in getattr(g, "geoms", [g]):
                if p.geom_type == "Polygon" and not p.is_empty:
                    ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=SEA, ec=SHORE, lw=0.7, zorder=1.2))

    # ---------------------------------------------------------------- projection
    def proj(self, g):
        return transform(self.T.transform, g)

    def xy(self, lon, lat):
        return self.T.transform(lon, lat)

    def _wrap(self, g):
        return self.proj(g.intersection(self.llclip))

    def _pts(self, pts):
        return [self.xy(*p) for p in pts]

    # ---------------------------------------------------------------- features, in lon/lat
    def area(self, pts, n=10):
        """A soft area through (lon, lat) points, as a projected geometry clipped to the land."""
        return self.proj(Polygon(smooth(pts, n=n, closed=True)).buffer(0)).intersection(self.land)

    def paint(self, geom, colour, alpha=0.42, hatch=None, lw=1.4, edge=None):
        """Fill a projected geometry (from area() or proj())."""
        fc = FILL.get(colour, colour)
        for p in getattr(geom, "geoms", [geom]):
            if p.is_empty or p.geom_type != "Polygon" or p.area < 50:
                continue
            xy = np.array(p.exterior.coords)
            self.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
            if hatch:
                self.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=edge or INK, lw=0, alpha=0.75,
                                          zorder=2.05, hatch=hatch))
            if lw:
                self.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=edge or fc, lw=lw, alpha=0.9, zorder=2.1))

    def line(self, pts, colour=INK, lw=2.4, style="-", curved=True):
        c = smooth(pts) if curved else np.array(pts, float)
        lib.Map.line(self, self._pts(c), colour, lw, style, curved=False)

    def route(self, pts, colour="red", lw=3.0, arrow=True, style="-"):
        c = smooth(pts)
        lib.Map.route(self, self._pts(c), colour, lw, arrow, style)

    def city(self, lon, lat, name=None, dx=0.0, dy=0.0, ha=None, r=8, size="city", star=False, bold=False):
        x, y = self.xy(lon, lat)
        lib.Map.city(self, x, y, name, dx, dy, ha, r, size, star, bold)

    def mark(self, lon, lat, marker="s", ms=13, colour=INK):
        lib.Map.mark(self, *self.xy(lon, lat), marker, ms, colour)

    def label(self, lon, lat, text, **kw):
        lib.Map.label(self, *self.xy(lon, lat), text, **kw)

    def scale(self, km, x=None, y=None):
        """A scale bar at projected position (x, y) in km; true near the standard parallels."""
        x0, x1, y0, y1 = self.ext
        x = x1 - (x1 - x0) * 0.05 - km if x is None else x
        y = y0 + (y1 - y0) * 0.06 if y is None else y
        self.ax.plot([x, x + km], [y, y], color=INK, lw=3, solid_capstyle="butt", zorder=8)
        self.ax.text(x + km / 2, y + (y1 - y0) * 0.022, f"{km:,} km", ha="center", va="bottom", fontsize=15,
                     color=INK, zorder=8, path_effects=HALO)
