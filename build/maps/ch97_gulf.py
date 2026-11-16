#!/usr/bin/env python3
"""Chapter 97: the Persian Gulf, with the states around it, the main oilfields named in the chapter or near
the places it names, the first well in Persia (1908), the refinery at Abadan, the well that struck oil in
Saudi Arabia in 1938, Baghdad (where OPEC was founded in 1960), Tehran, and the Strait of Hormuz.

Drawn for this chapter, which had no map. The states are the modern ones (Natural Earth admin-0, 110 m, as
shipped with geopandas), whose borders round the Gulf have changed little since the 1930s; Bahrain is too
small for that file and is marked by a label. The oilfields are soft areas drawn by hand, roughly, after the
maps of English Wikipedia's "Ghawar Field", "Burgan field", "Rumaila oil field", "Kirkuk Field" and "Masjed
Soleyman": Ghawar about 280 km long, running south from near Abqaiq; Burgan south of Kuwait City; Rumaila
west of Basra; Kirkuk running north-west to south-east past the city. The first well of 1908 at Masjed
Soleyman; the 1938 well (Dammam No. 7) at Dhahran. Pipelines are left out: the chapter does not mention them.
Positions from English Wikipedia.
"""
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
states = ["Iran", "Iraq", "Kuwait", "Saudi Arabia", "Qatar", "United Arab Emirates", "Oman", "Syria", "Jordan",
          "Turkey"]

m = Map(42.5, 58.0, 23.0, 36.4)
m.river("Tigris", "Euphrates", en=True)
# the Shatt al-Arab, from the meeting of the rivers at Qurna past Basra, Khorramshahr and Abadan to the sea
shatt = [(47.43, 31.00), (47.62, 30.78), (47.81, 30.53), (48.01, 30.46), (48.17, 30.42), (48.25, 30.36),
         (48.36, 30.25), (48.50, 30.10), (48.62, 29.97)]
c = smooth(shatt)
m.ax.plot(c[:, 0], c[:, 1], color=lib.WATER, lw=1.8, solid_capstyle="round", zorder=2.5)

# borders between the states: the shared edges of the admin-0 polygons, clipped to the land
seen = set()
for a in states:
    for b in states:
        if a >= b or (a, b) in seen:
            continue
        seen.add((a, b))
        if {a, b} == {"Iran", "Iraq"}:                  # the south end follows the Shatt al-Arab, below
            edge = G[a].boundary.intersection(G[b].buffer(0.03)).intersection(box(40, 30.5, 50, 40))
            edge = edge.intersection(m.land.buffer(-0.02))
        else:
            edge = G[a].boundary.intersection(G[b].buffer(0.03)).intersection(m.land.buffer(-0.02))
        for line in getattr(edge, "geoms", [edge]):
            if line.is_empty or line.geom_type != "LineString":
                continue
            xy = np.array(line.coords)
            m.ax.plot(xy[:, 0], xy[:, 1], color=SOFT, lw=1.6, ls=(0, (5, 2.5)), zorder=2.6)

c = smooth(shatt[3:])
m.ax.plot(c[:, 0], c[:, 1], color=SOFT, lw=1.6, ls=(0, (5, 2.5)), zorder=2.6)

# oilfields: soft areas
def field(pts):
    m.region(Polygon(smooth(pts, n=10, closed=True)).buffer(0), "brown", alpha=0.75, edge=True)

ghawar_axis = [(49.08, 24.02), (49.20, 24.65), (49.30, 25.25), (49.40, 25.80), (49.48, 26.22)]
left = [(x - 0.13, y) for x, y in ghawar_axis]
right = [(x + 0.13, y) for x, y in ghawar_axis][::-1]
field(left + right)
field([(47.82, 28.82), (48.10, 28.86), (48.12, 29.10), (47.88, 29.12)])                 # Burgan
field([(47.22, 30.12), (47.42, 30.14), (47.47, 30.75), (47.27, 30.75)])                 # Rumaila
field([(43.95, 35.80), (44.15, 35.85), (44.75, 35.25), (44.60, 35.15)])                 # Kirkuk
field([(49.12, 31.86), (49.42, 31.88), (49.45, 32.05), (49.16, 32.04)])                 # Masjed Soleyman

m.label(50.15, 27.7, "Persian Gulf", size="sea", fs=22)
m.label(57.0, 24.15, "Gulf of\nOman", size="sea", fs=18)
m.label(56.95, 26.95, "Strait of\nHormuz", size="sea", fs=17, ha="center")

m.label(53.6, 31.6, "IRAN", fs=26)
m.label(43.3, 32.2, "IRAQ", fs=26, ha="left")
m.label(46.3, 25.6, "SAUDI\nARABIA", fs=24)
m.label(47.35, 29.45, "KUWAIT", fs=17)
m.label(51.22, 25.0, "QATAR", fs=16, ha="center")
m.label(50.70, 26.30, "BAHRAIN", fs=15, ha="left")
m.label(54.4, 23.55, "UNITED ARAB EMIRATES", fs=16)
m.label(57.0, 23.4, "OMAN", fs=16, ha="center")

m.city(51.39, 35.69, "Tehran", dx=0.25, dy=0.2)
m.city(44.37, 33.31, "Baghdad", dx=0.3, dy=0.0)
m.label(44.67, 32.85, "OPEC founded, 1960", size="small", colour=INK, fs=16, ha="left")
m.city(48.30, 30.34, "Abadan refinery", dx=0.3, dy=0.05)
m.city(50.10, 26.30, None)
m.label(49.98, 26.66, "Dhahran:\noil found, 1938", size="small", colour=INK, fs=16, ha="right")
m.city(49.30, 31.94, None, star=True, r=10)
m.label(49.65, 32.35, "Masjed Soleyman:\nfirst oil, 1908", size="small", colour=INK, fs=16, ha="left")

m.label(48.75, 24.55, "Ghawar,\nthe largest\noilfield", size="small", colour=FILL["brown"], fs=17, ha="right",
        style="italic")
m.label(48.15, 28.55, "Burgan", size="small", colour=FILL["brown"], fs=16, ha="center", style="italic")
m.label(47.12, 30.3, "Rumaila", size="small", colour=FILL["brown"], fs=16, ha="right", style="italic")
m.label(44.85, 35.65, "Kirkuk", size="small", colour=FILL["brown"], fs=16, ha="left", style="italic")
m.label(45.05, 33.95, "Tigris", size="sea", fs=16, rot=-48)
m.label(43.55, 33.75, "Euphrates", size="sea", fs=16, rot=-30)
m.key([("brown", "oilfield")], loc="lower left")
m.scale(300, lon=54.0, lat=34.6)
m.save("chapters/97-oil/images/map_gulf.png")
