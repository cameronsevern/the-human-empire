#!/usr/bin/env python3
"""Chapter 73: Russia in the civil war, about October 1919. The land held by the Reds round Moscow and
Petrograd; the White armies in the south, in Siberia, in the north and on the Baltic; the foreign landings
at Murmansk, Arkhangelsk, Odessa and Vladivostok (1918); the lands given up by the treaty of March 1918;
Yekaterinburg; and the Trans-Siberian railway.

Drawn for this chapter, which had no map. The fronts moved all the time; this is a single moment, roughly
October 1919, when the Whites came nearest to Moscow and Petrograd, simplified after the maps in English
Wikipedia's "Russian Civil War", "Southern Front of the Russian Civil War" and "Eastern Front of the Russian
Civil War": Denikin's front through Kiev, Chernigov, Orel, Voronezh and Tsaritsyn; Kolchak's on the Tobol;
Yudenich at Gatchina and Luga; the northern front south of Arkhangelsk and north of Lake Onega; the Polish
front on the Berezina. Astrakhan and the left bank of the lower Volga stayed Red. Red Turkestan, cut off
from Moscow until September 1919, lies mostly south of the frame and is left out. The lands given up in
1918 are drawn from modern countries (Finland, Estonia, Latvia, Lithuania, the Russian part of Poland,
Ukraine without Galicia), so their edges are rough. The foreign troops are shown at the ports where they
landed. The railway is the original line of the 1890s, Moscow, Samara, Chelyabinsk, Omsk, Irkutsk, Chita,
and the Chinese Eastern line through Harbin to Vladivostok, with the branch to Yekaterinburg. Positions
from English Wikipedia.
"""
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from matplotlib.patches import Polygon as MplPoly
from lib import Map, INK, PAPER, FILL, smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
P = lambda pts: Polygon(pts).buffer(0)
S = lambda pts: Polygon(smooth(pts, n=10, closed=True)).buffer(0)

W, E, S0, N = 19.0, 136.0, 40.5, 71.0
m = Map(W, E, S0, N)

# ------------------------------------------------------------------ the lands given up in 1918
west_poland = G["Poland"].intersection(P([(14.0, 54.9), (19.6, 54.9), (22.9, 54.4), (22.8, 53.95), (22.2, 53.55),
    (21.0, 53.28), (20.0, 53.2), (19.35, 53.05), (18.95, 52.95), (18.7, 52.7), (18.4, 52.5), (17.9, 52.3),
    (17.95, 51.75), (18.1, 51.45), (18.5, 51.15), (18.95, 50.85), (19.1, 50.5), (19.17, 50.23), (19.15, 50.0),
    (14.0, 49.0)]))
galicia_pl = G["Poland"].intersection(P([(18.3, 48.8), (19.15, 50.0), (19.17, 50.23), (19.3, 50.08), (20.0, 50.13),
    (20.8, 50.25), (21.5, 50.5), (21.85, 50.68), (22.1, 50.55), (22.6, 50.35), (24.5, 50.4), (24.5, 48.5)]))
galicia_ua = G["Ukraine"].intersection(P([(21.5, 51.0), (22.6, 50.35), (24.1, 50.5), (25.2, 50.1), (25.9, 49.8),
    (26.1, 49.2), (26.2, 48.6), (26.3, 48.2), (25.0, 47.3), (21.5, 47.3)]))
lost = unary_union([G["Finland"], G["Estonia"], G["Latvia"], G["Lithuania"],
                    G["Poland"].difference(west_poland).difference(galicia_pl),
                    G["Ukraine"].difference(galicia_ua)]).buffer(0.05).intersection(m.land)
fc = FILL["grey"]
for p in getattr(lost, "geoms", [lost]):
    if p.geom_type != "Polygon" or p.area < 1e-2:
        continue
    xy = np.array(p.exterior.coords)
    m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=0.18, zorder=1.6))
    m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=0, alpha=0.8, hatch="///", zorder=1.65))
    m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec="#6d655c", lw=1.2, ls=(0, (3, 2)), zorder=1.7))

# ------------------------------------------------------------------ Reds and Whites, about October 1919
red = S([(29.9, 60.1), (31.0, 60.9), (32.6, 61.6), (33.8, 62.3), (35.2, 62.6), (37.5, 62.5), (40.5, 62.4),
         (43.5, 62.4), (47.0, 63.0), (51.0, 64.0), (55.5, 63.0), (59.5, 61.5), (63.0, 59.5), (65.4, 57.5),
         (66.4, 55.5), (64.5, 54.2), (61.5, 53.3), (58.5, 51.5), (55.1, 51.4), (52.0, 51.0), (49.2, 50.5),
         (47.6, 49.4), (47.6, 47.5), (48.6, 46.4), (47.6, 46.4), (46.6, 47.5), (46.4, 49.0), (45.6, 49.7),
         (44.4, 49.6), (42.0, 50.9), (40.0, 52.0), (38.3, 52.7), (36.5, 53.3), (35.0, 53.0), (33.5, 52.8),
         (32.0, 52.1), (30.6, 51.6), (29.4, 52.1), (29.3, 53.2), (28.6, 54.3), (28.1, 55.2), (28.0, 56.1),
         (28.6, 57.3), (29.6, 58.2), (30.7, 58.6), (31.0, 59.2), (30.5, 59.6), (30.0, 59.8)])
whites = {
    "south": S([(30.6, 51.5), (32.0, 52.0), (33.5, 52.7), (35.0, 52.9), (36.5, 53.2), (38.3, 52.6), (40.0, 51.9),
                (42.0, 50.8), (44.3, 49.5), (45.6, 49.6), (46.3, 48.9), (46.5, 47.4), (47.3, 46.3), (47.0, 44.5),
                (47.6, 43.0), (48.4, 41.9), (46.5, 42.0), (44.5, 42.7), (41.5, 43.4), (39.8, 43.6), (37.0, 45.0),
                (35.5, 44.3), (33.0, 44.5), (31.0, 46.3), (30.1, 46.4), (29.8, 47.5), (29.8, 49.0), (30.0, 50.4)]),
    "siberia": S([(63.3, 59.6), (65.6, 57.5), (66.8, 55.5), (65.0, 53.6), (61.5, 52.8), (61.5, 50.5), (70.0, 50.0),
                  (80.0, 49.5), (87.0, 49.8), (96.0, 50.8), (105.0, 50.6), (116.0, 49.4), (120.5, 51.8), (127.0, 49.3),
                  (131.0, 47.4), (134.5, 48.2), (133.5, 45.5), (131.0, 42.6), (139.0, 46.0), (139.0, 53.0),
                  (130.0, 56.5), (110.0, 58.0), (95.0, 59.0), (80.0, 60.0), (70.0, 61.0)]),
    "north": S([(30.6, 69.9), (33.0, 69.5), (37.0, 69.0), (41.0, 67.8), (44.0, 66.4), (48.0, 67.8), (54.0, 68.6),
                (59.0, 68.0), (58.5, 65.5), (55.5, 63.6), (51.0, 64.6), (47.0, 63.6), (43.5, 63.0), (40.5, 63.0),
                (37.5, 63.0), (35.4, 63.1), (33.7, 63.3), (31.2, 63.8), (30.0, 65.5), (29.3, 67.5), (29.0, 69.2)]),
    "baltic": S([(27.9, 59.45), (29.2, 59.85), (29.8, 59.75), (30.4, 59.5), (30.9, 59.0), (30.5, 58.55), (29.5, 58.3),
                 (28.4, 58.3), (27.8, 58.8)]),
}
m.region(red, "red", alpha=0.45, lakes_out=True)
for g in whites.values():
    m.region(g.difference(red), "blue", alpha=0.38, lakes_out=True)

m.river("Volga", lw=1.6)

# ------------------------------------------------------------------ the railway
rail = [(37.62, 55.75), (39.7, 54.6), (45.0, 53.2), (48.47, 53.15), (50.1, 53.2), (55.96, 54.74), (59.65, 55.17),
        (61.4, 55.16), (65.34, 55.44), (69.13, 54.87), (73.37, 54.99), (82.92, 55.03), (88.0, 55.9), (92.87, 56.01),
        (97.0, 55.9), (101.5, 54.3), (104.28, 52.29), (103.7, 51.66), (107.6, 51.83), (113.5, 52.03), (116.0, 50.6),
        (117.4, 49.6), (122.0, 48.0), (126.63, 45.75), (129.6, 44.6), (131.89, 43.12)]
branch = [(61.4, 55.16), (60.6, 56.84)]
for pts in (rail, branch):
    c = smooth(pts, n=8)
    m.ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=7.5, solid_capstyle="round", zorder=3.5)
    m.ax.plot(c[:, 0], c[:, 1], color=INK, lw=4.4, solid_capstyle="butt", zorder=3.6)
    m.ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=2.0, ls=(0, (3, 3)), solid_capstyle="butt", zorder=3.7)

# ------------------------------------------------------------------ foreign landings, 1918
for (x0, y0), (x1, y1) in [((38.5, 70.6), (33.6, 69.2)), ((46.6, 68.4), (41.0, 64.8)), ((29.9, 43.3), (30.7, 46.1)),
                           ((135.0, 41.6), (132.3, 43.0))]:
    m.ax.annotate("", xy=(x1, y1), xytext=(x0, y0), zorder=5,
                  arrowprops=dict(arrowstyle="-|>,head_width=0.5,head_length=0.9", color=INK, lw=3.2,
                                  shrinkA=0, shrinkB=0))

m.city(33.08, 68.97, None)
m.city(40.54, 64.54, None)
m.city(30.73, 46.48, None)
m.city(131.89, 43.12, None)
m.label(39.0, 70.35, "Murmansk: British, 1918", size="city", colour=INK, fs=16, ha="left")
m.label(47.0, 68.9, "Arkhangelsk: British, American, French, 1918", size="city", colour=INK, fs=16, ha="left")
m.label(28.0, 41.9, "Odessa: French, 1918", size="city", colour=INK, fs=16, ha="center")
m.label(133.3, 41.1, "Vladivostok: Japanese, American, 1918", size="city", colour=INK, fs=16, ha="right")

m.city(37.62, 55.75, "Moscow", dx=0.9, dy=-0.7, bold=True)
m.city(30.32, 59.94, "Petrograd", dx=0.9, dy=-0.55, bold=True)
m.city(60.6, 56.84, "Yekaterinburg", dx=-0.8, dy=0.75, star=True, bold=True)

# ------------------------------------------------------------------ names
m.label(44.5, 56.6, "REDS", fs=24, spaced=True)
m.label(39.0, 47.6, "WHITES", fs=19)
m.label(88.0, 53.2, "WHITES", fs=21, spaced=True)
m.label(52.5, 66.2, "WHITES", fs=17)
m.label(26.0, 61.8, "WHITES", fs=15)
m.ax.plot([27.6, 29.0], [61.4, 59.2], color=INK, lw=1.1, zorder=6.5)
m.label(23.9, 56.6, "given up\nby the treaty\nof 1918", size="small", colour=INK, fs=16)
m.label(92.0, 57.6, "Trans-Siberian railway", size="small", colour=INK, fs=16)
m.label(48.8, 52.4, "Volga", size="sea", fs=16)
m.label(35.0, 43.3, "Black Sea", size="sea", fs=16)
m.label(51.0, 43.0, "Caspian\nSea", size="sea", fs=16)
m.label(78.0, 46.0, "CENTRAL ASIA", size="land", fs=17)
m.label(103.0, 46.6, "MONGOLIA", size="land", fs=17)
m.label(116.5, 44.2, "CHINA", size="land", fs=17)
m.scale(1000, lon=100.0, lat=62.5)
m.save("chapters/73-revolution/images/map_civil_war.png")
