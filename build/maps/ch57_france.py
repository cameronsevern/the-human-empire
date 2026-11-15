#!/usr/bin/env python3
"""Chapter 57: France in 1793, the year the republic faced enemies on every frontier and rebels at home.
Paris and Versailles; Varennes, where the king's flight was stopped in 1791; the revolt in the west,
south of the Loire; Lyon, Marseille and Toulon, the cities of the south that rose against Paris, with the
British fleet at Toulon; and arrows for the invading armies of 1793: the Austrians, British and Dutch in
the north-east, the Prussians and Austrians on the Rhine, the Sardinians in the Alps and the Spaniards
over the Pyrenees.

Drawn for this chapter, which had no map. The arrows are schematic and show where the invaders came in
during 1793, after the maps of the War of the First Coalition in English Wikipedia ("War of the First
Coalition", "Flanders campaign", "Rhine campaign of 1793", "War of the Pyrenees"). The region in revolt
is the Vendee militaire, roughly, after English Wikipedia's "War in the Vendee". France's frontiers of
1793 are not drawn. Positions from English Wikipedia.
"""
import numpy as np
from matplotlib.patches import Polygon as MplPoly
import lib
from lib import Map, INK, FILL, PAPER


def arrow(m, pts, lw=5.5, style="-"):
    """An arrow whose paper edge stops where the solid head begins."""
    c = lib.smooth(pts)
    col = FILL["purple"]
    tip = c[-1]
    d = c[-1] - c[-4]
    d = d / np.hypot(*d)
    n = np.array([-d[1], d[0]])
    L, W = 0.32, 0.17
    base = tip - d * L
    k = np.array([p for p in c if np.dot(p - base, d) < 0] + [base])
    m.ax.plot(k[:, 0], k[:, 1], color=PAPER, lw=lw + 3, solid_capstyle="butt", zorder=3)
    m.ax.plot(k[:, 0], k[:, 1], color=col, lw=lw, ls=style, solid_capstyle="butt", zorder=4)
    m.ax.add_patch(MplPoly([tip, base + n * W, base - n * W], closed=True, fc=col, ec=PAPER, lw=1.2, zorder=4.5))


m = Map(-5.3, 10.0, 41.2, 51.6)
m.river("Loire", "Seine", "Rhine", "Rhône", en=True)

# the revolt in the west, roughly
m.region([(-2.2, 47.3), (-1.5, 47.45), (-0.7, 47.4), (0.0, 47.05), (-0.15, 46.5), (-0.8, 46.25), (-1.6, 46.35),
          (-2.25, 46.7)], "red", alpha=0.5, hatch="//")
m.label(-1.0, 46.85, "revolt in\nthe west,\n1793", size="small", colour=INK, fs=17, style="italic")

arrow(m, [(4.6, 51.15), (3.9, 50.65), (3.4, 50.25)])
arrow(m, [(8.4, 50.1), (7.9, 49.55), (7.45, 49.05)])
arrow(m, [(8.3, 45.0), (7.5, 45.25), (6.8, 45.4)])
arrow(m, [(2.05, 41.75), (2.45, 42.1), (2.75, 42.55)])
arrow(m, [(-2.4, 42.7), (-1.9, 43.05), (-1.6, 43.35)])
arrow(m, [(6.9, 41.8), (6.3, 42.4), (5.97, 42.98)], lw=3.2, style=(0, (3, 1.8)))

m.label(5.6, 51.25, "Austrians,\nBritish, Dutch", size="small", colour=INK, fs=18, ha="left")
m.label(8.5, 50.55, "Prussians,\nAustrians", size="small", colour=INK, fs=18)
m.label(8.6, 44.55, "Sardinians", size="small", colour=INK, fs=18)
m.label(1.0, 41.75, "Spaniards", size="small", colour=INK, fs=18)
m.label(-3.2, 42.55, "Spaniards", size="small", colour=INK, fs=18)
m.label(7.4, 41.55, "British fleet", size="small", colour=INK, fs=18, ha="left")

m.city(2.35, 48.86, "Paris", dx=0.18, dy=0.12, bold=True)
m.city(2.12, 48.80, "Versailles", dx=-0.18, dy=-0.1)
m.city(5.03, 49.23, "Varennes, 1791", dx=-0.18, dy=0.0)
m.city(4.84, 45.76, "Lyon", dx=-0.18, dy=0.0, bold=True)
m.city(5.37, 43.30, "Marseille", dx=-0.18, dy=0.05, bold=True)
m.city(5.93, 43.12, "Toulon", dx=0.18, dy=-0.12, bold=True)

m.label(2.2, 46.9, "FRANCE", size="region", fs=26, spaced=True)
m.label(-1.2, 47.75, "Loire", size="sea", fs=16)
m.label(-4.0, 45.5, "Bay of\nBiscay", size="sea", fs=20)
m.label(-1.2, 50.35, "English Channel", size="sea", fs=19)
m.label(5.0, 42.3, "Mediterranean", size="sea", fs=19)
m.label(5.5, 50.55, "AUSTRIAN\nNETHERLANDS", size="land", fs=15, style="normal")
m.label(-2.5, 42.0, "SPAIN", size="land", fs=18, style="normal")
m.label(8.9, 45.6, "PIEDMONT", size="land", fs=15, style="normal")
m.label(0.0, 51.4, "BRITAIN", size="land", fs=17, style="normal")
m.label(8.6, 48.4, "Rhine", size="sea", fs=16, rot=75)
m.scale(200, lon=-4.8, lat=41.7)
m.save("chapters/57-france/images/map_france_1793.png")
