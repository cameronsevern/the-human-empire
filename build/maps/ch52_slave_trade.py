#!/usr/bin/env python3
"""Chapter 52: the Atlantic slave trade, in two panels. Above: the ocean, with three arrows from the coast
of Africa to Brazil, to the Caribbean and Spanish America, and to North America, their widths roughly in
proportion to the numbers landed between 1501 and 1866. Below, closer: the coast from the Gold Coast to
Angola, with the states the text names (Asante, Dahomey, Oyo, Benin, Kongo, and Ndongo, Njinga's kingdom),
the forts at Elmina and Cape Coast, the ports of Whydah and Luanda, in two panels side by side.

Drawn for this chapter, which had no map. The numbers are the estimates of people landed in the
Trans-Atlantic Slave Trade Database (slavevoyages.org): Brazil about 4.9 million; the Caribbean and Spanish
America (British, French, Dutch and Danish Caribbean and the Spanish Americas) about 5.3 million; mainland
North America about 390,000. The arrows are schematic: they show where the people were taken from and to,
not the sailing tracks. The states are soft, rough areas about 1700-1750, after the maps of West and
West Central Africa in English Wikipedia's articles on each kingdom and in the Atlas of the Transatlantic
Slave Trade (Eltis and Richardson). Elmina and Cape Coast lie 13 km apart and share one dot. Positions
from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import lib
from lib import Map, INK, PAPER, FILL

SCRATCH = os.environ.get("SCRATCH", "/tmp")

# ---------------------------------------------------------------- the two panels below, closer
PW, PH = 7.93, 6.0


def panel(west, east, mid):
    dlat = PH * (east - west) * np.cos(np.radians(mid)) / PW
    return west, east, mid - dlat / 2, mid + dlat / 2


GW = panel(-4.5, 7.5, 7.2)          # the Gold Coast to Benin
KW = panel(10.6, 19.6, -7.6)        # Kongo and Ndongo


def fat_arrow(m, pts, lw):
    """A thick arrow: a body of width lw (points) and a solid head drawn as one triangle."""
    from matplotlib.patches import Polygon as MplPoly
    c = lib.smooth(pts)
    col = FILL["red"]
    tip = c[-1]
    d = c[-1] - c[-4]
    d = d / np.hypot(*d)
    n = np.array([-d[1], d[0]])
    L, W = 0.9 + 0.17 * lw, 0.6 + 0.12 * lw          # degrees
    base = tip - d * L
    keep = [p for p in c if np.dot(p - base, d) < 0] + [base]
    k = np.array(keep)
    m.ax.plot(k[:, 0], k[:, 1], color=PAPER, lw=lw + 3, solid_capstyle="butt", zorder=3)
    m.ax.plot(k[:, 0], k[:, 1], color=col, lw=lw, solid_capstyle="butt", zorder=4)
    m.ax.add_patch(MplPoly([tip, base + n * W, base - n * W], closed=True, fc=col, ec=PAPER, lw=1.2, zorder=4.5))


# ---------------------------------------------------------------- above: the ocean
a = Map(-100.0, 24.0, -34.0, 44.0, lakes=False)
for ext in (GW, KW):
    a.ax.add_patch(Rectangle((ext[0], ext[2]), ext[1] - ext[0], ext[3] - ext[2], fc="none", ec=INK, lw=1.4,
                             ls=(0, (4, 2)), zorder=4))
# to Brazil, mostly from West Central Africa and the Bight of Benin
fat_arrow(a, [(11.5, -9.0), (-5.0, -11.5), (-20.0, -13.0), (-37.6, -12.6)], 13)
# to the Caribbean and Spanish America
fat_arrow(a, [(1.0, 3.5), (-15.0, 6.0), (-35.0, 10.5), (-60.0, 14.5)], 13)
# to North America
fat_arrow(a, [(-16.0, 13.0), (-35.0, 21.0), (-58.0, 29.0), (-76.6, 34.4)], 3.0)

a.label(-20.0, -18.6, "to Brazil\nabout 4.9 million", size="small", colour=INK, fs=20)
a.label(-30.0, 2.6, "to the Caribbean and\nSpanish America\nabout 5.3 million", size="small", colour=INK, fs=20)
a.label(-40.0, 28.6, "to North America\nabout 400,000", size="small", colour=INK, fs=20)
a.label(-55.0, -10.0, "BRAZIL", size="land", fs=21, style="normal")
a.label(-68.0, -24.0, "SOUTH\nAMERICA", size="land", fs=18, style="normal")
a.label(-95.0, 39.0, "NORTH\nAMERICA", size="land", fs=18, style="normal", ha="left")
a.label(14.0, 18.0, "AFRICA", size="land", fs=24, style="normal")
a.label(-74.0, 13.0, "Caribbean", size="sea", fs=18)
a.label(-8.0, 38.5, "EUROPE", size="land", fs=18, style="normal")
a.label(-12.0, -27.0, "ATLANTIC OCEAN", size="sea", fs=22)
a.label(-82.0, -30.0, "people landed, 1501-1866", size="small", colour=INK, fs=19, ha="left")
pa = os.path.join(SCRATCH, "ch52_ocean.png")
a.save(pa)

# ---------------------------------------------------------------- below left: the Gold Coast to Benin
g = Map(*GW, width=PW, lakes=False)
g.river("Niger", "Volta")
g.region([(-3.2, 8.8), (-0.8, 8.8), (0.4, 7.6), (0.0, 6.6), (-1.2, 6.1), (-2.6, 6.2), (-3.4, 7.2)], "gold")   # Asante
g.region([(1.6, 7.9), (2.7, 7.9), (2.7, 6.7), (2.4, 6.3), (1.7, 6.3), (1.5, 7.0)], "red")              # Dahomey
g.region([(2.8, 9.9), (5.4, 9.8), (5.6, 8.2), (4.0, 7.3), (2.8, 7.8)], "green")                        # Oyo
g.region([(5.0, 7.4), (6.4, 7.3), (6.6, 6.0), (5.6, 5.6), (4.9, 6.2)], "brown")                        # Benin
g.label(-1.6, 7.45, "ASANTE", fs=19)
g.label(2.1, 8.55, "DAHOMEY", fs=17)
g.label(4.2, 9.0, "OYO", fs=19)
g.label(5.8, 6.6, "BENIN", fs=17)
g.city(-1.30, 5.09, "Elmina and\nCape Coast", dx=0.0, dy=-0.75, bold=True)
g.city(2.08, 6.36, "Whydah", dx=0.0, dy=-0.45, bold=True)
g.label(-3.0, 5.55, "GOLD COAST", size="land", fs=17, style="normal")
g.label(3.6, 4.0, "Bight of Benin", size="sea", fs=19)
g.label(6.2, 10.9, "Niger", size="sea", fs=17)
g.scale(200, lon=-4.0, lat=GW[2] + 0.5)
pg = os.path.join(SCRATCH, "ch52_gold.png")
g.save(pg)

# ---------------------------------------------------------------- below right: Kongo and Ndongo
k = Map(*KW, width=PW, lakes=False)
k.river("Congo", "Cuanza")
k.region([(12.3, -6.0), (13.5, -5.8), (15.0, -5.0), (16.4, -5.6), (16.8, -7.0), (15.8, -8.0), (13.4, -8.0),
          (12.6, -7.0)], "blue")                                                                          # Kongo
k.region([(14.0, -8.3), (16.4, -8.2), (17.2, -9.0), (16.2, -9.8), (14.3, -9.6)], "purple")              # Ndongo
k.label(14.9, -6.7, "KONGO", fs=19)
k.label(15.6, -8.95, "NDONGO", fs=17)
k.city(13.23, -8.84, "Luanda", dx=-0.3, dy=0.0, bold=True)
k.label(11.9, -9.8, "Atlantic\nOcean", size="sea", fs=19)
k.label(13.0, -5.1, "Congo", size="sea", fs=17)
k.scale(200, lon=17.2, lat=KW[2] + 0.4)
pk = os.path.join(SCRATCH, "ch52_kongo.png")
k.save(pk)

# ---------------------------------------------------------------- one above the other
ia, ig, ik = (mpimg.imread(p) for p in (pa, pg, pk))
h = min(ig.shape[0], ik.shape[0])
paper = np.array([int(PAPER[i:i + 2], 16) / 255 for i in (1, 3, 5)] + [1.0])
row = np.hstack([ig[:h], np.tile(paper, (h, 1600 - ig.shape[1] - ik.shape[1], 1)), ik[:h]])
out = np.vstack([ia, np.tile(paper, (14, 1600, 1)), row])
dest = os.path.join(lib.ROOT, "chapters/52-slave-trade/images/map_slave_trade.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
