#!/usr/bin/env python3
"""Chapter 31: the Grand Canal of the Sui and Tang, joining the rice lands of the Yangzi to the Yellow
River and the capitals of the north.

Replaces "China-Grand canal, Sui and Tang" by Yug (Wikimedia Commons, CC BY-SA 3.0), after Twitchett,
Cambridge History of China, vol. 3, p. 136, whose labels and legend were too small to read. The canal
follows that map: from Chang'an along the Wei to the Yellow River; from Luoyang past Bianzhou (later
Kaifeng) south-east to the Huai; from the Huai to Yangzhou and across the Yangzi to Hangzhou; and north
from the Yellow River to the site of modern Beijing. The courses are drawn through the towns on them
and are approximate. Rivers are Natural Earth's modern courses. The rice lands are a rough area: the
lower Yangzi valley and the land south of the Huai. Positions from English Wikipedia.
"""
from lib import Map, INK
from tracing import hatched

guangtong = [(108.94, 34.27), (109.5, 34.45), (110.25, 34.58)]
tongji = [(112.45, 34.62), (113.0, 34.75), (113.6, 34.85), (114.31, 34.80), (115.0, 34.55), (115.65, 34.41),
          (116.4, 33.93), (116.98, 33.64), (117.88, 33.48), (118.5, 33.1)]
shanyang = [(119.02, 33.55), (119.3, 33.1), (119.45, 32.78), (119.42, 32.39), (119.42, 32.25)]
jiangnan = [(119.45, 32.2), (119.97, 31.78), (120.3, 31.57), (120.62, 31.3), (120.75, 30.75), (120.15, 30.27)]
yongji = [(113.4, 35.08), (113.9, 35.3), (114.07, 35.4), (114.5, 35.67), (115.2, 36.3), (115.7, 36.84),
          (115.67, 37.06), (116.3, 37.45), (116.85, 38.3), (116.8, 38.6), (117.2, 39.13), (117.04, 39.38),
          (116.4, 39.9)]
rice = [(112.0, 30.8), (113.5, 32.4), (116.0, 32.6), (118.0, 33.0), (120.6, 33.2), (121.6, 32.0), (121.9, 30.6),
        (121.0, 29.6), (118.5, 28.8), (115.5, 28.6), (113.0, 29.0)]

m = Map(106.5, 123.0, 28.6, 41.2)
m.river("Yellow", "Yangtze", "Huai", "Wei", en=True, lw=2.0)
hatched(m, rice, colour="green", alpha=0.18)
for c in (guangtong, tongji, shanyang, jiangnan, yongji):
    m.line(c, colour="#7a4a2a", lw=4.2)

m.city(108.94, 34.27, "Chang'an", dx=0.0, dy=-0.55, star=True, bold=True, size=21)
m.label(108.94, 33.5, "Tang capital", size="small", colour=INK, fs=17)
m.city(112.45, 34.62, "Luoyang", dx=-0.15, dy=-0.4, size=20, ha="right")
m.city(114.31, 34.80, "Kaifeng", dx=-0.05, dy=-0.42, star=True, bold=True, size=21, ha="right")
m.label(114.26, 34.08, "Song capital", size="small", colour=INK, fs=17, ha="right")
m.city(119.42, 32.39, "Yangzhou", dx=-0.25, dy=0.0, size=20)
m.city(120.15, 30.27, "Hangzhou", dx=-0.3, dy=-0.1, size=20)
m.city(116.4, 39.9, "Beijing", dx=-0.3, dy=0.2, size=20)

m.label(115.55, 37.85, "Grand Canal", size="small", colour="#7a4a2a", fs=22, rot=52)
m.label(117.0, 34.25, "Grand Canal", size="small", colour="#7a4a2a", fs=20, rot=-22)
m.label(110.6, 36.0, "Yellow River", size="sea", fs=21)
m.label(111.2, 30.15, "Yangzi", size="sea", fs=22)
m.label(115.3, 32.15, "Huai", size="sea", fs=20)
m.label(116.4, 30.1, "THE RICE-GROWING\nSOUTH", fs=21)
m.label(113.0, 38.6, "THE NORTH", size="land", fs=22, style="normal")
m.label(121.5, 38.4, "Bohai\nSea", size="sea", fs=20)
m.label(122.2, 34.8, "Yellow\nSea", size="sea", fs=20)
m.scale(300, lon=107.2, lat=29.2)
m.save("chapters/31-exams/images/map_canal.png")
