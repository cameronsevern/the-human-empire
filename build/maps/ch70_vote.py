#!/usr/bin/env python3
"""Chapter 70: the decade in which women won the vote in national elections, country by country, on a
world map with Europe drawn larger below it. Modern borders (Natural Earth admin-0, as shipped with
geopandas), since the map is about countries.

Drawn for this chapter, which had no map. Years are those the chapter gives where it gives one (New
Zealand 1893, Australia 1902, Finland 1906, Norway 1913, Russia 1917, Germany, Austria, Poland, Britain
and Canada 1918, the United States 1920, France 1944, Switzerland 1971); for Italy and Japan the year the
law was made (1945; women first voted in 1946); the rest from the list of dates in English Wikipedia's
article "Women's suffrage" and the Inter-Parliamentary Union's table, used only where the date is not in
dispute. Countries where the answer depends on the definition (a vote first given only to some women,
or given by a colonial power and widened at independence), or where it is uncertain, are left unshaded:
among them Hungary, Portugal, Uruguay, South Africa, Pakistan, Indonesia and most of Africa.
"""
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Polygon as MplPoly, Patch
import geopandas as gpd
from shapely.affinity import translate
from shapely.ops import unary_union
import lib
from lib import Map, INK, PAPER, HALO

SCRATCH = os.environ.get("SCRATCH", "/tmp")
C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
C = C[C.name != "Antarctica"]

YEAR = {
    "New Zealand": 1893, "Australia": 1902, "Finland": 1906, "Norway": 1913,
    "Denmark": 1915, "Iceland": 1915, "Russia": 1917, "Estonia": 1918, "Latvia": 1918, "Lithuania": 1918,
    "Poland": 1918, "Germany": 1918, "Austria": 1918, "United Kingdom": 1918, "Ireland": 1918, "Canada": 1918,
    "Netherlands": 1919, "Sweden": 1919, "Luxembourg": 1919, "United States of America": 1920, "Czechia": 1920,
    "Slovakia": 1920, "Mongolia": 1924, "Ecuador": 1929,
    "Spain": 1931, "Sri Lanka": 1931, "Brazil": 1932, "Thailand": 1932, "Turkey": 1934, "Cuba": 1934,
    "Philippines": 1937, "France": 1944, "Italy": 1945, "Japan": 1945, "Venezuela": 1946, "Argentina": 1947,
    "Belgium": 1948, "Israel": 1948, "South Korea": 1948, "Chile": 1949, "China": 1949,
    "India": 1950, "Greece": 1952, "Bolivia": 1952, "Mexico": 1953, "Colombia": 1954, "Peru": 1955,
    "Egypt": 1956, "Paraguay": 1961, "Iran": 1963,
    "Switzerland": 1971, "Kuwait": 2005,
}
BANDS = [(1914, "#3d5a78", "before 1915"), (1929, "#5f86a8", "1915 to 1929"), (1949, "#93b0c8", "1930 to 1949"),
         (1969, "#c3d3e0", "1950 to 1969"), (9999, "#7d6a8f", "1970 and later")]


def colour(y):
    for top, c, _ in BANDS:
        if y <= top:
            return c


def shade(m):
    """Each dated country, filled with its band's colour, and every country's border drawn thinly."""
    geoms = {r["name"]: unary_union([translate(r.geometry, xoff=o) for o in m.offs]) for _, r in C.iterrows()}
    allc = unary_union(list(geoms.values()))
    for name, g in geoms.items():
        if name not in YEAR:
            continue
        others = allc.difference(g)
        area = g.buffer(0.5).intersection(m.land).difference(others).intersection(m.clip)
        for p in getattr(area, "geoms", [area]):
            if p.is_empty or p.geom_type != "Polygon" or p.area < 1e-3:
                continue
            m.ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=colour(YEAR[name]), ec="none",
                                   alpha=0.9, zorder=2))
    for name, g in geoms.items():
        b = g.intersection(m.clip).boundary.intersection(m.land.buffer(-0.15))
        for l in getattr(b, "geoms", [b]):
            if l.is_empty or l.geom_type != "LineString":
                continue
            xy = np.array(l.coords)
            m.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=0.9, zorder=2.2)


def tag(m, lon, lat, name, ha="center", fs=15):
    year = YEAR[name] if name in YEAR else None
    m.label(lon, lat, name.replace("United States of America", "United States").replace("United Kingdom", "Britain")
            + (f"\n{year}" if year else ""), size="small", colour=INK, fs=fs, ha=ha)


# ---------------------------------------------------------------- the world
w = Map(-168.0, 192.0, -56.0, 78.0, lakes=False)
shade(w)
for lon, lat, name in [(-102, 57, "Canada"), (-99, 39, "United States of America"), (-102, 25.5, "Mexico"),
                       (-52, -10, "Brazil"), (-63, -35, "Argentina"), (95, 63, "Russia"), (104, 33, "China"),
                       (78.5, 21, "India"), (153.5, 40, "Japan"), (134, -25, "Australia"), (170, -31.5, "New Zealand")]:
    tag(w, lon, lat, name, fs=16)
w.label(-130, 5, "Pacific\nOcean", size="sea", fs=18)
w.label(-30, 22, "Atlantic\nOcean", size="sea", fs=18)
w.label(80, -25, "Indian Ocean", size="sea", fs=18)
pw = os.path.join(SCRATCH, "ch70_world.png")
w.save(pw)

# ---------------------------------------------------------------- Europe, larger
EW = 9.9
e = Map(-11.0, 45.0, 35.0, 64.0, width=EW, lakes=False)
shade(e)
for lon, lat, name, ha in [(26.5, 62.3, "Finland", "center"), (9.0, 61.0, "Norway", "center"),
                           (15.6, 62.6, "Sweden", "center"), (-1.6, 52.6, "United Kingdom", "center"),
                           (10.2, 51.0, "Germany", "center"), (19.3, 52.2, "Poland", "center"),
                           (2.3, 46.6, "France", "center"), (-3.8, 39.8, "Spain", "center"),
                           (13.4, 42.3, "Italy", "left"), (33.5, 39.0, "Turkey", "center"),
                           (38.0, 56.5, "Russia", "center")]:
    tag(e, lon, lat, name, ha=ha)
e.ax.annotate("Switzerland\n1971", xy=(8.2, 46.8), xytext=(5.2, 41.3), fontsize=15, color=INK, ha="center",
              va="center", zorder=7, path_effects=HALO,
              arrowprops=dict(arrowstyle="-", color=INK, lw=1.2, shrinkA=14, shrinkB=2))
e.label(-6.5, 46.0, "Atlantic\nOcean", size="sea", fs=17)
e.label(18.0, 36.5, "Mediterranean Sea", size="sea", fs=17)
pe_ = os.path.join(SCRATCH, "ch70_europe.png")
e.save(pe_)

# ---------------------------------------------------------------- the key, beside Europe
ie = mpimg.imread(pe_)
kw = (1600 - ie.shape[1]) / 100.0
fig = plt.figure(figsize=(kw, ie.shape[0] / 100.0), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off")
handles = [Patch(fc=c, ec=c, alpha=0.9, label=t) for _, c, t in BANDS] + \
          [Patch(fc=lib.LAND, ec=lib.SHORE, label="not shaded:\ndate disputed\nor uncertain")]
leg = ax.legend(handles=handles, loc="center", fontsize=18, title="Women won the\nnational vote", title_fontsize=19,
                frameon=False, labelspacing=0.9, handlelength=2.2, handleheight=1.4)
pk = os.path.join(SCRATCH, "ch70_key.png")
fig.savefig(pk, dpi=100, facecolor=PAPER)
plt.close(fig)

# ---------------------------------------------------------------- put together
iw, ik = mpimg.imread(pw), mpimg.imread(pk)
paper = np.array([int(PAPER[i:i + 2], 16) / 255 for i in (1, 3, 5)] + [1.0])
if ik.shape[2] == 3:
    ik = np.dstack([ik, np.ones(ik.shape[:2])])
h = min(ie.shape[0], ik.shape[0])
row = np.hstack([ie[:h], ik[:h, :1600 - ie.shape[1]]])
gap = np.ones((14, 1600, 4)) * paper
out = np.vstack([iw, gap, row])
dest = os.path.join(lib.ROOT, "chapters/70-vote/images/map_vote.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
