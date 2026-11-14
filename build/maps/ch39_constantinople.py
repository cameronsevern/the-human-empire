#!/usr/bin/env python3
"""Chapter 39: Constantinople in 1453. The triangle of the city between the Sea of Marmara and the Golden
Horn, closed on the west by the land walls; the chain across the mouth of the Golden Horn; Galata on the
far side; the Bosphorus running north to the Ottoman forts, the Throat-Cutter (Rumeli Hisari) on the
European bank and the older fort (Anadolu Hisari) on the Asian bank; and the track over the ridge behind
Galata on which the Ottoman ships were dragged into the Golden Horn on 22 April.

Natural Earth is far too coarse at this scale, so the shores are drawn by hand from coordinates of
landmarks along them, and checked by overlaying a modern coastline (OpenStreetMap, used only for the
check and not drawn). The modern shore has been filled out in places (Yenikapi, Eminonu, Kadikoy);
the 1453 shore is followed where it differs. The line of the land walls follows their surviving
course, from Yedikule on the Marmara to Ayvansaray on the Golden Horn. The route of the ships is
uncertain: it is drawn, as most historians give it, from the Bosphorus shore near Tophane over the
heights of Pera and down to the Golden Horn at Kasimpasa (the Valley of the Springs). Positions from
English Wikipedia.

Set CHECK=path/to/osm_coast.json to overlay the modern coastline in red for checking.
"""
import os, json
import numpy as np
from matplotlib.patches import Polygon as MplPoly
import lib
from lib import Map, INK, PAPER, LAND, SEA, SHORE, FILL, smooth, HALO

W, E, S, N = 28.895, 29.095, 40.965, 41.102

# the European shore: Marmara coast west to east, round Seraglio Point, up the south shore of the
# Golden Horn, down its north shore past Galata, and up the Bosphorus
europe = [(28.860, 40.970), (28.880, 40.9745), (28.895, 40.9800), (28.9075, 40.9835), (28.9150, 40.9870),
          (28.9210, 40.9900), (28.9300, 40.9935), (28.9400, 40.9970), (28.9500, 41.0005), (28.9600, 41.0025),
          (28.9690, 41.0030), (28.9775, 41.0025), (28.9820, 41.0040), (28.9850, 41.0065), (28.9880, 41.0105),
          (28.9878, 41.0160), (28.9855, 41.0178), (28.9820, 41.0177), (28.9775, 41.0171), (28.9700, 41.0188),
          (28.9650, 41.0215), (28.9600, 41.0260), (28.9545, 41.0290), (28.9500, 41.0325), (28.9470, 41.0370),
          (28.9445, 41.0420), (28.9390, 41.0450), (28.9350, 41.0500), (28.9365, 41.0550), (28.9400, 41.0600),
          (28.9440, 41.0590), (28.9425, 41.0545), (28.9440, 41.0490), (28.9490, 41.0416), (28.9540, 41.0360),
          (28.9600, 41.0340), (28.9650, 41.0305), (28.9675, 41.0265), (28.9705, 41.0230), (28.9760, 41.0218),
          (28.9830, 41.0245), (28.9890, 41.0290), (28.9935, 41.0345), (28.9960, 41.0375), (29.0075, 41.0416),
          (29.0190, 41.0456), (29.0275, 41.0478), (29.0340, 41.0505), (29.0375, 41.0605), (29.0425, 41.0660),
          (29.0450, 41.0715), (29.0455, 41.0785), (29.0525, 41.0803), (29.0560, 41.0835), (29.0575, 41.0907),
          (29.0545, 41.0990), (29.0530, 41.1100), (29.0520, 41.1200), (28.8600, 41.1200)]
asia = [(29.0670, 41.1200), (29.0662, 41.1020), (29.0656, 41.0926), (29.0660, 41.0830), (29.0640, 41.0775),
        (29.0575, 41.0746), (29.0560, 41.0690), (29.0525, 41.0595), (29.0510, 41.0510), (29.0425, 41.0445),
        (29.0325, 41.0403), (29.0210, 41.0335), (29.0125, 41.0296), (29.0075, 41.0257), (29.0080, 41.0200),
        (29.0100, 41.0133), (29.0125, 41.0030), (29.0188, 40.9973), (29.0220, 40.9935), (29.0230, 40.9880),
        (29.0215, 40.9820), (29.0250, 40.9780), (29.0330, 40.9800), (29.0375, 40.9720), (29.0400, 40.9600),
        (29.0450, 40.9500), (29.1200, 40.9500), (29.1200, 41.1200)]
walls = [(28.9212, 40.9905), (28.9203, 41.0000), (28.9175, 41.0070), (28.9184, 41.0136), (28.9206, 41.0206),
         (28.9270, 41.0260), (28.9343, 41.0292), (28.9408, 41.0341), (28.9427, 41.0390), (28.9440, 41.0428)]

m = Map(W, E, S, N, lakes=False)
for p in list(m.ax.patches):
    p.remove()
for pts in (europe, asia):
    m.ax.add_patch(MplPoly(smooth(pts, n=6, closed=True), closed=True, fc=LAND, ec=SHORE, lw=1.4, zorder=1))

# the city inside its walls, shaded
from shapely.geometry import Polygon
land_eu = Polygon(smooth(europe, n=6, closed=True)).buffer(0)
horn_south = [(28.9475, 41.0378), (28.9505, 41.0333), (28.9550, 41.0298), (28.9605, 41.0268), (28.9655, 41.0223),
              (28.9705, 41.0196), (28.9775, 41.0180), (28.9950, 41.0180), (28.9950, 40.9900), (28.9212, 40.9850)]
city_poly = Polygon(walls + horn_south).buffer(0).intersection(land_eu)
for p in getattr(city_poly, "geoms", [city_poly]):
    m.ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=FILL["gold"], ec="none", alpha=0.32, zorder=1.5))

# the land walls: a heavy line with towers
wl = smooth(walls, n=8)
m.ax.plot(wl[:, 0], wl[:, 1], color=PAPER, lw=11, solid_capstyle="butt", zorder=3)
m.ax.plot(wl[:, 0], wl[:, 1], color=INK, lw=7, solid_capstyle="butt", zorder=3.1)
m.label(28.9128, 41.0130, "land walls", size="small", colour=INK, fs=20, rot=88)

# Galata, a small walled town
galata = [(28.9675, 41.0262), (28.9705, 41.0232), (28.9760, 41.0220), (28.9830, 41.0247), (28.9815, 41.0272),
          (28.9745, 41.0272), (28.9700, 41.0290)]
m.ax.add_patch(MplPoly(smooth(galata, n=6, closed=True), closed=True, fc=FILL["blue"], ec=FILL["blue"], lw=2.4,
                       alpha=0.55, zorder=2))
m.label(28.9780, 41.0322, "Galata", fs=22, colour=INK)

# the chain across the mouth of the Golden Horn
m.ax.plot([28.9790, 28.9765], [41.0179, 41.0223], color=PAPER, lw=9, zorder=4)
m.ax.plot([28.9790, 28.9765], [41.0179, 41.0223], color=INK, lw=4.5, ls=(0, (1, 0.8)), zorder=4.1)
m.label(28.9842, 41.0204, "chain", size="small", colour=INK, fs=19, ha="left")

# the ships dragged overland, 22 April 1453
m.route([(28.9940, 41.0360), (28.9890, 41.0392), (28.9810, 41.0400), (28.9735, 41.0372), (28.9672, 41.0322)],
        colour="red", lw=3.6, style=(0, (3, 1.6)))
m.label(28.9890, 41.0470, "ships dragged\noverland, 1453", size="small", colour=INK, fs=19)

# the two forts on the Bosphorus
m.ax.plot(29.0561, 41.0847, "s", ms=17, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
m.ax.plot(29.0665, 41.0825, "s", ms=17, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
m.label(29.0520, 41.0870, "Throat-Cutter\n(Rumeli Hisari)\nbuilt 1452", size=19, colour=INK, fs=19, ha="right")
m.label(29.0705, 41.0790, "older\nOttoman\nfort", size="small", colour=INK, fs=18, ha="left")

m.city(28.9802, 41.0086, "Hagia Sophia", dx=-0.0015, dy=0.0, size=18)
m.label(28.9500, 41.0140, "CONSTANTINOPLE", fs=25)
m.label(28.9545, 41.0400, "Golden Horn", size="sea", fs=20, rot=52)
m.label(28.9600, 40.9850, "Sea of Marmara", size="sea", fs=24)
m.label(29.0300, 41.0600, "Bosphorus", size="sea", fs=22, rot=60)
m.label(29.0610, 41.0930, "to the\nBlack Sea", size="sea", fs=17)
m.ax.annotate("", xy=(29.0600, 41.1015), xytext=(29.0600, 41.0965), zorder=5,
              arrowprops=dict(arrowstyle="-|>,head_width=0.4,head_length=0.8", color="#5d7686", lw=2))
m.label(28.9300, 41.0800, "EUROPE", size="land", fs=24, style="normal")
m.label(29.0750, 41.0300, "ASIA", size="land", fs=24, style="normal")
m.scale(1, lon=29.050, lat=40.972)

if os.environ.get("CHECK"):
    for el in json.load(open(os.environ["CHECK"]))["elements"]:
        xy = np.array([(g["lon"], g["lat"]) for g in el["geometry"]])
        m.ax.plot(xy[:, 0], xy[:, 1], color="red", lw=0.8, zorder=20)
    for x in np.arange(28.90, 29.10, 0.01):
        m.ax.axvline(x, color="k", lw=0.2, zorder=19)
    for y in np.arange(40.97, 41.10, 0.01):
        m.ax.axhline(y, color="k", lw=0.2, zorder=19)

m.save("chapters/39-constantinople/images/map_constantinople.png" if not os.environ.get("CHECK")
       else "/tmp/claude-1000/-home-cameron-Projects-human-empire/880837ba-c81e-4e6b-a385-d5025f3c2f35/scratchpad/check39.png")
