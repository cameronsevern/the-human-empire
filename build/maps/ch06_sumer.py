#!/usr/bin/env python3
"""Chapter 6: the plain of southern Iraq, with the sea where a higher level would put it.

The old shoreline is traced by eye from "Some Sumerian city states with elevated sea level"
by Merikanto (Wikimedia Commons, CC BY 4.0), which floods the modern terrain to a higher
sea level; it is a rough reconstruction, not a survey. The rivers are drawn in their modern
courses. City positions from English Wikipedia.
"""
import numpy as np
from lib import Map, SEA, SHORE, smooth

m = Map(43.4, 48.9, 29.85, 33.6)
old_sea = [(46.12, 30.92), (46.30, 31.10), (46.52, 31.36), (46.72, 31.49), (46.95, 31.66), (47.22, 31.73),
           (47.50, 31.73), (47.74, 31.65), (47.82, 31.37), (47.86, 31.10), (47.98, 30.86), (48.3, 30.80),
           (48.7, 30.76), (49.3, 30.70), (49.3, 29.2), (47.95, 29.2), (47.95, 30.28), (47.62, 30.25),
           (47.30, 30.55), (47.02, 30.66), (46.58, 30.76), (46.28, 30.86)]
m.river("Euphrates", "Tigris", lw=2.2)
# the old sea is laid over the land and the lower courses of the rivers, with a dashed shore
from shapely.geometry import Polygon
from matplotlib.patches import Polygon as MplPoly
c = smooth(old_sea, n=14, closed=True)
for p in getattr(Polygon(c).buffer(0), "geoms", [Polygon(c).buffer(0)]):
    m.ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=SEA, ec="none", zorder=2.6))
m.ax.plot(c[:, 0], c[:, 1], color=SHORE, lw=1.8, ls=(0, (4, 3)), zorder=2.7)

m.city(45.996, 30.816, "Eridu", dx=-0.12, bold=True)
m.city(46.103, 30.963, "Ur", dx=0.12)
m.city(45.636, 31.322, "Uruk", dx=0.12, bold=True)
m.city(46.401, 31.412, "Lagash", dx=-0.12, bold=True)
m.city(45.233, 32.127, "Nippur", dx=0.12)
m.city(44.605, 32.541, "Kish", dx=0.12)
m.city(48.258, 32.190, "Susa", dx=0.12)

m.label(44.24, 32.0, "Euphrates", size="sea", rot=-72)
m.label(45.0, 33.0, "Tigris", size="sea", rot=-28)
m.label(47.3, 31.3, "the Gulf,\nat a higher\nsea level", size="sea")
m.label(47.8, 33.25, "IRAN", size="land", spaced=True)
m.label(44.3, 30.7, "desert", size="land")
m.label(47.4, 32.4, "Zagros foothills", size="land", rot=-35)
m.scale(100, lon=43.7, lat=30.05)
m.save("chapters/06-taxes/images/map_sumer.png")
