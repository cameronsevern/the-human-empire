#!/usr/bin/env python3
"""Chapter 27: Europe and the Mediterranean in 476, the year Odoacer removed the last western emperor.

Drawn by eye after "Europe 476 A.D." by Alexander Keith Johnston (Wikimedia Commons, public domain),
the map this one replaces, and checked against the map of the west in 476 in Heather, The Fall of
the Roman Empire (2005), and English Wikipedia's articles on each kingdom. All borders are rough.
Departures from the old atlas: Provence goes to the Goths, who took Arles and Marseille in 476; the
Ostrogoths, who were on the move in the Balkans that year, are not given an area; and the peoples
beyond the Rhine and the Danube, whose lands had no fixed borders, are left unshaded. Sicily is
shown with Italy, which the Vandal king handed to Odoacer in 476 or 477 (all but one port).
"""
from lib import Map, INK
from tracing import states

vandal_africa = [(-1.2, 34.9), (3.0, 35.2), (6.0, 35.2), (8.0, 34.3), (9.6, 33.2), (11.5, 32.4), (13.5, 32.0),
                 (15.6, 31.0), (16.0, 32.0), (15.4, 34.5), (11.6, 37.6), (9.6, 37.7), (5.0, 37.3), (0.0, 36.4),
                 (-1.4, 35.9)]
vandal_islands = [(7.8, 38.6), (10.0, 38.6), (10.0, 41.0), (9.8, 43.2), (8.3, 43.2), (8.0, 41.0)]
balearics = [(1.0, 38.5), (4.6, 39.6), (4.3, 40.3), (2.2, 39.9), (1.2, 39.2)]
sueves = [(-10.0, 43.9), (-7.0, 43.8), (-6.0, 42.6), (-6.2, 41.2), (-7.0, 39.6), (-9.8, 38.9)]
goths = [(-9.8, 36.5), (-9.8, 38.9), (-7.0, 39.6), (-6.2, 41.2), (-6.0, 42.6), (-7.0, 43.8), (-1.8, 43.6),
         (-2.6, 47.3), (0.5, 47.4), (2.6, 47.2), (3.4, 46.4), (4.3, 45.2), (4.8, 44.3), (6.4, 43.9), (6.5, 43.0),
         (3.5, 42.6), (3.4, 41.8), (0.9, 40.5), (0.3, 38.6), (-1.0, 37.0), (-5.6, 35.8)]
burgundians = [(3.4, 46.4), (3.8, 47.9), (5.5, 48.1), (6.9, 47.5), (7.4, 46.5), (7.0, 45.6), (6.9, 44.8),
               (6.4, 43.9), (4.8, 44.3), (4.3, 45.2)]
roman_gaul = [(-1.6, 49.7), (1.5, 50.3), (2.7, 50.2), (4.3, 49.7), (5.0, 48.8), (5.5, 48.1), (3.8, 47.9),
              (2.6, 47.2), (0.5, 47.4), (-1.0, 47.6), (-1.8, 48.6)]
franks = [(1.5, 50.3), (2.5, 51.4), (4.5, 52.4), (6.8, 52.3), (8.6, 51.5), (8.4, 50.0), (6.6, 49.5), (5.0, 48.8),
          (4.3, 49.7), (2.7, 50.2)]
alamanni = [(5.5, 48.1), (5.0, 48.8), (6.6, 49.5), (8.4, 50.0), (10.0, 49.6), (11.2, 48.9), (10.3, 47.6),
            (9.4, 47.6), (7.6, 47.5), (6.9, 47.5)]
odoacer = [(7.6, 43.8), (6.9, 44.8), (7.0, 45.6), (7.4, 46.5), (7.6, 47.5), (9.4, 47.6), (10.3, 47.6),
           (12.5, 48.3), (15.6, 48.3), (16.4, 47.6), (15.4, 46.4), (14.0, 45.6), (13.6, 45.1), (14.0, 44.2),
           (16.5, 42.3), (19.2, 40.5), (18.6, 39.4), (16.3, 37.6), (15.7, 36.4), (12.1, 37.4), (12.0, 38.6),
           (11.0, 41.0), (10.1, 42.9), (8.7, 44.0)]
dalmatia = [(14.0, 45.6), (15.4, 46.4), (16.5, 45.3), (17.6, 44.9), (19.4, 43.6), (19.4, 42.0), (18.4, 42.2),
            (16.8, 43.1), (15.0, 44.2), (13.6, 45.1)]
east = [(19.4, 43.6), (19.7, 44.8), (22.5, 44.7), (24.0, 43.8), (26.0, 44.0), (28.2, 44.3), (29.7, 45.3),
        (31.5, 45.6), (32.0, 41.0), (32.0, 35.5), (23.0, 34.5), (19.3, 39.4), (19.4, 42.0)]
cyrenaica = [(19.5, 30.4), (32.0, 30.4), (32.0, 33.0), (23.0, 33.4), (19.8, 32.6)]

m = Map(-10.3, 31.0, 31.6, 55.2)
m.river("Rhine", "Danube", "Rhône", "Loire", en=True)
states(m, [(dalmatia, "red"), (roman_gaul, "red"), (east, "red"), (cyrenaica, "red"),
           (vandal_africa, "purple"), (vandal_islands, "purple"), (balearics, "purple"),
           (sueves, "olive"), (burgundians, "teal"), (franks, "blue"), (alamanni, "brown"),
           (goths, "gold"), (odoacer, "green")], alpha=0.45)

m.label(22.9, 43.1, "ROMAN\nEMPIRE", fs=28)
m.label(1.6, 48.8, "Roman", fs=19)
m.label(17.6, 44.0, "Roman", fs=19, rot=-35)
m.label(6.3, 35.75, "VANDALS", fs=24)
m.label(-3.6, 40.2, "GOTHS", fs=28)
m.label(-7.9, 42.2, "Sueves", fs=19, rot=-70)
m.label(5.7, 46.3, "BURGUNDIANS", fs=19, rot=-75)
m.label(5.3, 51.2, "FRANKS", fs=23)
m.label(8.4, 48.7, "Alamanni", fs=19)
m.label(12.6, 47.1, "ODOACER", fs=23)
m.label(1.0, 54.0, "Saxons", size="land", fs=21)
m.label(-4.6, 52.6, "Britons", size="land", fs=21)
m.label(12.0, 53.4, "peoples beyond the Rhine", size="land", fs=21)
m.city(12.48, 41.89, "Rome", dx=-0.35, dy=-0.3, bold=True, size=21)
m.city(12.20, 44.42, "Ravenna", dx=-0.4, size=20)
m.city(28.98, 41.01, "Constantinople", dx=-0.3, dy=0.5, ha="right", bold=True, size=21)
m.city(10.32, 36.85, "Carthage", dx=0.0, dy=0.55, size=20)
m.label(-5.0, 46.0, "Atlantic\nOcean", size="sea", fs=22)
m.label(5.0, 39.6, "Mediterranean Sea", size="sea", fs=22)
m.label(29.6, 43.6, "Black\nSea", size="sea", fs=21)
m.scale(500, lon=16.3, lat=33.7)
m.save("chapters/27-fall/images/map_europe_476.png")
