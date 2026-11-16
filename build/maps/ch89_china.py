#!/usr/bin/env python3
"""Chapter 89: China, 1934 to 1949. The Communist base in the south-east until 1934, the Long March of 1934
and 1935, Yan'an, the land held by Japan in 1940, the Communist areas of 1945, the three great battles of
1948 and 1949, and the Nationalist retreat to Taiwan.

Drawn for this chapter, which had no map. The base is the Central Soviet on the Jiangxi-Fujian border round
Ruijin, roughly, after English Wikipedia's "Jiangxi Soviet". The Long March is the route of ch75_china.py.
The land held by Japan is the shapes of asia1941.py (Manchuria, the occupied provinces, Korea, Taiwan),
after the 1940 map in English Wikipedia's "Second Sino-Japanese War"; Japan held the cities and railways
rather than all of it. The Communist areas of 1945 are the main base areas (Shaanxi-Gansu-Ningxia round
Yan'an; Shanxi-Suiyuan; Shanxi-Chahar-Hebei; Shanxi-Hebei-Shandong-Henan; Shandong; central China north of
the Yangtze; the Hubei-Henan border) as on the maps in English Wikipedia's "Chinese Civil War" and
"Liberated areas", much simplified and rough; they overlap the Japanese-held land, since they lay between
the towns and railways that Japan held. The three battles: Liaoshen (Jinzhou, Changchun, Shenyang),
Huaihai (round Xuzhou) and Pingjin (Beijing and Tianjin). Positions from English Wikipedia.
"""
import numpy as np
from shapely.geometry import Polygon
from shapely.ops import unary_union
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import lib
from lib import Map, INK, PAPER, FILL, SOFT, smooth
from asia1941 import G, soft, manchuria, occupied_china, korea

m = Map(100.3, 127.5, 21.0, 45.4)
LAND = m.land
japan_1940 = unary_union([manchuria, occupied_china, korea, G["Taiwan"].buffer(0.1)]).intersection(LAND)
m.region(japan_1940, "brown", alpha=0.32)

bases_1945 = unary_union([soft(p) for p in [
    [(106.6, 35.6), (107.5, 35.0), (108.6, 35.2), (109.8, 35.7), (110.4, 36.6), (110.5, 37.8), (110.0, 38.7),
     (108.6, 38.4), (107.2, 37.7), (106.5, 36.8)],
    [(110.7, 37.6), (111.8, 37.4), (112.6, 38.3), (112.8, 39.4), (112.0, 40.2), (111.0, 39.8), (110.7, 38.6)],
    [(113.1, 38.0), (114.4, 37.7), (115.6, 38.2), (116.6, 38.6), (117.6, 39.6), (118.8, 40.2), (118.2, 41.0),
     (116.0, 41.0), (114.6, 40.8), (113.6, 40.2), (113.2, 39.2)],
    [(112.4, 35.0), (113.6, 34.7), (115.2, 34.7), (116.3, 35.4), (116.5, 36.6), (115.6, 37.3), (114.2, 37.3),
     (113.0, 36.9), (112.4, 36.0)],
    [(116.9, 35.0), (118.0, 34.7), (119.4, 35.2), (120.6, 36.2), (122.3, 37.2), (121.2, 37.7), (119.6, 37.3),
     (118.4, 37.2), (117.2, 36.4)],
    [(116.6, 32.4), (118.0, 32.35), (119.4, 32.5), (120.9, 32.6), (120.6, 33.8), (119.6, 34.3), (118.4, 34.1),
     (117.2, 33.6), (116.4, 33.0)],
    [(112.6, 30.9), (113.8, 30.7), (114.8, 31.2), (114.8, 32.2), (113.6, 32.6), (112.6, 31.9)],
]]).intersection(LAND)
m.region(bases_1945, "red", alpha=0.25, hatch="///")

base_1934 = [(115.3, 25.3), (116.6, 25.2), (117.3, 25.9), (117.1, 26.9), (116.3, 27.4), (115.5, 27.2), (115.0, 26.3)]
m.region(base_1934, "red", alpha=0.55)

m.river("Chang Jiang", "Yangtze", "Jinsha", "Huang", lw=1.6)

# the Long March, 1934 to 1935
m.route([(116.03, 25.89), (114.3, 25.5), (112.4, 25.4), (111.07, 25.93), (109.2, 26.4), (107.8, 27.0), (106.93, 27.72),
         (105.9, 27.6), (106.5, 26.6), (104.8, 25.9), (103.2, 25.4), (102.45, 26.15), (102.25, 26.65),
         (102.27, 27.9), (102.3, 29.25), (102.23, 29.91), (102.75, 30.85), (102.4, 31.6), (103.4, 32.6),
         (104.25, 34.22), (106.2, 35.6), (108.17, 36.93)], colour=INK, lw=3.2, style=(0, (3, 1.6)))
# the Nationalists to Taiwan, 1949
m.route([(121.7, 30.9), (122.6, 28.6), (122.2, 26.4), (121.6, 25.25)], colour="blue", lw=3.0)

# the three battles of 1948 and 1949
for x, y in [(121.13, 41.10), (123.43, 41.80), (117.18, 34.26), (117.20, 39.13)]:  # Jinzhou, Shenyang, Xuzhou, Tianjin
    m.ax.plot(x, y, "X", ms=21, mfc=INK, mec=PAPER, mew=1.6, zorder=6.6)

m.city(116.40, 39.90, "Beijing", dx=-0.35, dy=0.3)
m.city(125.32, 43.88, "Changchun", dx=-0.35, dy=0.0)
m.city(118.80, 32.06, "Nanjing", dx=-0.35, dy=0.15)
m.city(121.47, 31.23, "Shanghai", dx=0.35, dy=0.2)
m.city(106.55, 29.56, "Chongqing", dx=-0.35, dy=0.0)
m.city(108.94, 34.34, "Xi'an", dx=0.3, dy=-0.3)
m.city(109.49, 36.60, "Yan'an", dx=0.35, dy=0.0, star=True, bold=True)

T = dict(size="small", colour=INK, fs=16)
m.label(116.2, 24.4, "Communist base\nto 1934", **T)
m.label(103.6, 33.9, "the Long March,\n1934 to 1935", **T, ha="right")
m.label(124.0, 42.75, "north-east,\nautumn 1948", **T, ha="left")
m.label(116.6, 34.85, "round Xuzhou,\nwinter 1948", **T, ha="right")
m.label(118.4, 38.4, "Beijing and Tianjin,\nwinter 1948", **T, ha="left")
m.label(123.6, 27.9, "Chiang to\nTaiwan, 1949", **T, ha="left")
m.label(122.6, 44.75, "MANCHURIA", fs=19)
m.label(121.4, 23.0, "TAIWAN", fs=15, ha="left")
m.label(127.0, 39.6, "KOREA", fs=16, ha="right")
m.label(122.6, 33.4, "Yellow\nSea", size="sea", fs=16)
m.label(113.5, 30.0, "Yangtze", size="sea", fs=16, rot=-12)
m.label(106.0, 39.6, "Yellow River", size="sea", fs=16, rot=-35)
m.label(116.8, 21.6, "South China Sea", size="sea", fs=17)

handles = [Patch(fc=FILL["brown"] + "55", ec=FILL["brown"], label="held by Japan, 1940"),
           Patch(fc=FILL["red"] + "40", ec=FILL["red"], hatch="///", label="Communist areas, 1945"),
           Line2D([0], [0], ls="none", marker="X", ms=17, mfc=INK, mec=PAPER, label="great battles, 1948 to 1949")]
leg = m.ax.legend(handles=handles, loc="lower left", fontsize=16, frameon=True, fancybox=False, edgecolor=INK,
                  facecolor=PAPER, framealpha=1, borderpad=0.7, labelspacing=0.5)
leg.set_zorder(9); leg.get_frame().set_linewidth(1.2)
m.scale(500, lon=122.0, lat=21.5)
m.save("chapters/89-mao/images/map_china_1949.png")
