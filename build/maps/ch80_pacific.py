#!/usr/bin/env python3
"""Chapter 80: Japan's empire in December 1941, the oil it went south for, the route of the carrier fleet to
Hawaii, and the places attacked on 7 and 8 December 1941 (the same hours, on either side of the date line).

Drawn for this chapter, which had no map. Japan's empire: Japan with Karafuto and the Kurils, Korea, Taiwan,
Manchuria, the occupied parts of China (roughly; see asia1941.py), and Indochina, where Japanese troops
had been stationed since 1940 and 1941 under the French administration. The islands of the Japanese
mandate in the Pacific (the Marianas without Guam, the Carolines, the Marshalls) are too small to shade
and are drawn as a soft outlined area of sea. The oilfields: Palembang in Sumatra; Balikpapan and Tarakan
in Dutch Borneo, Miri in British Borneo. The carrier route follows the map in English Wikipedia's "Attack
on Pearl Harbor": from Hitokappu Bay in the Kurils east along about 42 degrees north, then south-east to the
launch point about 370 km north of Oahu. The attacks: Pearl Harbor; Kota Bharu in Malaya; Clark Field in
the Philippines; Hong Kong; Guam; Wake. Positions from English Wikipedia.
"""
import numpy as np
from shapely.geometry import Polygon
from shapely.ops import unary_union
from lib import Map, INK, PAPER, FILL, smooth
from asia1941 import G, soft, manchuria, occupied_china, korea, japan, indochina

m = Map(93.0, 207.0, -9.0, 54.0)
land = m.land

m.region(unary_union([japan, korea, G["Taiwan"].buffer(0.2), manchuria]).intersection(land), "red", alpha=0.5)
m.region(occupied_china.intersection(land), "red", alpha=0.28, hatch="//")
m.region(indochina.buffer(0.1).intersection(land), "red", alpha=0.2, hatch="\\\\")

mandate = soft([(134.0, 8.5), (139.0, 6.0), (150.0, 4.5), (160.0, 4.0), (168.0, 4.0), (172.5, 5.0), (173.5, 9.5),
                (170.0, 12.5), (163.0, 10.5), (153.0, 10.0), (147.5, 13.0), (146.5, 20.5), (144.5, 20.5),
                (143.5, 14.2), (138.0, 11.5), (133.5, 9.5)])
c = np.array(mandate.exterior.coords)
m.ax.add_patch(__import__("matplotlib").patches.Polygon(c, closed=True, fc=FILL["red"], ec="none", alpha=0.10, zorder=1.5))
m.ax.plot(c[:, 0], c[:, 1], color=FILL["red"], lw=1.8, ls=(0, (3, 2)), zorder=1.6)

# the carrier fleet, 26 November to 7 December 1941
m.route([(147.7, 44.9), (152.0, 43.6), (160.0, 42.4), (170.0, 42.0), (180.0, 41.8), (188.0, 40.6), (194.0, 37.0),
         (198.5, 31.5), (201.6, 26.6)], colour=INK, lw=3.4)

# oil
for x, y in [(104.75, -2.99), (116.83, -1.27), (117.58, 3.3), (113.99, 4.39)]:
    m.ax.plot(x, y, "^", ms=17, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
# the attacks of 7 and 8 December
hits = [(202.03, 21.35), (102.24, 6.13), (120.55, 15.18), (114.17, 22.3), (144.79, 13.44), (166.65, 19.28)]
for x, y in hits:
    m.ax.plot(x, y, "*", ms=26, mfc=FILL["red"], mec=INK, mew=1.4, zorder=6.5)

m.label(200.3, 20.0, "Pearl Harbor", size="city", colour=INK, fs=17, ha="right")
m.label(100.6, 7.4, "Malaya,\nBritish", size="city", colour=INK, fs=17, ha="right")
m.label(122.0, 16.6, "Philippines, American", size="city", colour=INK, fs=17, ha="left")
m.label(113.6, 20.9, "Hong Kong", size="city", colour=INK, fs=17, ha="center")
m.label(146.3, 13.4, "Guam", size="city", colour=INK, fs=17, ha="left")
m.label(168.2, 19.3, "Wake", size="city", colour=INK, fs=17, ha="left")
m.city(139.69, 35.69, "Tokyo", dx=0.9, dy=-0.9, bold=True)
m.city(103.82, 1.35, "Singapore", dx=-0.8, dy=-0.5)
m.ax.plot(147.7, 44.9, "o", ms=8, mfc=INK, mec=PAPER, mew=1.4, zorder=6)
m.label(149.0, 46.6, "Hitokappu Bay", size="city", colour=INK, fs=16, ha="left")

m.label(137.5, 37.5, "JAPAN", fs=19)
m.label(127.4, 38.6, "KOREA", fs=15)
m.label(125.0, 45.6, "MANCHURIA", fs=17)
m.label(116.0, 33.2, "occupied\nChina", size="small", colour=INK, fs=16)
m.label(105.0, 30.0, "CHINA", size="land", fs=18)
m.label(105.9, 17.0, "INDO-\nCHINA", fs=15)
m.label(124.0, 23.6, "TAIWAN", fs=15, ha="left")
m.label(113.0, -4.3, "DUTCH EAST INDIES", size="land", fs=16)
m.label(113.6, 0.9, "BORNEO", size="land", fs=15)
m.label(99.6, -5.6, "SUMATRA", size="land", fs=15)
m.label(158.0, 7.2, "Japanese mandate islands", size="small", colour="#8a3a28", fs=16)
m.label(172.0, 44.4, "carrier fleet, 26 November to 7 December 1941", size="small", colour=INK, fs=16)
m.label(201.0, 23.4, "HAWAII", size="land", fs=15, ha="left")
m.label(176.0, 28.0, "Pacific Ocean", size="sea", fs=20)
m.ax.plot(176.5, 9.0, "*", ms=26, mfc=FILL["red"], mec=INK, mew=1.4, zorder=6.5)
m.label(178.0, 9.0, "attacked on 7 and 8\nDecember 1941", size="small", colour=INK, fs=16, ha="left")
m.ax.plot(176.5, 4.5, "^", ms=17, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
m.label(178.0, 4.5, "oilfield", size="small", colour=INK, fs=16, ha="left")
m.label(110.0, 50.5, "MONGOLIA", size="land", fs=16)
m.scale(1000, lon=185.0, lat=-6.5)
m.save("chapters/80-pearl-harbor/images/map_pacific_1941.png")
