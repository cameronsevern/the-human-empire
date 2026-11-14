#!/usr/bin/env python3
"""Chapter 18: the Athenian empire at the start of the war with Sparta, about 2,455 years ago
(431 BCE).

Drawn after "Map athenian empire 431 BC-en" by Marsyas and Once in a Blue Moon (Wikimedia
Commons, CC BY-SA 3.0), the map this one replaces, and checked against the map of the Athenian
empire in Meiggs, The Athenian Empire (1972). The paying cities stood on the coasts and the
islands; they are drawn as every island of the Aegean except those the source leaves out
(Crete, Melos, Thera, Kythera), and as a strip of coast about twenty kilometres deep along the
shores that the source marks: Chalcidice, Thrace, the Chersonese, both shores of the
Hellespont and the Sea of Marmara, and western Turkey from the Troad to Caria. Chios and the facing
peninsula of Erythrae are added by hand, because the coarse coastline joins them. Attica is
drawn by its natural frontiers. City positions from English Wikipedia.
"""
import numpy as np
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import unary_union
from matplotlib.patches import Polygon as MplPoly
from lib import Map, FILL, smooth
import lib

m = Map(21.9, 29.6, 35.7, 41.45)
land = lib._land.intersection(m.clip)

coasts = [[(23.85, 40.75), (24.4, 40.9), (25.2, 40.95), (25.9, 40.85), (26.2, 40.62)],
          [(26.2, 40.62), (26.65, 40.42), (26.2, 40.05)],
          [(26.7, 40.62), (27.5, 40.97), (28.2, 41.05), (28.98, 41.03), (29.1, 41.2)],
          [(26.4, 40.2), (27.0, 40.4), (27.9, 40.38), (28.6, 40.4), (29.4, 40.75), (29.9, 40.75)],
          [(26.15, 40.05), (26.1, 39.6), (26.7, 39.3), (27.0, 38.8), (26.8, 38.4), (27.2, 38.1), (27.3, 37.6),
           (27.4, 37.1), (27.8, 36.8), (28.3, 36.7), (28.9, 36.7)]]
strip = unary_union([LineString(c).buffer(0.2) for c in coasts])
chalcidice = Polygon(smooth([(22.75, 40.55), (23.9, 40.78), (24.4, 40.3), (24.0, 39.85), (23.3, 39.9), (22.8, 40.2)],
                            closed=True))
skip = [Point(24.42, 36.70), Point(25.43, 36.42), Point(23.0, 36.25)]   # Melos, Thera, Kythera
islands = []
for p in getattr(land, "geoms", [land]):
    c = p.centroid
    if p.area > 1.0 or c.y < 35.6 or c.x < 23.3 or any(p.distance(q) < 0.05 for q in skip):
        continue
    islands.append(p)
attica = Polygon(smooth([(23.3, 38.05), (23.45, 38.22), (23.7, 38.3), (24.05, 38.25), (24.12, 37.95), (24.03, 37.62),
                         (23.75, 37.8), (23.4, 37.7), (23.3, 37.9)], closed=True)).intersection(land)
from shapely.geometry import box
chios = box(25.8, 38.15, 26.62, 38.72)          # Chios and Erythrae; the coarse coastline joins them
allies = unary_union([strip.intersection(land), chalcidice.intersection(land), chios.intersection(land)]
                     + islands).difference(attica)


def draw(geom, colour, alpha):
    for p in getattr(geom, "geoms", [geom]):
        if p.is_empty or p.geom_type != "Polygon":
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=FILL[colour], ec="none", alpha=alpha, zorder=2))
        m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=FILL[colour], lw=1.4, alpha=0.95, zorder=2.1))


draw(allies, "gold", 0.6)
draw(attica, "red", 0.6)

m.city(23.7263, 37.9715, "Athens", dx=0.12, dy=-0.12, star=True, bold=True, size=20)
m.label(23.66, 38.15, "ATTICA", fs=17)
m.city(22.43, 37.08, "Sparta", dx=0.12, size=19, bold=True)
m.city(25.27, 37.40, "Delos", dx=0.0, dy=-0.13, size=17)
m.label(25.8, 37.1, "Naxos", size="land", fs=17)
m.city(26.555, 39.105, "Mytilene", dx=0.12, dy=-0.12, size=17)
m.label(26.0, 39.45, "Lesbos", size="land", fs=17)
m.city(28.98, 41.01, "Byzantium", dx=-0.12, dy=0.18, size=17)
m.label(25.4, 38.75, "AEGEAN\nSEA", size="sea", fs=21)
m.label(28.5, 38.4, "Persian\nempire", size="land", fs=21)
m.label(22.6, 39.5, "Thessaly", size="land", fs=17)
m.label(25.3, 41.3, "Thrace", size="land", fs=17)
m.label(28.1, 37.35, "cities that paid\ntribute to Athens", size="small", colour="#2f2a26", fs=17)
m.scale(100, lon=22.3, lat=35.95)
m.save("chapters/18-democracy/images/map_athens_empire.png")
