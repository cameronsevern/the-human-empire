#!/usr/bin/env python3
"""Chapter 45: Europe about 1600 by religion: Catholic, Lutheran, Reformed (Calvinist), the Church of
England, Orthodox, and the lands under Ottoman rule in the south-east. With the towns the chapter names.

Drawn for this chapter, which had no map. The areas are soft and approximate, following the divisions
usually shown on maps of religion in Europe about 1600 (as in English Wikipedia's article "Reformation"). Mixed lands are given to
their leading church: Bohemia and Silesia, where most people were Protestant though their kings were
Catholic, are shown with the Lutheran north; Transylvania, with its many churches, as Reformed; the
Huguenot towns of France and the Protestant minorities of Poland and Austria are not shown. The
Orthodox area includes the Orthodox lands of Poland-Lithuania and the principalities of Moldavia and
Wallachia, which paid tribute to the sultan. Positions from English Wikipedia.
"""
import numpy as np
import lib
from lib import Map, INK, FILL
from matplotlib.patches import Polygon as MplPoly
from tracing import states

england = [(-6.0, 49.8), (1.9, 50.8), (2.0, 52.9), (0.3, 53.7), (-1.6, 55.7), (-2.6, 55.4), (-3.3, 54.95),
           (-4.9, 54.4), (-5.4, 53.4), (-5.5, 51.7)]
scotland = [(-3.3, 54.95), (-1.8, 55.7), (-1.0, 59.2), (-8.0, 59.2), (-7.8, 56.0), (-6.4, 55.6), (-5.6, 55.2),
            (-5.0, 54.7)]
dutch = [(3.3, 51.45), (4.6, 51.3), (6.0, 51.75), (7.1, 52.2), (7.25, 53.3), (6.6, 53.8), (4.6, 53.4), (3.8, 52.1)]
swiss = [(5.9, 46.1), (6.2, 46.9), (7.4, 47.55), (8.6, 47.75), (9.5, 47.55), (9.2, 47.1), (8.0, 46.75),
         (7.0, 46.35), (6.3, 46.2)]
transylvania = [(21.4, 46.6), (22.6, 47.9), (24.6, 47.7), (25.8, 46.6), (25.2, 45.6), (23.6, 45.4), (22.0, 45.8)]
lutheran = [(7.1, 53.8), (8.3, 52.3), (8.5, 51.2), (9.1, 50.4), (8.8, 49.4), (8.4, 48.6), (9.5, 48.2),
            (10.3, 48.6), (11.4, 49.0), (12.6, 49.4), (13.8, 48.7), (15.2, 48.9), (16.6, 49.4), (18.6, 50.0),
            (18.3, 51.5), (16.4, 52.4), (16.0, 53.4), (17.6, 54.9), (19.5, 57.0), (23.0, 59.6), (28.0, 60.6),
            (30.0, 62.0), (30.5, 66.0), (4.0, 66.0), (4.0, 58.0), (7.6, 57.4), (8.0, 55.0), (8.5, 54.2)]
baltic = [(19.2, 54.45), (20.0, 53.5), (22.6, 53.8), (22.9, 54.5), (21.4, 55.3), (21.0, 56.2), (24.0, 56.4),
          (26.5, 55.8), (28.0, 56.3), (27.8, 57.6), (28.2, 59.4), (23.5, 59.6), (21.4, 57.6), (20.4, 55.0)]
ottoman = [(15.6, 44.2), (15.9, 45.0), (16.8, 45.4), (17.6, 45.9), (18.2, 46.7), (19.0, 47.7), (20.6, 48.0),
           (21.6, 47.3), (21.3, 46.4), (22.2, 45.0), (22.7, 44.3), (25.0, 43.6), (27.2, 44.0), (29.4, 45.2),
           (30.4, 46.7), (32.0, 47.0), (34.5, 47.5), (38.0, 47.4), (41.5, 47.0), (41.5, 35.0), (28.0, 35.6),
           (26.0, 36.1), (23.0, 36.0), (21.0, 37.0), (19.6, 39.8), (19.3, 41.8), (18.3, 42.5), (17.3, 43.2)]
orthodox = [(23.4, 51.0), (23.8, 52.5), (25.5, 53.8), (27.0, 55.2), (28.0, 56.2), (27.0, 57.6), (26.5, 59.4),
            (27.5, 61.0), (27.5, 64.0), (46.0, 64.0), (46.0, 46.0), (40.0, 46.6), (35.0, 46.4), (31.0, 46.0),
            (29.6, 45.4), (27.0, 43.9), (25.0, 43.5), (22.6, 44.0), (21.6, 45.0),
            (22.4, 45.9), (24.0, 46.0), (25.0, 46.5), (24.4, 47.8), (23.6, 48.6), (23.0, 49.4)]
catholic = [(-11.0, 36.2), (-6.6, 35.98), (-5.5, 36.0), (-2.0, 36.35), (0.5, 36.5), (5.0, 37.2), (9.5, 37.85),
            (12.0, 37.65), (14.0, 36.4), (16.5, 36.3), (19.0, 39.5), (19.8, 42.5), (17.0, 44.5), (19.5, 45.6),
            (22.6, 47.2), (24.0, 48.5), (27.0, 50.0), (28.0, 56.5), (22.0, 57.0), (14.0, 56.0), (8.0, 56.0),
            (-4.0, 56.0), (-11.0, 56.0)]

m = Map(-10.5, 40.0, 36.0, 62.5)
m.river("Rhine", "Danube", "Elbe", "Vistula", "Rhône", "Seine", "Thames", "Dnieper", "Po", en=True, lw=1.3)
states(m, [(england, "red"), (scotland, "green"), (dutch, "green"), (swiss, "green"), (transylvania, "green"),
           (lutheran, "blue"), (baltic, "blue"), (ottoman, "brown"), (orthodox, "purple"), (catholic, "gold")],
       alpha=0.45)
for _, r in lib._lakes.iterrows():
    if (r.get("scalerank", 0) or 0) > 3:
        continue
    g = r.geometry.intersection(m.clip)
    for p in getattr(g, "geoms", [g]):
        if not p.is_empty and p.geom_type == "Polygon":
            m.ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=lib.SEA, ec=lib.SHORE, lw=0.7, zorder=2.3))

m.label(-3.6, 40.0, "CATHOLIC", fs=21)
m.label(2.0, 46.6, "CATHOLIC", fs=21)
m.label(20.6, 52.2, "CATHOLIC", fs=21)
m.label(15.6, 60.6, "LUTHERAN", fs=21)
m.label(10.9, 53.5, "LUTHERAN", fs=19)
m.label(-1.4, 52.6, "CHURCH OF\nENGLAND", fs=19)
m.label(-4.1, 57.3, "REFORMED", fs=19)
m.label(5.6, 52.75, "Reformed", size="small", colour=INK, fs=18)
m.label(8.6, 47.15, "Reformed", size="small", colour=INK, fs=17)
m.label(23.7, 46.75, "Reformed", size="small", colour=INK, fs=18)
m.label(33.5, 55.0, "ORTHODOX", fs=21)
m.label(25.8, 41.8, "OTTOMAN\nRULE", fs=21)

m.city(12.65, 51.87, "Wittenberg", dx=0.5, dy=0.15, bold=True)
m.city(11.63, 52.13, "Magdeburg", dx=-0.5, dy=0.15)
m.city(8.27, 50.00, "Mainz", dx=-0.5, dy=0.0)
m.city(10.90, 48.37, "Augsburg", dx=0.5, dy=-0.3)
m.city(14.42, 50.09, "Prague", dx=0.5, dy=-0.2)
m.city(11.12, 46.07, "Trent", dx=0.5, dy=-0.2)
m.city(6.15, 46.20, "Geneva", dx=-0.5, dy=-0.2)
m.city(12.50, 41.90, "Rome", dx=0.5, dy=0.2, bold=True)
m.city(2.35, 48.86, "Paris", dx=0.5, dy=0.15)
m.city(-0.13, 51.51, "London", dx=0.5, dy=-0.3)

m.label(-8.0, 46.5, "ATLANTIC\nOCEAN", size="sea", fs=19)
m.label(3.0, 55.6, "North Sea", size="sea", fs=18)
m.label(19.4, 55.9, "Baltic", size="sea", fs=17, rot=60)
m.label(5.0, 39.0, "Mediterranean Sea", size="sea", fs=19)
m.label(34.0, 43.4, "Black Sea", size="sea", fs=18)
m.scale(500, lon=33.5, lat=37.0)
m.save("chapters/45-reformation/images/map_religion_1600.png")
