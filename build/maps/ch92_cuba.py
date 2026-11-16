#!/usr/bin/env python3
"""Chapter 92: the Cuban missile crisis, October 1962. Cuba and the south-eastern United States, with the
Soviet missile sites, the range of the medium-range missiles (enough to reach Washington), the quarantine
line, the Bay of Pigs and the American base at Guantanamo; inset: Turkey, with the range of the American
Jupiter missiles there, which could reach Moscow.

Drawn for this chapter, which had no map. Missile sites as identified by American photo-interpreters in
October 1962, after English Wikipedia's "Cuban Missile Crisis" and the CIA's published maps: medium-range
(R-12) sites near San Cristobal and Sagua la Grande, intermediate-range (R-14) sites, never finished, near
Guanajay and Remedios. Range circle: 2,000 km from San Cristobal, the round figure usually given for the
R-12 (about 1,100 nautical miles). The quarantine line: the arc 500 nautical miles from Cuba's eastern tip
(Cape Maisi) to which the interception line was drawn in on 23 and 24 October, roughly. The Jupiters were at
Cigli near Izmir, about 2,100 km from Moscow, within their range of 2,400 km; drawn as a line. Geodesic circles from pyproj. Positions from English Wikipedia.
"""
import os
import numpy as np
import pyproj
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO

GEOD = pyproj.Geod(ellps="WGS84")
SCRATCH = os.environ.get("SCRATCH", "/tmp")
RED, BLUE = FILL["red"], FILL["blue"]


def circle(lon, lat, km, a0=0, a1=360, n=240):
    az = np.linspace(a0, a1, n)
    x, y, _ = GEOD.fwd(np.full(n, lon), np.full(n, lat), az, np.full(n, km * 1000.0))
    return np.column_stack([x, y])


def ring(m, xy, colour, lw=2.6, style=(0, (6, 2.5))):
    m.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=lw + 2.6, zorder=3.4)
    m.ax.plot(xy[:, 0], xy[:, 1], color=colour, lw=lw, ls=style, zorder=3.5)


# ================================================================ inset: Turkey and Moscow
I = Map(22.0, 46.0, 35.5, 58.5, width=4.6)
izmir = (27.0, 38.51)
I.route([izmir, (31.0, 45.5), (37.4, 55.5)], colour="blue", lw=3.0, style=(0, (4, 1.8)))
I.ax.plot(*izmir, "^", ms=15, mfc=BLUE, mec=INK, mew=1.4, zorder=6)
I.city(37.62, 55.75, "Moscow", dx=-0.7, dy=0.0)
I.label(26.4, 37.0, "Jupiter\nmissiles", size="small", colour=INK, fs=15, ha="right")
I.label(35.0, 39.2, "TURKEY", fs=15)
I.label(35.8, 50.0, "in range:\nabout\n2,100 km", size="small", colour=BLUE, fs=15, style="italic", ha="left")
I.label(34.0, 43.4, "Black Sea", size="sea", fs=15)
pin = os.path.join(SCRATCH, "ch92_inset.png")
I.save(pin)

# ================================================================ Cuba and the United States
m = Map(-94.0, -66.0, 16.5, 41.0)
sites_mr = [(-83.05, 22.72), (-80.08, 22.81)]          # San Cristobal, Sagua la Grande
sites_ir = [(-82.69, 22.92), (-79.54, 22.49)]          # Guanajay, Remedios
ring(m, circle(-83.05, 22.72, 2000), RED)
q = circle(-74.13, 20.22, 926, a0=-28, a1=112)          # 500 nautical miles from Cape Maisi
m.ax.plot(q[:, 0], q[:, 1], color=PAPER, lw=6.5, zorder=3.4)
m.ax.plot(q[:, 0], q[:, 1], color=INK, lw=3.2, ls=(0, (1.2, 1.4)), zorder=3.5)
for x, y in sites_mr:
    m.ax.plot(x, y, "^", ms=17, mfc=RED, mec=INK, mew=1.5, zorder=6)
for x, y in sites_ir:
    m.ax.plot(x, y, "^", ms=13, mfc=PAPER, mec=RED, mew=2.4, zorder=6)
m.city(-82.38, 23.13, "Havana", dx=-0.3, dy=0.45)
m.city(-77.04, 38.90, "Washington", dx=0.4, dy=0.0, bold=True)
m.city(-80.19, 25.77, "Miami", dx=0.35, dy=0.1)
m.city(-90.07, 29.95, "New Orleans", dx=0.0, dy=0.5)
m.ax.plot(-81.15, 22.08, "X", ms=15, mfc=INK, mec=PAPER, mew=1.4, zorder=6)
m.label(-81.1, 21.35, "Bay of Pigs", size="small", colour=INK, fs=16)
m.ax.plot(-75.15, 19.93, "s", ms=12, mfc=BLUE, mec=INK, mew=1.4, zorder=6)
m.label(-75.5, 19.3, "Guantánamo", size="small", colour=INK, fs=16)
m.label(-77.4, 21.75, "CUBA", fs=19)
m.label(-84.6, 33.6, "UNITED STATES", size="land", colour="#5a534b", fs=19, style="normal")
m.label(-91.0, 19.0, "MEXICO", size="land", colour="#5a534b", fs=16, style="normal")
m.label(-89.8, 25.6, "Gulf of Mexico", size="sea", fs=18)
m.label(-80.5, 17.6, "Caribbean Sea", size="sea", fs=18)
m.label(-70.3, 29.6, "Atlantic Ocean", size="sea", fs=19)
m.label(-80.6, 24.1, "missile sites", size="small", colour=INK, fs=16)
m.label(-93.3, 37.6, "range of the\nSoviet missiles,\n2,000 km", size="small", colour=RED, fs=16,
        style="italic", ha="left")
m.label(-67.6, 23.6, "quarantine\nline", size="small", colour=INK, fs=16, ha="center")
from matplotlib.lines import Line2D
handles = [Line2D([0], [0], ls="none", marker="^", ms=15, mfc=RED, mec=INK, label="medium-range missile site"),
           Line2D([0], [0], ls="none", marker="^", ms=12, mfc=PAPER, mec=RED, mew=2.2,
                  label="longer-range site, unfinished"),
           Line2D([0], [0], ls="none", marker="s", ms=11, mfc=BLUE, mec=INK, label="American naval base")]
leg = m.ax.legend(handles=handles, loc="lower left", fontsize=16, frameon=True, fancybox=False, edgecolor=INK,
                  facecolor=PAPER, framealpha=1, borderpad=0.6, labelspacing=0.45)
leg.set_zorder(9); leg.get_frame().set_linewidth(1.2)
m.scale(500, lon=-76.0, lat=17.3)

img = mpimg.imread(pin)
H = m.fig.get_size_inches()[1] * 100
h, w = img.shape[:2]
ia = m.fig.add_axes([(1600 - w - 10) / 1600, (H - h - 10) / H, w / 1600, h / H])
ia.imshow(img); ia.axis("off")
m.save("chapters/92-missiles/images/map_cuba_1962.png")
