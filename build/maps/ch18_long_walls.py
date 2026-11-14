#!/usr/bin/env python3
"""Chapter 18: Athens and its harbour at Piraeus, joined by the long walls, about 2,450 years ago.

At this scale Natural Earth's coastline is far too coarse, so the coast, the walled areas of
Athens and Piraeus, and the walls are all traced by eye from "Athens and the Long walls to
Piraeus and Phaleron" in G. W. Cox, The Athenian Empire (1876; Wikimedia Commons, public domain),
the map this one replaces. The tracing is in the source map's pixels, turned into degrees by a
fit to five places (the Acropolis, Kolonos, the hill of Mounychia, the islet of Psyttaleia and
Phaleron), with errors under a kilometre. The coast has moved a little since antiquity; this is
the coast of the 1876 map.
"""
import numpy as np
from matplotlib.patches import Polygon as MplPoly, Rectangle
from lib import Map, LAND, SEA, SHORE, smooth, INK
from tracing import fit

deg = fit([((1190, 413), (23.7263, 37.9715)), ((1075, 320), (23.7137, 37.9897)), ((680, 700), (23.662, 37.940)),
           ((210, 710), (23.588, 37.944)), ((950, 795), (23.6887, 37.9293))])

sea = deg([(100, 500), (300, 497), (355, 505), (335, 530), (320, 570), (335, 610), (370, 640), (420, 665),
           (470, 660), (520, 665), (560, 655), (580, 642), (600, 652), (590, 680), (560, 700), (520, 720),
           (495, 760), (510, 800), (550, 830), (600, 820), (650, 800), (700, 772), (740, 762), (742, 700),
           (762, 672), (800, 660), (860, 666), (920, 700), (958, 760), (942, 800), (962, 832), (1020, 880),
           (1080, 950), (1150, 1050), (100, 1050)])
psyttaleia = deg([(155, 742), (200, 702), (250, 672), (278, 690), (232, 722), (172, 752)])
athens = deg([(1100, 420), (1110, 390), (1140, 355), (1190, 345), (1240, 350), (1280, 370), (1290, 410),
              (1260, 460), (1200, 480), (1150, 490), (1105, 472)])
piraeus = deg([(500, 750), (520, 715), (560, 695), (595, 660), (640, 642), (685, 650), (722, 690), (738, 730),
               (735, 758), (705, 768), (660, 748), (640, 775), (600, 795), (560, 822), (520, 808), (502, 785)])
north_wall = deg([(1106, 468), (645, 645)])
south_wall = deg([(1122, 488), (716, 652), (718, 676)])
phaleric_wall = deg([(1200, 480), (975, 768)])

m = Map(23.618, 23.746, 37.917, 37.9875, lakes=False)
ax = m.ax
w, e, s, n = m.ext
ax.add_patch(Rectangle((w, s), e - w, n - s, fc=LAND, ec="none", zorder=1.3))
ax.add_patch(MplPoly(smooth(sea, n=6, closed=True), closed=True, fc=SEA, ec=SHORE, lw=1.4, zorder=1.4))
ax.add_patch(MplPoly(smooth(psyttaleia, n=6, closed=True), closed=True, fc=LAND, ec=SHORE, lw=1.4, zorder=1.45))
m.region(athens, "red", alpha=0.45, land_only=False)
m.region(piraeus, "red", alpha=0.45, land_only=False)
m.line(north_wall, colour=INK, lw=4, curved=False)
m.line(south_wall, colour=INK, lw=4, curved=False)
m.line(phaleric_wall, colour=INK, lw=2.4, style=(0, (3, 2)), curved=False)

lon, lat = deg([(1195, 378)])[0]
m.label(lon, lat, "ATHENS", fs=28)
lon, lat = deg([(1190, 413)])[0]
m.city(lon, lat, "Acropolis", dy=-0.0028, size=19)
lon, lat = deg([(600, 745)])[0]
m.label(lon, lat, "PIRAEUS", fs=24)
lon, lat = deg([(935, 600)])[0]
m.label(lon, lat, "the long walls", size="small", colour=INK, fs=21, rot=21)
lon, lat = deg([(1110, 680)])[0]
m.label(lon, lat, "wall to Phaleron", size="small", colour=INK, fs=19, rot=-55)
lon, lat = deg([(885, 800)])[0]
m.label(lon, lat, "Phaleron\nbay", size="sea", fs=21)
m.label(23.648, 37.9215, "Saronic Gulf", size="sea", fs=24)
lon, lat = deg([(520, 680)])[0]
m.label(lon, lat, "harbour", size="sea", fs=17)
m.scale(2, lon=23.715, lat=37.921)
m.save("chapters/18-democracy/images/map_long_walls.png")
