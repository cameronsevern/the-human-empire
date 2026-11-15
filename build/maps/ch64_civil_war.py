#!/usr/bin/env python3
"""Chapter 64: the United States in 1861. The free states; the four slave states that stayed in the Union
(Delaware, Maryland, Kentucky, Missouri); the eleven Confederate states; the western territories and
Indian Territory. Fort Sumter and Atlanta on the main map; an inset of Virginia and Maryland with
Washington, Richmond, Fort Monroe, Antietam (1862), Gettysburg (1863) and Appomattox (1865).

Drawn for this chapter, which had no map. The state lines are drawn by hand, simplified, after the maps of
the Union and the Confederacy in 1861 in English Wikipedia ("Confederate States of America", "Border
states (American Civil War)"); boundaries along the Mississippi, Ohio, Potomac, Red and Rio Grande follow
the Natural Earth rivers. Virginia is shown whole, as it was in 1861, before West Virginia was split off
in 1863. Kansas is shown as a free state (January 1861); Nebraska, Dakota, Colorado, Nevada, Utah,
Washington and New Mexico as territories, without the lines between them. Positions from English
Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
from matplotlib.patches import Polygon as MplPoly, Rectangle
from shapely.geometry import Polygon
from lib import Map, INK, PAPER, FILL, HALO, course

SCRATCH = os.environ.get("SCRATCH", "/tmp")


def P(pts):
    return Polygon(pts).buffer(0)


def part(line, a, b):
    """The stretch of a river line between the vertices nearest a and b, in that order."""
    c = np.array(line)
    i = int(np.argmin(np.hypot(*(c - a).T)))
    j = int(np.argmin(np.hypot(*(c - b).T)))
    seg = c[i:j + 1] if i <= j else c[j:i + 1][::-1]
    return [tuple(p) for p in seg]


MISS = course("Mississippi", (-91.42, 40.38), (-89.25, 29.2), step=2)
OHIO = course("Ohio", (-80.1, 40.5), (-89.13, 37.0), step=2)
POT = course("Potomac", (-79.4, 39.25), (-76.3, 38.0), step=2)
RED = [(-94.04, 33.55), (-94.48, 33.64), (-95.3, 33.88), (-96.0, 33.83), (-96.6, 33.85), (-97.2, 33.75), (-97.95, 33.88),
       (-98.5, 34.1), (-99.2, 34.25), (-99.7, 34.4), (-100.0, 34.56)]          # the Red river, by hand
RIO = course("Rio Grande", (-106.53, 31.78), (-97.15, 25.95), step=4)

OHIO_WV = part(OHIO, (-80.52, 40.64), (-82.6, 38.42))
OHIO_KY = part(OHIO, (-82.6, 38.42), (-89.13, 37.0))
TUG = [(-82.5, 38.0), (-82.2, 37.65), (-81.97, 37.54), (-82.35, 37.27), (-82.9, 37.0), (-83.68, 36.6)]
KYTN = [(-83.68, 36.6), (-88.07, 36.68), (-88.07, 36.5), (-89.5, 36.5)]
ARK_N = [(-89.7, 36.0), (-90.37, 36.0), (-90.15, 36.5), (-94.62, 36.5)]
MD_E = [(-79.48, 39.72), (-75.79, 39.72), (-75.79, 38.46), (-75.05, 38.46), (-75.24, 38.03), (-75.65, 37.95),
        (-76.24, 37.9)]

CSA = P(MD_E[-3:] + POT[::-1] + [(-79.48, 39.2), (-79.48, 39.72), (-80.52, 39.72), (-80.52, 40.64)] + OHIO_WV + TUG
        + KYTN + part(MISS, (-89.5, 36.5), (-89.7, 36.0)) + ARK_N + [(-94.43, 35.4), (-94.48, 33.64)]
        + part(RED, (-94.48, 33.64), (-100.0, 34.56)) + [(-100.0, 36.5), (-103.04, 36.5), (-103.04, 32.0),
                                                         (-106.62, 32.0)] + RIO
        + [(-96.0, 25.0), (-88.0, 28.5), (-83.0, 24.0), (-79.5, 24.0), (-79.0, 30.0), (-75.0, 35.0), (-74.8, 37.5)])
MO = P([(-95.77, 40.58), (-91.73, 40.61)] + part(MISS, (-91.42, 40.38), (-89.7, 36.0)) + ARK_N[1:] +
       [(-94.62, 39.1), (-94.9, 39.5), (-95.0, 39.8), (-95.3, 40.0)])
KY = P(OHIO_KY + part(MISS, (-89.17, 37.0), (-89.5, 36.5)) + KYTN[::-1] + TUG[::-1][1:])
MD = P(MD_E + POT[::-1] + [(-79.48, 39.2)])
DE = P([(-75.79, 39.72), (-75.45, 39.81), (-75.57, 39.6), (-75.45, 39.35), (-75.2, 39.0), (-75.0, 38.78),
        (-75.05, 38.46), (-75.79, 38.46)])
TERR = P([(-96.6, 49.0), (-96.6, 45.3), (-96.45, 45.3), (-96.45, 43.5), (-96.6, 42.5), (-95.9, 41.3),
          (-95.77, 40.58), (-95.3, 40.0), (-102.05, 40.0), (-102.05, 37.0), (-100.0, 37.0), (-100.0, 36.5),
          (-103.04, 36.5), (-103.04, 32.0), (-106.62, 32.0), (-106.53, 31.78), (-108.2, 31.78), (-108.2, 31.33),
          (-111.07, 31.33), (-114.8, 32.49), (-114.72, 32.72), (-114.63, 35.0), (-120.0, 39.0), (-120.0, 42.0),
          (-117.0, 42.0), (-117.0, 44.3), (-116.9, 46.0), (-118.98, 46.0), (-119.5, 46.2), (-124.1, 46.25),
          (-125.5, 46.3), (-125.5, 48.4), (-124.7, 48.5), (-123.2, 48.3), (-123.2, 49.0)])
IT = P([(-94.62, 37.0), (-100.0, 37.0), (-100.0, 34.56)] + part(RED, (-100.0, 34.56), (-94.48, 33.64))
       + [(-94.43, 35.4)])
USA = P([(-125.5, 49.0), (-95.15, 49.0), (-95.15, 49.38), (-94.8, 48.7), (-93.0, 48.6), (-91.0, 48.2), (-89.6, 48.0),
         (-87.0, 47.5), (-84.6, 46.5), (-84.1, 46.2), (-82.5, 45.3), (-82.4, 43.0), (-83.05, 42.3), (-82.5, 41.7),
         (-79.2, 42.6), (-79.0, 43.3), (-76.3, 43.6), (-76.3, 44.2), (-74.7, 45.0), (-71.5, 45.0), (-70.0, 46.0),
         (-69.2, 47.45), (-67.8, 47.1), (-67.8, 45.7), (-66.95, 44.8), (-66.0, 44.5), (-66.0, 40.0), (-74.8, 37.5),
         (-75.0, 35.0), (-79.0, 30.0), (-79.5, 24.0), (-83.0, 24.0), (-88.0, 28.5), (-96.0, 25.0)] + RIO[::-1]
        + [(-108.2, 31.78), (-108.2, 31.33), (-111.07, 31.33), (-114.8, 32.49), (-114.72, 32.72), (-117.12, 32.53),
           (-118.0, 32.0), (-126.0, 35.0)])
FREE = USA
for g in (CSA, MO, KY, MD, DE, TERR, IT):
    FREE = FREE.difference(g)

STATE_LINES = [
    [(-83.68, 36.6), (-75.9, 36.55)],                                                           # VA south
    [(-81.68, 36.59), (-82.2, 36.1), (-83.0, 35.8), (-84.0, 35.5), (-84.32, 35.0)],              # NC / TN
    [(-83.1, 35.0), (-82.4, 35.2), (-80.9, 35.1), (-80.8, 34.8), (-79.7, 34.8), (-78.55, 33.85)],  # NC / SC
    [(-83.1, 35.0), (-82.6, 34.5), (-81.9, 33.6), (-81.4, 32.6), (-80.9, 32.03)],                # SC / GA
    [(-90.3, 35.0), (-84.32, 35.0)],                                                             # TN south
    [(-85.6, 35.0), (-85.18, 32.86), (-85.0, 32.3), (-85.0, 31.0)],                              # GA / AL
    [(-88.2, 35.0), (-88.47, 31.9), (-88.4, 30.4)],                                              # AL / MS
    [(-87.45, 30.3), (-87.6, 31.0), (-85.0, 31.0), (-84.86, 30.7), (-82.2, 30.57), (-81.45, 30.71)],  # FL
    [(-91.64, 31.0), (-89.73, 31.0), (-89.6, 30.2)],                                             # MS / LA
    [(-94.04, 33.55), (-94.04, 33.02), (-91.16, 33.02)],                                         # AR / LA
    [(-94.04, 33.02), (-94.04, 32.0), (-93.75, 31.0), (-93.85, 29.7)],                           # TX / LA
]
REGIONS = ((FREE, "blue", 0.36), (MO, "gold", 0.5), (KY, "gold", 0.5), (MD, "gold", 0.5), (DE, "gold", 0.5),
           (CSA, "red", 0.36), (TERR, "grey", 0.25), (IT, "grey", 0.25))


def draw(m, lw=1.1):
    for g, c, a in REGIONS:
        m.region(g, c, alpha=a, lakes_out=True)
    for ln in STATE_LINES:
        xy = np.array(ln)
        m.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=lw, alpha=0.7, zorder=2.3)
    m.river("Mississippi", "Ohio", "Potomac", "James")


# ---------------------------------------------------------------- the inset: Virginia and Maryland
IW, IE, IS, IN = -80.6, -75.4, 36.75, 40.35
FX0, FY0, FW = 0.773, 0.007, 0.22
n = Map(IW, IE, IS, IN, width=16.0 * FW, lakes=False)
draw(n)
n.city(-77.04, 38.90, "Washington", dx=-0.12, dy=0.1, ha="right", bold=True)
n.city(-77.44, 37.54, "Richmond", dx=-0.12, dy=0.12, ha="right", bold=True)
n.city(-76.31, 37.00, "Fort Monroe", dx=-0.12, dy=-0.12, ha="right", size=15)
n.city(-77.74, 39.47, "Antietam 1862", dx=-0.12, dy=-0.1, ha="right", star=True, r=7, size=15)
n.city(-77.23, 39.83, "Gettysburg 1863", dx=0.0, dy=0.2, ha="center", star=True, r=7, size=15)
n.city(-78.80, 37.38, "Appomattox 1865", dx=0.0, dy=-0.22, ha="center", star=True, r=7, size=15)
n.label(-79.2, 38.25, "VIRGINIA", fs=15)
n.label(-76.6, 39.55, "MD", fs=15)
n.ax.add_patch(MplPoly([(IW, IS), (IE, IS), (IE, IN), (IW, IN)], closed=True, fc="none", ec=INK, lw=3, zorder=10))
pi = os.path.join(SCRATCH, "ch64_inset.png")
n.save(pi)

# ---------------------------------------------------------------- the main map
m = Map(-125.0, -66.0, 22.6, 49.6)
draw(m, lw=1.0)
m.river("Rio Grande", "Missouri")
m.ax.add_patch(Rectangle((IW, IS), IE - IW, IN - IS, fc="none", ec=INK, lw=1.4, ls=(0, (4, 2)), zorder=5))

for lon, lat, t, r in [(-99.0, 31.4, "TEXAS", 0), (-92.4, 34.8, "ARKANSAS", 0), (-92.3, 30.9, "LOUISIANA", 0),
                       (-89.75, 32.7, "MISSISSIPPI", 90), (-86.75, 32.6, "ALABAMA", 90), (-83.3, 31.75, "GEORGIA", 0),
                       (-81.45, 28.1, "FLORIDA", -68), (-80.55, 34.25, "SOUTH\nCAROLINA", 0),
                       (-79.0, 35.65, "NORTH CAROLINA", 0), (-86.2, 35.75, "TENNESSEE", 0),
                       (-80.8, 37.7, "VIRGINIA", 0), (-85.4, 37.45, "KENTUCKY", 0), (-92.5, 38.4, "MISSOURI", 0)]:
    m.label(lon, lat, t, fs=15, rot=r)
for (x0, y0), (x1, y1), t in [((-76.7, 39.3), (-72.0, 38.4), "MARYLAND"), ((-75.5, 39.0), (-72.0, 37.5), "DELAWARE")]:
    m.ax.plot([x0, x1 - 0.15], [y0, y1], color=INK, lw=1.0, zorder=6.5)
    m.label(x1, y1, t, fs=15, ha="left")
m.label(-109.0, 41.5, "TERRITORIES", size="land", fs=19, style="normal", spaced=True)
m.label(-97.2, 35.6, "Indian\nTerritory", size="land", fs=15)
m.label(-91.6, 45.3, "FREE STATES", size="land", fs=18, style="normal", colour="#3e5f7a")
m.label(-120.4, 40.0, "FREE", size="land", fs=16, style="normal", colour="#3e5f7a")

m.city(-79.87, 32.75, "Fort Sumter", dx=0.45, dy=0.0, ha="left")
m.city(-84.39, 33.75, "Atlanta 1864", dx=0.0, dy=-0.62, ha="center")
m.label(-89.0, 25.4, "Gulf of Mexico", size="sea", fs=18)
m.label(-71.0, 34.6, "ATLANTIC\nOCEAN", size="sea", fs=19)
m.label(-104.0, 27.0, "MEXICO", size="land", fs=17, style="normal", spaced=True)
m.key([("blue", "free states"), ("gold", "slave states that stayed in the Union"), ("red", "Confederate states"),
       ("grey", "territories")], loc="lower left", size=15)

img = mpimg.imread(pi)
fh = m.fig.get_size_inches()[1]
ax = m.fig.add_axes([FX0, FY0, FW, img.shape[0] / 100.0 / fh])
ax.imshow(img)
ax.set_axis_off()
m.save("chapters/64-civil-war/images/map_1861.png")
