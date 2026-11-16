#!/usr/bin/env python3
"""Chapter 81: the furthest advance of Germany and of Japan, in two panels, one above the other. Above,
Europe in November 1942: the land held by Germany, its allies and the countries they occupied, the eastern
front just before the Soviet attack at Stalingrad, Leningrad under siege, Moscow, Stalingrad, the oilfields
of the Caucasus (and Romania's, at Ploiesti), and the convoy route across the Atlantic to Britain. Below,
Asia and the Pacific in mid 1942: the land Japan held, the furthest line of its advance, Midway, and the
oilfields of the Dutch islands.

Drawn for this chapter, which had no map. Europe: the Axis area is built from the modern countries
(Natural Earth admin-0, as shipped with geopandas) west of the front line, without the neutrals (Spain,
Portugal, Switzerland, Sweden, Ireland, Turkey) and without Britain; in North Africa it is Libya and
Tunisia, and Egypt west of El Alamein. All of France is shaded, since Germany occupied the south on 11
November 1942. Algeria and Morocco, where the Allies landed that month, are left unshaded. The front of 18
November 1942 is simplified after the maps in English Wikipedia's "Eastern Front (World War II)", "Battle of
Stalingrad" and "Case Blue": the Finnish front from the Litsa river west of Murmansk through Karelia to the
Svir; the siege lines south of Lake Ladoga; the Volkhov, Lake Ilmen, the Demyansk salient, Velikiye Luki,
the Rzhev salient, east of Orel and Kursk, Voronezh, the Don to Stalingrad, the Kalmyk steppe east of
Elista, the Terek at Mozdok, Nalchik, the main Caucasus ridge, and the coast at Novorossiysk. The convoy
route is the usual track from Halifax south of Iceland to the North Channel and Liverpool, shown from the
edge of the map.

Pacific: Japan's empire as in ch80_pacific.py, with Thailand (allied to Japan from December 1941, hatched),
Burma, Malaya, the Philippines, the Dutch East Indies, northern New Guinea, New Britain and the northern
Solomons. The line of furthest advance in mid 1942 (after Midway, before Guadalcanal) is simplified after
the maps in English Wikipedia's "Pacific War": the Burma-India frontier, the Andaman Islands, south of Java
and Timor, the north coast of New Guinea, the Solomons to Tulagi, the Gilberts, Wake, and the Aleutian
islands of Attu and Kiska. Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from matplotlib.patches import Polygon as MplPoly
import lib
from lib import Map, INK, PAPER, FILL, smooth
from asia1941 import G, soft, manchuria, occupied_china, korea, japan, indochina
import geopandas as gpd

SCRATCH = os.environ.get("SCRATCH", "/tmp")
C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
P = lambda pts: Polygon(pts).buffer(0)


def paint(m, geom, colour, alpha, hatch=None, lw=1.3):
    fc = FILL[colour]
    for p in getattr(geom, "geoms", [geom]):
        if p.is_empty or p.geom_type != "Polygon" or p.area < 2e-3:
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
        if hatch:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=0, alpha=0.7, zorder=2.05, hatch=hatch))
        if lw:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=lw, alpha=0.95, zorder=2.1))


def front_line(m, pts, lw=4.0):
    c = smooth(pts, n=8)
    m.ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=lw + 3.5, solid_capstyle="round", zorder=4.4)
    m.ax.plot(c[:, 0], c[:, 1], color=INK, lw=lw, solid_capstyle="round", zorder=4.5)
    return c


# ================================================================ Europe, November 1942
a = Map(-26.0, 58.0, 29.5, 71.0)
front = [(31.2, 69.6), (32.0, 68.0), (30.6, 67.0), (31.6, 65.9), (32.6, 64.0), (34.4, 62.9), (35.3, 61.6),
         (33.6, 60.9), (32.6, 60.5), (31.0, 60.0), (31.6, 59.9), (32.0, 59.4), (31.6, 58.7), (31.4, 58.2),
         (32.0, 57.8), (33.4, 57.6), (32.6, 57.0), (31.1, 56.6), (30.6, 56.3), (32.0, 55.9), (33.6, 56.3),
         (34.4, 56.2), (35.1, 55.6), (35.3, 54.8), (34.6, 54.0), (35.6, 53.6), (36.6, 53.1), (37.3, 52.3),
         (38.1, 51.9), (39.2, 51.7), (40.0, 50.6), (41.5, 49.9), (43.0, 49.3), (44.5, 48.75), (44.4, 47.9),
         (44.9, 46.5), (44.8, 44.9), (44.6, 43.8), (43.6, 43.4), (42.4, 43.4), (40.6, 43.7), (39.2, 44.25),
         (37.8, 44.7)]
fc = smooth(front, n=8)
west_of_front = Polygon(list(map(tuple, fc)) + [(37.0, 44.3), (34.0, 43.6), (29.0, 42.0), (25.0, 38.0),
                                                (-30.0, 36.0), (-30.0, 72.0), (31.2, 72.0)]).buffer(0)
europe = unary_union([r.geometry for _, r in C.iterrows() if r["continent"] == "Europe"])
neutral = unary_union([G[n] for n in ["Spain", "Portugal", "Switzerland", "Sweden", "Ireland", "Turkey"]])
allied = unary_union([G["United Kingdom"], G["Iceland"]])
egypt_west = G["Egypt"].intersection(box(24.0, 29.0, 28.95, 32.0))
axis = unary_union([europe.intersection(west_of_front), G["Libya"], G["Tunisia"], egypt_west])
axis = axis.buffer(0.15).difference(neutral.buffer(0.02)).difference(allied.buffer(0.3)).intersection(a.land)
soviet = G["Russia"].union(unary_union([G[n] for n in ["Ukraine", "Belarus", "Estonia", "Latvia", "Lithuania",
                                                          "Moldova", "Georgia", "Armenia", "Azerbaijan",
                                                          "Kazakhstan"]])).buffer(0.15).intersection(a.land)
soviet = soviet.difference(axis).difference(G["Finland"].buffer(0.2))
paint(a, axis, "red", 0.42)
paint(a, soviet, "blue", 0.3)
paint(a, allied.buffer(0.15).intersection(a.land), "blue", 0.45)
paint(a, neutral.buffer(0.1).intersection(a.land).difference(axis), "grey", 0.18, hatch="///")
a.river("Volga", "Don", lw=1.5)
front_line(a, front)

# the convoys
a.route([(-26.5, 50.5), (-20.0, 54.2), (-12.0, 56.0), (-7.0, 55.6), (-4.0, 54.0), (-3.3, 53.6)], colour=INK, lw=3.2,
        style=(0, (3, 1.6)))
# oil
for x, y in [(40.1, 44.6), (45.7, 43.3), (49.87, 40.41), (26.02, 44.94)]:
    a.ax.plot(x, y, "^", ms=17, mfc=INK, mec=PAPER, mew=1.6, zorder=6)

a.city(30.32, 59.94, "Leningrad,\nbesieged", dx=-0.8, dy=0.9, bold=True)
a.city(37.62, 55.75, "Moscow", dx=0.8, dy=0.55, bold=True)
a.city(44.52, 48.71, "Stalingrad", dx=0.9, dy=0.5, bold=True)
a.city(13.40, 52.52, "Berlin", dx=0.7, dy=0.55)
a.city(-0.13, 51.51, "London", dx=-0.7, dy=-0.6)
a.label(47.4, 41.6, "Caucasus\noilfields", size="small", colour=INK, fs=16, ha="left")
a.label(26.0, 43.6, "Ploiesti oil", size="small", colour=INK, fs=15, ha="center")
a.label(19.5, 49.0, "GERMANY, ITS ALLIES\nAND THE LANDS\nTHEY OCCUPIED", fs=16, ha="center")
a.label(48.5, 57.5, "SOVIET UNION", fs=19)
a.label(-4.3, 57.2, "BRITAIN", fs=15)
a.label(-17.5, 51.0, "Atlantic convoys\nfrom North America", size="small", colour=INK, fs=16)
a.label(41.6, 52.4, "front,\nNovember 1942", size="small", colour=INK, fs=15, ha="left")
a.label(-4.0, 40.2, "SPAIN", size="land", colour="#5a534b", fs=15, style="normal")
a.label(34.0, 39.2, "TURKEY", size="land", colour="#5a534b", fs=15, style="normal")
a.label(16.0, 63.5, "SWEDEN", size="land", colour="#5a534b", fs=15, style="normal")
a.label(-16.0, 44.5, "Atlantic Ocean", size="sea", fs=18)
a.label(18.0, 34.3, "Mediterranean Sea", size="sea", fs=16)
a.label(-22.0, 68.4, "EUROPE, NOVEMBER 1942", fs=19, ha="left")
pa = os.path.join(SCRATCH, "ch81_europe.png")
a.save(pa)

# ================================================================ Asia and the Pacific, mid 1942
b = Map(88.0, 186.0, -14.0, 55.0)
land = b.land
newguinea = land.intersection(box(130.9, -11.0, 151.0, -0.3)).difference(box(146.0, -7.0, 156, -2.0)) \
    .difference(box(130.0, -9.0, 135.5, -5.0))
ng_north = newguinea.intersection(soft([(130.5, -0.2), (135.0, -0.3), (137.5, -1.4), (141.0, -2.4), (144.5, -3.5),
                                         (147.0, -5.5), (148.0, -7.6), (146.8, -7.9), (145.2, -6.0), (142.0, -4.4),
                                         (138.0, -3.4), (134.5, -2.6), (131.0, -2.0)]))
islands = land.intersection(unary_union([box(148.0, -6.8, 156.0, -2.0), soft([(154.3, -5.0), (156.2, -6.2),
                                         (160.4, -8.8), (160.2, -9.9), (158.5, -9.5), (155.4, -7.2)])]))
indies = unary_union([G["Indonesia"], G["Timor-Leste"], G["Malaysia"], G["Brunei"]]).buffer(0.2).intersection(land)
indies = indies.difference(box(130.9, -11.0, 141.5, -0.3))
held = unary_union([japan.intersection(land), korea, G["Taiwan"].buffer(0.2), manchuria, occupied_china,
                    indochina, G["Myanmar"], G["Philippines"].buffer(0.2), indies, ng_north, islands,
                    land.intersection(box(92.0, 10.4, 94.0, 14.0))]).intersection(land)
paint(b, held, "red", 0.45)
paint(b, G["Thailand"].intersection(land).difference(held), "red", 0.2, hatch="\\\\")

reach = [(94.5, 27.5), (94.0, 24.0), (92.6, 21.0), (91.0, 14.0), (93.0, 8.5), (96.0, 3.0), (100.0, -4.0),
         (106.0, -9.5), (116.0, -10.5), (125.0, -11.0), (131.0, -9.5), (138.5, -7.0), (145.5, -9.0),
         (151.0, -11.0), (160.5, -11.0), (166.0, -5.0), (174.5, -1.5), (175.0, 4.0), (168.5, 13.5),
         (167.0, 21.0), (175.0, 33.0), (180.0, 47.0), (178.5, 53.0), (170.0, 54.5)]
c = smooth(reach, n=8)
b.ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=6.5, zorder=4.4)
b.ax.plot(c[:, 0], c[:, 1], color=INK, lw=3.4, ls=(0, (4, 2)), zorder=4.5)

for x, y in [(104.75, -2.99), (116.83, -1.27), (117.58, 3.3), (113.99, 4.39)]:
    b.ax.plot(x, y, "^", ms=17, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
b.ax.plot(182.63, 28.21, "*", ms=26, mfc=INK, mec=PAPER, mew=1.4, zorder=6.5)
b.label(181.0, 25.6, "Midway,\nJune 1942", size="city", colour=INK, fs=17, ha="center")
b.city(166.65, 19.28, "Wake", dx=-0.9, dy=0.0)
b.city(177.5, 51.98, None)
b.label(176.0, 50.2, "Kiska", size="city", colour=INK, fs=16, ha="right")
b.city(139.69, 35.69, "Tokyo", dx=0.9, dy=-1.0, bold=True)
b.city(103.82, 1.35, "Singapore", dx=-0.8, dy=-0.6)
b.city(160.15, -9.43, None)
b.label(157.0, -12.3, "Guadalcanal", size="city", colour=INK, fs=16.5)

b.label(115.6, 46.5, "JAPANESE EMPIRE\nAND CONQUESTS", fs=17)
b.label(105.0, 31.5, "CHINA", size="land", fs=18)
b.label(101.0, 16.0, "THAILAND,\nallied", size="small", colour=INK, fs=15)
b.label(96.0, 22.0, "BURMA", fs=15, ha="center")
b.label(120.0, -7.4, "oil of the\nDutch islands", size="small", colour=INK, fs=16)
b.label(91.0, 27.5, "INDIA", size="land", fs=16, ha="center")
b.label(133.0, -24.0 + 3.0, "AUSTRALIA", size="land", fs=17)
b.label(156.0, 30.0, "Pacific Ocean", size="sea", fs=20)
b.label(158.0, 5.0, "furthest Japanese\nadvance, mid 1942", size="small", colour=INK, fs=16)
b.label(90.0, 53.0, "ASIA AND THE PACIFIC, MID 1942", fs=19, ha="left")
b.scale(1000, lon=165.0, lat=-11.5)
pb = os.path.join(SCRATCH, "ch81_pacific.png")
b.save(pb)

# ================================================================ stacked
ia, ib = mpimg.imread(pa), mpimg.imread(pb)
gap = np.ones((16, 1600, 4))
gap[:, :, :3] = np.array([int(PAPER[i:i + 2], 16) / 255 for i in (1, 3, 5)])
out = np.vstack([ia, gap, ib])
dest = os.path.join(lib.ROOT, "chapters/81-war/images/map_furthest_advance.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
