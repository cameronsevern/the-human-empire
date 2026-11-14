#!/usr/bin/env python3
"""Chapter 5: the spread of farming from the Middle East across Europe.

Areas and dates are traced by eye from "Expansion of farming in western Eurasia,
9600-4000 cal BC" by Gronenborn, Horejs, Börner and Ober (LEIZA/ÖAI 2023, CC BY-SA 4.0),
checked against the map in Shennan, The First Farmers of Europe (2018). Its dates BC are
turned into years ago (BC + 2,000) and rounded; Greece is given as the chapter gives it.
Only the main areas are shown.
"""
from lib import Map, INK

m = Map(-11, 47, 30.5, 60)
m.region([(34.6, 31.0), (35.3, 33.5), (36.4, 36.3), (38.5, 37.9), (41.0, 37.9), (43.5, 37.1), (45.6, 35.5),
          (46.6, 33.9), (45.5, 33.5), (43.5, 35.2), (40.5, 36.0), (38.0, 35.7), (36.8, 33.8), (36.0, 31.0)], "red", alpha=0.55)
m.region([(31.5, 37.2), (32.8, 38.7), (35.0, 38.7), (35.6, 37.6), (33.5, 36.9)], "red", alpha=0.55)
# about 8,500 and 8,000 years ago
m.region([(20.3, 39.6), (22.3, 41.0), (24.5, 41.3), (26.4, 41.0), (26.2, 40.2), (24.0, 38.0), (22.9, 36.4),
          (21.4, 36.9), (21.0, 38.5)], "gold", alpha=0.55)
m.region([(26.6, 38.0), (27.2, 40.4), (29.8, 40.9), (30.6, 38.6), (28.4, 37.1)], "gold", alpha=0.55)
m.region([(20.6, 41.4), (20.0, 44.4), (22.6, 45.0), (26.0, 44.4), (28.6, 43.9), (28.0, 42.0), (26.2, 41.5), (23.5, 41.5)], "gold", alpha=0.4)
m.region([(15.0, 41.9), (16.6, 41.3), (18.6, 40.3), (18.1, 39.7), (16.4, 38.6), (15.6, 40.0), (14.6, 41.0)], "gold", alpha=0.4)
# about 7,700 to 7,000 years ago
m.region([(17.5, 46.0), (18.5, 47.8), (21.5, 48.3), (23.0, 47.2), (22.0, 45.3), (19.5, 45.1)], "green", alpha=0.5)
m.region([(14.5, 47.9), (17.5, 48.1), (19.5, 48.9), (21.5, 50.1), (20.0, 51.8), (16.0, 52.5), (12.0, 52.3), (8.0, 51.6),
          (6.0, 50.6), (6.6, 49.1), (9.0, 48.4), (12.0, 48.3)], "green", alpha=0.5)
m.region([(-1.5, 48.0), (0.5, 49.6), (3.5, 49.9), (5.6, 48.9), (4.5, 47.2), (1.5, 46.9), (-1.0, 47.2)], "green", alpha=0.35)
m.region([(8.6, 44.5), (6.0, 43.6), (3.2, 43.7), (2.6, 42.2), (0.6, 41.0), (-0.6, 39.2), (-1.4, 37.6), (-0.4, 38.4),
          (0.5, 40.4), (3.0, 41.9), (5.5, 43.2), (8.4, 44.1)], "green", alpha=0.35)
# about 6,000 years ago
m.region([(-10.6, 51.4), (-10.4, 55.5), (-6.0, 58.8), (-2.6, 58.9), (0.2, 53.5), (1.9, 52.8), (1.6, 51.0),
          (-5.9, 49.8), (-8.0, 51.2)], "blue", alpha=0.45)
m.region([(7.8, 54.9), (7.9, 57.3), (10.6, 57.9), (12.6, 56.6), (14.6, 56.3), (14.6, 55.2), (11.0, 54.3)], "blue", alpha=0.45)

m.route([(37.5, 37.4), (33.5, 39.4), (29.8, 40.0), (26.2, 41.0), (22.8, 43.2), (20.0, 45.6), (16.5, 48.2), (11.0, 49.9),
         (5.5, 50.2), (1.0, 50.6), (-1.5, 52.6)], "red", lw=3.0)

N = 17
m.note(41.0, 36.7, "11,500", size=N)
m.note(33.8, 37.75, "10,000", size=N)
m.note(25.3, 38.9, "8,500", size=N)
m.note(26.0, 43.3, "8,000", size=N)
m.note(16.7, 40.3, "8,000", size=N)
m.note(21.2, 46.9, "7,700", size=N)
m.note(15.0, 51.0, "7,400", size=N)
m.note(2.2, 48.3, "7,000", size=N)
m.note(4.2, 41.6, "7,500", size=N)
m.note(-3.0, 54.5, "6,000", size=N)
m.note(10.1, 56.2, "6,000", size=N)

m.label(37.0, 39.6, "Turkey", size="land")
m.label(19.6, 38.0, "Greece", size="land")
m.label(-2.0, 57.2, "Britain", size="land")
m.label(25.0, 33.6, "Mediterranean Sea", size="sea")
m.label(34.5, 43.3, "Black Sea", size="sea")
m.label(-8.0, 46.0, "Atlantic\nOcean", size="sea")
m.label(36.0, 56.4, "When farming arrived,\nin years ago", fs=19, colour=INK)
m.scale(500, lon=-9.5, lat=32.0)
m.save("chapters/05-farming/images/map_farming_europe.png")
