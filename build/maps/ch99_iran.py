#!/usr/bin/env python3
"""Chapter 99: Iran, Iraq, Afghanistan and the Gulf, 1978 to 1989: Tehran, Qom, Abadan (the cinema fire of
1978), Najaf (Khomeini's exile), Baghdad, the land Iraq took in 1980 and lost by 1982, Halabja (gassed in
1988), Mecca (the Grand Mosque seized in 1979), Kabul, the Soviet invasion of 1979 and the withdrawal over the
bridge at Termez in 1989, the flight of Afghan refugees to Pakistan and Iran, and Peshawar.

Drawn for this chapter, which had no map. The states are the modern ones (Natural Earth admin-0, 110 m, as
shipped with geopandas), whose borders here are those of the 1980s; the Soviet Union is drawn as the modern
states that were then part of it. The land taken by Iraq in 1980 is drawn roughly, after the maps in English
Wikipedia's "Iran-Iraq War" and "Iraqi invasion of Iran": the strip of Khuzestan west of the Karun and the
Karkheh, short of Dezful, Ahvaz and Abadan, with Khorramshahr, and the border towns of the central front
(Qasr-e Shirin, Mehran). The Soviet invasion is drawn as one arrow, along the main road from Termez over the
Salang pass to Kabul; the refugee arrows are schematic. Positions from English Wikipedia.
"""
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
states = ["Iran", "Iraq", "Afghanistan", "Pakistan", "Saudi Arabia", "Kuwait", "Turkey", "Syria", "Jordan",
          "Qatar", "United Arab Emirates", "Oman", "Turkmenistan", "Uzbekistan", "Tajikistan", "Azerbaijan",
          "Armenia", "Georgia", "Egypt", "Israel", "Lebanon", "India", "Kyrgyzstan", "Kazakhstan", "China",
          "Yemen", "Eritrea", "Sudan"]
soviet = unary_union([G[n] for n in ["Turkmenistan", "Uzbekistan", "Tajikistan", "Azerbaijan", "Armenia", "Georgia",
                                     "Kyrgyzstan", "Kazakhstan", "Russia"]])

m = Map(37.5, 74.5, 20.3, 41.6)
LAND = m.land
m.region(G["Iran"], "gold", alpha=0.42, edge=False)
m.region(G["Iraq"], "blue", alpha=0.32, edge=False)
m.region(G["Afghanistan"], "green", alpha=0.38, edge=False)
m.region(soviet, "red", alpha=0.20, edge=False, lakes_out=True)
m.river("Tigris", "Euphrates", en=True, lw=1.4)
m.river("Amu Darya", lw=1.6)

# borders between the states: the shared edges of the admin-0 polygons, clipped to the land
seen = set()
U = {n: G[n] for n in states if n not in ("Turkmenistan", "Uzbekistan", "Tajikistan", "Azerbaijan", "Armenia",
                                          "Georgia", "Kyrgyzstan", "Kazakhstan")}
U["Soviet"] = soviet
names = list(U)
for i, a in enumerate(names):
    for b in names[i + 1:]:
        e = U[a].boundary.intersection(U[b].buffer(0.03)).intersection(LAND.buffer(-0.02))
        for line in getattr(e, "geoms", [e]):
            if line.is_empty or line.geom_type != "LineString":
                continue
            xy = np.array(line.coords)
            soviet_edge = "Soviet" in (a, b)
            m.ax.plot(xy[:, 0], xy[:, 1], color=INK if soviet_edge else SOFT, lw=2.4 if soviet_edge else 1.6,
                      ls="-" if soviet_edge else (0, (5, 2.5)), zorder=2.6)

# the land Iraq took in 1980, roughly
taken = [(47.42, 32.47), (47.85, 32.62), (48.17, 32.35), (48.30, 31.85), (48.20, 31.55), (48.55, 31.30),
         (48.55, 30.95), (48.35, 30.62), (48.20, 30.42), (48.02, 30.45), (47.85, 30.95), (47.70, 31.0),
         (47.70, 31.95)]
central = [(45.45, 34.62), (45.95, 34.55), (46.05, 34.25), (45.75, 34.10), (45.40, 34.30)]
mehran = [(46.00, 33.25), (46.35, 33.15), (46.30, 32.95), (45.95, 33.05)]
for pts in (taken, central, mehran):
    m.region(Polygon(smooth(pts, n=8, closed=True)).buffer(0).intersection(G["Iran"].buffer(0.02)), "#7a2f22",
             alpha=0.30, hatch="///", edge=True, smooth_n=8)

# the Soviet invasion, December 1979, and the refugees
m.route([(67.35, 37.6), (67.9, 36.6), (69.1, 35.4), (69.2, 34.75)], colour="red", lw=4.0)
REF = dict(colour="#3f6b3b", lw=3.6, style=(0, (2.2, 1.0)))
m.route([(70.0, 34.32), (70.6, 34.32), (71.35, 34.08)], **REF)
m.route([(64.4, 33.6), (62.6, 33.7), (60.3, 34.2)], **REF)

# places
m.city(51.39, 35.69, "Tehran", dx=0.35, dy=0.3, bold=True)
m.city(50.88, 34.64, "Qom", dx=0.35, dy=-0.2)
m.city(48.30, 30.34, "Abadan", dx=0.35, dy=-0.15)
m.city(44.37, 33.31, "Baghdad", dx=-0.3, dy=0.35)
m.city(44.34, 32.03, "Najaf", dx=-0.35, dy=-0.1)
m.city(45.98, 35.18, "Halabja", dx=-0.35, dy=0.25)
m.city(39.83, 21.42, "Mecca", dx=0.35, dy=0.0)
m.city(69.18, 34.53, "Kabul", dx=0.0, dy=-0.55, ha="center", bold=True)
m.city(71.58, 34.01, "Peshawar", dx=0.35, dy=-0.1, ha="left")
m.city(67.28, 37.22, None, r=7)
m.label(67.0, 38.2, "Termez: the bridge\nover the border river", size="small", colour=INK, fs=15, ha="right")
m.ax.plot([66.0, 67.15], [37.75, 37.3], color=INK, lw=1.2, zorder=6.5)

m.label(54.5, 32.6, "IRAN", fs=28)
m.label(42.0, 31.25, "IRAQ", fs=24)
m.label(65.6, 32.0, "AFGHANISTAN", fs=19)
m.label(59.0, 39.6, "SOVIET UNION", fs=21, colour="#7a2f22")
G3 = dict(size="land", colour="#5a534b", style="normal", fs=16)
m.label(44.5, 25.0, "SAUDI ARABIA", **G3)
m.label(70.0, 29.0, "PAKISTAN", **G3)
m.label(38.6, 38.9, "TURKEY", **G3)
m.label(47.6, 28.6, "KUWAIT", fs=15, size="land", colour="#5a534b", style="normal", ha="right")
m.label(51.0, 40.6, "Caspian\nSea", size="sea", fs=18)
m.label(51.2, 27.4, "Persian Gulf", size="sea", fs=19, rot=-32)
m.label(58.8, 23.8, "Gulf of Oman", size="sea", fs=16)
m.label(39.6, 24.0, "Red\nSea", size="sea", fs=17)
m.label(47.2, 29.85, "front,\n1980 to 1988", size="small", colour=INK, fs=15, ha="right", style="italic")
m.label(66.9, 36.15, "Soviet\ninvasion,\n1979", size="small", colour="#7a2f22", fs=15, ha="right", style="italic")
m.label(62.8, 34.55, "refugees", size="small", colour="#3f6b3b", fs=15, style="italic")
m.label(70.6, 33.55, "refugees", size="small", colour="#3f6b3b", fs=15, style="italic")

handles = [Patch(fc="#7a2f2240", ec="#7a2f22", hatch="///", label="taken by Iraq in 1980,\nretaken by Iran by 1982"),
           Line2D([0], [0], color=INK, lw=2.4, label="Soviet frontier"),
           Line2D([0], [0], color=FILL["red"], lw=4.0, label="Soviet invasion, 1979"),
           Line2D([0], [0], color="#3f6b3b", lw=3.6, ls=(0, (2.2, 1.0)), label="Afghan refugees")]
leg = m.ax.legend(handles=handles, loc="lower right", fontsize=16, frameon=True, fancybox=False, edgecolor=INK,
                  facecolor=PAPER, framealpha=1, borderpad=0.7, labelspacing=0.5, handlelength=2.4)
leg.set_zorder(9); leg.get_frame().set_linewidth(1.2)
m.scale(500, lon=55.0, lat=21.2)
m.save("chapters/99-iran/images/map_iran.png")
