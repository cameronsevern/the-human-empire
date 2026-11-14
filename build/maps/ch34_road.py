#!/usr/bin/env python3
"""Chapter 34: the road to Jerusalem, 1096 to 1099. The main land route of the First Crusade, from
the Rhineland down the Danube to Constantinople, across Turkey to Antioch and down the coast to
Jerusalem, with Clermont, where the crusade was preached.

Drawn for this chapter, which had no map. The route is the one taken by Godfrey's army as far as
Constantinople (by Regensburg, the Danube, Belgrade, Nish, Sofia and Adrianople), then the road of the
united army in 1097 to 1099 as given in English Wikipedia's article on the First Crusade: Nicaea,
Dorylaeum, Iconium, Heraclea, Caesarea, Marash, Antioch, then south along the coast by Tripoli and
Acre to Ramla and Jerusalem. Other leaders came by Italy and the sea, which is not shown. The names of
the two powers are placed by region only; no frontier is drawn. Positions from English Wikipedia.
"""
from lib import Map, INK

m = Map(1.0, 41.0, 29.9, 51.4)
m.river("Danube", "Rhine", "Rhein", "Euphrates", "Firat", "Nile", "Jordan", en=True)

west = [(5.1, 49.8), (7.0, 49.9), (8.3, 49.8), (10.5, 49.3), (12.1, 49.0), (14.3, 48.3), (16.4, 48.2),
        (17.8, 47.8), (19.0, 47.3), (19.6, 46.0), (20.46, 44.82), (21.2, 44.0), (21.9, 43.32),
        (23.32, 42.70), (24.75, 42.15), (26.56, 41.68), (28.0, 41.2), (28.98, 41.01)]
east = [(28.98, 41.01), (29.4, 40.8), (29.72, 40.43), (30.52, 39.79), (31.42, 38.36), (32.48, 37.87),
        (34.05, 37.51), (35.48, 38.72), (36.5, 38.02), (36.93, 37.58), (36.5, 36.9), (36.16, 36.20),
        (35.78, 35.52), (35.95, 34.60), (35.5, 33.89), (35.2, 33.27), (35.08, 32.93), (34.89, 32.5),
        (34.87, 31.93), (35.23, 31.78)]
m.route(west, colour="red", lw=4.2, arrow=False)
m.route(east, colour="red", lw=4.2, arrow=True)

m.city(3.08, 45.78, "Clermont", dx=0.7, dy=0.0, size=22, star=True, r=11, bold=True)
m.label(3.0, 44.85, "the call, 1095", size="small", colour=INK, fs=19, ha="left")
m.city(8.36, 49.63, None)
m.city(8.27, 50.00, None)
m.label(8.6, 50.85, "Worms and Mainz", size=21, colour=INK, fs=21, ha="center")
m.city(28.98, 41.01, "Constantinople", dx=-0.5, dy=0.75, size=21, bold=True, ha="right")
m.city(29.72, 40.43, "Nicaea", dx=-0.5, dy=-0.55, size=21, ha="right")
m.city(36.16, 36.20, "Antioch", dx=-0.55, dy=0.15, size=21)
m.city(38.79, 37.16, "Edessa", dx=0.0, dy=0.85, size=21)
m.city(35.23, 31.78, "Jerusalem", dx=0.5, dy=-0.45, size=21, bold=True)

m.label(5.5, 47.4, "FRANCE", size="land", fs=21, style="normal")
m.label(19.5, 49.4, "HUNGARY", size="land", fs=19, style="normal")
m.label(22.4, 39.7, "ROMAN\nEMPIRE", fs=23)
m.label(33.6, 40.25, "LANDS OF\nTHE TURKS", fs=23)
m.label(30.0, 30.55, "EGYPT", size="land", fs=21, style="normal")
m.label(25.3, 44.35, "Danube", size="sea", fs=19)
m.label(34.5, 43.0, "Black Sea", size="sea", fs=22)
m.label(19.0, 34.0, "Mediterranean Sea", size="sea", fs=22)
m.scale(500, lon=4.0, lat=31.0)
m.save("chapters/34-crusades/images/map_road_to_jerusalem.png")
