#!/usr/bin/env python3
"""Chapter 88: Europe in 1955, after West Germany joined NATO (May) and the Warsaw Pact was signed (May), with
the neutral states, the iron curtain and divided Germany; below, Germany with West Berlin and the three air
corridors, and Berlin's four sectors.

Drawn for this chapter, which had no map. The alliances: NATO in 1955 (Britain, France, the Low Countries,
Norway, Denmark, Iceland, Italy, Portugal, Greece, Turkey and West Germany); the Warsaw Pact (the Soviet
Union, Poland, East Germany, Czechoslovakia, Hungary, Romania, Bulgaria, Albania); neutral: Sweden, Finland,
Switzerland, Ireland, and Austria, neutral from October 1955; in neither: Spain and Yugoslavia. Countries are
built from the modern ones (Natural Earth admin-0, 110 m, as shipped with geopandas), which matches 1955
closely enough at this scale, apart from Germany: the border between the two Germanies is drawn by hand
through Luebeck Bay, Lauenburg on the Elbe, Schnackenburg, Helmstedt, the Harz, Eschwege, the Rhoen and
Hof, after the maps in English Wikipedia's "Inner German border", roughly. The Saar, under French
administration until 1957, is not shown apart. The iron curtain is drawn as the land border of the Warsaw Pact
states with the rest of Europe, from the Baltic to the Black Sea.
The air corridors (each 20 miles wide) run from Berlin to Hamburg, Hanover (Bueckeburg) and Frankfurt, after
"Berlin air corridors" in English Wikipedia. The sectors of Berlin are built from the boroughs of 1920, from
OpenStreetMap: see berlin_sectors.py. Positions from English Wikipedia.
"""
import os, json
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from shapely.geometry import Polygon, LineString, Point, box, shape
from shapely.ops import unary_union, split
from matplotlib.patches import Polygon as MplPoly, Patch
from matplotlib.lines import Line2D
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth
from projmap import ProjMap

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
U = lambda names: unary_union([G[n] for n in names])

# ------------------------------------------------------------------ the two Germanies
border = [(10.88, 54.10), (10.88, 53.96), (10.95, 53.80), (10.76, 53.62), (10.84, 53.45), (10.60, 53.38),
          (10.85, 53.30), (11.20, 53.15), (11.58, 53.04), (11.38, 52.92), (11.05, 52.88), (10.76, 52.84),
          (10.93, 52.62), (11.03, 52.38), (10.95, 52.18), (10.78, 52.02), (10.62, 51.90), (10.56, 51.72),
          (10.40, 51.62), (10.22, 51.50), (10.05, 51.40), (9.92, 51.30), (10.05, 51.18), (10.03, 51.00),
          (9.94, 50.88), (9.96, 50.70), (10.07, 50.55), (10.40, 50.40), (10.73, 50.35), (10.86, 50.27),
          (11.16, 50.32), (11.40, 50.50), (11.60, 50.40), (11.88, 50.38), (12.10, 50.32)]
east_side = Polygon(border + [(13.0, 49.5), (16.5, 50.0), (16.5, 55.5), (10.88, 55.5)]).buffer(0)
west_germany = G["Germany"].difference(east_side)
east_germany = G["Germany"].intersection(east_side)

nato = unary_union([U(["United Kingdom", "France", "Belgium", "Netherlands", "Luxembourg", "Norway", "Denmark",
                       "Iceland", "Italy", "Portugal", "Greece", "Turkey"]), west_germany])
soviet = U(["Russia", "Belarus", "Ukraine", "Moldova", "Lithuania", "Latvia", "Estonia", "Georgia", "Armenia",
            "Azerbaijan", "Kazakhstan"])
pact = unary_union([soviet, U(["Poland", "Czechia", "Slovakia", "Hungary", "Romania", "Bulgaria", "Albania"]),
                    east_germany])
neutral = U(["Sweden", "Finland", "Switzerland", "Austria", "Ireland"])
yugoslavia = U(["Slovenia", "Croatia", "Bosnia and Herz.", "Serbia", "Montenegro", "Kosovo", "North Macedonia"])
neither = unary_union([yugoslavia, G["Spain"]])

# the iron curtain: the land border of the Warsaw Pact with the rest of Europe, Baltic to Black Sea
others = unary_union([nato, neutral, neither]).buffer(0.08)
curtain = pact.boundary.intersection(others).intersection(box(5, 38, 30, 54.05))
curtain = curtain.difference(Point(18.0, 54.0).buffer(0.01))

SCRATCH = os.environ.get("SCRATCH", "/tmp")
BLUE, RED, GREEN, GREY = FILL["blue"], FILL["red"], FILL["green"], "#a39a8e"


def paint(m, geom, colour, alpha=0.42, hatch=None, lw=1.3, minarea=0):
    fc = FILL.get(colour, colour)
    for p in getattr(geom, "geoms", [geom]):
        if p.is_empty or p.geom_type != "Polygon" or p.area < minarea:
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
        if hatch:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=0, alpha=0.9, zorder=2.05, hatch=hatch))
        if lw:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=lw, alpha=0.9, zorder=2.1))


def lines(m, geom, colour=INK, lw=3.6, style=(0, (3.2, 1.4)), halo=True, proj=None):
    for l in getattr(geom, "geoms", [geom]):
        if l.is_empty or l.geom_type != "LineString":
            continue
        xy = np.array((proj(l) if proj else l).coords)
        if halo:
            m.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=lw + 3, solid_capstyle="round", zorder=4.4)
        m.ax.plot(xy[:, 0], xy[:, 1], color=colour, lw=lw, ls=style, solid_capstyle="round", zorder=4.5)


# ================================================================ the main map: Europe
m = ProjMap("+proj=lcc +lat_1=40 +lat_2=62 +lat_0=52 +lon_0=15 +units=km", (-2250, 2450, -1880, 2120),
            lonlat_box=box(-35, 25, 70, 75))
LAND = m.land.buffer(0)
P = lambda g: m.proj(g.intersection(m.llclip)).buffer(0).intersection(LAND)
paint(m, P(nato), BLUE, minarea=50)
paint(m, P(pact), RED, minarea=50)
paint(m, P(neutral), GREEN, alpha=0.3, hatch="//", minarea=50)
paint(m, P(neither), GREY, alpha=0.35, minarea=50)
states = [west_germany, east_germany, soviet, yugoslavia, U(["Czechia", "Slovakia"])] + [G[n] for n in [
    "United Kingdom", "France", "Belgium", "Netherlands", "Luxembourg", "Norway", "Denmark", "Italy", "Portugal",
    "Greece", "Turkey", "Poland", "Hungary", "Romania", "Bulgaria", "Albania", "Sweden", "Finland",
    "Switzerland", "Austria", "Ireland", "Spain"]]
for g in states:
    for p in getattr(g, "geoms", [g]):
        xy = np.array(m.proj(p.intersection(m.llclip)).exterior.coords) if not p.intersection(m.llclip).is_empty and p.intersection(m.llclip).geom_type == "Polygon" else None
        if xy is not None:
            m.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=1.2, zorder=2.3)
lines(m, curtain, proj=m.proj)
# the border between the two Germanies (a line of its own, part of the curtain)
lines(m, LineString(smooth(border, n=6)), proj=m.proj)
x, y = m.xy(13.35, 52.5)
m.ax.plot(x, y, "o", ms=13, mfc=BLUE, mec=INK, mew=1.6, zorder=6)
m.ax.text(x + 45, y - 30, "West Berlin", fontsize=16.5, ha="left", va="top", color=INK, zorder=7,
          path_effects=HALO)
m.city(37.62, 55.75, "Moscow", dx=60, dy=55)
m.city(14.42, 50.09, "Prague", dx=0, dy=60)
m.city(19.04, 47.50, "Budapest", dx=0, dy=60)

m.label(2.0, 46.6, "NATO", fs=26, colour="#2f4f6a")
m.label(38.0, 51.0, "WARSAW PACT", fs=26, colour="#7a2f22")
S = dict(size="region", fs=15, colour=INK)
m.label(20.2, 52.6, "POLAND", **S)
m.label(14.2, 55.45, "EAST GERMANY", **S)
m.ax.plot(*zip(m.xy(13.6, 55.25), m.xy(12.9, 53.9)), color=INK, lw=1.4, zorder=6.5)
m.label(5.3, 54.9, "WEST\nGERMANY", **S)
m.ax.plot(*zip(m.xy(6.6, 54.4), m.xy(8.3, 52.9)), color=INK, lw=1.4, zorder=6.5)
m.label(17.2, 49.25, "CZECHOSLOVAKIA", **S)
m.label(20.4, 46.6, "HUNGARY", **S)
m.label(25.0, 45.9, "ROMANIA", **S)
m.label(25.0, 43.1, "BULGARIA", **S)
m.label(31.0, 55.5, "SOVIET UNION", **S)
m.label(23.6, 39.4, "GREECE", **S)
m.label(34.0, 39.0, "TURKEY", **S)
m.label(14.2, 47.25, "AUSTRIA", **S)
m.label(8.0, 46.75, "SWITZ.", **S)
m.label(15.6, 62.6, "SWEDEN", **S)
m.label(26.0, 63.0, "FINLAND", **S)
m.label(-8.1, 53.2, "IRELAND", **S)
m.label(19.4, 44.25, "YUGOSLAVIA", **S)
m.label(-3.6, 40.0, "SPAIN", **S)
m.label(4.2, 59.6, "iron curtain", size="small", colour=INK, fs=17, style="italic")
m.ax.annotate("", xy=m.xy(10.6, 54.2), xytext=m.xy(5.6, 58.7), zorder=8,
              arrowprops=dict(arrowstyle="-|>,head_width=0.3,head_length=0.6", color=INK, lw=1.6))
m.label(-20.0, 58.0, "Atlantic\nOcean", size="sea", fs=19)
m.label(18.0, 35.6, "Mediterranean Sea", size="sea", fs=17)
m.label(34.5, 43.3, "Black Sea", size="sea", fs=17)
m.label(2.6, 57.3, "North\nSea", size="sea", fs=16)
handles = [Patch(fc=BLUE + "70", ec=BLUE, label="NATO"),
           Patch(fc=RED + "70", ec=RED, label="Warsaw Pact"),
           Patch(fc=GREEN + "4d", ec=GREEN, hatch="//", label="neutral"),
           Patch(fc=GREY + "59", ec=GREY, label="in neither"),
           Line2D([0], [0], color=INK, lw=3.6, ls=(0, (3.2, 1.4)), label="iron curtain")]
leg = m.ax.legend(handles=handles, loc="lower left", fontsize=16, frameon=True, fancybox=False, edgecolor=INK,
                  facecolor=PAPER, framealpha=1, borderpad=0.7, labelspacing=0.45, bbox_to_anchor=(0.012, 0.36))
leg.set_zorder(9); leg.get_frame().set_linewidth(1.2)
m.scale(500, x=1700, y=-1780)
pmain = os.path.join(SCRATCH, "ch88_main.png")
m.save(pmain)

# ================================================================ Germany and the air corridors
A = Map(7.6, 15.2, 49.85, 54.3, width=7.92)
paint(A, west_germany.intersection(A.land), BLUE)
paint(A, east_germany.intersection(A.land), RED)
lines(A, LineString(smooth(border, n=6)))
berlin = (13.38, 52.50)
cities = {"Hamburg": (9.99, 53.55), "Hanover": (9.73, 52.37), "Frankfurt": (8.68, 50.11)}
ends = {"Hamburg": (9.99, 53.55), "Hanover": (9.05, 52.26), "Frankfurt": (8.68, 50.11)}
for name, (ex, ey) in ends.items():
    dx, dy = ex - berlin[0], (ey - berlin[1])
    k = np.cos(np.radians(52))
    v = np.array([dx * k, dy]); v = v / np.hypot(*v)
    n = np.array([-v[1], v[0]]) * 0.145                    # half of 32 km, in degrees of latitude
    nx, ny = n[0] / k, n[1]
    poly = [(berlin[0] + nx, berlin[1] + ny), (ex + nx, ey + ny), (ex - nx, ey - ny), (berlin[0] - nx, berlin[1] - ny)]
    xy = np.array(poly + [poly[0]])
    A.ax.add_patch(MplPoly(xy, closed=True, fc=PAPER, ec=INK, lw=1.8, alpha=0.85, zorder=3.6))
A.ax.plot(*berlin, "o", ms=17, mfc=BLUE, mec=INK, mew=1.8, zorder=6)
for name, (cx, cy) in cities.items():
    A.city(cx, cy, None)
A.label(9.85, 53.82, "Hamburg", size="city", colour=INK, fs=16.5)
A.label(9.55, 52.05, "Hanover", size="city", colour=INK, fs=16.5)
A.label(9.0, 50.02, "Frankfurt", size="city", colour=INK, fs=16.5, ha="left")
A.label(13.55, 52.84, "West\nBerlin", size="city", colour=INK, fs=16.5, ha="left")
A.label(12.25, 53.05, "air corridors", size="small", colour=INK, fs=16, style="italic", rot=0)
A.label(8.6, 51.25, "WEST\nGERMANY", fs=17)
A.label(13.2, 51.35, "EAST\nGERMANY", fs=17)
A.label(13.2, 54.05, "Baltic Sea", size="sea", fs=16)
A.label(7.75, 54.12, "GERMANY AND BERLIN", fs=16, ha="left")
A.scale(100, lon=13.1, lat=50.08)
pA = os.path.join(SCRATCH, "ch88_corridors.png")
A.save(pA)

# ================================================================ Berlin, the four sectors
B = Map(13.0, 13.84, 52.29, 52.745, width=7.92)
B.ax.add_patch(MplPoly([(12.9, 52.2), (14.0, 52.2), (14.0, 52.8), (12.9, 52.8)], closed=True, fc=RED, alpha=0.12,
                       ec="none", zorder=1.5))
sec = {f["properties"]["sector"]: shape(f["geometry"])
       for f in json.load(open(os.path.join(lib.DATA, "berlin_sectors_1945.geojson")))["features"]}
col = {"Soviet": RED, "American": BLUE, "British": GREEN, "French": FILL["gold"]}
for s, g in sec.items():
    paint(B, g, col[s], alpha=0.45, lw=0)
west = unary_union([sec["American"], sec["British"], sec["French"]])
for s, g in sec.items():
    for p in getattr(g, "geoms", [g]):
        if p.area > 1e-4:
            xy = np.array(p.exterior.coords)
            B.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=2.2, zorder=3)
            B.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=0.9, zorder=3.1)
lines(B, west.buffer(0.0004).buffer(-0.0004).boundary.intersection(sec["Soviet"].buffer(0.002)).simplify(0.0003),
      lw=3.4, style="-")
outline = unary_union(list(sec.values())).buffer(0.0004).buffer(-0.0004)
for p in getattr(outline, "geoms", [outline]):
    if p.area > 1e-3:
        xy = np.array(p.exterior.coords)
        B.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=2.4, zorder=3.2)
B.label(13.56, 52.53, "SOVIET\nSECTOR", fs=17)
B.label(13.30, 52.43, "AMERICAN\nSECTOR", fs=17)
B.label(13.17, 52.56, "BRITISH\nSECTOR", fs=17)
B.label(13.30, 52.635, "FRENCH\nSECTOR", fs=17)
B.city(13.403, 52.473, None, r=7)
B.label(13.415, 52.462, "Tempelhof\nairfield", size="small", colour=INK, fs=15, ha="left")
B.label(13.02, 52.725, "BERLIN", fs=16, ha="left")
B.label(13.80, 52.33, "EAST GERMANY", size="land", colour="#7a2f22", fs=15, ha="right", style="normal")
B.scale(5, lon=13.04, lat=52.31)
pB = os.path.join(SCRATCH, "ch88_berlin.png")
B.save(pB)

# ================================================================ put them together
main, a, b = (mpimg.imread(p)[:, :, :3] for p in (pmain, pA, pB))
h = max(a.shape[0], b.shape[0])
pad = lambda im: np.vstack([im, np.ones((h - im.shape[0], im.shape[1], 3)) * np.array(lib.matplotlib.colors.to_rgb(PAPER))])
gap = np.ones((h, 1600 - a.shape[1] - b.shape[1], 3)) * np.array(lib.matplotlib.colors.to_rgb(PAPER))
row = np.hstack([pad(a), gap, pad(b)])
sep = np.ones((16, 1600, 3)) * np.array(lib.matplotlib.colors.to_rgb(PAPER))
out = np.vstack([main, sep, row])
path = os.path.join(lib.ROOT, "chapters/88-cold-war/images/map_europe_1955.png")
plt.imsave(path, out)
print("wrote", path)
