#!/usr/bin/env python3
"""Chapter 65: eastern China about 1860. Canton and Hong Kong; the five ports opened in 1842 (Canton,
Xiamen, Fuzhou, Ningbo, Shanghai); the Yangzi and the Grand Canal, and Zhenjiang, the city at their
crossing, taken in 1842; Nanjing and, roughly, the land held by the Taiping about 1860; Beijing; and the
lands north of the Amur and east of the Ussuri taken by Russia in 1858 and 1860, with Vladivostok.

Drawn for this chapter, which had no map. The Grand Canal of the Ming and Qing is drawn through the towns
on it (Hangzhou, Suzhou, Zhenjiang, Yangzhou, Huai'an, Jining, Linqing, Dezhou, Tianjin, Tongzhou), as on
the maps in English Wikipedia's "Grand Canal (China)". The Taiping lands are a rough area, after the maps
in English Wikipedia's "Taiping Rebellion": the Yangzi valley from Anqing to Nanjing and the country
south-east of it about 1860 to 1861; their extent changed from year to year. The Russian gains follow the
Amur from the mouth of the Argun to the sea, and the Ussuri, Lake Khanka and the Tumen, after English
Wikipedia's "Treaty of Aigun" and "Convention of Peking". Positions from English Wikipedia.
"""
from lib import Map, INK, FILL

m = Map(106.0, 142.0, 20.6, 54.6)
m.river("Yangtze", "Huang", "Amur", "Heilong Jiang", "Argun’", "Xi", en=True)

# the lands taken by Russia
RUS = [(121.5, 53.33), (123.0, 53.5), (124.7, 53.15), (125.6, 52.9), (126.6, 51.6), (127.5, 50.25), (128.5, 49.55),
       (130.0, 48.85), (130.9, 47.9), (132.5, 47.7), (134.0, 48.3), (134.75, 48.4), (134.2, 47.4), (133.9, 46.8),
       (133.5, 46.0), (133.1, 45.3), (132.4, 45.0), (131.8, 44.9), (131.3, 44.2), (131.2, 43.4), (130.65, 42.42),
       (131.2, 42.2), (136.0, 43.6), (139.5, 47.0), (140.8, 50.5), (141.3, 52.2), (141.0, 55.0), (121.5, 55.0)]
m.region(RUS, "purple", alpha=0.34, smooth_n=3, hatch="//")
m.label(131.8, 51.8, "taken by Russia,\n1858 and 1860", fs=18, colour="#5d4470")
m.city(131.89, 43.12, "Vladivostok", dx=0.5, dy=-0.3)

# the Taiping lands about 1860
m.region([(115.9, 30.9), (117.0, 31.5), (118.0, 32.25), (118.9, 32.4), (119.8, 32.05), (120.6, 31.6), (120.95, 31.0),
          (120.6, 30.4), (119.6, 29.7), (118.2, 29.5), (116.8, 29.7), (115.8, 30.2)], "red", alpha=0.45, hatch="\\\\")
m.label(118.2, 29.0, "TAIPING", fs=17, colour="#8a3a2a")
m.label(118.2, 28.45, "about 1860", size="small", colour="#8a3a2a", fs=15)

# the Grand Canal
CANAL = [(120.15, 30.27), (120.75, 30.75), (120.62, 31.3), (120.3, 31.57), (119.97, 31.78), (119.45, 32.2),
         (119.42, 32.39), (119.45, 32.78), (119.3, 33.1), (119.02, 33.55), (118.28, 33.96), (117.95, 34.33),
         (117.73, 34.56), (116.8, 35.0), (116.59, 35.41), (116.3, 35.95), (115.7, 36.84), (116.3, 37.45),
         (116.85, 38.3), (117.2, 39.13), (116.66, 39.91)]
m.line(CANAL, colour="#7a4a2a", lw=3.2)
m.label(114.6, 36.4, "Grand Canal", size="small", colour="#7a4a2a", fs=18, rot=62)
m.label(111.0, 30.9, "Yangzi", size="sea", fs=20)
m.label(110.6, 35.6, "Yellow River", size="sea", fs=17)
m.label(127.0, 49.4, "Amur", size="sea", fs=17, rot=-35)

# places
m.city(116.40, 39.90, "Beijing", dx=-0.5, dy=0.35, bold=True, star=True, r=8)
m.city(118.80, 32.06, "Nanjing", dx=-0.45, dy=0.35, bold=True)
m.city(119.45, 32.20, "Zhenjiang, 1842", dx=0.45, dy=0.45)
for lon, lat, name, dx, dy in [(113.26, 23.13, "Canton", -0.45, 0.25), (118.09, 24.48, "Xiamen", 0.45, -0.25),
                               (119.30, 26.08, "Fuzhou", 0.45, -0.2), (121.55, 29.87, "Ningbo", 0.45, -0.25),
                               (121.47, 31.23, "Shanghai", 0.5, 0.0)]:
    m.mark(lon, lat, "s", ms=13)
    m.label(lon + dx, lat + dy, name, size="small", colour=INK, fs=16.5, ha="left" if dx > 0 else "right",
            style="normal")
m.city(114.17, 22.28, "Hong Kong, British 1842", dx=0.45, dy=-0.25, bold=True)

m.label(112.5, 33.6, "QING CHINA", size="land", fs=24, style="normal", spaced=True)
m.label(113.5, 52.6, "RUSSIA", size="land", fs=22, style="normal", spaced=True)
m.label(127.4, 40.4, "KOREA", size="land", fs=17, style="normal")
m.label(137.2, 36.6, "JAPAN", size="land", fs=17, style="normal")
m.label(121.0, 23.6, "Taiwan", size="land", fs=15)
m.label(116.0, 21.2, "South China Sea", size="sea", fs=18)
m.label(125.4, 29.2, "East China\nSea", size="sea", fs=18)
m.label(123.6, 35.6, "Yellow\nSea", size="sea", fs=18)
m.label(135.0, 41.2, "Sea of\nJapan", size="sea", fs=18)
m.key([(("marker", "s"), "ports opened to Britain in 1842")], loc="lower right", size=16)
m.scale(500, lon=107.0, lat=21.6)
m.save("chapters/65-opium/images/map_china_1860.png")
