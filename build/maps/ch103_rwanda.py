#!/usr/bin/env python3
"""Chapter 103: above, Rwanda and eastern Zaire in 1994 to 1997: Kigali, the churches at Ntarama and Nyamata
south of the capital, the advance of Kagame's army from Uganda, the French zone in the south-west (June to
August 1994), the flight of the refugees into Zaire at Goma and Bukavu and into Tanzania, the Kagera river that
carried the bodies into Lake Victoria, and the march of 1996 and 1997 towards Kinshasa. Below, Bosnia in 1995:
Sarajevo, Srebrenica and the other safe areas declared by the United Nations, and the division of 1995.

Drawn for this chapter, which had no map. Borders are those of Natural Earth admin-0, 1:10 million (public
domain), cut to the frame and simplified (data/ch103_rwanda_ne10m.geojson, data/ch103_bosnia_ne10m.geojson).
The division of Bosnia is the line agreed at Dayton in November 1995, which followed the front at the end of
the war with some exchanges, taken from geoBoundaries (gbOpen BIH ADM1, from Wikimedia Commons, public domain;
data/ch103_bosnia_entities_geoboundaries.geojson): the Serb Republic, and the Federation of the Muslims and
Croats. The Brcko district, whose status was left to arbitration, is left unshaded. Drawn roughly.

The French zone is drawn roughly after the maps of the "Zone humanitaire sure" (the prefectures of Cyangugu and
Gikongoro and the south of Kibuye). The refugee arrows are schematic: about 850,000 crossed at Goma in July
1994, about 330,000 at Bukavu in July and August, and about 500,000 into Tanzania at the Rusumo bridge from
late April. The arrow of 1996 and 1997 shows only the direction of the march on Kinshasa (about 1,500 km to the
west). Positions from English Wikipedia; Ntarama and Nyamata after their memorials.
"""
import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth

SCRATCH = os.environ.get("SCRATCH", "/tmp")
G3 = dict(size="land", colour="#5a534b", style="normal")
REF = dict(colour="#3f6b3b", lw=3.6, style=(0, (2.2, 1.0)))
lib._load()
BIG_LAKES = unary_union([g for g, r in zip(lib._lakes.geometry, lib._lakes.scalerank) if (r or 0) <= 3])


def borders(m, C, names, lw=1.8, colour="#5a534b", style=(0, (5, 2.5))):
    """The shared edges of the given states, on land only."""
    land = m.land.buffer(-0.01).difference(BIG_LAKES.buffer(0.01))
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            e = C[a].boundary.intersection(C[b].buffer(0.01)).intersection(land)
            for l in getattr(e, "geoms", [e]):
                if l.is_empty or l.geom_type != "LineString":
                    continue
                xy = np.array(l.coords)
                m.ax.plot(xy[:, 0], xy[:, 1], color=colour, lw=lw, ls=style, zorder=2.6)


# ================================================================ above: Rwanda and eastern Zaire
R = gpd.read_file(os.path.join(lib.DATA, "ch103_rwanda_ne10m.geojson"))
C = {r["NAME"]: r.geometry for _, r in R.iterrows()}
m = Map(27.0, 32.0, -3.45, 0.0)
m.region(C["Rwanda"], "red", alpha=0.30, edge=False, lakes_out=True)
m.region(C["Dem. Rep. Congo"], "gold", alpha=0.18, edge=False, lakes_out=True)
borders(m, C, ["Rwanda", "Dem. Rep. Congo", "Uganda", "Burundi", "Tanzania"])
rw = C["Rwanda"].boundary.intersection(m.land.buffer(-0.01).difference(BIG_LAKES.buffer(0.005)))
for l in getattr(rw, "geoms", [rw]):
    if l.geom_type == "LineString":
        xy = np.array(l.coords)
        m.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=2.4, zorder=2.7)
m.river("Kagera", lw=2.2)
m.river("Rusizi", lw=1.6)

# the French zone, June to August 1994, roughly
fz = [(29.22, -1.98), (29.52, -2.02), (29.72, -2.22), (29.78, -2.52), (29.62, -2.80), (29.0, -2.84),
      (28.85, -2.48), (29.0, -2.2)]
m.region(Polygon(smooth(fz, n=8, closed=True)).buffer(0).intersection(C["Rwanda"]).difference(BIG_LAKES), "#4f5f8a", alpha=0.25,
         hatch="///", edge=True)

# Kagame's army, from Uganda (1990, and again in 1994); the flight of 1994; the march of 1996 and 1997
m.route([(30.45, -0.95), (30.40, -1.30), (30.22, -1.65), (30.11, -1.885)], colour="red", lw=4.0)
m.route([(29.45, -1.62), (29.33, -1.66), (29.24, -1.67)], **REF)
m.route([(29.22, -2.22), (29.05, -2.36), (28.93, -2.47)], **REF)
m.route([(30.70, -2.27), (30.85, -2.38), (31.0, -2.49), (31.15, -2.58)], **REF)
m.route([(28.85, -2.05), (28.30, -1.92), (27.70, -1.95), (27.08, -2.05)], colour="#7a2f22", lw=4.0,
        style=(0, (4, 1.6)))

# places
m.city(30.06, -1.94, "Kigali", dx=-0.08, dy=0.0, bold=True)
m.city(30.03, -2.115, None, r=7)
m.city(30.10, -2.15, None, r=7)
m.label(30.26, -2.06, "churches at\nNtarama and\nNyamata", size="small", colour=INK, fs=15, ha="left")
m.ax.plot([30.12, 30.245], [-2.14, -2.08], color=INK, lw=1.2, zorder=6.5)
m.city(29.23, -1.68, "Goma", dx=-0.10, dy=0.08, ha="right", bold=True)
m.city(28.86, -2.51, "Bukavu", dx=-0.10, dy=-0.05, ha="right")
m.city(30.66, -2.51, "Ngara", dx=0.08, dy=-0.14)
m.label(27.08, -2.30, "Rwanda's army and its allies,\n1996; to Kinshasa, 1997", size="small", colour="#7a2f22", fs=15,
        ha="left", style="italic")

m.label(29.95, -1.55, "RWANDA", fs=23)
m.label(27.9, -1.0, "ZAIRE", fs=28)
m.label(31.0, -0.4, "UGANDA", fs=21, colour="#5a534b")
m.label(29.9, -3.15, "BURUNDI", fs=19, colour="#5a534b")
m.label(31.25, -3.0, "TANZANIA", fs=19, colour="#5a534b")
m.label(29.45, -2.62, "French\nzone,\n1994", size="small", colour="#2f3c63", fs=15, style="italic")
m.label(30.45, -0.82, "Kagame's army,\n1990 to 1994", size="small", colour="#7a2f22", fs=15, style="italic",
        ha="left")
m.label(29.6, -1.38, "refugees", size="small", colour="#3f6b3b", fs=15, style="italic")
m.label(31.25, -2.33, "refugees", size="small", colour="#3f6b3b", fs=15, style="italic", ha="left")
m.label(31.0, -1.75, "Kagera", size="sea", fs=15, style="italic")
m.label(29.15, -2.05, "Lake\nKivu", size="sea", fs=15)
m.label(29.62, -0.22, "Lake\nEdward", size="sea", fs=15)
m.label(31.93, -1.2, "Lake\nVictoria", size="sea", fs=16, ha="right")
m.label(29.2, -3.3, "Lake\nTanganyika", size="sea", fs=15, ha="right")
m.scale(100, lon=27.3, lat=-3.25)
p1 = os.path.join(SCRATCH, "ch103_1.png"); m.save(p1)

# ================================================================ below: Bosnia, 1995
B = gpd.read_file(os.path.join(lib.DATA, "ch103_bosnia_ne10m.geojson"))
D = {r["NAME"]: r.geometry for _, r in B.iterrows()}
E = gpd.read_file(os.path.join(lib.DATA, "ch103_bosnia_entities_geoboundaries.geojson"))
F = {r["shapeName"]: r.geometry for _, r in E.iterrows()}
W2 = 9.6
n = Map(15.65, 19.75, 42.5, 45.35, width=W2)
BIH = D["Bosnia and Herz."]
brcko = BIH.intersection(F["Brčko District"])
FED = BIH.intersection(F["Federation of Bosnia and Herzegovina"].buffer(0.02)).difference(brcko)
RS = BIH.difference(FED).difference(brcko)
n.region(RS, "red", alpha=0.38, edge=False)
n.region(FED, "green", alpha=0.36, edge=False)
borders(n, D, ["Bosnia and Herz.", "Croatia", "Serbia", "Montenegro", "Hungary", "Kosovo", "Albania"])
bb = D["Bosnia and Herz."].boundary.intersection(n.land.buffer(-0.01))
for l in getattr(bb, "geoms", [bb]):
    if l.geom_type == "LineString":
        xy = np.array(l.coords)
        n.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=2.4, zorder=2.7)
line = RS.boundary.intersection(FED.buffer(0.005)).intersection(BIH.buffer(-0.01))
for l in getattr(line, "geoms", [line]):
    if l.geom_type == "LineString" and l.length > 0.02:
        xy = np.array(l.coords)
        n.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=4.6, zorder=2.75)
        n.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=2.0, ls=(0, (3, 1.5)), zorder=2.8)
n.river("Drina", "Sava", "Danube", lw=1.6)

for lon, lat, name, dx, dy, bold in [(18.41, 43.86, "Sarajevo", 0.0, -0.12, True),
                                     (19.30, 44.10, "Srebrenica", -0.05, 0.11, True),
                                     (19.13, 43.94, "Žepa", 0.09, -0.04, False),
                                     (18.98, 43.67, "Goražde", 0.09, -0.04, False),
                                     (18.67, 44.54, "Tuzla", 0.0, 0.11, False),
                                     (15.87, 44.82, "Bihać", 0.09, -0.06, False)]:
    n.ax.plot(lon, lat, "s", ms=12, mfc=INK, mec=PAPER, mew=1.4, zorder=6)
    n.ax.text(lon + dx, lat + dy, name, ha="left" if dx > 0 else "center" if dx == 0 else "right", va="center", fontsize=17 if bold else 16,
              fontweight="bold" if bold else "normal", color=INK, zorder=7, path_effects=HALO)
n.label(17.75, 44.25, "Muslims\nand Croats", fs=16, colour="#2f5a2b")
n.label(17.15, 44.85, "Bosnian\nSerbs", fs=16, colour="#7a2f22")
n.label(18.35, 43.05, "Bosnian\nSerbs", fs=16, colour="#7a2f22")
n.label(16.15, 43.95, "CROATIA", fs=17, colour="#5a534b")
n.label(19.35, 44.85, "SERBIA", fs=17, colour="#5a534b")
n.label(19.25, 42.75, "MONTENEGRO", fs=16, colour="#5a534b")
n.label(16.6, 43.15, "Adriatic\nSea", size="sea", fs=17)
n.label(19.48, 43.35, "Drina", size="sea", fs=15, style="italic", rot=0)
n.ax.text(0.025, 0.975, "BOSNIA, 1995", transform=n.ax.transAxes, ha="left", va="top", fontsize=18,
          fontweight="bold", color=INK, zorder=9, bbox=dict(boxstyle="square,pad=0.35", fc=PAPER, ec=INK, lw=1.2))
n.scale(50, lon=15.9, lat=42.62)
p2 = os.path.join(SCRATCH, "ch103_2.png"); n.save(p2)

# ---------------------------------------------------------------- the key, beside Bosnia
img2 = mpimg.imread(p2)[:, :, :3]
k = plt.figure(figsize=(16.0 - W2 - 0.16, img2.shape[0] / 100.0), dpi=100)
k.patch.set_facecolor(PAPER)
handles = [Line2D([0], [0], color=FILL["red"], lw=4.0, label="Kagame's army\nadvancing"),
           Patch(fc="#4f5f8a40", ec="#4f5f8a", hatch="///", label="French zone,\nJune to August 1994"),
           Line2D([0], [0], color="#3f6b3b", lw=3.6, ls=(0, (2.2, 1.0)), label="refugees, 1994"),
           Line2D([0], [0], color="#7a2f22", lw=4.0, ls=(0, (4, 1.6)), label="Rwanda's army and\nits allies, 1996 and 1997"),
           Line2D([0], [0], ls="none", marker="s", ms=12, mfc=INK, mec=PAPER, label="safe areas of the\nUnited Nations, Bosnia"),
           Line2D([0], [0], color=INK, lw=2.0, ls=(0, (3, 1.5)), label="line dividing Bosnia,\n1995")]
k.legend(handles=handles, loc="center", fontsize=17, frameon=False, labelspacing=1.0, handlelength=2.4,
         handleheight=1.6)
p3 = os.path.join(SCRATCH, "ch103_key.png"); k.savefig(p3, dpi=100, facecolor=PAPER); plt.close(k)

top, key = mpimg.imread(p1)[:, :, :3], mpimg.imread(p3)[:, :, :3]
paper = np.array(lib.matplotlib.colors.to_rgb(PAPER))
h = img2.shape[0]
key = key[:h]
row = np.hstack([img2, np.ones((h, 1600 - img2.shape[1] - key.shape[1], 3)) * paper, key])
out = np.vstack([top, np.ones((16, 1600, 3)) * paper, row])
path = os.path.join(lib.ROOT, "chapters/103-rwanda/images/map_rwanda_bosnia.png")
plt.imsave(path, out)
print("wrote", path, out.shape)
