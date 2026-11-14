#!/usr/bin/env python3
"""Chapter 10: the steppe, the belt of grassland from Hungary to the north-east of China.

The outline is traced by eye from "Eurasian steppe belt" by Mdf and Shattered Gnome
(Wikimedia Commons, public domain), which marks the WWF grassland ecoregions, and checked
against the WWF map of the Pontic-Caspian, Kazakh, Mongolian-Manchurian and Pannonian
steppes. It is approximate.
"""
from lib import Map

m = Map(12, 132, 30, 62)
m.river("Volga", "Don", "Danube", "Ural", en=True)
m.region([(17.5, 46.0), (18.5, 47.9), (21.0, 48.3), (22.6, 47.3), (21.6, 45.5), (19.0, 45.4)], "olive", alpha=0.5)   # Hungary
m.region([(27.5, 45.5), (28.0, 48.0), (32.0, 49.8), (37.0, 50.6), (42.0, 52.0), (48.0, 53.3), (54.0, 54.0),
          (60.0, 54.6), (66.0, 54.8), (73.0, 54.4), (78.0, 53.6), (82.0, 52.6), (85.0, 51.5), (89.0, 50.6),
          (93.0, 50.8), (98.0, 51.0), (104.0, 51.2), (110.0, 50.6), (115.0, 50.5), (119.0, 50.0), (122.0, 48.5),
          (124.5, 46.5), (124.0, 43.5), (120.0, 42.0), (116.0, 42.2), (112.0, 42.5), (108.0, 43.6), (103.0, 44.4),
          (98.0, 45.0), (93.0, 46.3), (88.0, 47.5), (83.0, 48.4), (78.0, 48.0), (72.0, 48.2), (66.0, 48.4),
          (60.0, 48.4), (55.0, 48.0), (51.0, 47.3), (47.0, 46.0), (45.0, 44.5), (41.0, 44.6), (38.0, 45.6),
          (35.0, 45.0), (32.0, 46.0)], "olive", alpha=0.5)

m.label(62.0, 51.4, "T H E   S T E P P E", size="region")
m.label(20.0, 49.4, "Hungary", size="land")
m.label(32.0, 51.6, "Ukraine", size="land")
m.label(68.0, 46.4, "Kazakhstan", size="land")
m.label(103.0, 47.6, "Mongolia", size="land")
m.label(110.0, 37.5, "China", size="land")
m.label(57.5, 58.0, "Urals", size="land")
m.label(43.0, 42.2, "Caucasus", size="land")
m.label(35.0, 43.4, "Black Sea", size="sea")
m.label(50.8, 41.6, "Caspian\nSea", size="sea")
m.label(46.5, 50.6, "Volga", size="sea", rot=-55)
m.label(39.8, 48.6, "Don", size="sea")
m.scale(1000)
m.save("chapters/10-wheel/images/map_steppe.png")
