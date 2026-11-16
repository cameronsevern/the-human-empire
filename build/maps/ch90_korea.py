#!/usr/bin/env python3
"""Chapter 90: the Korean War in four panels: the front on 25 June 1950 (the 38th parallel), early September
1950 (the Pusan pocket, with the Inchon landing of 15 September), late November 1950 (the furthest advance
of the United Nations forces, and the Chinese attack), and 27 July 1953 (the armistice line).

Drawn for this chapter, which had no map. The fronts are simplified, after the maps in English Wikipedia's
"Korean War", "Pusan Perimeter" and "Battle of the Ch'ongch'on River", and the US Army Center of Military
History's maps of the war, roughly: the Pusan perimeter along the Naktong from the south coast near Masan
past Waegwan, then east to the coast near Pohang; the line of about 24 November 1950 north of the
Ch'ongch'on river in the west and from the Chosin reservoir to the Yalu at Hyesan and up the east coast
towards Chongjin; the armistice line from the Han estuary past Panmunjom and Cheorwon to the east coast
north of Goseong. The land of Korea is Natural Earth admin-0 (as shipped with geopandas). Positions from
English Wikipedia.
"""
import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from shapely.geometry import Polygon
from shapely.ops import unary_union
import lib
from lib import Map, INK, PAPER, FILL, SOFT, smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
# the peninsula: the Natural Earth 50 m land, cut off from China and Russia along the 110 m admin-0 border
korea = unary_union([G["North Korea"], G["South Korea"]]).buffer(0.5).difference(G["China"]).difference(G["Russia"])
W, E, S, N = 124.15, 130.85, 34.25, 43.05
SCRATCH = os.environ.get("SCRATCH", "/tmp")
RED, BLUE = FILL["red"], FILL["blue"]

june = [(123.5, 38.0), (131.5, 38.0)]
sept = [(128.40, 33.8), (128.47, 35.10), (128.42, 35.35), (128.47, 35.62), (128.38, 35.96), (128.55, 36.17),
        (128.95, 36.18), (129.25, 36.13), (129.7, 36.10)]
nov = [(124.4, 39.70), (125.2, 39.80), (125.9, 39.95), (126.5, 40.0), (127.0, 40.25), (127.25, 40.55),
       (127.7, 40.95), (128.2, 41.35), (128.9, 41.45), (129.5, 41.62), (130.0, 41.75)]
july = [(126.40, 37.72), (126.68, 37.92), (126.95, 38.05), (127.15, 38.25), (127.45, 38.30), (127.75, 38.30),
        (128.05, 38.30), (128.25, 38.45), (128.42, 38.62), (128.9, 38.62)]


drawn = {"September 1950": sept[1:], "November 1950": nov[:-1] + [(129.82, 41.74)],
         "July 1953": july[:-1] + [(128.45, 38.62)]}


def panel(title, front, north_poly, labels, extra=None, path=None):
    m = Map(W, E, S, N, width=7.92)
    land = m.land.intersection(korea)
    north = Polygon(north_poly).buffer(0)
    m.region(land.intersection(north), "red", alpha=0.42)
    m.region(land.difference(north), "blue", alpha=0.42)
    m.river("Yalu", lw=1.6, en=True)
    m.ax.plot([W, E], [38, 38], color=SOFT, lw=1.6, ls=(0, (6, 3)), zorder=3.5)
    if front is not None:
        m.line(drawn.get(title, front), colour=INK, lw=3.4, curved=front is not june)
    if extra:
        extra(m)
    m.city(126.98, 37.57, "Seoul", dx=0.25, dy=0.12)
    m.city(125.75, 39.02, "Pyongyang", dx=0.0, dy=0.3)
    m.city(129.08, 35.18, "Pusan", dx=0.2, dy=-0.25)
    for args, kw in labels:
        m.label(*args, **kw)
    m.ax.text(0.03, 0.975, title, transform=m.ax.transAxes, ha="left", va="top", fontsize=21, fontweight="bold",
              color=INK, zorder=9, bbox=dict(boxstyle="square,pad=0.35", fc=PAPER, ec=INK, lw=1.2))
    m.save(path)
    return path


R = lambda **kw: dict(size="region", fs=17, **kw)
Sm = lambda **kw: dict(size="small", colour=INK, fs=16, **kw)

def june_extra(m):
    for pts in [[(126.4, 38.25), (126.8, 37.75)], [(127.0, 38.3), (127.05, 37.8)], [(127.8, 38.3), (127.9, 37.5)],
                [(128.6, 38.3), (128.9, 37.6)]]:
        m.route(pts, colour=INK, lw=3.0)

def sept_extra(m):
    m.route([(124.6, 36.55), (125.4, 36.9), (126.1, 37.25), (126.5, 37.45)], colour="blue", lw=3.6)
    m.city(126.62, 37.47, None, r=7)

def nov_extra(m):
    for pts in [[(124.9, 40.75), (125.15, 40.35), (125.35, 39.95)], [(126.0, 41.1), (126.1, 40.6), (126.2, 40.15)],
                [(126.6, 41.5), (126.9, 41.0), (127.15, 40.7)]]:
        m.route(pts, colour=INK, lw=3.2)

def july_extra(m):
    m.ax.plot(126.68, 37.96, "s", ms=11, mfc=INK, mec=PAPER, mew=1.4, zorder=6)


big = [(131.5, 50), (123.0, 50)]
p1 = panel("June 1950", june, june + big,
           [((127.6, 39.6, "NORTH KOREA"), R()), ((127.9, 36.5, "SOUTH KOREA"), R()),
            ((124.3, 37.75, "38th parallel"), Sm(ha="left", style="italic")),
            ((128.2, 37.1, "invasion,\n25 June"), Sm(ha="left")),
            ((125.6, 41.9, "CHINA"), dict(size="land", colour="#5a534b", fs=17, style="normal")),
            ((124.9, 40.55, "Yalu"), dict(size="sea", fs=16, rot=38)),
            ((125.0, 35.6, "Yellow\nSea"), dict(size="sea", fs=16)),
            ((130.2, 37.6, "Sea of\nJapan"), dict(size="sea", fs=16))],
           june_extra, os.path.join(SCRATCH, "ch90_1.png"))
p2 = panel("September 1950", sept, [(123.0, 33.8)] + sept + [(131.5, 36.10), (131.5, 50), (123.0, 50)],
           [((127.5, 38.9, "NORTH KOREAN\nARMY"), R()), ((128.95, 35.75, "UN"), R(ha="left")),
            ((125.4, 36.45, "Inchon landing,\n15 September"), Sm()),
            ((126.5, 37.68, "Inchon"), Sm(ha="right"))],
           sept_extra, os.path.join(SCRATCH, "ch90_2.png"))
p3 = panel("November 1950", nov, [(123.5, 39.70)] + nov + [(131.5, 41.75), (131.5, 50), (123.0, 50)],
           [((127.8, 37.3, "UN FORCES"), R()), ((127.4, 42.3, "CHINA"), dict(size="land", colour="#5a534b", fs=17, style="normal")),
            ((124.3, 41.55, "Chinese\nattack"), Sm(ha="left")),
            ((128.3, 40.35, "furthest\nUN advance"), Sm(ha="left"))],
           nov_extra, os.path.join(SCRATCH, "ch90_3.png"))
p4 = panel("July 1953", july, [(123.0, 37.72)] + july + [(131.5, 38.62), (131.5, 50), (123.0, 50)],
           [((127.6, 39.6, "NORTH KOREA"), R()), ((127.9, 36.5, "SOUTH KOREA"), R()),
            ((126.55, 38.2, "Panmunjom"), Sm(ha="right")),
            ((128.6, 38.95, "armistice line,\n27 July 1953"), Sm(ha="left"))],
           july_extra, os.path.join(SCRATCH, "ch90_4.png"))

ims = [mpimg.imread(p)[:, :, :3] for p in (p1, p2, p3, p4)]
paper = np.array(lib.matplotlib.colors.to_rgb(PAPER))
h, w = ims[0].shape[:2]
vgap = np.ones((h, 1600 - 2 * w, 3)) * paper
hgap = np.ones((16, 1600, 3)) * paper
out = np.vstack([np.hstack([ims[0], vgap, ims[1]]), hgap, np.hstack([ims[2], vgap, ims[3]])])
path = os.path.join(lib.ROOT, "chapters/90-korea/images/map_korea_fronts.png")
plt.imsave(path, out)
print("wrote", path)
