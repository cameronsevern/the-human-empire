#!/usr/bin/env python3
"""Chapter 36: the Americas before Columbus, with the three regions the chapter describes: the Maya
lowlands and Teotihuacan, the Andes with Tiwanaku and Wari, and Cahokia on the Mississippi. A second
map (ch36_maya.py) shows the Maya country close up.

Drawn for this chapter, which had no map. The areas are soft and approximate: the Maya lowlands as in
English Wikipedia's article on the Maya civilization; Tiwanaku's and Wari's areas of rule or influence
at their height, about 500 to 1000, drawn by eye after the maps in English Wikipedia's articles on the
two states. Positions from English Wikipedia.
"""
from lib import Map, INK
from tracing import states

maya = [(-92.6, 17.4), (-91.4, 18.6), (-90.6, 19.9), (-90.4, 21.2), (-88.0, 21.7), (-86.7, 21.4),
        (-87.4, 18.4), (-88.3, 15.8), (-89.4, 15.0), (-90.8, 15.9), (-92.0, 16.3)]
wari = [(-79.6, -7.6), (-77.8, -7.2), (-76.4, -9.4), (-74.2, -11.2), (-72.2, -12.6), (-71.0, -14.3),
        (-71.8, -15.6), (-73.6, -16.4), (-76.0, -14.4), (-77.6, -12.0), (-79.0, -9.5)]
tiwanaku = [(-70.6, -14.6), (-68.6, -14.6), (-66.6, -16.4), (-66.4, -18.8), (-67.6, -20.6), (-69.6, -20.4),
            (-70.6, -18.4), (-71.4, -16.8)]

m = Map(-101.5, -60.0, -21.5, 41.3)
m.river("Mississippi", "Missouri", "Ohio", "Amazon", "Amazonas", en=True, lw=1.8)
states(m, [(maya, "green"), (wari, "red"), (tiwanaku, "gold")], alpha=0.5)
# Lake Titicaca and the other lakes, drawn again above the shading
import numpy as np, lib
from matplotlib.patches import Polygon as MplPoly
for _, r in lib._lakes.iterrows():
    if (r.get("scalerank", 0) or 0) > 1:
        continue
    g = r.geometry.intersection(m.clip)
    for p in getattr(g, "geoms", [g]):
        if not p.is_empty and p.geom_type == "Polygon":
            m.ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=lib.SEA, ec=lib.SHORE, lw=0.7, zorder=2.3))

m.label(-86.0, 19.6, "MAYA\nLOWLANDS", fs=23, ha="left")
m.city(-98.84, 19.69, "Teotihuacan", dx=0.5, dy=-1.3, size=22, ha="left")

m.label(-78.6, -11.0, "WARI", fs=23, ha="right")
m.label(-71.6, -19.3, "TIWANAKU", fs=23, ha="right")
m.label(-67.9, -14.6, "Lake Titicaca", size="sea", fs=20, ha="left")
m.label(-78.2, -2.6, "ANDES", size="land", fs=22, style="normal", rot=-62)

m.city(-90.06, 38.66, "Cahokia", dx=0.9, dy=0.0, size=22, bold=True)
m.label(-93.0, 33.0, "Mississippi", size="sea", fs=20, rot=-80)

m.label(-90.0, 25.3, "Gulf of\nMexico", size="sea", fs=21)
m.label(-76.0, 15.0, "Caribbean Sea", size="sea", fs=21)
m.label(-92.0, 2.0, "PACIFIC\nOCEAN", size="sea", fs=23)
m.label(-66.0, 29.0, "ATLANTIC\nOCEAN", size="sea", fs=23)
m.label(-95.0, 36.5, "NORTH AMERICA", size="land", fs=21, style="normal")
m.label(-65.5, -8.0, "SOUTH\nAMERICA", size="land", fs=21, style="normal")
m.scale(1000, lon=-99.5, lat=-19.0)
m.save("chapters/36-americas/images/map_americas.png")
