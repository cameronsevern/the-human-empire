#!/usr/bin/env python3
"""Chapter 30: the Abbasid caliphate about the year 800, with Baghdad, the older capital Damascus, and
the places the chapter names: Samarkand, Khwarazm, Basra, Mecca, and Cordoba in Spain, which was ruled
separately.

Replaces "Abbasids786-809" by Gabagool (Wikimedia Commons, CC BY 3.0), which had no names on it. The
extent is traced roughly by eye from that map, from Ifriqiya (Tunisia) to the Indus; Spain is drawn as
the emirate of Cordoba held it, without the Christian north. Morocco, under its own rulers from 788,
is left out. The areas are soft and approximate. Positions from English Wikipedia.
"""
from lib import Map, INK
from tracing import states, hatched

abbasid = [(5.5, 37.0), (10.0, 37.4), (11.2, 36.8), (11.0, 35.0), (12.5, 33.2), (15.0, 32.3), (20.0, 31.2),
           (25.0, 32.2), (29.0, 31.6), (32.0, 31.4), (34.6, 33.6), (35.8, 36.4), (37.5, 37.3), (40.0, 38.2),
           (42.0, 40.5), (44.0, 41.8), (46.5, 42.0), (49.0, 40.5), (50.0, 37.4), (53.5, 36.8), (54.0, 39.5),
           (56.0, 41.5), (58.5, 43.5), (61.0, 44.0), (64.5, 43.5), (68.0, 43.0), (71.0, 41.8), (71.5, 40.0),
           (70.5, 37.5), (71.2, 35.5), (70.5, 33.0), (71.0, 31.0), (72.0, 29.5), (70.6, 27.4), (69.6, 25.0),
           (68.6, 23.4), (66.6, 25.0), (61.0, 25.0), (57.0, 24.0), (60.5, 22.5), (59.0, 17.0), (52.0, 14.5),
           (44.0, 11.8), (42.0, 13.0), (37.5, 20.0), (36.8, 22.5), (30.0, 22.0), (25.0, 24.5), (20.0, 26.5),
           (15.0, 28.5), (10.0, 29.5), (6.0, 30.0)]
spain = [(-10.0, 36.8), (-9.6, 39.5), (-8.8, 41.2), (-6.0, 41.4), (-4.0, 41.6), (-1.5, 42.2), (1.5, 42.2),
         (3.4, 42.0), (2.0, 41.2), (0.2, 39.5), (-0.5, 38.0), (-2.0, 36.6), (-4.5, 36.4), (-5.6, 36.0), (-7.0, 36.6)]

m = Map(-10.5, 75.0, 13.0, 46.2)
m.river("Nile", "Tigris", "Euphrates", "Firat", "Indus", "Amu Darya", "Syr Darya", en=True)
states(m, [(abbasid, "green")], alpha=0.42)
hatched(m, spain, colour="blue", alpha=0.28)

m.label(45.8, 26.8, "THE ABBASID\nCALIPHATE", fs=24)
m.label(-4.2, 41.35, "SPAIN", fs=22)
m.label(-4.2, 39.7, "ruled separately", size="small", colour=INK, fs=19)
m.label(5.0, 33.3, "NORTH AFRICA", size="land", fs=21, style="normal")
m.label(27.5, 27.0, "EGYPT", size="land", fs=21, style="normal")
m.label(38.3, 35.3, "SYRIA", size="land", fs=19, style="normal")
m.label(45.5, 22.5, "ARABIA", size="land", fs=21, style="normal")
m.label(56.0, 31.5, "IRAN", size="land", fs=21, style="normal")
m.label(71.8, 21.0, "INDIA", size="land", fs=21, style="normal")
m.label(58.0, 42.4, "Khwarazm", size="small", colour=INK, fs=19)

m.city(44.37, 33.31, "Baghdad", dx=0.55, dy=-0.35, star=True, bold=True, size=22)
m.city(36.29, 33.51, "Damascus", dx=-0.5, dy=0.3, size=20)
m.city(47.78, 30.51, "Basra", dx=0.55, dy=-0.2, size=20)
m.city(39.83, 21.42, "Mecca", dx=-0.6, dy=0.0, size=20)
m.city(66.96, 39.65, "Samarkand", dx=0.0, dy=-1.1, size=20)
m.city(-4.78, 37.88, "Córdoba", dx=0.5, dy=0.0, size=20)
m.label(70.3, 25.4, "Indus", size="sea", fs=20, ha="left")
m.label(17.0, 35.0, "Mediterranean Sea", size="sea", fs=22)
m.label(62.0, 18.5, "Arabian Sea", size="sea", fs=22)
m.scale(1000, lon=-8.5, lat=14.4)
m.save("chapters/30-numbers/images/map_abbasid.png")
