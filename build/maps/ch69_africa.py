#!/usr/bin/env python3
"""Chapter 69: Africa in 1870 and in 1914, side by side, coloured by the European power that ruled each
part, with Ethiopia and Liberia independent, the rivers Nile, Niger and Congo, and the places the text
names: Suez and Kimberley on the first map; Omdurman, Adwa and Isandlwana on the second.

Drawn for this chapter, which had no map. 1870 rather than 1880 because the text describes the map of
1870 ("a scatter of footholds on the edge"); this also avoids the brief British annexation of the
Transvaal (1877 to 1881). The footholds of 1870 are drawn roughly, after the maps of Africa in 1870 in
Pakenham's The Scramble for Africa and in English Wikipedia's article "Scramble for Africa": French
Algeria (the coastal north, to about Laghouat and Biskra) and the Senegal river posts; the British Cape
Colony (to the Orange river and the Kei), Natal, Basutoland, and the posts at Bathurst, Freetown, the
Gold Coast forts and Lagos; Portuguese Angola (Luanda to Mossamedes, and a little inland), the
Mozambique coast and the lower Zambezi, and Bissau; French Gabon and Spanish Fernando Po as posts. The
colonies of 1914 are built from the modern countries that grew out of them (Natural Earth admin-0, as
shipped with geopandas), so their borders are approximate in places: German Togoland is drawn as modern
Togo, German Kamerun as modern Cameroon, the Spanish zone of Morocco as a strip along the north coast.
Egypt, occupied by Britain from 1882 and made a protectorate in December 1914, is drawn as British.
Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
import geopandas as gpd
from shapely.geometry import Point, Polygon
from shapely.ops import unary_union
import lib
from lib import Map, INK, PAPER, FILL, smooth
from matplotlib.patches import Polygon as MplPoly

SCRATCH = os.environ.get("SCRATCH", "/tmp")
W, E, S, N = -19.0, 53.0, -36.0, 38.0
PW = 7.93
C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
GEOM = {r["name"]: r.geometry for _, r in C.iterrows()}

POWER = dict(Britain="red", France="blue", Germany="brown", Belgium="gold", Portugal="green", Italy="purple",
             Spain="olive")


def paint(m, poly, colour, alpha=0.5):
    fc = FILL[colour]
    for p in getattr(poly, "geoms", [poly]):
        if p.is_empty or p.geom_type != "Polygon" or p.area < 1e-3:
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
        m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=1.4, alpha=0.95, zorder=2.1))


def soft(pts):
    return Polygon(smooth(pts, n=10, closed=True)).buffer(0)


def base(m):
    m.river("Nile", "Niger", "Congo", lw=1.4)


# ---------------------------------------------------------------- 1870
a = Map(W, E, S, N, width=PW)
base(a)
held = {
    "France": [soft([(-2.2, 35.2), (-1.7, 34.0), (0.5, 33.4), (3.0, 33.6), (5.5, 34.5), (8.2, 34.4), (8.7, 36.0),
                     (8.7, 37.4), (-2.2, 37.4)]),
               soft([(-17.6, 14.5), (-16.6, 16.3), (-14.5, 16.7), (-12.5, 15.5), (-11.2, 14.6), (-11.5, 14.1),
                     (-13.0, 14.9), (-15.0, 15.3), (-16.7, 14.2)]),
               Point(9.45, 0.39).buffer(0.8)],
    "Britain": [soft([(16.0, -28.4), (20.0, -28.6), (24.0, -29.4), (26.5, -30.6), (27.6, -31.8), (28.6, -32.8),
                      (26.0, -35.5), (17.0, -35.5), (15.5, -31.0)]),
                soft([(30.1, -31.2), (31.9, -29.2), (30.9, -28.6), (30.0, -27.5), (29.3, -28.2), (29.1, -29.7),
                      (29.6, -30.6)]),
                GEOM["Lesotho"].buffer(0.1),
                Point(-16.58, 13.45).buffer(0.8), Point(-13.23, 8.48).buffer(0.9),
                soft([(-3.1, 4.6), (1.2, 5.6), (1.2, 6.3), (-3.1, 5.7)]), Point(3.39, 6.45).buffer(0.8)],
    "Portugal": [soft([(12.6, -6.0), (14.0, -7.8), (15.2, -8.8), (15.0, -10.5), (14.0, -12.8), (13.2, -15.6),
                       (11.6, -15.6), (12.0, -6.0)]),
                 soft([(41.2, -14.6), (40.6, -15.8), (36.9, -18.3), (35.2, -17.8), (33.4, -16.4), (33.6, -15.8),
                       (35.2, -17.0), (36.8, -17.4), (40.2, -15.0)]),
                 Point(35.38, -23.87).buffer(0.8), Point(32.57, -25.97).buffer(0.8), Point(34.8, -20.2).buffer(0.8),
                 Point(-15.6, 11.86).buffer(0.8)],
    "Spain": [Point(8.7, 3.5).buffer(0.7)],
}
for power, polys in held.items():
    paint(a, unary_union(polys).intersection(a.land), POWER[power])

a.label(-11.0, -6.0, "1870", fs=30)
a.label(39.3, 9.0, "ETHIOPIA", fs=16)
a.label(-13.0, 2.0, "LIBERIA", fs=15)
for x, y, t in [(3.0, 31.6, "Algeria"), (-12.0, 18.4, "Senegal"), (11.5, -33.0, "Cape Colony"),
                (32.8, -30.2, "Natal"), (9.0, -11.5, "Angola"), (36.0, -12.0, "Mozambique")]:
    a.label(x, y, t, size="small", colour=INK, fs=15, ha="left" if t == "Natal" else "center")
a.label(17.0, 28.5, "Ottoman\nlands", size="land", fs=16)
a.label(28.6, -23.2, "Boer\nrepublics", size="land", fs=15)
a.city(32.55, 29.97, "Suez", dx=0.9, dy=0.6)
a.city(24.76, -28.74, "Kimberley", dx=0.0, dy=1.5)
a.label(5.0, 13.6, "Niger", size="sea", fs=16)
a.label(18.5, 1.8, "Congo", size="sea", fs=16)
a.label(29.2, 21.0, "Nile", size="sea", fs=16)
a.label(-8.0, -22.0, "Atlantic\nOcean", size="sea", fs=18)
a.label(45.5, -6.0, "Indian\nOcean", size="sea", fs=18)
pa = os.path.join(SCRATCH, "ch69_1870.png")
a.save(pa)

# ---------------------------------------------------------------- 1914
b = Map(W, E, S, N, width=PW)
base(b)
spanish_morocco = soft([(-6.2, 35.0), (-5.3, 34.8), (-3.8, 34.75), (-2.1, 34.9), (-2.1, 36.2), (-6.2, 36.2)])
ruled = [
    ("Spain", [GEOM["W. Sahara"], GEOM["Eq. Guinea"], spanish_morocco]),
    ("France", ["Morocco", "Algeria", "Tunisia", "Mauritania", "Senegal", "Mali", "Guinea", "Côte d'Ivoire",
                "Burkina Faso", "Niger", "Benin", "Chad", "Central African Rep.", "Congo", "Gabon", "Madagascar",
                "Djibouti"]),
    ("Britain", ["Egypt", "Sudan", "S. Sudan", "Uganda", "Kenya", "Somaliland", "Nigeria", "Ghana", "Sierra Leone",
                 "Gambia", "South Africa", "Lesotho", "eSwatini", "Botswana", "Zimbabwe", "Zambia", "Malawi"]),
    ("Germany", ["Togo", "Cameroon", "Namibia", "Tanzania", "Rwanda", "Burundi"]),
    ("Belgium", ["Dem. Rep. Congo"]),
    ("Portugal", ["Angola", "Mozambique", "Guinea-Bissau"]),
    ("Italy", ["Libya", "Eritrea", "Somalia"]),
]
taken = unary_union([GEOM["Ethiopia"], GEOM["Liberia"]])
for power, items in ruled:
    g = unary_union([GEOM[i] if isinstance(i, str) else i for i in items]).buffer(0.25)
    g = g.intersection(b.land).difference(taken)
    taken = taken.union(g)
    paint(b, g, POWER[power])

b.label(-11.0, -6.0, "1914", fs=30)
b.label(39.3, 9.0, "ETHIOPIA", fs=16)
b.label(39.3, 6.6, "independent", size="small", colour=INK, fs=15)
b.label(-13.0, 2.0, "LIBERIA", fs=15)
b.label(-13.0, -0.4, "independent", size="small", colour=INK, fs=15)
for x, y, t in [(0.0, 21.0, "FRENCH"), (29.5, 19.0, "BRITISH"), (24.5, -30.0, "BRITISH"), (18.5, 26.0, "ITALIAN"),
                (23.0, -5.0, "BELGIAN"), (17.6, -12.6, "PORTU-\nGUESE"), (35.0, -6.5, "GERMAN"),
                (17.6, -21.5, "GERMAN")]:
    b.label(x, y, t, fs=15)
b.city(32.48, 15.64, "Omdurman", dx=-0.9, dy=0.3)
b.city(38.90, 14.17, "Adwa", dx=0.9, dy=0.6)
b.city(30.65, -28.36, "Isandlwana", dx=1.0, dy=0.0)
b.label(18.5, 1.8, "Congo", size="sea", fs=16)
b.key([("red", "British"), ("blue", "French"), ("brown", "German"), ("gold", "Belgian"), ("green", "Portuguese"),
       ("purple", "Italian"), ("olive", "Spanish")], loc="lower left", size=15)
pb = os.path.join(SCRATCH, "ch69_1914.png")
b.save(pb)

# ---------------------------------------------------------------- side by side
ia, ib = mpimg.imread(pa), mpimg.imread(pb)
gap = np.ones((ia.shape[0], 1600 - ia.shape[1] - ib.shape[1], 4))
gap[:, :, :3] = np.array([int(PAPER[i:i + 2], 16) / 255 for i in (1, 3, 5)])
out = np.hstack([ia, gap, ib])
dest = os.path.join(lib.ROOT, "chapters/69-africa/images/map_africa.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
