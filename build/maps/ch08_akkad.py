#!/usr/bin/env python3
"""Chapter 8: the empire of Akkad at its greatest extent, about 4,250 years ago.

Both areas are traced by eye from "The Akkadian Empire" by Ennomus (Wikimedia Commons,
CC BY-SA 4.0): its darker "boundaries" as the land Akkad ruled, its lighter "raids and
vassals" as the land it raided or took tribute from. Checked against the map of the
Akkadian state in Van De Mieroop, A History of the Ancient Near East. The tracing is in
the source map's pixels, turned into degrees by a fit to ten cities (error under half a
degree), so the extents are rough. Akkad itself has never been found: it has no dot.
"""
from lib import Map

def deg(px):
    return [(0.014590 * x - 0.000185 * y + 30.0886, -0.000119 * x - 0.013828 * y + 41.9905) for x, y in px]

m = Map(34.3, 50.8, 29.0, 38.6)
m.river("Euphrates", "Tigris", en=True)
outer = deg([(392, 330), (470, 318), (560, 312), (650, 312), (760, 315), (860, 325), (960, 350), (1040, 400),
             (1110, 470), (1200, 540), (1300, 600), (1420, 660), (1480, 720), (1530, 800), (1530, 880), (1490, 940),
             (1420, 960), (1340, 900), (1290, 820), (1200, 800), (1100, 800), (1000, 740), (900, 640), (800, 575),
             (700, 490), (620, 470), (560, 480), (500, 520), (450, 580), (420, 615), (392, 600)])
core = deg([(668, 420), (690, 360), (720, 330), (800, 325), (880, 335), (960, 360), (1020, 400), (1080, 460),
            (1150, 540), (1230, 600), (1300, 640), (1330, 690), (1320, 740), (1280, 780), (1240, 790), (1150, 800),
            (1090, 795), (1040, 770), (980, 700), (920, 640), (860, 590), (780, 560), (720, 500), (680, 450)])
# the outer area is drawn only where it lies outside the core, hatched, so that the two differ in more than colour
import numpy as np
from shapely.geometry import Polygon
from matplotlib.patches import Polygon as MplPoly
from lib import smooth, FILL, _land
ring = Polygon(smooth(outer, n=14, closed=True)).buffer(0).difference(Polygon(smooth(core, n=14, closed=True)).buffer(0))
for p in getattr(ring.intersection(_land), "geoms", [ring.intersection(_land)]):
    if p.geom_type == "Polygon" and not p.is_empty:
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=FILL["green"], ec="none", alpha=0.16, zorder=2))
        m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=FILL["green"], lw=0, alpha=0.8, zorder=2.05, hatch="//"))
m.region(outer, "green", alpha=0.0)
m.region(core, "green", alpha=0.5)

m.label(42.4, 34.75, "EMPIRE\nOF AKKAD", size="region")
m.label(36.95, 35.2, "raided or\nmade to pay", size="small", colour="#2f2a26", fs=16.5)
m.label(44.05, 33.6, "Akkad?", size="land", fs=17)
m.city(44.605, 32.541, "Kish", dx=-0.25)
m.city(45.233, 32.127, "Nippur", dx=0.25)
m.city(45.636, 31.322, "Uruk", dx=-0.25)
m.city(46.103, 30.963, "Ur", dx=-0.25, dy=-0.15)
m.city(46.401, 31.412, "Lagash", dx=0.25, dy=0.1)
m.city(43.153, 36.360, "Nineveh", dx=0.25)
m.city(41.92, 36.96, "Tell Leilan", dx=-0.25)
m.city(48.258, 32.190, "Susa", dx=0.25)

m.label(35.6, 33.0, "Mediterranean\nSea", size="sea")
m.label(49.5, 29.4, "Gulf", size="sea")
m.label(39.3, 36.3, "Euphrates", size="sea", rot=-12)
m.label(44.3, 35.7, "Tigris", size="sea", rot=-60)
m.label(47.4, 35.0, "Gutians", size="land", fs=19)
m.label(40.0, 31.3, "desert", size="land")
m.label(37.0, 38.3, "mountains of Turkey", size="land")
m.scale(300, lon=35.2, lat=29.4)
m.save("chapters/08-empire/images/map_akkad.png")
