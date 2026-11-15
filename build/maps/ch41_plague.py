#!/usr/bin/env python3
"""Chapter 41: the spread of the Black Death, 1338 to 1353. From the graves at Lake Issyk-Kul (off the
map to the east) to the Italian ports on the Black Sea, then by sea to Constantinople, Messina and
Alexandria, and on to the rest of Europe, with the year it reached each place. Siena, Strasbourg and
Ragusa, which the chapter also names, are marked without a year.

Drawn for this chapter, which had no map. Dates of arrival as given in the chapter; Cairo is given 1348,
the spring after the plague reached Alexandria (to be confirmed in the fact check). The Black Sea ports are Caffa in the
Crimea and Tana on the Don. The English harbour is Melcombe (Weymouth). The sea routes are drawn as
simple arrows, not as the tracks of particular ships. Positions from English Wikipedia.
"""
from lib import Map, INK

m = Map(-11.0, 56.0, 27.5, 63.0)
m.river("Volga", "Don", "Dnieper", "Danube", "Rhine", "Rhône", "Seine", "Nile", "Thames", "Po", "Arno", en=True, lw=1.4)

SEA = "red"
# by sea, 1346 to 1349
m.route([(35.38, 45.03), (33.0, 43.6), (30.4, 42.2), (29.2, 41.3)], colour=SEA)
m.route([(28.6, 40.7), (26.2, 40.1), (25.0, 38.6), (24.3, 36.9), (23.0, 35.8), (21.0, 36.1), (18.5, 37.2), (16.0, 38.0)], colour=SEA)
m.route([(25.6, 39.4), (26.1, 37.6), (27.4, 35.6), (29.0, 33.2), (29.8, 31.7)], colour=SEA)
m.route([(15.2, 38.5), (13.0, 40.0), (10.4, 41.6), (7.6, 42.8), (5.8, 43.1)], colour=SEA)
m.route([(-1.6, 50.3), (1.6, 52.6), (3.2, 56.2), (4.6, 59.6)], colour=SEA)
# overland from Central Asia
m.route([(56.0, 46.2), (50.5, 46.6), (45.0, 47.4), (40.2, 47.2)], colour=INK, lw=2.6, style=(0, (4, 2.5)))
m.label(55.4, 47.6, "from Lake\nIssyk-Kul, 1338", size="small", colour=INK, fs=17, ha="right")

m.city(35.38, 45.03, None)
m.city(39.42, 47.21, None)
m.label(38.2, 48.6, "Black Sea\nports 1346", size=17, colour=INK, fs=17)

m.city(28.98, 41.01, "Constantinople 1347", dx=0.6, dy=0.55, ha="left")
m.city(15.55, 38.19, "Messina 1347", dx=-0.3, dy=-0.9, ha="right")
m.city(29.92, 31.20, "Alexandria 1347", dx=-0.6, dy=0.0)
m.city(31.24, 30.04, "Cairo 1348", dx=0.6, dy=-0.3, ha="left")
m.city(5.37, 43.30, "Marseille 1348", dx=-0.6, dy=-0.2)
m.city(11.25, 43.77, "Florence 1348", dx=-0.5, dy=0.6, ha="right")
m.city(11.33, 43.32, "Siena", dx=0.55, dy=-0.25, ha="left")
m.city(2.35, 48.86, "Paris 1348", dx=0.0, dy=-0.75)
m.city(-2.46, 50.61, None)
m.label(-2.6, 49.6, "English coast\n1348", size=17, colour=INK, fs=17, ha="right")
m.city(5.32, 60.39, "Norway 1349", dx=0.6, dy=0.1, ha="left")
m.city(37.62, 55.76, "Moscow 1353", dx=0.6, dy=0.0, ha="left")
m.city(7.75, 48.58, "Strasbourg", dx=0.55, dy=0.25, ha="left")
m.city(18.09, 42.65, "Ragusa", dx=0.5, dy=0.5, ha="left")

m.label(18.5, 34.6, "Mediterranean Sea", size="sea", fs=19)
m.label(34.6, 43.4, "Black Sea", size="sea", fs=17)
m.label(4.0, 55.5, "North\nSea", size="sea", fs=17, ha="right")
m.label(-7.5, 45.5, "ATLANTIC\nOCEAN", size="sea", fs=18)
m.label(51.0, 41.6, "Caspian", size="sea", fs=16, rot=-80)
m.scale(500, lon=44.0, lat=29.0)
m.save("chapters/41-plague/images/map_plague.png")
