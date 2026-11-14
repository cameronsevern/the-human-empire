#!/usr/bin/env python3
"""Chapter 34: the four crusader states about 1135, with the Muslim cities around them and the site of
Hattin.

Drawn for this chapter, which had no map. The four areas are soft and approximate, drawn by eye after
the map "Crusader states in 1135" in English Wikipedia's article on the crusader states and checked
against the descriptions in its articles on each state: Edessa on both sides of the upper Euphrates,
Antioch from the Amanus hills to Jabala, Tripoli from Maraclea to Byblos with the hills behind, and
Jerusalem from Beirut to the edge of Egypt, with the lands beyond the Jordan down to the Red Sea.
Ascalon, still held by Egypt until 1153, is left out of the kingdom. Positions from English Wikipedia.
"""
from lib import Map, INK, FILL
from tracing import states

edessa = [(36.7, 37.75), (37.4, 38.15), (38.3, 38.05), (39.2, 37.75), (39.75, 37.35), (39.35, 36.9),
          (38.6, 36.7), (38.0, 36.6), (37.5, 36.75), (37.0, 37.05)]
antioch = [(35.6, 37.0), (36.0, 37.25), (36.7, 37.1), (37.0, 36.85), (36.95, 36.3), (36.75, 35.8),
           (36.45, 35.35), (36.1, 35.12), (35.6, 35.2), (35.4, 35.8), (35.6, 36.6)]
tripoli = [(35.7, 35.12), (36.1, 35.08), (36.45, 34.9), (36.5, 34.6), (36.3, 34.3), (35.95, 34.08),
           (35.6, 33.98), (35.3, 34.1), (35.4, 34.7)]
jerusalem = [(35.2, 33.95), (35.6, 33.93), (35.85, 33.55), (35.75, 33.15), (35.95, 32.7), (36.05, 32.2),
             (36.15, 31.6), (36.1, 30.9), (35.9, 30.3), (35.3, 29.6), (35.0, 29.45), (34.85, 29.7),
             (35.0, 30.4), (34.95, 31.1), (34.85, 31.6), (34.62, 31.86), (34.4, 32.3), (34.6, 32.6), (34.9, 33.3)]

m = Map(30.9, 40.6, 29.4, 38.4)
m.river("Euphrates", "Firat", "Nile", "Jordan", en=True)
states(m, [(edessa, "blue"), (antioch, "gold"), (tripoli, "green"), (jerusalem, "red")], alpha=0.5)
# the Sea of Galilee and the Dead Sea, drawn again above the shading
import numpy as np, lib
from matplotlib.patches import Polygon as MplPoly
for _, r in lib._lakes.iterrows():
    g = r.geometry.intersection(m.clip)
    for p in getattr(g, "geoms", [g]):
        if not p.is_empty and p.geom_type == "Polygon":
            m.ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=lib.SEA, ec=lib.SHORE, lw=0.7, zorder=2.3))

# the four states, named on or beside them
m.label(38.25, 37.75, "EDESSA", fs=23)
m.label(36.42, 36.72, "ANTIOCH", fs=22)
m.label(35.25, 34.75, "TRIPOLI", fs=22, ha="right")
m.label(34.3, 32.35, "KINGDOM OF\nJERUSALEM", fs=22, ha="right")

m.city(38.79, 37.16, "Edessa", dx=0.25, dy=-0.3, ha="left", size=20)
m.city(36.16, 36.20, "Antioch", dx=-0.2, dy=-0.3, ha="right", size=20)
m.city(35.85, 34.44, "Tripoli", dx=-0.2, dy=-0.12, ha="right", size=20)
m.city(35.08, 32.93, "Acre", dx=-0.2, dy=0.05, ha="right", size=20)
m.city(35.23, 31.78, "Jerusalem", dx=-0.2, dy=-0.15, ha="right", size=20, bold=True)
m.mark(35.45, 32.80, marker="X", ms=17)
m.label(35.3, 32.68, "Hattin", size="small", colour=INK, fs=20, ha="right")
m.city(36.29, 33.51, "Damascus", dx=0.2, dy=0.0, size=20)
m.city(37.16, 36.20, "Aleppo", dx=0.2, dy=-0.15, size=20)
m.city(31.24, 30.04, "Cairo", dx=0.2, dy=0.15, size=20)

m.label(32.4, 29.85, "EGYPT", size="land", fs=21, style="normal")
m.label(38.6, 34.2, "SYRIA", size="land", fs=21, style="normal")
m.label(38.9, 35.62, "Euphrates", size="sea", fs=19, rot=0)
m.label(33.0, 34.9, "Mediterranean\nSea", size="sea", fs=21)
m.scale(200, lon=38.3, lat=29.9)
m.save("chapters/34-crusades/images/map_crusader_states.png")
