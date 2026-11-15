#!/usr/bin/env python3
"""Chapter 38: the Sahara and West Africa. The empires of Ghana, Mali and Songhai, each at roughly its
greatest extent, the gold fields of Bambuk and Bure, the salt mine at Taghaza, the towns of the Niger,
and the caravan road across the desert to Sijilmasa and Marrakesh.

Drawn for this chapter, which had no map. The three empires overlap, so each has its own kind of edge:
Ghana hatched, Mali shaded, Songhai a dashed outline. Their extents are soft and approximate, drawn by
eye after the maps in English Wikipedia's articles on the Ghana Empire (about 1050), the Mali Empire
(about 1350) and the Songhai Empire (about 1500), and checked against the Britannica articles on each.
The caravan road is the one Ibn Battuta took in 1352, by Taghaza to Walata, with its branch to
Timbuktu. The gold fields are areas, not points: Bambuk between the Bafing and Faleme rivers, Bure on the
upper Niger around Siguiri. Positions from English Wikipedia.
"""
import numpy as np
from shapely.geometry import Polygon
from matplotlib.patches import Polygon as MplPoly
import lib
from lib import Map, INK, FILL, smooth

ghana = [(-12.6, 15.2), (-11.6, 17.4), (-9.2, 18.3), (-6.6, 17.9), (-5.2, 16.6), (-5.6, 14.9), (-8.0, 14.1),
         (-10.6, 14.1)]
mali = [(-17.0, 16.3), (-16.8, 13.0), (-15.0, 11.4), (-12.2, 10.0), (-9.2, 9.6), (-6.6, 10.2), (-4.4, 11.6),
        (-2.0, 13.4), (0.6, 14.9), (1.2, 16.4), (0.2, 17.6), (-3.0, 17.9), (-6.5, 18.3), (-10.0, 17.7),
        (-13.2, 16.9)]
songhai = [(-10.6, 15.2), (-9.6, 17.5), (-6.2, 18.7), (-3.0, 19.6), (0.6, 19.6), (4.2, 18.6), (7.5, 17.0),
           (7.0, 13.6), (4.0, 12.0), (0.5, 12.4), (-2.6, 12.6), (-5.4, 12.6), (-8.0, 13.8)]

m = Map(-17.6, 5.6, 9.0, 32.6)
m.river("Niger", "Senegal", "Sénégal", "Bafing", "Bani", en=True, lw=2.2)


def area(pts, colour, fill_alpha, hatch=None, ls="-", lw=2.4):
    poly = Polygon(smooth(pts, n=12, closed=True)).buffer(0).intersection(lib._land)
    fc = FILL[colour]
    for p in getattr(poly, "geoms", [poly]):
        if p.is_empty or p.geom_type != "Polygon":
            continue
        xy = np.array(p.exterior.coords)
        if fill_alpha:
            m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=fill_alpha, zorder=2))
        if hatch:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=0, alpha=0.75, zorder=2.05, hatch=hatch))
        m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=lw, ls=ls, alpha=1, zorder=2.2))


area(mali, "gold", 0.38)
area(ghana, "red", 0.0, hatch="//", lw=2.6)
area(songhai, "blue", 0.0, hatch=None, ls=(0, (5, 3)), lw=3.4)

# the empires, named with their dates
m.label(-8.4, 16.65, "GHANA", colour="red", fs=23)
m.label(-8.4, 15.75, "about 800 to 1100", size="small", colour=INK, fs=19)
m.label(-13.6, 12.3, "MALI", colour=INK, fs=25)
m.label(-13.6, 11.35, "about 1235 to 1400s", size="small", colour=INK, fs=19)
m.label(3.4, 14.9, "SONGHAI", colour="blue", fs=23)
m.label(3.4, 14.0, "1460s to 1591", size="small", colour=INK, fs=19)

# the gold fields
for lon, lat, name in [(-11.4, 13.1, "Bambuk"), (-9.0, 11.5, "Bure")]:
    m.mark(lon, lat, marker="D", ms=17, colour=INK)
m.label(-11.4, 13.85, "gold: Bambuk", size="small", colour=INK, fs=19)
m.label(-8.55, 11.5, "gold: Bure", size="small", colour=INK, fs=19, ha="left")

# the caravan road and the salt mine
road = [(-7.99, 31.63), (-6.2, 31.9), (-4.27, 31.28)]
m.route(road, colour=INK, lw=2.6, arrow=False, style=(0, (4, 2.5)))
m.route([(-4.27, 31.28), (-4.6, 27.5), (-4.98, 23.60), (-6.0, 20.5), (-7.03, 17.32)], colour=INK, lw=2.6,
        arrow=False, style=(0, (4, 2.5)))
m.route([(-4.98, 23.60), (-3.9, 20.0), (-3.0, 16.77)], colour=INK, lw=2.6, arrow=False, style=(0, (4, 2.5)))
m.route([(-0.04, 16.27), (2.0, 17.6), (5.4, 19.4)], colour=INK, lw=2.6, arrow=True, style=(0, (4, 2.5)))
m.label(4.9, 20.6, "to Cairo\nand Mecca", size="small", colour=INK, fs=19, ha="right")

m.mark(-4.98, 23.60, marker="s", ms=16, colour=INK)
m.label(-4.4, 23.60, "Taghaza", size=20, colour=INK, fs=21, ha="left")
m.label(-4.4, 22.75, "salt mine", size="small", fs=19, ha="left")

m.city(-7.99, 31.63, "Marrakesh", dx=0.0, dy=-0.75, size=20)
m.city(-4.27, 31.28, "Sijilmasa", dx=0.45, dy=0.0, size=20)
m.city(-7.03, 17.32, "Walata", dx=-0.45, dy=0.45, size=20)
m.city(-3.00, 16.77, "Timbuktu", dx=0.0, dy=0.75, size=20, bold=True)
m.city(-0.04, 16.27, "Gao", dx=0.0, dy=-0.7, size=20)
m.city(-4.55, 13.91, "Djenné", dx=0.45, dy=-0.2, size=20)

m.label(-3.0, 26.8, "S A H A R A", size="land", fs=26, style="normal")
m.label(-1.8, 14.5, "Niger", size="sea", fs=20, rot=-30)
m.label(-14.5, 15.9, "Senegal", size="sea", fs=19, rot=-25)
m.label(-14.3, 25.0, "ATLANTIC\nOCEAN", size="sea", fs=21)
m.scale(500, lon=-16.5, lat=29.6)
m.save("chapters/38-gold/images/map_sahara.png")
