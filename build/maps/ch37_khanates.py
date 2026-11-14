#!/usr/bin/env python3
"""Chapter 37: the Mongol empire at its widest, about 1280, as the four realms it had become: the lands
of the Great Khan in Mongolia and China, the Chagatai lands in Central Asia, the Ilkhans in Persia and
the Golden Horde on the Russian steppe. With the cities and battles the chapter names, and the Mongol
homeland on the Onon and Kherlen rivers.

Drawn for this chapter, which had no map. The four areas are soft and approximate, following the
boundaries usually drawn for about 1280, as on the map in English Wikipedia's article "Division of the
Mongol Empire": the Amu Darya between the Chagatai lands and the Ilkhans, Khwarezm with the Golden Horde,
the Euphrates as the Ilkhans' frontier with the Mamluks. The Russian principalities, which
paid tribute to the Golden Horde, are included in its area. Positions from English Wikipedia.
"""
import numpy as np
import lib
from lib import Map, INK
from matplotlib.patches import Polygon as MplPoly
from tracing import states

chagatai = [(59.6, 41.6), (63.5, 42.2), (66.0, 43.9), (70.0, 45.2), (74.0, 46.9), (78.0, 48.6), (82.5, 48.4),
            (86.5, 46.6), (90.5, 44.6), (92.0, 42.8), (90.5, 40.6), (87.5, 38.6), (82.0, 36.6), (77.0, 35.8),
            (72.5, 35.2), (69.5, 35.6), (67.6, 37.0), (65.4, 37.6), (63.4, 38.8), (61.0, 39.8)]
ilkhans = [(29.6, 41.3), (34.0, 42.2), (38.5, 41.4), (42.0, 41.9), (45.0, 42.6), (48.6, 41.9), (50.5, 39.8),
           (53.5, 39.6), (57.5, 40.2), (61.2, 40.4), (63.4, 39.0), (65.4, 37.6), (67.6, 37.0), (69.6, 35.4),
           (69.0, 31.6), (66.0, 28.6), (62.0, 25.8), (57.6, 25.2), (54.0, 26.2), (50.0, 29.4), (47.6, 30.0),
           (45.2, 30.6), (42.4, 32.6), (40.6, 34.8), (38.6, 36.6), (36.4, 37.1), (33.2, 36.4), (30.6, 37.0),
           (29.4, 39.0)]
horde = [(26.4, 45.4), (27.2, 48.0), (25.2, 50.2), (28.4, 53.4), (31.4, 56.4), (36.0, 58.4), (44.0, 58.8),
         (52.0, 58.4), (60.0, 57.4), (70.0, 56.8), (76.4, 54.4), (79.0, 50.6), (78.0, 48.6), (74.0, 46.9),
         (70.0, 45.2), (66.0, 43.9), (63.5, 42.2), (61.2, 40.6), (57.5, 40.3), (53.5, 41.0), (51.0, 44.0),
         (48.6, 41.9), (45.0, 42.6), (40.6, 43.6), (37.2, 44.8), (33.0, 44.2), (30.0, 45.6)]
khan = [(90.5, 44.6), (88.5, 47.8), (90.5, 50.6), (95.0, 52.4), (101.0, 52.6), (108.0, 53.6), (115.0, 52.6),
        (121.0, 53.4), (127.0, 51.0), (134.0, 48.4), (133.0, 43.6), (130.0, 42.6), (126.6, 41.6),
        (124.0, 39.6), (122.6, 36.0), (122.6, 30.0), (120.0, 24.6), (115.0, 21.4), (110.0, 19.4),
        (107.6, 21.6), (104.0, 22.8), (101.0, 21.6), (98.4, 24.0), (97.6, 27.6), (93.0, 28.6), (88.0, 28.6),
        (82.0, 30.4), (78.6, 33.0), (77.0, 35.8), (82.0, 36.6), (87.5, 38.6), (90.5, 40.6), (92.0, 42.8)]

m = Map(9.0, 134.0, 19.0, 61.0)
m.river("Volga", "Amu Darya", "Syr Darya", "Huang", "Yangtze", "Chang Jiang", "Huang He", "Dnieper", "Danube",
        "Onon", "Kherlen", "Orkhon", "Kerulen", en=True, lw=1.4)
states(m, [(chagatai, "teal"), (ilkhans, "red"), (horde, "gold"), (khan, "blue")], alpha=0.42)

# lakes and inland seas again, above the shading
for _, r in lib._lakes.iterrows():
    if (r.get("scalerank", 0) or 0) > 1:
        continue
    g = r.geometry.intersection(m.clip)
    for p in getattr(g, "geoms", [g]):
        if not p.is_empty and p.geom_type == "Polygon":
            m.ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=lib.SEA, ec=lib.SHORE, lw=0.7, zorder=2.3))

# the homeland on the Onon and Kherlen
from lib import smooth
home = smooth([(107.6, 47.4), (110.4, 46.8), (113.6, 47.4), (114.4, 49.0), (112.0, 50.2), (108.6, 49.6)], closed=True)
m.ax.add_patch(MplPoly(home, closed=True, fc="none", ec=INK, lw=2.4, ls=(0, (4, 2.5)), zorder=4))
m.label(115.0, 48.6, "Mongol\nhomeland", size="small", colour=INK, fs=18, ha="left")

m.label(103.0, 37.6, "LANDS OF THE\nGREAT KHAN", fs=21)
m.label(77.2, 42.0, "CHAGATAI", fs=21)
m.label(54.5, 33.4, "ILKHANS", fs=21)
m.label(52.0, 52.4, "GOLDEN HORDE", fs=21)

m.city(102.83, 47.20, "Karakorum", dx=0.0, dy=-1.5, bold=True)
m.city(116.40, 39.90, "Beijing", dx=1.0, dy=0.6)
m.city(114.31, 34.80, "Kaifeng", dx=1.0, dy=0.0)
m.city(112.14, 32.01, "Xiangyang", dx=1.0, dy=-0.4)
m.city(64.42, 39.77, "Bukhara", dx=-0.9, dy=0.9)
m.city(66.96, 39.65, "Samarkand", dx=0.9, dy=0.4)
m.city(62.19, 37.66, "Merv", dx=0.9, dy=-0.7)
m.city(58.80, 36.21, "Nishapur", dx=0.0, dy=-1.3)
m.city(44.36, 33.31, "Baghdad", dx=-0.9, dy=-0.6)
m.city(35.36, 32.55, "Ain Jalut", dx=-0.9, dy=0.0)
m.city(30.52, 50.45, "Kiev", dx=-0.9, dy=0.0)

# the two battles of 1241
for lon, lat in [(16.16, 51.21), (20.97, 47.95)]:
    m.mark(lon, lat, marker="X", ms=17, colour=INK)
m.label(16.16, 53.6, "battle in\nPoland, 1241", size="small", colour=INK, fs=17)
m.label(20.97, 45.3, "battle in\nHungary, 1241", size="small", colour=INK, fs=17)

m.label(19.0, 37.0, "Mediterranean", size="sea", fs=17, ha="left")
m.label(34.6, 43.2, "Black Sea", size="sea", fs=16)
m.label(51.0, 41.0, "Caspian", size="sea", fs=16, rot=-80)
m.label(66.0, 22.0, "Arabian Sea", size="sea", fs=18)
m.label(106.0, 43.0, "GOBI", size="land", fs=18, style="normal")
m.label(127.0, 31.0, "East\nChina Sea", size="sea", fs=17)
m.scale(1000, lon=118.0, lat=21.0)
m.save("chapters/37-mongols/images/map_khanates.png")
