#!/usr/bin/env python3
"""Chapter 15: the kingdom of Lydia at its largest, under Croesus, about 2,570 years ago.

The extent is traced by eye from "Kingdom of Lydia" by Ennomus (Wikimedia Commons,
CC BY-SA 4.0), the map this one replaces, with its "boundaries" and its "vassals" (the Greek
cities of the coast) drawn as one area, and checked against the map of Lydia in the
Cambridge Ancient History, volume III part 2. The river Halys, the border with the Medes, is
the modern Kizilirmak. The tracing is in the source map's pixels, turned into degrees by a
fit to eleven cities. City positions from English Wikipedia.
"""
from lib import Map
from tracing import fit

deg = fit([((307, 518), (28.04, 38.49)), ((1263, 38), (35.15, 42.03)), ((793, 742), (31.40, 36.77)),
           ((918, 593), (32.48, 37.87)), ((1000, 298), (32.86, 39.93)), ((889, 352), (31.99, 39.65)),
           ((222, 637), (27.28, 37.53)), ((474, 168), (29.03, 40.99)), ((241, 710), (27.42, 37.04)),
           ((484, 762), (29.12, 36.62)), ((148, 262), (26.40, 40.20))], quad=True)

lydia = deg([(470, 150), (600, 140), (800, 110), (1000, 60), (1200, 25), (1300, 10), (1420, 95), (1350, 150),
             (1250, 200), (1150, 230), (1100, 280), (1080, 350), (1150, 440), (1240, 480), (1150, 600),
             (1050, 700), (900, 790), (800, 760), (700, 740), (600, 730), (520, 745), (480, 775), (380, 780),
             (280, 770), (230, 730), (185, 650), (195, 565), (150, 520), (165, 450), (150, 385), (112, 335),
             (122, 285), (172, 250), (290, 225), (400, 195)])

m = Map(25.7, 36.6, 35.9, 42.3)
m.river("Kızılırmak", "Sakarya", "Büyük Menderes")
m.region(lydia, "gold", alpha=0.5)

m.label(30.6, 38.9, "L Y D I A", size="region", fs=28)
m.city(28.04, 38.49, "Sardis", dx=0.15, star=True, bold=True, size=19)
m.city(27.34, 37.94, "Ephesus", dx=0.18, dy=-0.12, size=19)
m.city(27.28, 37.53, "Miletus", dx=0.18, dy=-0.1, size=19)
m.label(27.0, 39.6, "Greek\ncities", size="small", colour="#2f2a26", fs=18)
m.label(35.6, 39.0, "Medes", size="land", fs=21)
m.label(34.55, 40.45, "Halys", size="sea", fs=18, rot=55)
m.label(26.2, 38.2, "Aegean\nSea", size="sea", fs=19)
m.label(32.5, 42.0, "Black Sea", size="sea", fs=19)
m.label(31.5, 36.2, "Mediterranean Sea", size="sea", fs=19)
m.label(26.6, 41.6, "Thrace", size="land", fs=19)
m.scale(200, lon=34.2, lat=36.3)
m.save("chapters/15-money/images/map_lydia_croesus.png")
