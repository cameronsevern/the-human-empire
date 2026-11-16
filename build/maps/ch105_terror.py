#!/usr/bin/env python3
"""Chapter 105: the wars after 11 September 2001, from Tunisia to Afghanistan: the two countries invaded by the
United States (Afghanistan in 2001 and Iraq in 2003), the countries of the risings of 2011 (Tunisia, Egypt,
Libya, Yemen, Bahrain and Syria), the land held by the Islamic State at its height in 2014 and 2015, the way
taken by refugees from Syria to Europe in 2015, and the places named in the chapter: Kabul, the caves of Tora
Bora, the garrison town where bin Laden was found (Abbottabad), Baghdad, Mosul, Damascus, Cairo, the town where
the fruit seller set himself alight (Sidi Bouzid), Mecca and Medina, and Gaza.

Drawn for this chapter, which had no map. The states are the modern ones (Natural Earth admin-0, 110 m, as
shipped with geopandas); Bahrain, too small for that scale, is marked by a dot. The Islamic State's land is
drawn roughly, as one soft area, after the maps in English Wikipedia's "Territorial control of the Islamic
State" and "Timeline of the Islamic State" for late 2014 and mid-2015: the Euphrates valley from Jarabulus and
Raqqa to Deir ez-Zor, Abu Kamal and al-Qaim, the Syrian desert to Palmyra (taken May 2015), Mosul, Tal Afar
and Sinjar, the country west of Kirkuk, and Anbar with Fallujah and Ramadi (taken May 2015); much of the desert
inside it was empty and only loosely held. Its land in Libya (Sirte) and Afghanistan was small and is left
out. The refugee arrow is schematic: the overland way across Turkey and the short crossing to the Greek
islands. Positions from English Wikipedia.
"""
import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from shapely.geometry import Polygon
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth

SCRATCH = os.environ.get("SCRATCH", "/tmp")

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
states = ["Tunisia", "Algeria", "Libya", "Egypt", "Sudan", "Chad", "Niger", "Israel", "Palestine", "Lebanon",
          "Syria", "Jordan", "Iraq", "Iran", "Saudi Arabia", "Kuwait", "Qatar", "United Arab Emirates", "Oman",
          "Yemen", "Turkey", "Afghanistan", "Pakistan", "India", "Turkmenistan", "Uzbekistan", "Tajikistan",
          "Azerbaijan", "Armenia", "Georgia", "Greece", "Bulgaria", "Eritrea", "Ethiopia", "Cyprus", "N. Cyprus",
          "China", "Somaliland", "Djibouti"]
states = [s for s in states if s in G]

def base(m, lw=1.5):
    LAND = m.land
    for n in ("Afghanistan", "Iraq"):
        m.region(G[n], "red", alpha=0.36, edge=False)
    for n in ("Tunisia", "Egypt", "Libya", "Yemen", "Syria"):
        m.region(G[n], "gold", alpha=0.36, edge=False)
    m.river("Tigris", "Euphrates", en=True, lw=1.4)
    m.river("Nile", lw=1.4)

    land = LAND.buffer(-0.03)
    for i, a in enumerate(states):
        for b in states[i + 1:]:
            e = G[a].boundary.intersection(G[b].buffer(0.03)).intersection(land)
            for l in getattr(e, "geoms", [e]):
                if l.is_empty or l.geom_type != "LineString":
                    continue
                xy = np.array(l.coords)
                m.ax.plot(xy[:, 0], xy[:, 1], color=SOFT, lw=lw, ls=(0, (5, 2.5)), zorder=2.6)

    # the Islamic State at its height, 2014 and 2015, roughly
    isis = [(37.25, 36.45), (38.0, 36.82), (39.0, 36.70), (39.9, 36.45), (40.75, 36.15), (41.6, 36.45),
            (42.45, 36.55), (43.25, 36.55), (43.55, 36.25), (43.95, 35.45), (43.8, 34.65), (43.95, 33.5),
            (43.35, 33.05), (42.3, 33.25), (41.0, 33.1), (40.0, 33.4), (38.9, 33.95), (38.0, 34.35), (37.7, 34.85),
            (38.1, 35.45), (37.7, 35.95)]
    m.region(Polygon(smooth(isis, n=8, closed=True)).buffer(0), "#3b3330", alpha=0.30, hatch="xx", edge=True)

    # refugees to Europe, 2015
    m.route([(37.1, 36.6), (34.5, 37.4), (31.0, 38.0), (28.0, 38.6), (26.5, 39.1)], colour="#3f6b3b", lw=3.6,
            style=(0, (2.2, 1.0)))


INSET = (32.6, 48.6, 29.6, 37.9)

# ================================================================ the whole region
m = Map(7.5, 76.0, 12.5, 41.6)
base(m)
w, e, s_, n_ = INSET
m.ax.plot([w, e, e, w, w], [s_, s_, n_, n_, s_], color=INK, lw=1.6, zorder=8)
m.city(69.17, 34.53, "Kabul", dx=-0.4, dy=0.55, ha="right", bold=True)
m.city(70.08, 34.11, None, r=7)
m.label(70.7, 33.25, "Tora Bora", size="small", colour=INK, fs=16.5, ha="left")
m.ax.plot([70.2, 70.75], [33.95, 33.45], color=INK, lw=1.2, zorder=6.5)
m.city(73.22, 34.15, "Abbottabad", dx=0.0, dy=0.75, ha="center")
m.city(31.24, 30.04, "Cairo", dx=-0.45, dy=0.0, ha="right", bold=True)
m.city(9.48, 35.04, "Sidi Bouzid", dx=0.45, dy=0.0, ha="left")
m.city(39.83, 21.42, "Mecca", dx=0.45, dy=-0.1, ha="left")
m.city(39.61, 24.47, "Medina", dx=0.45, dy=0.0, ha="left")
m.city(50.55, 26.07, "Bahrain", dx=0.0, dy=0.65, ha="center", r=7)
G4 = dict(colour="#5a534b", size="land", style="normal")
m.label(65.0, 32.9, "AFGHANISTAN\ninvaded 2001", fs=16)
m.label(17.5, 29.6, "LIBYA", fs=19)
m.label(29.5, 27.5, "EGYPT", fs=19)
m.label(10.6, 33.0, "TUNISIA", fs=15)
m.label(47.0, 15.2, "YEMEN", fs=17)
m.label(45.0, 22.3, "SAUDI ARABIA", **G4, fs=17)
m.label(55.5, 32.0, "IRAN", **G4, fs=20)
m.label(69.5, 28.6, "PAKISTAN", **G4, fs=17)
m.label(34.0, 39.4, "TURKEY", **G4, fs=17)
m.label(27.3, 39.9, "refugees to\nEurope, 2015", size="small", colour="#3f6b3b", fs=15, style="italic")
m.label(19.5, 35.0, "Mediterranean Sea", size="sea", fs=19)
m.label(38.4, 19.5, "Red\nSea", size="sea", fs=16)
m.label(51.6, 27.9, "Gulf", size="sea", fs=16)
m.label(63.0, 18.5, "Arabian Sea", size="sea", fs=19)
m.label(51.0, 40.2, "Caspian\nSea", size="sea", fs=16)
m.scale(500, lon=67.0, lat=13.6)
p1 = os.path.join(SCRATCH, "ch105_1.png"); m.save(p1)

# ================================================================ inset: Syria and Iraq
WI = 9.0
n = Map(*INSET, width=WI)
base(n, lw=1.6)
n.city(44.37, 33.31, "Baghdad", dx=0.25, dy=-0.25, ha="left", bold=True)
n.city(43.13, 36.34, "Mosul", dx=0.25, dy=0.25, ha="left", bold=True)
n.city(36.29, 33.51, "Damascus", dx=0.2, dy=-0.25, ha="left")
n.city(34.45, 31.50, "Gaza", dx=-0.2, dy=0.22, ha="right")
n.label(36.7, 35.4, "SYRIA", fs=15)
n.label(45.6, 32.0, "IRAQ\ninvaded 2003", fs=16)
n.label(40.6, 34.75, "ISLAMIC\nSTATE", fs=16)
n.label(35.0, 30.85, "ISRAEL", fs=15, colour="#5a534b")
n.label(33.8, 33.9, "Mediterranean\nSea", size="sea", fs=15)
n.label(38.0, 31.0, "JORDAN", fs=15, colour="#5a534b")
n.label(46.5, 37.3, "TURKEY", fs=15, colour="#5a534b")
n.ax.text(0.975, 0.03, "SYRIA AND IRAQ, ENLARGED", transform=n.ax.transAxes, ha="right", va="bottom", fontsize=16,
          fontweight="bold", color=INK, zorder=9, bbox=dict(boxstyle="square,pad=0.35", fc=PAPER, ec=INK, lw=1.2))
n.scale(200, lon=39.6, lat=29.95)
pi = os.path.join(SCRATCH, "ch105_inset.png"); n.save(pi)

# ---------------------------------------------------------------- the key, beside the inset
img2 = mpimg.imread(pi)[:, :, :3]
k = plt.figure(figsize=(16.0 - WI - 0.16, img2.shape[0] / 100.0), dpi=100)
k.patch.set_facecolor(PAPER)
handles = [Patch(fc=FILL["red"] + "5c", ec=FILL["red"], label="invaded by the\nUnited States"),
           Patch(fc=FILL["gold"] + "5c", ec=FILL["gold"], label="risings of 2011"),
           Patch(fc="#3b33304d", ec="#3b3330", hatch="xx", label="held by the Islamic\nState, 2014 to 2015,\nroughly"),
           Line2D([0], [0], color="#3f6b3b", lw=3.6, ls=(0, (2.2, 1.0)), label="refugees to\nEurope, 2015"),
           Line2D([0], [0], color=INK, lw=1.6, label="area of the\nenlarged map")]
k.legend(handles=handles, loc="center", fontsize=17, frameon=False, labelspacing=1.0, handlelength=2.4,
         handleheight=1.6)
pk = os.path.join(SCRATCH, "ch105_key.png"); k.savefig(pk, dpi=100, facecolor=PAPER); plt.close(k)

top, key = mpimg.imread(p1)[:, :, :3], mpimg.imread(pk)[:, :, :3]
paper = np.array(lib.matplotlib.colors.to_rgb(PAPER))
h = img2.shape[0]
key = key[:h]
row = np.hstack([img2, np.ones((h, 1600 - img2.shape[1] - key.shape[1], 3)) * paper, key])
out = np.vstack([top, np.ones((16, 1600, 3)) * paper, row])
path = os.path.join(lib.ROOT, "chapters/105-terror/images/map_terror.png")
plt.imsave(path, out)
print("wrote", path, out.shape)
