#!/usr/bin/env python3
"""Chapter 78: the Soviet Union in the 1930s. The regions worst hit by the famine of 1932 and 1933 (Ukraine,
the north Caucasus, the Volga and Kazakhstan), Moscow, Leningrad, Magnitogorsk, the Dnieper dam, the White
Sea canal, and the camp regions of Kolyma and Vorkuta.

Drawn for this chapter, which had no map. The Soviet Union is built from the modern countries (Natural
Earth admin-0, as shipped with geopandas) that made it up in the 1930s, without the Baltic states, which
were independent, and cut along the western border of 1921 to 1939: the land west of a line from the
Latvian border west of Polotsk, west of Minsk, through Polesia and Volhynia to the Zbruch, and then the
Dniester, was Polish or Romanian. The small changes on the Finnish border, and Tuva (a separate state until
1944), are not shown. The famine regions follow the maps in English Wikipedia's "Soviet famine of 1930-1933"
and "Holodomor", roughly: Soviet Ukraine without Crimea; the north Caucasus territory (the Kuban, the Don
and Stavropol); the lower and middle Volga; and Kazakhstan. The camp regions follow the maps of the Gulag in
English Wikipedia ("Gulag", "Dalstroy", "Vorkutlag"): the Kolyma basin north of Magadan, and the Pechora
basin round Vorkuta. The White Sea canal runs from Povenets on Lake Onega to Belomorsk. Positions from
English Wikipedia.
"""
import geopandas as gpd
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from projmap import ProjMap
from lib import INK

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}

m = ProjMap("+proj=lcc +lat_1=50 +lat_2=68 +lat_0=60 +lon_0=92 +units=km", (-4700, 3800, -2300, 3550),
            lonlat_box=unary_union([box(8, 25, 180, 84), box(-180, 60, -168.6, 75)]))
west = Polygon([(27.6, 56.2), (27.3, 55.0), (27.1, 54.2), (27.0, 53.4), (27.6, 52.3), (27.4, 51.4),
                (26.9, 50.6), (26.3, 49.9), (26.0, 49.2), (26.2, 48.55), (27.4, 48.4), (28.6, 47.8),
                (29.4, 47.0), (29.9, 46.5), (30.2, 46.0), (30.0, 40.0), (10.0, 40.0), (10.0, 58.0)]).buffer(0)
parts = ["Russia", "Ukraine", "Belarus", "Kazakhstan", "Uzbekistan", "Turkmenistan", "Kyrgyzstan", "Tajikistan",
         "Georgia", "Armenia", "Azerbaijan"]
ussr = m.proj(unary_union([G[n] for n in parts]).buffer(0.05).difference(west).difference(box(19, 54, 23, 56))
              .intersection(m.llclip)).intersection(m.land)
crimea = box(32.3, 44.2, 36.8, 46.05)
ukraine = m.proj(G["Ukraine"].buffer(0.05).difference(west).difference(crimea)).intersection(m.land)
caucasus = m.area([(38.2, 47.1), (39.8, 49.6), (41.5, 50.0), (43.2, 48.6), (45.2, 46.3), (46.3, 44.6), (44.5, 43.5),
                   (41.5, 43.6), (39.5, 44.2), (36.8, 45.2), (37.5, 46.6)])
volga = m.area([(43.8, 54.8), (47.5, 55.3), (52.3, 54.4), (53.0, 51.8), (50.5, 50.4), (49.2, 48.2), (47.6, 46.4),
                (45.6, 46.8), (43.4, 48.6), (42.6, 51.3), (43.0, 53.5)]).difference(caucasus)
kazakh = m.proj(G["Kazakhstan"].buffer(0.02)).intersection(m.land).difference(volga)
famine = unary_union([ukraine, caucasus, volga, kazakh]).intersection(ussr.buffer(5))
kolyma = m.area([(141.0, 59.3), (143.5, 62.0), (146.5, 65.0), (151.5, 67.3), (157.5, 68.2), (161.5, 66.5),
                 (160.0, 63.0), (155.5, 60.6), (150.5, 59.4), (145.0, 59.0)])
vorkuta = m.area([(51.0, 61.8), (54.0, 64.8), (58.0, 67.4), (63.0, 68.6), (66.3, 67.4), (63.5, 64.6),
                  (58.5, 62.4), (54.0, 61.2)])

m.paint(ussr, "gold", 0.16, lw=1.6)
m.paint(famine, "red", 0.48, lw=1.4)
for g in (kolyma, vorkuta):
    m.paint(g, "grey", 0.22, hatch="///", lw=1.6, edge=INK)
m.river("Volga", "Dnieper", "Kolyma", lw=1.5)

# the White Sea canal, Povenets to Belomorsk
m.line([(34.83, 62.85), (34.6, 63.4), (34.95, 64.0), (34.77, 64.52)], colour=INK, lw=3.4, style=(0, (2, 1.2)))

m.city(37.62, 55.75, "Moscow", dx=70, dy=55, bold=True)
m.city(30.32, 59.94, "Leningrad", dx=-80, dy=70)
m.city(59.0, 53.41, "Magnitogorsk", dx=110, dy=0)
m.city(35.08, 47.87, "Dnieper dam", dx=65, dy=0)
m.label(37.6, 64.0, "White Sea\ncanal", size="city", colour=INK, fs=16, ha="left")
m.city(64.03, 67.50, None)
m.label(57.0, 60.2, "Vorkuta camps", size="city", colour=INK, fs=17)
m.label(137.5, 64.0, "Kolyma\ncamps", size="city", colour=INK, fs=17, ha="center")

m.label(31.5, 50.3, "UKRAINE", fs=16)
m.label(41.5, 46.4, "NORTH\nCAUCASUS", fs=15, ha="center")
m.label(47.6, 52.0, "VOLGA", fs=15)
m.label(67.5, 48.3, "KAZAKHSTAN", fs=18)
m.label(67.5, 45.6, "famine regions, 1932 to 1933", size="small", colour=INK, fs=16, style="italic")
m.label(100.0, 61.0, "SOVIET UNION", fs=26, spaced=True)
m.label(102.0, 46.0, "MONGOLIA", size="land", fs=16)
m.label(80.0, 77.0, "Arctic Ocean", size="sea", fs=19)
m.label(34.5, 43.2, "Black Sea", size="sea", fs=15)
m.label(51.4, 42.4, "Caspian\nSea", size="sea", fs=15)
m.scale(1000, x=1500, y=-2100)
m.save("chapters/78-stalin/images/map_soviet_union.png")
