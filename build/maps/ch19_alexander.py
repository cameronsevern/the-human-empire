#!/usr/bin/env python3
"""Chapter 19: Alexander's march, from Macedon to the Punjab and back to Babylon, between about 2,360
and 2,350 years ago (334-323 BCE).

The route follows the towns and battlefields that the march passed, in order, after "The
Empire of Alexander 334-323 B.C." (Wikimedia Commons, CC BY-SA 3.0), the map this one replaces,
and the maps in Bosworth, Conquest and Empire (1988). The shaded empire is the Persian empire
of chapter 13 (traced from Cattette's map) with Macedon and Greece added; it is rough. The
smaller loops of the march (to the oracle in the Libyan desert, and to and fro across Central
Asia) are left out. Positions from English Wikipedia.
"""
from lib import Map
from tracing import fit

deg = fit([((286, 240), (28.04, 38.49)), ((830, 497), (48.26, 32.19)), ((973, 580), (52.89, 29.93)),
           ((711, 491), (44.42, 32.54)), ((330, 550), (31.25, 29.85)), ((356, 694), (32.64, 25.70)),
           ((1510, 357), (72.83, 33.75)), ((1188, 294), (61.84, 37.66)), ((1302, 196), (66.97, 39.65)),
           ((493, 157), (35.15, 42.03)), ((330, 170), (28.98, 41.01)), ((170, 140), (22.52, 40.76)),
           ((78, 398), (21.86, 32.82)), ((456, 514), (35.23, 31.78)), ((803, 414), (48.52, 34.80)),
           ((708, 372), (44.01, 36.19))], quad=True)
# the Persian empire as traced for chapter 13, with Greece and Macedon (and without Libya)
empire = deg([(150, 175), (140, 125), (230, 92), (260, 68), (320, 40), (362, 58), (352, 110), (348, 150),
              (420, 138), (500, 128), (580, 128), (645, 138), (700, 145), (760, 170), (800, 210), (900, 230),
              (985, 200), (995, 150), (1060, 60), (1150, 30), (1300, 50), (1420, 110), (1500, 180),
              (1570, 260), (1590, 330), (1560, 420), (1520, 480), (1485, 560), (1470, 620), (1440, 690),
              (1300, 715), (1205, 700), (1100, 690), (950, 690),
              (880, 640), (830, 610), (760, 560), (690, 505), (640, 440), (590, 400), (520, 392),
              (505, 470), (540, 530), (570, 610), (560, 690), (520, 705), (470, 785), (420, 800), (320, 765),
              (250, 700), (200, 600), (160, 520), (180, 470), (260, 400), (262, 330),
              (240, 300), (160, 300), (130, 240)])

out = [(22.52, 40.76), (24.5, 40.9), (26.4, 40.25), (27.25, 40.2), (28.04, 38.49), (27.34, 37.94), (27.42, 37.04),
       (30.5, 36.6), (31.4, 36.9), (31.99, 39.65), (32.9, 39.4), (34.90, 36.92), (36.2, 36.85), (35.20, 33.27),
       (34.47, 31.50), (31.25, 29.85), (29.92, 31.20)]
east = [(31.0, 30.5), (34.47, 31.50), (35.4, 33.6), (38.2, 35.9), (43.43, 36.57), (44.42, 32.54), (48.26, 32.19),
        (52.89, 29.93), (49.5, 33.0), (48.52, 34.80), (51.43, 35.60), (54.4, 36.2), (58.5, 35.6), (62.2, 34.35),
        (62.1, 32.37), (65.7, 31.6), (69.0, 35.0), (68.9, 36.7), (66.9, 36.76), (66.97, 39.65)]
india = [(66.97, 39.65), (67.4, 37.2), (69.0, 35.0), (71.0, 34.1), (72.83, 33.75), (73.7, 32.9), (75.1, 31.6)]
back = [(75.1, 31.6), (73.5, 32.6), (72.0, 31.0), (70.6, 28.5), (68.4, 25.4), (65.5, 25.5), (62.5, 25.9),
        (60.45, 27.19), (57.5, 28.6), (53.17, 30.20), (52.89, 29.93), (48.26, 32.19), (44.42, 32.54)]

m = Map(19.3, 77.0, 23.6, 42.6)
m.river("Nile", "Euphrates", "Tigris", "Indus", en=True)
m.region(empire, "gold", alpha=0.32)
for leg in (out, east, india):
    m.route(leg, colour="red", lw=3.4)
m.route(back, colour="red", lw=3.4, style=(0, (2.2, 1.4)))
for lon, lat in [(27.25, 40.2), (36.2, 36.85), (43.43, 36.57), (73.7, 32.9)]:
    m.ax.plot(lon, lat, marker="X", ms=17, mfc="#2f2a26", mec="#faf6ee", mew=1.6, zorder=6.5)

m.label(22.9, 41.85, "MACEDON", fs=19)
m.city(22.52, 40.76, "Pella", dx=-0.6, dy=-0.3)
m.city(29.92, 31.20, "Alexandria", dx=-0.6, dy=-0.4)
m.city(44.42, 32.54, "Babylon", dx=-0.6, dy=-0.5)
m.city(52.89, 29.93, "Persepolis", dx=0.0, dy=-0.85)
m.city(66.97, 39.65, "Samarkand", dx=-0.6, dy=0.3)
m.label(74.7, 30.4, "turned\nback", size="small", colour="red", fs=17)
m.label(64.8, 27.3, "the way back", size="small", colour="red", fs=17)
m.label(73.2, 35.6, "PUNJAB", size="land", fs=17)
m.label(65.5, 33.6, "Afghanistan", size="land", fs=17)
m.label(30.0, 27.6, "EGYPT", size="land", fs=17)
m.label(55.5, 33.0, "PERSIA", size="land", fs=19)
m.label(30.0, 34.0, "Mediterranean Sea", size="sea")
m.label(34.5, 43.0 - 0.9, "Black Sea", size="sea")
m.label(50.9, 41.0, "Caspian\nSea", size="sea")
m.label(52.0, 26.9, "Gulf", size="sea")
m.label(62.0, 24.3, "Arabian Sea", size="sea")
m.scale(1000, lon=36.0, lat=24.3)
m.save("chapters/19-alexander/images/map_alexander_march.png")
