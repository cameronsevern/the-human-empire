#!/usr/bin/env python3
"""Chapter 61: the thread of cotton about 1850. Raw cotton from the cotton fields of the American South,
shipped from New Orleans across the Atlantic to Liverpool; the cloth made in and around Manchester shipped
out again to Europe, the Americas, Africa and India (round the Cape of Good Hope, before the Suez canal).
An inset shows Liverpool and Manchester, and the railway of 1830 between them.

Drawn for this chapter, which had no map. The cotton fields are a rough area: the cotton belt about 1850,
from South Carolina to east Texas, after the maps of cotton growing and of slavery in the 1850s in English
Wikipedia ("Cotton plantation", "Slavery in the United States"). The sea routes are schematic: they show
where the cotton and the cloth went, not the sailing tracks. New Orleans stands for the cotton ports of
the Gulf and the Atlantic coast. Positions from English Wikipedia.
"""
import os
import matplotlib.image as mpimg
from matplotlib.patches import Polygon as MplPoly, Rectangle
from lib import Map, INK, PAPER, FILL, HALO

SCRATCH = os.environ.get("SCRATCH", "/tmp")

m = Map(-112.0, 96.0, -41.0, 67.0, lakes=False)
m.river("Mississippi")

# the cotton fields
m.region([(-81.0, 34.8), (-83.5, 34.6), (-87.0, 35.2), (-90.0, 36.5), (-92.5, 35.0), (-95.5, 33.0), (-97.0, 30.5),
          (-96.0, 29.2), (-93.0, 30.5), (-91.0, 30.6), (-88.5, 31.0), (-85.5, 31.2), (-82.5, 31.6), (-80.8, 32.8)],
         "green", alpha=0.6, hatch="//")
m.label(-89.5, 40.2, "cotton fields\nof the American South", size="small", colour=INK, fs=17)

# raw cotton to Liverpool
RAW = [(-90.07, 29.95), (-88.0, 27.0), (-84.0, 24.4), (-79.8, 25.6), (-75.0, 33.0), (-60.0, 40.5), (-38.0, 46.5),
       (-16.0, 50.0), (-7.0, 51.6), (-5.2, 53.2), (-3.6, 53.45)]
m.route(RAW, colour="red", lw=4.2)
m.label(-44.0, 49.8, "raw cotton", size="small", colour=FILL["red"], fs=19)

# cloth out again
cloth = dict(colour=INK, lw=2.6, style=(0, (4, 2.2)))
TRUNK = [(-3.6, 53.3), (-5.6, 52.6), (-7.5, 50.6)]
m.route(TRUNK, arrow=False, **cloth)
m.route([(-7.5, 50.6), (-4.0, 49.8), (1.5, 50.6), (5.0, 53.2), (8.4, 54.0)], **cloth)                    # Europe
m.route([(-7.5, 50.6), (-20.0, 38.0), (-30.0, 10.0), (-35.0, -8.0), (-42.5, -22.5)], **cloth)             # Americas
m.route([(-7.5, 50.6), (-15.0, 40.0), (-20.0, 20.0), (-14.0, 8.0), (-3.0, 4.2)], **cloth)                # Africa
m.route([(-7.5, 50.6), (-18.0, 32.0), (-22.0, 0.0), (-5.0, -28.0), (20.0, -38.0), (45.0, -30.0), (62.0, -8.0),
         (80.0, 3.5), (86.0, 12.0), (88.0, 20.8)], **cloth)                                                # India
m.label(11.0, 46.5, "cloth to Europe", size="small", colour=INK, fs=17)
m.label(-46.0, -6.0, "cloth to the\nAmericas", size="small", colour=INK, fs=17)
m.label(-4.5, 10.8, "cloth to\nAfrica", size="small", colour=INK, fs=17)
m.label(73.0, -9.0, "cloth to India", size="small", colour=INK, fs=17)

m.city(-90.07, 29.95, "New Orleans", dx=-1.5, dy=-2.4, bold=True)
m.city(-2.6, 53.45, None, r=9)
m.label(-8.0, 60.6, "Liverpool and\nManchester", size="small", colour=INK, fs=17, ha="right", style="normal")
m.ax.plot([-8.6, -3.0], [59.0, 54.0], color=INK, lw=1.0, zorder=6.5)
m.city(88.36, 22.57, None)
m.label(91.5, 26.2, "Bengal", size="small", colour=INK, fs=17)

m.label(-58.0, -16.0, "SOUTH\nAMERICA", size="land", fs=17, style="normal")
m.label(22.0, 10.0, "AFRICA", size="land", fs=21, style="normal")
m.label(32.0, 57.0, "EUROPE", size="land", fs=19, style="normal")
m.label(78.0, 19.0, "INDIA", size="land", fs=19, style="normal")
m.label(-48.0, 25.0, "ATLANTIC\nOCEAN", size="sea", fs=20)
m.label(80.0, -27.0, "INDIAN\nOCEAN", size="sea", fs=19)

# ---------------------------------------------------------------- the inset: Liverpool and Manchester
IW, IE, IS, IN = -3.22, -1.98, 53.22, 53.66
FX0, FY0, FW = 0.006, 0.008, 0.215
n = Map(IW, IE, IS, IN, width=16.0 * FW, lakes=False)
n.river("Mersey")
n.line([(-2.98, 53.405), (-2.75, 53.43), (-2.52, 53.455), (-2.24, 53.477)], colour=INK, lw=2.4, style=(0, (4, 2)),
       curved=False)
n.city(-2.98, 53.41, "Liverpool", dx=0.0, dy=0.07, bold=True, r=9)
n.city(-2.24, 53.48, "Manchester", dx=0.0, dy=0.07, bold=True, r=9)
n.label(-2.56, 53.39, "railway, 1830", size="small", colour=INK, fs=15)
n.label(-2.6, 53.28, "50 km apart", size="small", colour=INK, fs=15)
n.ax.add_patch(MplPoly([(IW, IS), (IE, IS), (IE, IN), (IW, IN)], closed=True, fc="none", ec=INK, lw=3, zorder=10))
pi = os.path.join(SCRATCH, "ch61_inset.png")
n.save(pi)

img = mpimg.imread(pi)
fh = m.fig.get_size_inches()[1]
ax = m.fig.add_axes([FX0, FY0, FW, img.shape[0] / 100.0 / fh])
ax.imshow(img)
ax.set_axis_off()
m.save("chapters/61-coal/images/map_cotton_thread.png")
