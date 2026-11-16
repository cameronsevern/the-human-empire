#!/usr/bin/env python3
"""Chapter 83: Japan in August 1945. The land Japan still held (the home islands, Korea, Manchuria, southern
Sakhalin, the Kurils and the occupied part of China); a selection of the cities already burned by American
bombers between March and August; the four cities on the target list of 25 July (Hiroshima, Kokura,
Niigata, Nagasaki), with Kyoto, struck off it; the two cities struck, Hiroshima on 6 August and Nagasaki on
9 August; the direction of Tinian, the bombers' base; and the Soviet attack into Manchuria of 9 August.

Drawn for this chapter, which had no map. Japan's holdings are the shapes of asia1941.py; the occupied part
of China had changed little by 1945 and is shown as there, roughly. The burned cities are about forty of
the more than sixty Japanese cities attacked with fire bombs from March 1945, as listed in English
Wikipedia's "Air raids on Japan"; those right beside a target city (Kure, Yawata, Shimonoseki) and a few
crowded round Tokyo and Osaka are left out so that the marks stay clear. The Soviet attack follows the
three fronts in English Wikipedia's "Soviet invasion of Manchuria": from Mongolia towards Changchun and
Mukden, across the Amur towards Harbin, and from the Vladivostok region westward. Positions from English
Wikipedia.
"""
import numpy as np
from shapely.ops import unary_union
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import lib
from lib import Map, INK, PAPER, FILL, SOFT
from asia1941 import G, manchuria, occupied_china, korea, japan

m = Map(113.0, 150.0, 29.0, 54.0)
held = unary_union([japan, korea, manchuria, occupied_china, G["Taiwan"]]).intersection(m.land)
fc = FILL["red"]
for p in getattr(held, "geoms", [held]):
    if p.geom_type == "Polygon" and p.area > 1e-3:
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(lib.MplPoly(xy, closed=True, fc=fc, ec="none", alpha=0.32, zorder=2))
        m.ax.add_patch(lib.MplPoly(xy, closed=True, fc="none", ec=fc, lw=1.3, alpha=0.9, zorder=2.1))
m.river("Amur", "Songhua", "Yalu", lw=1.4, en=True)

# the Soviet attack, 9 August
for pts in [[(114.8, 48.6), (117.6, 46.6), (120.6, 45.0), (123.2, 44.1), (124.4, 43.6)],
            [(127.6, 50.6), (127.3, 48.8), (126.9, 47.2), (126.7, 46.2)],
            [(132.6, 44.0), (131.2, 44.4), (129.6, 44.6), (128.0, 44.9)]]:
    m.route(pts, colour=INK, lw=4.2)

# Tinian, 1,500 miles to the south-east
m.route([(146.6, 29.0), (143.0, 30.4), (139.0, 31.6), (135.6, 32.4), (133.7, 32.75)], colour=INK, lw=2.6,
        style=(0, (3, 1.6)))

burned = [(139.64, 35.44), (136.91, 35.18), (135.50, 34.69), (135.20, 34.69), (130.56, 31.60), (130.71, 32.80),
          (130.45, 33.03), (130.40, 33.59), (129.72, 33.18), (131.81, 34.05), (133.92, 34.66), (134.69, 34.82),
          (135.17, 34.23), (136.76, 35.42), (137.73, 34.71), (138.38, 34.98), (138.86, 35.10), (138.57, 35.66),
          (140.12, 35.61), (140.47, 36.37), (140.65, 36.60), (139.88, 36.56), (139.06, 36.39), (139.39, 36.15),
          (140.87, 38.27), (140.74, 40.82), (137.21, 36.70), (136.22, 36.06), (136.06, 35.65), (138.85, 37.45),
          (133.53, 33.56), (134.05, 34.34), (134.55, 34.07), (132.77, 33.84), (133.00, 34.07), (132.56, 33.22),
          (131.61, 33.24), (131.67, 32.58), (137.39, 34.77), (136.51, 34.72), (136.62, 34.97), (139.35, 35.33),
          (140.83, 35.73), (130.30, 33.25)]
for x, y in burned:
    m.ax.plot(x, y, "s", ms=8, mfc=SOFT, mec=PAPER, mew=1.0, zorder=5.5)
m.ax.plot(139.69, 35.69, "s", ms=11, mfc=SOFT, mec=PAPER, mew=1.0, zorder=5.6)
m.label(140.3, 34.85, "Tokyo", size="city", colour=INK, fs=16.5, ha="left")

for x, y in [(130.88, 33.88), (139.02, 37.92)]:                     # on the list, not struck
    m.ax.plot(x, y, "o", ms=15, mfc=PAPER, mec=INK, mew=3.0, zorder=6)
m.label(130.6, 34.55, "Kokura", size="city", colour=INK, fs=17, ha="right")
m.label(138.6, 38.45, "Niigata", size="city", colour=INK, fs=17, ha="right")
m.ax.plot(135.77, 35.01, "o", ms=13, mfc=PAPER, mec=SOFT, mew=2.4, zorder=6)
m.label(135.3, 35.75, "Kyoto,\nstruck off", size="small", colour=INK, fs=15, ha="center")
for x, y in [(132.46, 34.39), (129.87, 32.75)]:
    m.ax.plot(x, y, "*", ms=30, mfc=INK, mec=PAPER, mew=1.6, zorder=6.5)
m.label(131.6, 35.25, "Hiroshima,\n6 August", size="city", colour=INK, fs=17, ha="center", style=None)
m.label(129.4, 31.75, "Nagasaki,\n9 August", size="city", colour=INK, fs=17, ha="right", style=None)
m.ax.texts[-1].set_fontweight("bold"); m.ax.texts[-2].set_fontweight("bold")

m.label(141.2, 30.0, "from Tinian,\n1,500 miles", size="small", colour=INK, fs=16, ha="right")
m.label(117.0, 49.6, "Soviet attack,\n9 August", size="small", colour=INK, fs=16, ha="center")
m.label(125.3, 47.0, "MANCHURIA", fs=19)
m.label(127.4, 39.2, "KOREA", fs=17)
m.label(137.6, 39.6, "JAPAN", fs=19)
m.label(134.5, 52.0, "SOVIET UNION", size="land", colour="#5a534b", fs=17, style="normal")
m.label(115.6, 42.5, "MONGOLIA", size="land", colour="#5a534b", fs=15, style="normal")
m.label(116.5, 34.0, "CHINA", size="land", colour="#5a534b", fs=17, style="normal")
m.label(134.8, 41.0, "Sea of\nJapan", size="sea", fs=17)
m.label(145.5, 36.5, "Pacific\nOcean", size="sea", fs=19)
m.label(123.5, 33.3, "East China\nSea", size="sea", fs=16)

handles = [Patch(fc=fc + "55", ec=fc, label="held by Japan"),
           Line2D([0], [0], ls="none", marker="s", ms=8, mfc=SOFT, mec=PAPER, label="cities already burned"),
           Line2D([0], [0], ls="none", marker="o", ms=15, mfc=PAPER, mec=INK, mew=3.0, label="on the target list"),
           Line2D([0], [0], ls="none", marker="*", ms=24, mfc=INK, mec=PAPER, label="struck by an atomic bomb")]
leg = m.ax.legend(handles=handles, loc="upper right", fontsize=16, frameon=True, fancybox=False, edgecolor=INK,
                  facecolor=PAPER, framealpha=1, borderpad=0.7, labelspacing=0.6)
leg.set_zorder(9); leg.get_frame().set_linewidth(1.2)
m.scale(500, lon=119.2, lat=35.2)
m.save("chapters/83-bomb/images/map_japan_1945.png")
