#!/usr/bin/env python3
"""Chapter 66: Japan and its neighbours about 1905. Japan, with the Ryukyu islands and Taiwan (Japanese
from 1895), the two south-western domains that made the revolution (Satsuma and Choshu), Tokyo, Kyoto and
Nagasaki; Korea; Port Arthur on the Chinese coast, where the war with Russia began in 1904; and the strait
of Tsushima, with the last stage of the Russian fleet's voyage from the south in May 1905.

Drawn for this chapter, which had no map. The domains are drawn roughly as the provinces they held:
Satsuma as Satsuma and Osumi (the mainland of the modern Kagoshima prefecture), Choshu as Nagato and Suo
(the modern Yamaguchi prefecture). The fleet's track is simplified, after the maps in English
Wikipedia's articles "Battle of Tsushima" and "Voyage of the Second Pacific Squadron": from the South
China Sea past Taiwan and through the East China Sea to the strait. Positions from English Wikipedia.
"""
from lib import Map, INK, FILL

m = Map(116.5, 146.0, 21.0, 44.5)
japan = [(122.8, 24.0), (125.5, 24.0), (131.5, 27.0), (132.2, 30.0), (136.0, 33.0), (141.0, 34.5), (142.5, 37.5),
         (142.5, 41.0), (146.5, 42.5), (146.5, 45.6), (141.5, 45.6), (139.5, 42.0), (138.5, 39.0), (136.0, 37.5),
         (132.5, 36.0), (130.5, 35.0), (129.6, 35.0), (129.0, 34.5), (128.8, 33.5), (128.0, 32.0), (127.5, 27.5),
         (122.8, 24.8)]
taiwan = [(119.2, 21.7), (122.3, 21.7), (122.3, 25.5), (119.2, 25.5)]
m.region(japan, "gold", alpha=0.45, smooth_n=4)
m.region(taiwan, "gold", alpha=0.45, smooth_n=4)
satsuma = [(130.15, 32.1), (130.6, 32.15), (131.0, 31.9), (131.35, 31.45), (131.1, 30.95), (130.65, 31.0),
           (130.2, 31.25), (130.1, 31.7)]
choshu = [(130.85, 34.35), (130.9, 34.0), (131.4, 33.9), (132.1, 33.95), (132.3, 34.2), (132.0, 34.6),
          (131.6, 34.7), (131.2, 34.6)]
m.region(satsuma, "red", alpha=0.6)
m.region(choshu, "red", alpha=0.6)

# the Russian fleet, May 1905
m.route([(117.0, 21.6), (121.5, 21.2), (124.0, 22.0), (125.6, 24.5), (126.4, 27.0), (127.4, 30.0),
         (128.6, 32.7), (129.45, 33.95)], colour=INK, lw=3.0, style=(0, (3, 2)))

m.city(139.69, 35.69, "Tokyo", dx=0.4, dy=-0.45, bold=True)
m.city(135.77, 35.01, "Kyoto", dx=0.0, dy=0.65, bold=True)
m.city(129.87, 32.75, "Nagasaki", dx=-0.4, dy=0.0)
m.city(121.26, 38.81, "Port Arthur", dx=-0.4, dy=0.35, bold=True)
m.label(131.95, 31.15, "SATSUMA", fs=17, ha="left")
m.label(132.6, 34.55, "CHŌSHŪ", fs=17, ha="left")
m.label(139.6, 38.6, "JAPAN", fs=26)
m.label(127.6, 39.6, "KOREA", fs=22)
m.label(120.4, 35.0, "CHINA", size="land", fs=22, style="normal", spaced=True)
m.label(127.0, 43.4, "MANCHURIA", size="land", fs=18, style="normal")
m.label(134.6, 44.0, "RUSSIA", size="land", fs=18, style="normal")
m.label(121.7, 24.0, "TAIWAN", fs=18, ha="left")
m.label(121.75, 23.35, "Japanese\nfrom 1895", size="small", colour=INK, fs=15, ha="left")
m.label(129.75, 35.75, "strait of\nTsushima", size="sea", fs=17, ha="left")
m.label(125.9, 29.2, "Russian fleet,\nMay 1905", size="small", colour=INK, fs=16, ha="right")
m.label(134.5, 40.4, "Sea of Japan", size="sea", fs=20)
m.label(123.2, 35.8, "Yellow\nSea", size="sea", fs=19)
m.label(125.0, 31.6, "East China\nSea", size="sea", fs=19)
m.label(140.0, 28.5, "Pacific Ocean", size="sea", fs=22)
m.label(118.5, 21.8, "from the\nIndian Ocean", size="small", colour=INK, fs=15)
m.scale(500, lon=139.0, lat=22.3)
m.save("chapters/66-meiji/images/map_japan.png")
