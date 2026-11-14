#!/usr/bin/env python3
"""Chapter 20: Ashoka's empire, about 2,250 years ago, with the places where his edicts were cut.

The empire is traced by eye from "Maurya Empire, c.250 BCE 2" by Avantiputra7 (Wikimedia Commons,
CC BY-SA 3.0), the map this one replaces, and checked against the map of the Mauryan empire in
Thapar, Asoka and the Decline of the Mauryas. The tracing is in the source map's pixels, turned
into degrees by a quadratic fit to fourteen cities. Only the land frontiers come from the
tracing (the north-west, the Himalaya, Bengal and the south); the coasts are Natural Earth.
The edict sites are a selection of the rock edicts (major and minor) and the pillars, with
positions from English Wikipedia. The pillar at Delhi stands where the sultan moved it.
"""
from lib import Map
from tracing import fit

deg = fit([((835, 447), (85.14, 25.61)), ((162, 244), (65.71, 31.61)), ((411, 163), (72.83, 33.75)),
           ((561, 331), (77.24, 28.61)), ((514, 545), (75.78, 23.18)), ((332, 591), (70.48, 21.53)),
           ((417, 664), (72.79, 19.42)), ((870, 638), (85.84, 20.19)), ((690, 774), (80.36, 16.57)),
           ((761, 463), (83.00, 25.32)), ((770, 380), (83.28, 27.47)), ((580, 383), (77.67, 27.49)),
           ((940, 553), (87.92, 22.30)), ((586, 525), (77.74, 23.48))], quad=True)

empire = deg([(70, 190), (150, 150), (250, 110), (330, 90), (390, 85), (440, 120), (480, 190), (540, 240),
              (600, 280), (660, 320), (720, 345), (780, 360), (840, 375), (900, 400), (960, 440), (1010, 465),
              (1040, 500), (1000, 600), (950, 640), (850, 720), (760, 800), (715, 835), (680, 852),
              (600, 885), (530, 895), (470, 885), (420, 850), (370, 780), (320, 680), (250, 600),
              (150, 520), (60, 470), (40, 330)])

m = Map(61.0, 91.2, 5.8, 36.6)
m.river("Ganges", "Indus", "Yamuna")
m.region(empire, "gold", alpha=0.42)

rock = [(65.71, 31.61), (72.165, 34.224), (73.20, 34.33), (77.85, 30.52), (70.48, 21.53), (72.79, 19.42),
        (85.84, 20.19), (84.83, 19.52), (77.58, 15.18), (76.95, 16.83), (76.81, 14.81), (76.66, 15.96),
        (76.18, 27.45), (80.07, 23.60), (84.03, 24.95)]
pillar = [(77.244, 28.636), (83.28, 27.47), (83.02, 25.38), (84.41, 27.10),
          (77.74, 23.48), (81.39, 25.34)]
for lon, lat in rock:
    m.mark(lon, lat, "s", ms=13)
for lon, lat in pillar:
    m.mark(lon, lat, "^", ms=15)

m.city(85.14, 25.61, "Pataliputra", dx=0.55, dy=0.45, star=True, bold=True, size=19)
m.label(84.2, 21.25, "KALINGA", fs=21)
m.label(65.71, 32.35, "Kandahar", size="small", colour="#2f2a26", fs=18)
m.label(77.244 - 0.5, 28.636 + 0.3, "Delhi", size="small", colour="#2f2a26", fs=18, ha="right")
m.label(83.28 - 0.4, 27.47 + 0.55, "Lumbini", size="small", colour="#2f2a26", fs=18, ha="right")
m.label(83.02 - 0.5, 25.38 - 0.45, "Sarnath", size="small", colour="#2f2a26", fs=18, ha="right")
m.label(78.3, 19.3, "ASHOKA'S EMPIRE", fs=25)
m.label(87.8, 26.6, "Ganges", size="sea", fs=19)
m.label(67.9, 28.2, "Indus", size="sea", fs=19)
m.label(77.4, 11.2, "kingdoms of\nthe far south", size="land", fs=19)
m.label(82.6, 7.6, "Sri Lanka", size="land", fs=19, ha="left")
m.label(65.5, 35.3, "lands of Seleucus", size="land", fs=19)
m.label(81.0, 31.5, "Himalaya", size="land", fs=19, rot=-22)
m.label(67.5, 15.0, "Arabian Sea", size="sea", fs=21)
m.label(87.3, 15.0, "Bay of\nBengal", size="sea", fs=21)
m.key([(("marker", "s"), "rock edict"), (("marker", "^", 15), "pillar")], loc="lower left", size=18)
m.scale(500, lon=85.0, lat=10.6)
m.save("chapters/20-ashoka/images/map_ashoka_empire.png")
