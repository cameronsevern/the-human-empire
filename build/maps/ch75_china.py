#!/usr/bin/env python3
"""Chapter 75: China about 1926. The Nationalist base round Canton, the march north of 1926 and 1927 to
Wuchang, Nanjing and Shanghai, the north held by rival warlords, Beijing, Shandong, Hunan, Manchuria
(seized by Japan in 1931), and the Long March of 1934 to 1935 as a dashed line.

Drawn for this chapter, which had no map. The chapter names no single warlord, so the warlord lands are
given one general label rather than drawn as separate territories. The Nationalist base is drawn roughly as
the province of Guangdong. Manchuria is drawn roughly as the three north-eastern provinces. The march north
is simplified to its two main thrusts, after the maps in English Wikipedia's "Northern Expedition":
Canton, Shaoguan, Hengyang, Changsha, Wuchang; and Shaoguan, Ganzhou, Nanchang, then down the Yangzi to
Nanjing and through Hangzhou to Shanghai. The Long March is the route of the Central Red Army, simplified
after the map in English Wikipedia's "Long March": Ruijin, the Xiang river, Zunyi, the loop into Yunnan,
the Jinsha crossing at Jiaopingdu, Luding bridge on the Dadu, the Jiajin mountain, the grasslands at
Maoergai, Hadapu, and Wuqi in northern Shaanxi. Positions from English Wikipedia.
"""
from lib import Map, INK, FILL

m = Map(96.0, 132.0, 18.0, 47.0)

canton_base = [(109.7, 21.5), (110.4, 20.3), (111.0, 21.4), (112.5, 21.8), (114.2, 22.2), (116.5, 22.9), (117.2, 23.6),
               (116.5, 24.6), (115.6, 24.9), (114.6, 25.2), (113.5, 25.5), (112.5, 25.2), (111.8, 24.6), (111.4, 23.8),
               (110.6, 22.6), (109.6, 22.2)]
m.region(canton_base, "red", alpha=0.45)
manchuria = [(119.3, 40.0), (121.2, 38.7), (124.3, 39.9), (126.5, 41.4), (129.0, 42.3), (130.6, 42.4), (131.2, 43.5),
             (131.0, 44.9), (133.5, 45.5), (135.0, 48.3), (132.5, 47.8), (130.8, 48.9), (127.6, 49.8), (125.5, 53.0),
             (121.5, 53.3), (120.5, 50.5), (121.0, 47.0), (122.0, 45.0), (120.5, 43.0), (119.3, 41.5)]
m.region(manchuria, "brown", alpha=0.32, hatch="//")

m.river("Chang Jiang", "Yangtze", "Jinsha", "Huang", "Xi", lw=1.6)

# the march north, 1926 to 1927
m.route([(113.26, 23.13), (113.6, 24.8), (112.6, 26.9), (112.94, 28.23), (114.31, 30.55)], colour="red", lw=3.4)
m.route([(113.6, 24.8), (114.93, 25.83), (115.86, 28.68), (117.2, 29.9), (118.8, 32.06)], colour="red", lw=3.4)
m.route([(115.86, 28.68), (118.0, 29.4), (120.16, 30.27), (121.47, 31.23)], colour="red", lw=3.4)

# the Long March, 1934 to 1935
m.route([(116.03, 25.89), (114.3, 25.5), (112.4, 25.4), (111.07, 25.93), (109.2, 26.4), (107.8, 27.0), (106.93, 27.72),
         (105.9, 27.6), (106.5, 26.6), (104.8, 25.9), (103.2, 25.4), (102.45, 26.15), (102.25, 26.65),
         (102.27, 27.9), (102.3, 29.25), (102.23, 29.91), (102.75, 30.85), (102.4, 31.6), (103.4, 32.6),
         (104.25, 34.22), (106.2, 35.6), (108.17, 36.93)], colour=INK, lw=3.0, style=(0, (3, 2)))

m.city(116.40, 39.90, "Beijing", dx=-0.5, dy=0.35, bold=True)
m.city(121.47, 31.23, "Shanghai", dx=0.5, dy=0.0, bold=True)
m.city(118.80, 32.06, "Nanjing", dx=-0.4, dy=0.5, ha="right", bold=True)
m.city(114.31, 30.55, "Wuchang", dx=-0.45, dy=0.45, ha="right", bold=True)
m.city(113.26, 23.13, "Canton", dx=-0.5, dy=0.0, bold=True)

m.label(114.3, 21.05, "NATIONALISTS, 1926", fs=17, colour="#8a3a28")
m.label(125.8, 45.4, "MANCHURIA", fs=20)
m.label(125.8, 44.2, "seized by Japan, 1931", size="small", colour=INK, fs=15)
m.label(112.3, 33.6, "held by rival warlords, 1926", size="land", fs=18)
m.label(118.3, 36.0, "SHANDONG", size="small", colour=INK, fs=15)
m.label(110.6, 28.0, "HUNAN", size="small", colour=INK, fs=15)
m.label(118.9, 27.0, "march north,\n1926 to 1927", size="small", colour="#8a3a28", fs=16)
m.label(100.2, 33.0, "Long March,\n1934 to 1935", size="small", colour=INK, fs=16)
m.label(116.4, 25.0, "1934", size="small", colour=INK, fs=15, ha="left")
m.label(108.6, 37.6, "1935", size="small", colour=INK, fs=15, ha="left")
m.label(115.8, 31.1, "Yangzi", size="sea", fs=16)
m.label(111.5, 39.6, "Yellow River", size="sea", fs=16)
m.label(127.4, 39.4, "KOREA", size="land", fs=16, style="normal")
m.label(103.0, 44.5, "MONGOLIA", size="land", fs=17, style="normal")
m.label(123.2, 35.4, "Yellow\nSea", size="sea", fs=17)
m.label(125.0, 29.0, "East China\nSea", size="sea", fs=17)
m.label(115.0, 19.5, "South China Sea", size="sea", fs=17)
m.scale(500, lon=97.5, lat=19.0)
m.save("chapters/75-puyi/images/map_china.png")
