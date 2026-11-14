#!/usr/bin/env python3
"""Chapter 29: the Arab conquests in three stages: Arabia by 632, the lands won by 661, and those
added by 750, with the cities the chapter names.

Replaces "Map of expansion of Caliphate" by DieBuche (Wikimedia Commons, public domain), which had no
names on it. The three areas are traced roughly by eye from that map. Two edges are drawn as the
chapter and English Wikipedia's articles on the conquests give them: Spain without the mountains of the
far north, which were never taken, and Sind up the Indus as far as Multan. The areas are soft and
approximate; raids and short-lived conquests (Septimania, Kabul) are left out. Positions from English
Wikipedia; Aphrodito is the modern village of Kom Ishqaw.
"""
import numpy as np
from shapely.geometry import Polygon
from matplotlib.patches import Polygon as MplPoly
import lib
from lib import Map, INK, FILL, smooth

by632 = [(34.6, 29.6), (36.6, 30.6), (38.6, 31.6), (41.0, 31.2), (44.0, 30.6), (47.6, 30.0), (48.6, 29.0),
         (51.0, 26.0), (57.0, 24.0), (60.5, 22.5), (59.0, 17.0), (52.0, 14.5), (44.0, 11.8), (42.4, 13.0),
         (39.0, 20.0), (35.0, 27.0)]
by661 = [(12.0, 33.2), (15.0, 32.2), (20.0, 31.2), (25.0, 32.2), (29.0, 31.6), (32.0, 31.6), (34.6, 33.6),
         (35.8, 36.2), (37.0, 37.2), (39.0, 38.0), (41.0, 39.6), (44.0, 41.4), (46.5, 41.6), (49.0, 39.5),
         (50.0, 37.4), (53.5, 36.8), (56.0, 37.6), (60.0, 37.8), (62.5, 36.6), (63.5, 33.5), (63.0, 29.5),
         (62.0, 26.5), (61.6, 24.8), (56.0, 25.5), (48.0, 29.5), (36.0, 29.0), (33.8, 26.0), (32.8, 22.4),
         (30.0, 22.0), (25.0, 24.0), (20.0, 26.5), (15.0, 29.0), (12.0, 31.0)]
# by 750: the Maghreb and Spain, and in the east Transoxiana, the Afghan hills and Sind
west750 = [(-10.0, 36.8), (-9.6, 39.5), (-9.2, 42.2), (-7.0, 42.3), (-4.5, 42.4), (-1.5, 42.6), (1.5, 42.6),
           (3.4, 42.4), (2.0, 41.2), (0.2, 39.5), (-0.5, 38.0), (-2.0, 36.6), (-4.5, 36.4), (-5.6, 36.0),
           (-1.0, 35.6), (5.0, 37.2), (10.0, 37.6), (11.4, 36.2), (12.6, 33.0), (15.0, 32.2), (14.0, 29.0),
           (9.0, 29.5), (3.0, 30.5), (-3.0, 30.5), (-8.0, 29.0), (-10.5, 29.5), (-10.5, 31.5), (-9.6, 33.0)]
east750 = [(53.0, 37.2), (53.6, 39.5), (56.0, 41.5), (58.5, 43.2), (60.5, 43.6), (62.0, 42.0), (64.5, 41.2),
           (67.0, 41.6), (69.0, 42.4), (71.0, 41.4), (71.4, 40.2), (69.0, 38.8), (70.4, 37.2), (71.2, 36.0),
           (69.6, 34.6), (71.4, 33.0), (70.8, 31.2), (72.0, 30.4), (72.2, 29.4), (70.6, 27.4), (69.6, 25.0),
           (68.6, 23.4), (66.6, 25.0), (63.0, 25.0), (62.0, 27.0), (63.5, 33.0), (62.0, 37.0), (57.0, 37.2)]

m = Map(-10.5, 75.0, 13.0, 46.2)
m.river("Nile", "Tigris", "Euphrates", "Firat", "Indus", "Amu Darya", "Syr Darya", en=True)

taken = None
for pts, colour, alpha, hatch in [(by632, "red", 0.62, None), (by661, "red", 0.30, None),
                                  (west750, "gold", 0.30, "//"), (east750, "gold", 0.30, "//")]:
    poly = Polygon(smooth(pts, n=10, closed=True)).buffer(0).intersection(lib._land)
    if taken is not None:
        poly = poly.difference(taken)
    taken = poly if taken is None else taken.union(poly)
    fc = FILL[colour]
    for p in getattr(poly, "geoms", [poly]):
        if p.is_empty or p.geom_type != "Polygon" or p.area < 2e-2:
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
        if hatch:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=0, alpha=0.8, zorder=2.05, hatch=hatch))
        m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=1.6, alpha=0.95, zorder=2.1))

# the stages, named on the map
m.label(47.0, 22.2, "ARABIA\nby 632", fs=23)
m.label(55.0, 32.6, "IRAN", fs=23)
m.label(55.0, 30.9, "by 661", size="small", colour=INK, fs=21)
m.label(27.0, 27.6, "EGYPT", fs=23)
m.label(27.0, 25.9, "by 661", size="small", colour=INK, fs=21)
m.label(-3.8, 40.0, "SPAIN", fs=23)
m.label(-3.8, 38.4, "by 750", size="small", colour=INK, fs=21)
m.label(3.0, 33.0, "NORTH AFRICA", fs=23)
m.label(3.0, 31.4, "by 750", size="small", colour=INK, fs=21)
m.label(64.2, 40.9, "CENTRAL\nASIA", fs=21)
m.label(64.2, 38.4, "by 750", size="small", colour=INK, fs=21)
m.label(37.9, 36.4, "SYRIA", fs=19)
m.label(45.0, 35.2, "IRAQ", fs=19)

m.city(39.61, 24.47, "Medina", dx=-0.6, dy=0.3, bold=True, size=20)
m.city(39.83, 21.42, "Mecca", dx=-0.6, dy=-0.3, size=20)
m.city(36.29, 33.51, "Damascus", dx=-0.5, dy=0.4, bold=True, size=20)
m.city(35.23, 31.78, "Jerusalem", dx=0.5, dy=-0.6, size=20)
m.city(29.92, 31.20, "Alexandria", dx=-0.6, dy=0.3, size=20)
m.city(31.23, 30.01, "Fustat (later Cairo)", dx=-0.6, dy=-0.4, size=20)
m.city(31.42, 26.88, "Aphrodito", dx=0.6, size=20)
m.city(44.58, 33.09, "Ctesiphon", dx=0.5, dy=0.5, size=20)
m.city(44.03, 32.62, "Karbala", dx=-0.5, dy=-0.1, size=20)
m.city(47.78, 30.51, "Basra", dx=0.6, dy=-0.3, size=20)
m.city(28.98, 41.01, "Constantinople", dx=0.0, dy=0.9, size=20)
m.label(32.5, 39.0, "ROMAN\nEMPIRE", size="land", fs=21, style="normal")
m.label(1.5, 45.4, "FRANKS", size="land", fs=21, style="normal")
m.label(70.0, 24.6, "Indus", size="sea", fs=20, ha="left")
m.label(17.0, 35.0, "Mediterranean Sea", size="sea", fs=22)
m.label(62.0, 18.5, "Arabian Sea", size="sea", fs=22)
m.scale(1000, lon=-8.5, lat=14.4)
m.save("chapters/29-conquests/images/map_conquests.png")
