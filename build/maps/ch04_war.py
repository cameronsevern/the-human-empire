#!/usr/bin/env python3
"""Chapter 4: Nataruk, beside Lake Turkana in the north of Kenya.

Nataruk at 2.707 N, 36.142 E (English Wikipedia). Drawn to replace the Commons
location map by Uwe Dedering (CC BY-SA 3.0) with a dot added.
"""
from lib import Map

m = Map(33.0, 42.8, -2.6, 5.8)
m.river("Omo", "Nile", "Victoria Nile", "Albert Nile")

m.city(36.142, 2.707, "Nataruk", dx=-0.25, size="region", bold=True)
m.label(36.45, 3.75, "Lake\nTurkana", size="sea", ha="left")
m.label(33.45, -1.1, "Lake\nVictoria", size="sea")
m.label(41.95, -1.75, "Indian\nOcean", size="sea")
m.label(38.6, 1.0, "KENYA", size="land", spaced=True)
m.label(39.6, 5.4, "ETHIOPIA", size="land", spaced=True)
m.label(33.9, 2.4, "UGANDA", size="land", spaced=True)
m.label(36.55, 5.6, "Omo", size="sea", ha="left")
m.city(36.82, -1.29, "Nairobi", dx=0.22, size="small")
m.scale(100, lon=38.6, lat=-2.2)
m.save("chapters/04-war/images/map_nataruk.png")
