#!/usr/bin/env python3
"""Chapter 59: Europe in 1812, at the height of Napoleon's power. The French empire, with the lands annexed
to it (the Low Countries, the North Sea coast to Lübeck, the left bank of the Rhine, north-west Italy and
Rome, Catalonia, the Illyrian provinces); the states ruled by his family or allied to him (Spain, the
kingdom of Italy, Naples, the Confederation of the Rhine, the Duchy of Warsaw, Denmark, and Prussia and
Austria, which sent corps to Russia in 1812); his enemies Britain, Portugal and Russia. Paris, Madrid,
Berlin, Vienna and Moscow; the battles of Trafalgar and Austerlitz (1805), Leipzig (1813) and Waterloo
(1815); and the march from the Niemen to Moscow in 1812.

Drawn for this chapter, which had no map. The borders are rough, after the maps of Europe in 1812 in
English Wikipedia ("First French Empire", "Confederation of the Rhine", "Duchy of Warsaw", "Illyrian
Provinces") and the Times Atlas of European History. Switzerland, Sweden, Sicily, Sardinia and the
Ottoman lands are left unshaded. The march follows the usual line Kovno, Vilna, Vitebsk, Smolensk,
Borodino. Positions from English Wikipedia.
"""
from shapely.geometry import Polygon, box
from lib import Map, INK, FILL, smooth

m = Map(-11.0, 41.0, 35.5, 60.5)
m.river("Rhine", "Danube", "Elbe", "Vistula")


def P(pts):
    return Polygon(pts).buffer(0)


FE = P([(-1.8, 43.38), (0.0, 42.75), (0.4, 41.8), (0.4, 40.6), (1.5, 40.3), (7.5, 41.2), (9.25, 41.33), (10.5, 41.6),
        (12.0, 41.0), (13.1, 41.25), (13.6, 41.75), (13.4, 42.4), (13.9, 42.85), (13.0, 42.8), (12.6, 43.4),
        (12.2, 43.75), (11.6, 44.0), (11.0, 44.15), (10.4, 44.3), (10.45, 44.7), (10.5, 45.0), (9.15, 45.15),
        (8.65, 45.75), (8.6, 46.1), (8.4, 46.45), (7.9, 46.5), (7.1, 46.4), (6.9, 46.35), (6.15, 46.25), (6.1, 46.5),
        (6.5, 46.9), (7.0, 47.35), (7.6, 47.55), (7.6, 48.0), (8.2, 49.0), (8.45, 49.5), (8.27, 50.0), (7.6, 50.35),
        (6.96, 50.94), (6.77, 51.23), (6.62, 51.66), (8.0, 52.05), (9.0, 52.5), (10.0, 53.0), (10.6, 53.4),
        (10.9, 53.95), (10.95, 54.0), (10.25, 53.62), (9.5, 53.75), (8.9, 54.0), (8.4, 54.3), (5.0, 54.0),
        (2.0, 51.5), (0.5, 50.5), (-2.5, 49.9), (-5.5, 48.4), (-3.0, 45.0), (-1.8, 43.6)])
ILLYRIA = P([(13.55, 45.75), (13.6, 46.4), (12.4, 46.6), (12.4, 46.85), (13.9, 46.95), (14.2, 46.6), (15.0, 46.5),
             (15.6, 46.0), (15.7, 45.8), (16.3, 45.5), (16.6, 45.3), (17.0, 45.25), (16.9, 45.2), (16.0, 44.9),
             (16.0, 44.6), (16.3, 44.0), (17.3, 43.4), (18.5, 42.5), (18.6, 42.3), (18.0, 42.2), (14.0, 44.5),
             (13.3, 45.2), (13.4, 45.7)])
ITALY = P([(8.6, 46.1), (8.65, 45.75), (9.15, 45.15), (10.5, 45.0), (10.45, 44.7), (10.4, 44.3), (11.0, 44.15),
           (11.6, 44.0), (12.2, 43.75), (12.6, 43.4), (13.0, 42.8), (13.9, 42.85), (14.5, 43.4), (13.0, 44.9),
           (13.4, 45.6), (13.55, 45.75), (13.6, 46.4), (12.4, 46.6), (11.5, 46.75), (10.5, 46.6), (10.1, 46.4),
           (9.3, 46.5)])
NAPLES = P([(13.1, 41.25), (13.6, 41.75), (13.4, 42.4), (13.9, 42.85), (16.5, 42.5), (19.0, 40.3), (17.0, 38.6),
            (16.3, 37.6), (15.5, 37.7), (15.0, 38.5), (12.5, 40.5)]).difference(box(11.5, 36.3, 15.6, 38.32))
PORTUGAL = P([(-8.87, 41.87), (-8.2, 42.1), (-6.6, 41.95), (-6.2, 41.6), (-6.9, 41.0), (-6.9, 40.2), (-7.0, 39.6),
              (-7.5, 39.65), (-7.0, 39.0), (-7.3, 38.4), (-7.0, 38.0), (-7.45, 37.5), (-7.4, 37.17), (-7.5, 36.5),
              (-10.5, 36.5), (-10.5, 42.3)])
SPAIN = P([(-10.5, 36.0), (-5.6, 35.97), (-4.0, 36.3), (-1.0, 36.9), (1.0, 37.6), (4.5, 38.6), (4.5, 44.2),
           (-10.5, 44.2)]).difference(PORTUGAL).difference(FE)
PRUSSIA = P([(13.8, 53.85), (13.4, 53.4), (12.3, 53.0), (11.75, 53.0), (11.63, 52.13), (12.4, 52.0), (13.5, 51.9),
             (14.8, 51.9), (15.1, 51.3), (15.0, 50.9), (16.0, 50.6), (16.4, 50.2), (17.0, 50.25), (18.0, 50.0),
             (18.9, 50.3), (18.5, 51.0), (17.6, 51.3), (16.8, 51.6), (16.0, 52.0), (15.8, 52.5), (16.4, 53.1),
             (17.5, 53.2), (19.5, 53.3), (21.5, 53.2), (22.4, 53.6), (22.8, 54.3), (22.8, 55.0), (21.1, 55.75),
             (19.0, 55.5), (14.5, 54.4), (13.8, 54.2)])
WARSAW = P([(15.8, 52.5), (16.0, 52.0), (16.8, 51.6), (17.6, 51.3), (18.5, 51.0), (18.9, 50.3), (19.3, 50.0),
            (19.9, 49.95), (20.5, 50.1), (21.0, 50.25), (21.8, 50.6), (22.5, 50.6), (23.4, 50.4), (24.1, 50.6),
            (24.1, 51.0), (23.6, 51.6), (23.5, 52.2), (22.6, 52.6), (22.4, 52.9), (21.9, 53.2), (21.5, 53.2),
            (19.5, 53.3), (17.5, 53.2), (16.4, 53.1)])
AUSTRIA = P([(14.8, 50.9), (15.0, 50.9), (16.0, 50.6), (16.4, 50.2), (17.0, 50.25), (18.0, 50.0), (18.9, 50.3),
             (19.3, 50.0), (19.9, 49.95), (20.5, 50.1), (21.0, 50.25), (21.8, 50.6), (22.5, 50.6), (23.4, 50.4),
             (24.1, 50.6), (25.6, 50.0), (26.0, 49.4), (26.4, 48.4), (26.0, 47.8), (25.3, 47.3), (26.0, 46.5),
             (26.3, 45.6), (25.0, 45.4), (23.5, 45.3), (22.5, 44.6), (21.5, 44.8), (20.5, 44.8), (19.3, 44.9),
             (18.0, 45.1), (17.0, 45.25), (16.6, 45.3), (16.3, 45.5), (15.7, 45.8), (15.6, 46.0), (15.0, 46.5),
             (14.2, 46.6), (13.9, 46.95), (13.8, 47.6), (13.6, 48.2), (13.8, 48.8), (13.0, 49.3), (12.4, 49.8),
             (12.1, 50.3), (13.0, 50.4)])
SWEDEN = P([(12.66, 56.05), (12.75, 55.7), (12.85, 55.35), (14.4, 55.2), (19.5, 57.0), (20.0, 61.5), (12.5, 61.5),
            (12.3, 60.3), (11.8, 59.8), (11.27, 59.1), (10.9, 58.8), (11.3, 57.8), (12.4, 56.6)])
SWISS = P([(6.15, 46.25), (6.1, 46.5), (6.5, 46.9), (7.0, 47.35), (7.6, 47.55), (8.6, 47.7), (9.6, 47.55),
           (9.6, 47.1), (10.5, 46.85), (10.1, 46.4), (9.3, 46.5), (8.6, 46.1), (8.4, 46.45), (7.9, 46.5), (7.1, 46.4),
           (6.9, 46.35)])
DENMARK = P([(8.4, 54.3), (8.9, 54.0), (9.5, 53.75), (10.25, 53.62), (10.95, 54.0), (11.5, 54.3), (13.0, 54.9),
             (13.0, 56.0), (12.0, 57.5), (12.5, 61.5), (4.0, 61.5), (4.0, 57.0), (8.0, 55.0)]).difference(SWEDEN)
RHINE = box(5.5, 46.5, 15.6, 55.0)
for g in (FE, ITALY, ILLYRIA, AUSTRIA, PRUSSIA, WARSAW, DENMARK, SWISS, SWEDEN):
    RHINE = RHINE.difference(g)
RUSSIA = P([(29.7, 45.2), (28.2, 45.5), (28.1, 46.5), (27.3, 47.7), (26.6, 48.25), (26.4, 48.4), (25.5, 49.5),
            (23.0, 50.5), (22.0, 52.0), (21.0, 53.5), (20.5, 55.0), (21.1, 55.75), (20.0, 57.0), (19.5, 59.5),
            (20.0, 61.5), (42.0, 61.5), (42.0, 44.0), (30.5, 44.0)])
for g in (AUSTRIA, WARSAW, PRUSSIA, SWEDEN):
    RUSSIA = RUSSIA.difference(g)
BRITAIN = P([(-11.0, 51.0), (-5.5, 49.8), (0.0, 50.5), (1.0, 50.85), (1.6, 51.05), (2.0, 51.4), (2.0, 53.0),
             (-1.5, 61.5), (-11.0, 61.5)])

for g in (FE, ILLYRIA):
    m.region(g, "blue", alpha=0.45)
for g in (SPAIN, ITALY, NAPLES, RHINE, WARSAW, PRUSSIA, AUSTRIA, DENMARK):
    m.region(g, "gold", alpha=0.42)
for g in (BRITAIN, PORTUGAL, RUSSIA):
    m.region(g, "red", alpha=0.32)

# the march to Moscow
MARCH = [(23.9, 54.9), (25.28, 54.69), (28.0, 55.1), (30.2, 55.19), (32.05, 54.78), (35.82, 55.52), (37.5, 55.75)]
m.route(MARCH, colour=INK, lw=3.4)
m.label(28.6, 54.45, "June to September 1812", size="small", colour=INK, fs=16)

# the regions
m.label(2.4, 46.6, "FRENCH EMPIRE", fs=21)
m.label(-3.6, 39.6, "SPAIN", fs=21)
m.label(-3.6, 38.85, "under his brother Joseph", size="small", colour=INK, fs=15)
m.label(-8.0, 39.6, "PORTUGAL", fs=16, rot=90)
m.label(11.6, 45.35, "KINGDOM\nOF ITALY", fs=15)
m.label(15.9, 40.9, "NAPLES", fs=16)
m.label(11.2, 49.1, "CONFEDERATION\nOF THE RHINE", fs=16)
m.label(19.9, 52.1, "DUCHY OF\nWARSAW", fs=16)
m.label(21.0, 54.35, "PRUSSIA", fs=16)
m.label(15.6, 53.45, "PRUSSIA", fs=16)
m.label(22.3, 47.2, "AUSTRIA", fs=21)
m.label(9.2, 56.3, "DENMARK", fs=16, rot=0)
m.label(-2.0, 53.6, "BRITAIN", fs=19)
m.label(33.0, 51.6, "RUSSIA", fs=24)

# cities and battles
m.city(2.35, 48.86, "Paris", dx=-0.6, dy=0.4, bold=True)
m.city(-3.70, 40.42, "Madrid", dx=0.5, dy=0.35, bold=True)
m.city(13.40, 52.52, "Berlin", dx=-0.45, dy=0.35, bold=True)
m.city(16.37, 48.21, "Vienna", dx=0.5, dy=-0.4, bold=True)
m.city(37.62, 55.76, "Moscow", dx=0.0, dy=0.65, bold=True)
m.city(16.76, 49.15, "Austerlitz 1805", dx=0.5, dy=0.15, star=True, r=7)
m.city(-6.03, 36.18, "Trafalgar 1805", dx=0.5, dy=-0.3, star=True, r=7)
m.city(12.37, 51.34, "Leipzig 1813", dx=0.5, dy=-0.3, star=True, r=7)
m.city(4.40, 50.68, "Waterloo 1815", dx=0.5, dy=-0.4, star=True, r=7)

m.label(-6.8, 46.4, "ATLANTIC\nOCEAN", size="sea", fs=19)
m.label(5.5, 38.6, "Mediterranean Sea", size="sea", fs=18)
m.label(34.0, 43.3, "Black Sea", size="sea", fs=18)
m.label(4.2, 55.8, "North\nSea", size="sea", fs=17)
m.key([("blue", "French empire"), ("gold", "ruled by his family or allied to him"), ("red", "his enemies")],
      loc="lower right")
m.scale(300, lon=-10.5, lat=48.4)
m.save("chapters/59-napoleon/images/map_europe_1812.png")
