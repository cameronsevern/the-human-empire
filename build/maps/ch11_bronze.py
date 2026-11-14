#!/usr/bin/env python3
"""Chapter 11: the great kingdoms about 3,300 years ago.

Extents are approximate spheres of influence about 1300 BCE, drawn after the map by Enyavar
(Wikimedia Commons, CC BY-SA 4.0) that this one replaces, and the standard atlases.
"""
from lib import Map

m = Map(18.5, 53, 21.5, 43.5)
m.river("Nile", "Euphrates", "Tigris")

m.region([(20.6, 39.4), (23.6, 40.0), (24.6, 38.2), (26.8, 35.4), (24.0, 34.6), (21.4, 36.4), (20.8, 38.0)], "teal")
m.region([(27.5, 39.6), (31, 41.2), (36, 41.4), (40.3, 40.2), (41, 38), (39.2, 36.4), (37.6, 35.2), (36.9, 34.3),
          (35.9, 35.3), (34.2, 36.2), (31, 36.6), (28.6, 37.2)], "red")
m.region([(29.4, 31.2), (31.5, 31.7), (33.4, 31.2), (34.4, 31.5), (35.0, 33.1), (35.8, 34.7), (36.6, 34.5), (36.3, 32.8),
          (35.6, 31.0), (35.0, 29.6), (34.3, 28.2), (34.0, 26.4), (33.7, 24), (33.5, 21.8), (31.4, 21.8), (31.4, 24),
          (30.2, 27), (29.7, 29.6)], "gold")
m.region([(41.0, 37.3), (44.8, 37.3), (45.4, 35.6), (44.2, 34.3), (42.2, 34.6), (40.4, 36.0)], "blue")
m.region([(43.2, 34.0), (45.6, 33.9), (48.2, 31.2), (48.4, 30.0), (46.2, 30.0), (44.0, 31.4), (42.8, 33.0)], "purple")
m.region([(47.6, 33.2), (50.2, 32.6), (52.0, 30.2), (50.4, 29.0), (48.8, 30.4)], "brown")
m.region([(32.2, 35.4), (34.7, 35.8), (34.2, 34.5), (32.4, 34.6)], "olive")

m.label(34.2, 38.9, "HATTI")
m.label(28.6, 26.2, "EGYPT")
m.label(21.0, 40.9, "MYCENAEAN\nGREECE", ha="center")
m.label(44.9, 38.2, "ASSYRIA")
m.label(42.0, 31.0, "BABYLON")
m.label(51.0, 31.9, "ELAM")
m.label(33.0, 33.9, "Cyprus", size="land")
m.label(25.0, 33.6, "Crete", size="land")
m.label(27.5, 32.4, "Mediterranean Sea", size="sea")
m.label(34.5, 42.6, "Black Sea", size="sea")
m.label(37.4, 23.4, "Red\nSea", size="sea")
m.label(50.6, 27.4, "Gulf", size="sea")
m.label(41.5, 26.5, "ARABIA", size="land")

m.city(34.62, 40.02, "Hattusa", dx=0.5, dy=0.45)
m.city(35.78, 35.60, "Ugarit", dx=0.5, dy=-0.1)
m.city(22.76, 37.73, "Mycenae", dx=0.45, dy=-0.5)
m.city(26.24, 39.96, "Troy", dx=0.5)
m.city(31.25, 29.85, "Memphis", dx=-0.5)
m.city(32.64, 25.70, "Thebes", dx=-0.5)
m.city(44.42, 32.54, "Babylon", dx=-0.5, dy=-0.2)
m.city(43.26, 35.46, "Ashur", dx=-0.5, dy=0.1)
m.scale(500)
m.save("chapters/11-bronze/images/map_great_kingdoms.png")
