#!/usr/bin/env python3
"""Chapter 74: the Ottoman lands in 1916 and in 1923, side by side. First, the Ottoman empire of 1914 with
the zones agreed in secret by Britain and France in 1916: French rule on the Syrian coast and in Cilicia and
the south-east of Anatolia; British rule in southern Iraq and at Haifa and Acre; area A (French influence)
and area B (British influence), divided by the line "from the e in Acre to the last k in Kirkuk"; and
Palestine under an international administration. Second, the same region in 1923: Turkey, the French
mandates of Syria and Lebanon, the British mandates of Iraq, Palestine and Transjordan, the Hejaz and Nejd,
Persia, and the area where Kurds live, hatched across the new borders.

Drawn for this chapter, which had no map. The Ottoman empire of 1914 is drawn as modern Turkey without the
Kars and Ardahan country (Russian from 1878 to 1918), with Syria, Lebanon, Palestine, Transjordan and Iraq,
and the Hejaz as a soft strip along the Red Sea coast; Yemen and Asir, also Ottoman, lie south of the
frame. The zones of 1916 are traced roughly from the map signed by Sykes and Picot (Royal Geographical
Society copy, on Commons) and the map in English Wikipedia's "Sykes-Picot Agreement". The states of 1923
are the modern countries, whose borders were mostly drawn then; Alexandretta (Hatay), part of French Syria
until 1939, is given to Syria; the Hejaz and Nejd are soft areas with no border drawn between them, since
none was fixed. The Kurdish area follows the usual maps of where Kurds live (for example English
Wikipedia's "Kurdistan"), roughly. Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
import geopandas as gpd
from shapely.geometry import Polygon
from shapely.ops import unary_union, linemerge
from matplotlib.patches import Polygon as MplPoly
import lib
from lib import Map, INK, PAPER, FILL, smooth

SCRATCH = os.environ.get("SCRATCH", "/tmp")
W, E, S, N = 25.5, 50.5, 19.5, 42.6
PW = 7.93
C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
P = lambda pts: Polygon(pts).buffer(0)
soft = lambda pts: Polygon(smooth(pts, n=10, closed=True)).buffer(0)

kars = P([(41.4, 41.45), (41.9, 41.6), (43.5, 41.3), (43.8, 40.9), (44.1, 40.1), (43.4, 39.85), (42.8, 40.05),
          (42.0, 40.35), (41.55, 40.8)])
hejaz = soft([(34.9, 29.4), (36.0, 29.9), (37.5, 29.3), (38.6, 27.4), (40.0, 25.5), (40.8, 23.5), (41.4, 21.5),
              (41.6, 19.5), (40.0, 19.4), (39.2, 21.0), (38.4, 23.0), (37.2, 25.0), (35.8, 27.3)])
hatay = P([(35.7, 36.0), (36.0, 35.8), (36.7, 36.2), (36.6, 36.9), (36.0, 37.0), (35.8, 36.6)])


def paint(m, poly, colour, alpha=0.45, hatch=None, lw=1.4, ls="-"):
    fc = FILL.get(colour, colour)
    for p in getattr(poly, "geoms", [poly]):
        if p.is_empty or p.geom_type != "Polygon" or p.area < 1e-3:
            continue
        xy = np.array(p.exterior.coords)
        if alpha:
            m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
        if hatch:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=0, alpha=0.9, zorder=2.05, hatch=hatch))
        if lw:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=lw, ls=ls, alpha=0.95, zorder=2.1))


def seas(m):
    m.label(29.3, 34.0, "Mediterranean\nSea", size="sea", fs=16)
    m.label(35.8, 42.2, "Black Sea", size="sea", fs=16)
    m.label(49.2, 27.3, "Gulf", size="sea", fs=16)
    m.label(38.6, 21.0, "Red\nSea", size="sea", fs=16)
    m.river("Euphrates", "Tigris", "Firat", "Dicle", lw=1.4)


# ---------------------------------------------------------------- 1916
a = Map(W, E, S, N, width=PW)
seas(a)
ottoman = unary_union([G["Turkey"].difference(kars), G["Syria"], G["Lebanon"], G["Israel"], G["Palestine"],
                       G["Jordan"], G["Iraq"], hejaz]).buffer(0.08).intersection(a.land)
paint(a, ottoman, "#b9a98c", alpha=0.35, lw=1.6)

blue = soft([(35.1, 33.1), (35.5, 33.4), (35.95, 33.75), (36.25, 34.35), (36.45, 34.9), (36.5, 35.6),
             (36.75, 36.15), (37.4, 36.6), (38.5, 36.8), (40.0, 37.0), (41.4, 37.1), (42.3, 37.4), (42.0, 38.3),
             (40.6, 38.9), (39.3, 39.6), (37.8, 40.2), (36.3, 39.6), (35.2, 38.6), (34.4, 37.6), (33.7, 36.3),
             (34.7, 36.5), (35.6, 35.5), (35.8, 34.5)])
area_a = soft([(35.65, 32.75), (36.6, 32.45), (38.2, 32.7), (39.8, 33.5), (41.0, 34.4), (42.6, 35.1), (43.7, 35.4),
               (44.8, 35.7), (45.6, 35.95), (45.0, 37.2), (44.0, 37.3), (42.3, 37.2), (41.4, 36.95), (40.0, 36.85),
               (38.5, 36.65), (37.4, 36.45), (36.85, 36.0), (36.6, 35.4), (36.55, 34.8), (36.35, 34.25),
               (36.05, 33.6), (35.8, 33.2)])
red = soft([(43.3, 34.7), (44.6, 34.8), (45.6, 34.2), (46.2, 33.3), (47.5, 32.4), (48.0, 30.9), (48.5, 29.9),
            (47.9, 29.6), (46.6, 30.0), (45.2, 30.9), (43.7, 32.0), (42.9, 33.2)])
haifa = soft([(34.95, 32.75), (35.15, 32.98), (35.3, 32.85), (35.15, 32.7)])
brown = soft([(34.3, 31.25), (34.85, 32.3), (35.0, 32.95), (35.3, 33.05), (35.55, 32.85), (35.55, 32.2),
              (35.5, 31.55), (35.0, 31.25)])
area_b = soft([(34.9, 29.6), (36.1, 30.0), (37.3, 29.5), (38.8, 29.9), (41.0, 30.6), (43.0, 31.4), (43.7, 32.0),
               (42.9, 33.2), (43.3, 34.7), (44.6, 34.8), (45.6, 34.2), (45.6, 35.9), (44.8, 35.7), (43.7, 35.4), (42.6, 35.1),
               (41.0, 34.4), (39.8, 33.5), (38.2, 32.7), (36.6, 32.45), (35.65, 32.75), (35.55, 32.2),
               (35.5, 31.5), (35.2, 30.6)])
area_b = area_b.difference(red).difference(area_a)
paint(a, area_a.difference(blue).intersection(ottoman), "blue", alpha=0.18, hatch="\\\\", lw=0)
paint(a, area_b.difference(brown).intersection(ottoman), "red", alpha=0.18, hatch="//", lw=0)
paint(a, blue.intersection(ottoman), "blue", alpha=0.6, lw=1.2)
paint(a, red.intersection(ottoman), "red", alpha=0.6, lw=1.2)
paint(a, haifa.intersection(a.land), "red", alpha=0.8, lw=1.0)
paint(a, brown.intersection(ottoman).difference(haifa), "brown", alpha=0.6, lw=1.2)

# the line from Acre to Kirkuk: the boundary between areas A and B
ab = [(35.65, 32.75), (36.6, 32.45), (38.2, 32.7), (39.8, 33.5), (41.0, 34.4), (42.6, 35.1), (43.7, 35.4),
      (44.8, 35.7), (45.6, 35.95)]
a.line(ab, colour=INK, lw=3.4, style=(0, (4, 2)))

a.label(27.0, 21.3, "1916", fs=30, ha="left")
a.label(31.6, 38.4, "OTTOMAN\nEMPIRE, 1914", fs=17)
a.label(37.6, 38.9, "French\nrule", size="small", colour=INK, fs=15)
a.label(39.2, 35.4, "A: French\ninfluence", size="small", colour=INK, fs=15)
a.label(39.3, 31.3, "B: British\ninfluence", size="small", colour=INK, fs=15)
a.label(46.4, 31.9, "British\nrule", size="small", colour=INK, fs=15)
a.label(31.3, 30.9, "inter-\nnational", size="small", colour=INK, fs=15)
a.ax.plot([32.6, 34.8], [31.0, 31.6], color=INK, lw=1.1, zorder=6.5)
a.city(35.08, 32.93, "Acre", dx=-0.5, dy=0.55)
a.city(44.39, 35.47, "Kirkuk", dx=0.45, dy=0.7)
a.city(28.98, 41.01, "Constantinople", dx=0.45, dy=-0.6, ha="left")
a.city(36.29, 33.51, "Damascus", dx=0.4, dy=-0.55)
a.city(44.37, 33.31, "Baghdad", dx=-0.45, dy=-0.2)
a.city(39.83, 21.42, "Mecca", dx=0.45, dy=0.0)
a.label(44.5, 25.0, "NEJD", size="land", fs=16)
a.label(30.5, 27.5, "EGYPT", size="land", fs=16)
a.label(47.5, 38.8, "PERSIA", size="land", fs=16)
pa = os.path.join(SCRATCH, "ch74_1916.png")
a.save(pa)

# ---------------------------------------------------------------- 1923
b = Map(W, E, S, N, width=PW)
seas(b)
saudi = G["Saudi Arabia"]
states = [
    ("Turkey", G["Turkey"].difference(hatay), "gold", 0.4),
    ("Syria", G["Syria"].union(hatay), "blue", 0.45),
    ("Lebanon", G["Lebanon"], "blue", 0.75),
    ("Iraq", G["Iraq"], "red", 0.45),
    ("Palestine", unary_union([G["Israel"], G["Palestine"]]), "red", 0.75),
    ("Transjordan", G["Jordan"], "red", 0.3),
    ("Hejaz", hejaz.intersection(saudi), "green", 0.45),
    ("Nejd", saudi.difference(hejaz), "olive", 0.35),
    ("Persia", G["Iran"], "grey", 0.3),
]
taken = None
for name, g, col, al in states:
    g = g.buffer(0.06).intersection(b.land)
    if taken is not None:
        g = g.difference(taken)
    taken = g if taken is None else taken.union(g)
    paint(b, g, col, alpha=al, lw=1.4 if name not in ("Hejaz", "Nejd") else 0)

kurds = soft([(37.6, 37.0), (37.5, 38.0), (38.6, 39.0), (39.5, 39.7), (41.0, 39.9), (42.5, 39.9), (43.8, 39.7),
              (44.6, 38.9), (44.9, 37.8), (45.8, 36.9), (46.6, 36.3), (47.6, 35.0), (47.2, 33.8), (46.2, 33.5),
              (45.5, 34.2), (44.6, 35.0), (43.6, 35.6), (42.6, 36.1), (41.6, 36.6), (40.5, 36.75), (39.0, 36.6)])
kurds = kurds.intersection(b.land)
for p in getattr(kurds, "geoms", [kurds]):
    xy = np.array(p.exterior.coords)
    b.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=INK, lw=0, alpha=0.55, zorder=2.6, hatch="xx"))
    b.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=1.6, ls=(0, (2, 2)), zorder=2.7)

b.label(27.0, 21.3, "1923", fs=30, ha="left")
b.label(31.2, 38.4, "TURKEY", fs=19)
b.label(38.6, 34.6, "SYRIA", fs=17)
b.label(43.3, 32.7, "IRAQ", fs=18)
b.label(37.4, 30.9, "TRANS-\nJORDAN", fs=15)
b.label(31.4, 32.4, "PALESTINE", fs=15, ha="center")
b.ax.plot([33.4, 34.75], [32.2, 31.75], color=INK, lw=1.1, zorder=6.5)
b.label(31.8, 35.6, "LEBANON", fs=15, ha="center")
b.ax.plot([33.6, 35.6], [35.4, 34.0], color=INK, lw=1.1, zorder=6.5)
b.label(39.6, 24.6, "HEJAZ", fs=16)
b.label(44.6, 25.0, "NEJD", fs=17)
b.label(48.7, 32.7, "PERSIA", fs=17)
b.label(43.4, 41.2, "KURDS", fs=16)
b.ax.plot([43.4, 42.6], [40.85, 39.4], color=INK, lw=1.1, zorder=6.5)
b.label(39.0, 33.4, "French mandate", size="small", colour=INK, fs=15)
b.label(43.2, 31.6, "British mandate", size="small", colour=INK, fs=15)
b.city(32.86, 39.93, "Ankara", dx=0.45, dy=0.45, ha="left")
b.city(39.83, 21.42, "Mecca", dx=0.45, dy=0.0)
b.label(30.5, 27.5, "EGYPT", size="land", fs=16)
pb = os.path.join(SCRATCH, "ch74_1923.png")
b.save(pb)

# ---------------------------------------------------------------- side by side
ia, ib = mpimg.imread(pa), mpimg.imread(pb)
h = min(ia.shape[0], ib.shape[0])
ia, ib = ia[:h], ib[:h]
gap = np.ones((h, 1600 - ia.shape[1] - ib.shape[1], 4))
gap[:, :, :3] = np.array([int(PAPER[i:i + 2], 16) / 255 for i in (1, 3, 5)])
out = np.hstack([ia, gap, ib])
dest = os.path.join(lib.ROOT, "chapters/74-mandates/images/map_mandates.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
