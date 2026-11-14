#!/usr/bin/env python3
"""Chapter 26: Faxian's journey (399 to about 413), out by land and home by sea, with the other
places named in the chapter.

Replaces "Buddhist Expansion" by Gunawan Kartapranata (Wikimedia Commons, CC BY-SA 3.0), whose routes
and dates ran far beyond the chapter. The route follows Faxian's own record as set out in English
Wikipedia's article on him and in Legge's translation (1886): the corridor to Dunhuang, the desert
to Shanshan, north to Agni, across the desert to Khotan, over the mountains to Swat and Gandhara,
down the Ganges plain to Pataliputra, by river to Tamralipti, by sea to Sri Lanka, and home by sea.
On the way home his ship put in at an island of the Indies (Java or Sumatra; scholars differ), so
the course through the Malacca Strait is schematic, and so is the course up the coast of China to
Shandong, where he landed. Positions from English Wikipedia.
"""
from lib import Map, INK

changan = (108.94, 34.34)
dunhuang = (94.66, 40.14)
khotan = (79.93, 37.11)
gandhara = (71.57, 34.01)
pataliputra = (85.14, 25.61)
tamralipti = (87.92, 22.30)

out = [changan, (103.8, 36.1), (100.45, 38.93), dunhuang, (88.17, 39.02), (86.57, 42.06), khotan, (77.42, 37.88),
       (75.23, 37.77), (73.6, 35.6), (72.4, 35.2), gandhara, (72.83, 33.75), (75.5, 31.0), (77.67, 27.49),
       (79.92, 27.06), (82.05, 27.51), (83.28, 27.47), pataliputra, tamralipti]
home = [tamralipti, (86.5, 18.5), (82.6, 12.5), (80.9, 9.4), (82.4, 6.0), (90.0, 5.8), (96.5, 6.4), (99.0, 4.6),
        (100.6, 3.0), (103.6, 1.3), (107.0, 5.0), (109.9, 12.0), (110.6, 17.0), (114.0, 21.3), (118.0, 24.2), (121.0, 28.0),
        (122.4, 31.0), (121.3, 34.6), (120.6, 36.2)]

m = Map(66.0, 124.0, 0.5, 44.6)
m.river("Ganges", "Indus", "Tarim")
m.route(out, colour="red", lw=3.4, arrow=False)
m.route(home, colour="red", lw=3.4, style=(0, (2.2, 1.4)))

m.city(*changan, "Chang'an", dx=0.0, dy=-1.2, bold=True, size=21)
m.city(*dunhuang, "Dunhuang", dx=0.0, dy=1.2, size=20)
m.city(*khotan, "Khotan", dx=0.0, dy=-1.2, size=20)
m.city(82.96, 41.72, "Kucha", dx=-0.7, dy=0.6, size=20)
m.city(*gandhara, "Gandhara", dx=-0.7, size=20)
m.city(*pataliputra, "Pataliputra", dx=0.7, dy=0.6, size=20)
m.city(73.48, 18.78, "Karla", dx=-0.7, size=20)
m.city(80.40, 8.31, None)
m.label(76.6, 7.4, "Sri Lanka", size="small", colour=INK, fs=20)
m.city(113.12, 40.11, "Yungang", dx=0.7, size=20)
m.city(112.47, 34.56, "Longmen", dx=0.7, size=20)
m.city(120.6, 36.2, None)
m.label(119.8, 37.4, "ashore", size="small", colour="red", fs=20, ha="right")
m.label(101.0, 40.4, "out by land", size="small", colour="red", fs=21)
m.label(93.5, 9.4, "home by sea", size="small", colour="red", fs=21)
m.label(84.4, 37.6, "desert of\ndunes", size="land", fs=21)
m.label(79.0, 34.0, "the highest\nmountains", size="land", fs=21)
m.label(80.6, 24.4, "Ganges", size="sea", fs=20)
m.label(78.5, 21.0, "INDIA", size="land", fs=26, style="normal")
m.label(110.0, 30.5, "CHINA", size="land", fs=26, style="normal")
m.label(71.0, 13.0, "Arabian Sea", size="sea", fs=22)
m.label(88.5, 14.5, "Bay of\nBengal", size="sea", fs=22)
m.label(115.0, 14.0, "South China\nSea", size="sea", fs=22)
m.scale(1000, lon=67.5, lat=2.0)
m.save("chapters/26-monks/images/map_faxian.png")
