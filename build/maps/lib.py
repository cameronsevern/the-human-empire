"""Shared code for the book's maps: one house style, large labels, readable at phone width.

    uv run --python 3.12 --with 'geopandas<1' --with matplotlib build/maps/<script>.py

Coastlines, rivers and lakes are Natural Earth (public domain), kept in build/maps/data.
A map is 1600 px wide. Nothing on it is smaller than about 26 px, so that it can still be
read when the page is shown 400 px wide. No distinction rests on colour alone: each region
carries its name, and routes and frontiers differ in line style.

    m = Map(west, east, south, north)            # degrees
    m.region([(lon, lat), ...], "red")           # a soft-edged area: a kingdom, an empire
    m.river("Nile")                              # by Natural Earth name
    m.city(lon, lat, "Ugarit", dx=1, dy=0)       # a dot and its name
    m.label(lon, lat, "HATTI", size="region")    # region | sea | land | small
    m.route([(lon, lat), ...], arrow=True)
    m.key([("red", "Roman land"), ...])          # only when names cannot sit on the map
    m.save("chapters/11-bronze/images/map_near_east.png")
"""
import os, warnings
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPoly, Rectangle, Patch
from matplotlib.lines import Line2D
from matplotlib import patheffects as pe
from shapely.geometry import box
warnings.filterwarnings("ignore")
import geopandas as gpd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(HERE, "data")

INK, PAPER, SOFT, ACC = "#2f2a26", "#faf6ee", "#7a7168", "#b5523b"
LAND, SEA, SHORE, WATER = "#e9dfc8", "#f4f0e6", "#a89c86", "#8fa9b8"
# region fills: muted, distinct in greyscale as well as in colour
FILL = {"red": "#c4654d", "gold": "#d9a441", "blue": "#5b84a6", "green": "#6f9a6a", "purple": "#8c6c9c",
        "brown": "#a07a52", "teal": "#4f9a94", "grey": "#8d857b", "pink": "#c98a9b", "olive": "#99974a"}
SIZE = {"region": 23, "sea": 17, "land": 17, "city": 16.5, "small": 15, "title": 19}

plt.rcParams["font.family"] = ["P052", "serif"]
HALO = [pe.withStroke(linewidth=4, foreground=PAPER)]

_land = _rivers = _lakes = None


def _load():
    global _land, _rivers, _lakes
    if _land is None:
        _land = gpd.read_file(os.path.join(DATA, "ne_50m_land")).geometry.unary_union
        _rivers = gpd.read_file(os.path.join(DATA, "ne_10m_rivers_lake_centerlines"))
        _lakes = gpd.read_file(os.path.join(DATA, "ne_50m_lakes"))


def smooth(pts, n=16, closed=False):
    """A Catmull-Rom curve through the points."""
    p = np.array(pts, float)
    if closed:
        p = np.vstack([p[-1], p, p[0], p[1]])
    else:
        p = np.vstack([p[0], p, p[-1]])
    out = []
    for i in range(1, len(p) - 2):
        for t in np.linspace(0, 1, n, endpoint=False):
            a, b, c, d = p[i - 1], p[i], p[i + 1], p[i + 2]
            out.append(0.5 * ((2 * b) + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t * t + (-a + 3 * b - 3 * c + d) * t ** 3))
    if not closed:
        out.append(p[-2])
    return np.array(out)


class Map:
    def __init__(self, west, east, south, north, width=16.0, lakes=True):
        _load()
        self.ext = (west, east, south, north)
        mid = np.radians((south + north) / 2)
        h = width * (north - south) / ((east - west) * np.cos(mid))     # true shape at the middle latitude
        self.fig = plt.figure(figsize=(width, h), dpi=100)
        ax = self.ax = self.fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(west, east); ax.set_ylim(south, north)
        ax.set_facecolor(SEA); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_edgecolor(INK); s.set_linewidth(1.8)
        self.clip = box(west - 2, south - 2, east + 2, north + 2)
        land = _land.intersection(self.clip)
        for p in getattr(land, "geoms", [land]):
            if p.is_empty or p.geom_type != "Polygon":
                continue
            ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=LAND, ec=SHORE, lw=0.8, zorder=1))
            for hole in p.interiors:
                ax.add_patch(MplPoly(np.array(hole.coords), closed=True, fc=SEA, ec=SHORE, lw=0.8, zorder=1.1))
        if lakes:
            span = east - west
            for _, r in _lakes.iterrows():
                g = r.geometry.intersection(self.clip)
                if g.is_empty or (r.get("scalerank", 0) or 0) > (1 if span > 60 else 3):
                    continue
                for p in getattr(g, "geoms", [g]):
                    if p.geom_type == "Polygon":
                        ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=SEA, ec=SHORE, lw=0.7, zorder=1.2))

    # ------------------------------------------------------------------ features
    def river(self, *names, lw=1.6):
        """Draw rivers by their Natural Earth names ("Nile", "Euphrates", "Tigris", "Danube"...)."""
        for name in names:
            rows = _rivers[_rivers["name"].fillna("").str.lower() == name.lower()]
            if rows.empty:
                rows = _rivers[_rivers["name_en"].fillna("").str.lower() == name.lower()]
            if rows.empty:
                print("no river named", name)
            for g in rows.geometry:
                g = g.intersection(self.clip)
                for line in getattr(g, "geoms", [g]):
                    if line.is_empty or line.geom_type != "LineString":
                        continue
                    xy = np.array(line.coords)
                    self.ax.plot(xy[:, 0], xy[:, 1], color=WATER, lw=lw, solid_capstyle="round", zorder=2.5)

    def region(self, pts, colour="red", alpha=0.42, edge=True, hatch=None, land_only=True, smooth_n=14):
        """A soft-cornered area through the given (lon, lat) points, clipped to the land."""
        from shapely.geometry import Polygon
        c = smooth(pts, n=smooth_n, closed=True)
        poly = Polygon(c).buffer(0)
        if land_only:
            poly = poly.intersection(_land)
        fc = FILL.get(colour, colour)
        for p in getattr(poly, "geoms", [poly]):
            if p.is_empty or p.geom_type != "Polygon":
                continue
            xy = np.array(p.exterior.coords)
            self.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2, hatch=None))
            if hatch:
                self.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=0, alpha=0.9, zorder=2.05, hatch=hatch))
            if edge:
                self.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=1.8, alpha=0.95, zorder=2.1))

    def line(self, pts, colour=INK, lw=2.4, style="-", curved=True):
        """A frontier, wall or road."""
        c = smooth(pts) if curved else np.array(pts, float)
        self.ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=lw + 2.4, solid_capstyle="round", zorder=3)
        self.ax.plot(c[:, 0], c[:, 1], color=FILL.get(colour, colour), lw=lw, ls=style, solid_capstyle="round", zorder=4)

    def route(self, pts, colour="red", lw=3.0, arrow=True, style="-"):
        c = smooth(pts)
        col = FILL.get(colour, colour)
        self.ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=lw + 2.6, solid_capstyle="round", zorder=3)
        end = -4 if arrow else None
        self.ax.plot(c[:end, 0], c[:end, 1], color=col, lw=lw, ls=style, solid_capstyle="round", zorder=4)
        if arrow:
            self.ax.annotate("", xy=c[-1], xytext=c[-8], zorder=5,
                             arrowprops=dict(arrowstyle="-|>,head_width=0.4,head_length=0.8", color=col, lw=lw, shrinkA=0, shrinkB=0))

    def city(self, lon, lat, name=None, dx=0.0, dy=0.0, ha=None, r=8, size="city", star=False, bold=False):
        """A dot with its name. dx, dy move the name, in degrees; ha is worked out from dx."""
        self.ax.plot(lon, lat, "*" if star else "o", ms=r * (1.9 if star else 1), mfc=INK, mec=PAPER, mew=1.4, zorder=6)
        if name:
            if ha is None:
                ha = "left" if dx > 0 else "right" if dx < 0 else "center"
            self.ax.text(lon + dx, lat + dy, name, ha=ha, va="center", fontsize=SIZE.get(size, size), color=INK,
                         fontweight="bold" if bold else "normal", zorder=7, path_effects=HALO)

    def label(self, lon, lat, text, size="region", colour=None, rot=0, ha="center", style=None, spaced=False):
        """A name on the map. region: bold capitals. sea: blue-grey italic. land: grey italic. small: grey."""
        if spaced:
            text = " ".join(text)
        kw = dict(region=dict(color=INK, fontweight="bold"),
                  sea=dict(color="#5d7686", style="italic"),
                  land=dict(color=SOFT, style="italic"),
                  small=dict(color=SOFT))[size if size in ("region", "sea", "land", "small") else "small"]
        if colour:
            kw["color"] = FILL.get(colour, colour)
        if style:
            kw["style"] = style
        self.ax.text(lon, lat, text, ha=ha, va="center", fontsize=SIZE.get(size, size), rotation=rot, zorder=7,
                     path_effects=HALO, linespacing=1.05, **kw)

    def note(self, lon, lat, text, size=16, ha="center"):
        """A boxed note: a date, a number, a short remark."""
        self.ax.text(lon, lat, text, ha=ha, va="center", fontsize=size, color=INK, zorder=8,
                     bbox=dict(boxstyle="round,pad=0.3", fc=PAPER, ec=INK, lw=1))

    def key(self, items, loc="lower left", title=None, size=16):
        """items: (colour or ("line", colour, style), text). Use only when names cannot sit on the map."""
        handles = []
        for what, text in items:
            if isinstance(what, tuple):
                handles.append(Line2D([0], [0], color=FILL.get(what[1], what[1]), lw=3, ls=what[2] if len(what) > 2 else "-", label=text))
            else:
                handles.append(Patch(fc=FILL.get(what, what), ec=FILL.get(what, what), alpha=0.6, label=text))
        leg = self.ax.legend(handles=handles, loc=loc, fontsize=size, title=title, title_fontsize=size + 1, frameon=True,
                             fancybox=False, edgecolor=INK, facecolor=PAPER, framealpha=1, borderpad=0.7, labelspacing=0.5)
        leg.set_zorder(9)
        leg.get_frame().set_linewidth(1.2)

    def scale(self, km, lon=None, lat=None):
        """A scale bar of the given length, by default at the lower right."""
        w, e, s, n = self.ext
        lat = s + (n - s) * 0.06 if lat is None else lat
        deg = km / (111.32 * np.cos(np.radians(lat)))
        lon = e - (e - w) * 0.05 - deg if lon is None else lon
        self.ax.plot([lon, lon + deg], [lat, lat], color=INK, lw=3, solid_capstyle="butt", zorder=8)
        self.ax.text(lon + deg / 2, lat + (n - s) * 0.022, f"{km:,} km", ha="center", va="bottom", fontsize=15, color=INK,
                     zorder=8, path_effects=HALO)

    def save(self, path):
        out = path if os.path.isabs(path) else os.path.join(ROOT, path)
        self.fig.savefig(out, dpi=100)
        plt.close(self.fig)
        print("wrote", out)
