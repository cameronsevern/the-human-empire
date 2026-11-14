#!/usr/bin/env python3
"""Chapter 32: China about the year 1100: the Song, the Khitan empire to the north with the strip of
passes around modern Beijing that the Song never recovered, the kingdom in the north-west (the
Western Xia), and the homeland of the Jurchen in Manchuria.

Drawn for this chapter, which had no map. The states are traced roughly by eye from
"Song-Liao-Xixia-1111" (Wikimedia Commons), a map of the three states in 1111. The lost strip is the Sixteen
Prefectures, from about Beijing to Datong, south of which the frontier ran roughly along the 39th
parallel. The Jurchen homeland is placed on the Songhua and Ashi rivers, around their later capital
Huining. The Grand Canal is shown from Kaifeng to Hangzhou only, the part that fed the Song capital.
The Yellow River is left out because its lower course changed in these years. Areas are soft and
approximate. Positions from English Wikipedia.
"""
import numpy as np
from lib import Map, INK
from tracing import states, hatched

song = [(117.8, 38.9), (116.0, 39.0), (114.5, 39.1), (113.2, 39.0), (111.5, 39.3), (110.8, 38.6), (109.8, 37.8),
        (108.0, 37.3), (106.5, 36.6), (105.0, 36.4), (103.8, 36.3), (103.0, 35.2), (103.5, 33.5), (102.5, 32.0),
        (102.0, 30.0), (102.4, 28.0), (104.5, 27.2), (105.5, 25.5), (105.5, 24.0), (106.8, 22.8), (108.0, 21.5),
        (111.0, 19.5), (118.0, 22.0), (123.0, 30.0), (123.5, 37.5), (120.0, 38.0)]
liao = [(111.5, 39.3), (113.2, 39.0), (114.5, 39.1), (116.0, 39.0), (117.8, 38.9), (119.0, 39.6), (121.5, 39.0),
        (124.0, 39.6), (125.5, 40.2), (128.0, 41.5), (129.0, 43.0), (129.5, 45.5), (128.5, 49.0), (98.0, 49.0),
        (100.0, 44.0), (104.5, 42.0), (107.0, 41.6), (109.0, 41.0), (111.0, 40.2)]
xia = [(94.0, 40.6), (96.0, 41.6), (100.0, 42.2), (104.5, 42.0), (107.0, 41.6), (109.0, 41.0), (111.0, 40.2),
       (111.5, 39.3), (110.8, 38.6), (109.8, 37.8), (108.0, 37.3), (106.5, 36.6), (105.0, 36.4), (103.8, 36.3),
       (102.5, 37.0), (101.0, 37.6), (99.0, 38.6), (97.0, 39.3), (94.0, 39.6)]
strip = [(113.0, 39.0), (114.5, 39.1), (116.0, 39.0), (117.6, 38.9), (119.0, 39.6), (119.2, 40.6), (117.0, 41.0),
         (115.0, 40.9), (113.5, 40.6), (112.6, 40.3), (112.4, 39.5)]
jurchen = [(125.0, 44.0), (127.5, 43.8), (130.0, 44.5), (130.8, 46.2), (128.5, 47.2), (125.5, 46.8)]
canal = [(114.31, 34.80), (115.65, 34.41), (116.98, 33.64), (118.5, 33.1), (119.02, 33.55), (119.45, 32.78),
         (119.42, 32.39), (119.97, 31.78), (120.62, 31.3), (120.75, 30.75), (120.15, 30.27)]

m = Map(95.0, 131.5, 21.6, 47.5)
m.river("Yangtze", en=True, lw=2.0)
states(m, [(song, "red"), (xia, "purple"), (liao, "blue")], alpha=0.36)
hatched(m, strip, colour="#2f4f6f", alpha=0.25, hatch="xx")
hatched(m, jurchen, colour="green", alpha=0.22, hatch="..")
m.line(canal, colour="#7a4a2a", lw=4.0)

m.label(112.5, 29.0, "SONG", fs=30)
m.label(115.5, 45.0, "KHITAN EMPIRE", fs=26)
m.label(115.5, 43.8, "(Liao)", size="small", colour=INK, fs=20)
m.label(101.5, 40.4, "WESTERN XIA", fs=22)
m.label(128.0, 45.7, "JURCHEN", fs=20)
m.label(128.0, 44.6, "homeland", size="small", colour=INK, fs=18)
m.label(105.0, 30.5, "SICHUAN", size="land", fs=21, style="normal")
m.label(115.6, 41.75, "the lost strip of passes", size="small", colour=INK, fs=19)

m.city(114.31, 34.80, "Kaifeng", dx=-0.5, dy=0.0, star=True, bold=True, size=22)
m.label(113.8, 34.0, "Song capital", size="small", colour=INK, fs=17, ha="right")
m.city(120.15, 30.27, "Hangzhou", dx=-0.5, dy=-0.2, size=20)
m.city(116.40, 39.90, "Beijing", dx=0.4, dy=0.0, size=19)
m.label(116.6, 35.2, "Grand Canal", size="small", colour="#7a4a2a", fs=19, rot=-20)
m.label(110.5, 30.8, "Yangzi", size="sea", fs=21)
m.label(124.5, 34.0, "Yellow\nSea", size="sea", fs=21)
m.label(119.5, 23.4, "South China Sea", size="sea", fs=20)
m.scale(500, lon=96.0, lat=22.0)
m.save("chapters/32-gunpowder/images/map_song.png")
