#!/usr/bin/env python3
"""Chapter 13: the Persian empire under Darius, about 2,500 years ago, with the royal road.

The extent and the line of the road are traced by eye from "Achaemenid Empire 500 BCE" by
Cattette (Wikimedia Commons, CC BY 4.0), the map this one replaces, and checked against the
map of the Achaemenid empire in Briant, From Cyrus to Alexander. The tracing is in the source
map's pixels, turned into degrees by a fit to sixteen cities. The extent is rough. City
positions from English Wikipedia.
"""
from lib import Map
from tracing import fit

deg = fit([((286, 240), (28.04, 38.49)), ((830, 497), (48.26, 32.19)), ((973, 580), (52.89, 29.93)),
           ((711, 491), (44.42, 32.54)), ((330, 550), (31.25, 29.85)), ((356, 694), (32.64, 25.70)),
           ((1510, 357), (72.83, 33.75)), ((1188, 294), (61.84, 37.66)), ((1302, 196), (66.97, 39.65)),
           ((493, 157), (35.15, 42.03)), ((330, 170), (28.98, 41.01)), ((170, 140), (22.52, 40.76)),
           ((78, 398), (21.86, 32.82)), ((456, 514), (35.23, 31.78)), ((803, 414), (48.52, 34.80)),
           ((708, 372), (44.01, 36.19))], quad=True)

empire = deg([(178, 135), (188, 110), (230, 92), (260, 68), (320, 40), (362, 58), (352, 110), (348, 150),
              (420, 138), (500, 128), (580, 128), (645, 138), (700, 145), (760, 170), (800, 210), (900, 230),
              (985, 200), (995, 150), (1060, 60), (1150, 30), (1300, 50), (1420, 110), (1500, 180),
              (1570, 260), (1590, 330), (1560, 420), (1520, 480), (1485, 560), (1470, 620), (1440, 690),
              (1300, 715), (1205, 700), (1200, 830), (1150, 845), (1060, 785), (1030, 720), (950, 690),
              (880, 640), (830, 610), (760, 560), (690, 505), (640, 440), (590, 400), (520, 392),
              (505, 470), (540, 530), (570, 610), (560, 690), (520, 705), (470, 785), (420, 800), (320, 765),
              (250, 700), (150, 600), (60, 505), (25, 435), (40, 392), (120, 395), (220, 395), (262, 330),
              (240, 270), (225, 205), (195, 165), (175, 152)])
road = deg([(286, 240), (330, 246), (380, 236), (430, 226), (490, 222), (520, 235), (545, 270), (585, 305),
            (640, 340), (708, 372), (735, 405), (765, 440), (795, 470), (830, 497)])

m = Map(19.0, 75.0, 22.5, 45.5)
m.river("Nile", "Euphrates", "Tigris", "Indus", en=True)
m.region(empire, "gold", alpha=0.45)
m.line(road, colour="red", lw=3.2, style=(0, (2, 1.4)))

m.label(55.5, 35.3, "P E R S I A N   E M P I R E", size="region", fs=25)
m.label(29.2, 27.0, "Egypt", size="land", fs=19)
m.label(31.0, 39.4, "Lydia", size="land", fs=19)
m.label(47.0, 36.8, "Media", size="land", fs=19)
m.label(53.0, 31.2, "Persians", size="land", fs=19)
m.label(70.6, 30.0, "India", size="land", fs=19)
m.label(64.0, 41.3, "Central Asia", size="land", fs=19)
m.label(22.2, 39.4, "Greece", size="land", fs=19)
m.label(37.0, 37.5, "royal road", size="small", colour="red", fs=18, rot=-8)

m.city(28.04, 38.49, "Sardis", dx=0.4, dy=-0.75, bold=True)
m.city(48.26, 32.19, "Susa", dx=-0.5, dy=-0.5, bold=True)
m.city(52.89, 29.93, "Persepolis", dx=0.5, dy=-0.3)
m.city(44.42, 32.54, "Babylon", dx=-0.5, dy=0.2)
m.city(31.25, 29.85, "Memphis", dx=-0.5)

m.label(27.5, 34.0, "Mediterranean Sea", size="sea")
m.label(34.5, 43.6, "Black Sea", size="sea")
m.label(50.9, 41.6, "Caspian\nSea", size="sea")
m.label(51.3, 27.6, "Gulf", size="sea")
m.label(37.0, 24.4, "Red\nSea", size="sea")
m.label(25.3, 37.3, "Aegean\nSea", size="sea", fs=16)
m.label(63.5, 23.6, "Arabian Sea", size="sea")
m.scale(1000, lon=40.0, lat=23.3)
m.save("chapters/13-persia/images/map_persian_empire.png")
