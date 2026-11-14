#!/usr/bin/env python3
"""Chapter 14: the kingdoms of Israel and Judah among their neighbours, about 2,850 years ago.

The two kingdoms are drawn by eye after "Kingdoms of Israel and Judah map 830" by FinnWikiNo
and Richardprins (Wikimedia Commons, CC BY-SA 3.0), the map this one replaces, by way of the
towns each one takes in (Bethel and Jericho in Israel; Jerusalem, Lachish, Hebron and Beersheba
in Judah; Gilead across the Jordan in Israel, Dibon in Moab), and checked against the map of
the two kingdoms in the ninth century BCE in Finkelstein, The Forgotten Kingdom. The borders
are rough: nobody knows them closely. Town positions from English Wikipedia.
"""
from lib import Map, SEA, SHORE
import lib
import numpy as np
from matplotlib.patches import Polygon as MplPoly

israel = [(34.72, 31.98), (34.85, 32.40), (34.95, 32.75), (35.08, 32.95), (35.25, 33.08), (35.45, 33.25),
          (35.55, 33.45), (35.70, 33.48), (35.85, 33.28), (35.82, 33.00), (35.78, 32.75), (35.88, 32.55),
          (36.05, 32.45), (36.05, 32.10), (35.97, 31.85), (35.98, 31.70), (35.75, 31.68), (35.58, 31.76),
          (35.47, 31.86), (35.30, 31.87), (35.10, 31.87), (34.92, 31.88), (34.76, 31.90)]
judah = [(34.80, 31.88), (35.00, 31.88), (35.20, 31.87), (35.35, 31.86), (35.44, 31.80), (35.38, 31.55),
         (35.36, 31.30), (35.32, 31.10), (35.10, 31.00), (34.85, 31.05), (34.74, 31.22), (34.73, 31.50),
         (34.76, 31.72)]

m = Map(34.2, 36.5, 30.85, 33.6, width=13)
m.river("Jordan")
m.region(israel, "blue", alpha=0.45)
m.region(judah, "gold", alpha=0.55)
for _, r in lib._lakes.iterrows():          # the lakes again, over the kingdoms
    g = r.geometry.intersection(m.clip)
    for p in getattr(g, "geoms", [g]):
        if p.geom_type == "Polygon" and not p.is_empty:
            m.ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=SEA, ec=SHORE, lw=0.8, zorder=2.3))

m.label(35.15, 32.62, "ISRAEL", fs=26)
m.label(35.02, 31.33, "JUDAH", fs=26)
m.label(36.20, 33.15, "Aram", size="land", fs=21)
m.label(36.28, 31.95, "Ammon", size="land", fs=21)
m.label(35.85, 31.38, "Moab", size="land", fs=21)
m.label(35.55, 30.98, "Edom", size="land", fs=21)
m.label(34.50, 31.30, "Philistines", size="land", fs=21, rot=52)
m.label(35.30, 33.40, "Phoenicians", size="land", fs=21)
m.label(34.55, 32.75, "Mediterranean\nSea", size="sea", fs=21)
m.label(35.62, 31.12, "Dead\nSea", size="sea", fs=18)
m.label(35.38, 32.83, "Sea of\nGalilee", size="sea", fs=17)
m.label(35.62, 32.25, "Jordan", size="sea", rot=-85, fs=17)

m.city(35.23, 31.78, "Jerusalem", dx=-0.06, star=True, bold=True, size=19)
m.city(35.19, 32.28, "Samaria", dx=-0.05, star=True, bold=True, size=19)
m.city(34.85, 31.56, "Lachish", dx=0.05, size=19)
m.city(36.29, 33.51, "Damascus", dx=-0.05, size=19)
m.scale(50)
m.save("chapters/14-one-god/images/map_two_kingdoms.png")
