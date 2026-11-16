#!/usr/bin/env python3
"""Chapter 104: above, Ukraine in its internationally recognised borders, with the Crimea (annexed by Russia
in 2014), the Donbas and the line of contact of 2015 to 2022, the furthest Russian advance in March 2022, and
the land held by Russia at the end of 2025; the places named in the chapter (Kyiv, Bucha, Mariupol, the
Dnieper, where the airliner was brought down in 2014), and a few for orientation. Below, the members of the
Atlantic alliance in Europe in 1990, and those that had joined by 2004 and by 2024.

Drawn for this chapter, which had no map. Borders from Natural Earth admin-0, 1:10 million, in its Ukrainian
point-of-view edition, which shows Ukraine in its internationally recognised borders with the Crimea (public
domain; cut to the frame and simplified: data/ch104_ukraine_ne10m_ukr.geojson). The inset uses Natural Earth
admin-0, 1:110 million (as shipped with geopandas).

All the lines of the war are drawn roughly, by hand, and are approximate; positions are good to some
kilometres at best. The line of contact of 2015 to 2022 is drawn after the maps of the OSCE monitoring
mission and English Wikipedia's "War in Donbas": from the Siverskyi Donets near Stanytsia Luhanska, west of
Debaltseve and Horlivka, between Avdiivka and Donetsk, by Marinka, to the coast at Shyrokyne east of
Mariupol. The furthest advance of March 2022 is drawn after the Institute for the Study of War's daily maps of
March 2022 and English Wikipedia's "Kyiv offensive", "Northeastern Ukraine campaign" and "Southern Ukraine
campaign": west of the Dnieper to Ivankiv, Borodianka, Makariv, Bucha, Irpin and Hostomel; east of it to the
edge of Brovary, round Chernihiv, Konotop and Sumy (not taken), to Trostianets and the outskirts of Kharkiv;
Balakliia and Izium; in the south to the edge of Zaporizhzhia, across the Dnieper at Kherson to Vysokopillia,
Voznesensk (held for a day) and the edge of Mykolaiv. The front at the end of 2025 is drawn after the
Institute for the Study of War's assessed map of late December 2025: Kupiansk (contested), short of Lyman,
Siversk, the edge of Kostiantynivka, west of Pokrovsk and Myrnohrad, into the east of Dnipropetrovsk region,
Huliaipole, Stepnohirsk, and then the old course of the Dnieper (the Kakhovka reservoir, drained in 2023) to
the sea; the small Russian footholds on the northern border of Sumy and Kharkiv regions are left out. Nothing
after the end of 2025 is shown. Positions of places from English Wikipedia.

Alliance members (in Europe; the United States and Canada were members throughout): by 1990, Belgium,
Denmark, France, Germany (the east joining with unification in October 1990), Greece, Iceland, Italy,
Luxembourg, the Netherlands, Norway, Portugal, Spain, Turkey and Britain; joined 1999, the Czech Republic,
Hungary and Poland; joined 2004, Bulgaria, Estonia, Latvia, Lithuania, Romania, Slovakia and Slovenia; joined
2009 to 2024, Albania and Croatia (2009), Montenegro (2017), North Macedonia (2020), Finland (2023) and Sweden
(2024).
"""
import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from shapely.geometry import Polygon, LineString, box
from shapely.ops import unary_union
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth, course
from projmap import ProjMap

SCRATCH = os.environ.get("SCRATCH", "/tmp")
RED, BLUE = FILL["red"], FILL["blue"]
DARK = "#7a2f22"
G3 = dict(size="land", colour="#5a534b", style="normal")

U = gpd.read_file(os.path.join(lib.DATA, "ch104_ukraine_ne10m_ukr.geojson"))
C = {r["NAME"]: r.geometry for _, r in U.iterrows()}
UKR = C["Ukraine"]

# ------------------------------------------------------------------ the lines of the war, approximate
contact = [(39.80, 48.60), (39.48, 48.68), (39.22, 48.74), (38.85, 48.72), (38.55, 48.68), (38.42, 48.55),
           (38.42, 48.40), (38.15, 48.35), (37.92, 48.35), (37.78, 48.17), (37.68, 48.03), (37.50, 47.95),
           (37.45, 47.85), (37.65, 47.60), (37.75, 47.40), (37.85, 47.20), (37.88, 47.06)]
march_north = [(29.10, 51.52), (29.35, 51.05), (29.55, 50.75), (29.75, 50.48), (30.05, 50.42), (30.25, 50.49),
               (30.42, 50.62), (30.55, 50.78), (30.75, 50.82), (30.95, 50.62), (31.30, 50.62), (31.80, 50.75),
               (32.40, 50.75), (33.10, 50.60), (33.80, 50.35), (34.50, 50.15), (35.20, 50.05), (35.80, 50.10),
               (36.15, 50.07), (36.55, 49.95), (36.75, 49.78), (36.85, 49.45), (37.15, 49.15), (37.60, 49.05),
               (38.00, 48.98), (38.30, 48.80), (38.42, 48.62)]
march_south = [(37.45, 47.85), (37.00, 47.75), (36.60, 47.72), (36.25, 47.60), (35.85, 47.48), (35.45, 47.48),
               (35.20, 47.58)]
march_west = [(34.00, 47.22), (33.55, 47.45), (33.00, 47.45), (32.40, 47.40), (31.65, 47.58), (31.55, 47.35),
              (32.05, 47.05), (31.95, 46.78), (31.95, 46.62)]
front = [(36.80, 50.42), (36.95, 50.27), (37.30, 50.05), (37.55, 49.88), (37.66, 49.72), (37.72, 49.50),
         (37.68, 49.30), (37.80, 49.12), (37.90, 49.00), (38.05, 48.92), (38.12, 48.85), (38.00, 48.68),
         (37.80, 48.55), (37.55, 48.45), (37.25, 48.42), (37.05, 48.32), (36.95, 48.20), (36.60, 48.00),
         (36.45, 47.85), (36.26, 47.66), (35.95, 47.55), (35.70, 47.53), (35.45, 47.55), (35.20, 47.60)]
dnieper = course("Dnipro", (35.20, 47.60), (31.60, 46.50), step=2)
held = Polygon(list(smooth(front, n=6)) + dnieper + [(31.0, 46.3), (31.0, 43.5), (42.0, 43.5), (42.0, 51.5),
                                                     (36.80, 51.5)]).buffer(0).intersection(UKR)
crimea = gpd.read_file(os.path.join(lib.DATA, "ch104_crimea_ne10m.geojson")).geometry.iloc[0].buffer(0.003).intersection(UKR)
donbas = Polygon(list(smooth(contact, n=6)) + [(38.0, 46.9), (40.5, 46.9), (40.5, 48.7)]).buffer(0).intersection(UKR)

# ================================================================ above: Ukraine
m = Map(22.0, 41.2, 44.1, 52.7)
LAND = m.land
m.region(UKR, "gold", alpha=0.22, edge=False)
m.region(held, RED, alpha=0.32, edge=False)
m.region(donbas, DARK, alpha=0.30, edge=False, hatch="///")
m.region(crimea, DARK, alpha=0.30, edge=False, hatch="///")
m.river("Dnipro", "Desna", lw=1.8)

land = LAND.buffer(-0.02)
names = ["Ukraine", "Russia", "Belarus", "Poland", "Slovakia", "Hungary", "Romania", "Moldova", "Lithuania"]
for i, a in enumerate(names):
    for b in names[i + 1:]:
        e = C[a].boundary.intersection(C[b].buffer(0.02)).intersection(land)
        for l in getattr(e, "geoms", [e]):
            if l.is_empty or l.geom_type != "LineString":
                continue
            xy = np.array(l.coords)
            ukr = "Ukraine" in (a, b)
            m.ax.plot(xy[:, 0], xy[:, 1], color=INK if ukr else SOFT, lw=2.6 if ukr else 1.6,
                      ls="-" if ukr else (0, (5, 2.5)), zorder=2.6)
# Crimea's border with the mainland, as recognised
cb = crimea.boundary.intersection(land).intersection(UKR.difference(crimea).buffer(0.02))
for l in getattr(cb, "geoms", [cb]):
    if l.geom_type == "LineString":
        xy = np.array(l.coords)
        m.ax.plot(xy[:, 0], xy[:, 1], color=SOFT, lw=1.4, ls=(0, (5, 2.5)), zorder=2.6)

m.line(contact, colour=INK, lw=3.2, style="-")
for pts in (march_north, march_south, march_west):
    m.line(pts, colour=BLUE, lw=3.4, style=(0, (2.4, 1.2)))
m.line(front, colour=DARK, lw=3.6)
m.line(dnieper, colour=DARK, lw=3.6, curved=False)

# places
m.city(30.52, 50.45, "Kyiv", dx=0.22, dy=-0.18, bold=True, size=19)
m.city(30.21, 50.54, None, r=7)
m.label(29.0, 50.2, "Bucha", size="small", colour=INK, fs=16)
m.ax.plot([29.3, 30.12], [50.26, 50.51], color=INK, lw=1.2, zorder=6.5)
m.city(36.23, 49.99, "Kharkiv", dx=-0.2, dy=-0.2, ha="right")
m.city(37.55, 47.10, "Mariupol", dx=-0.2, dy=-0.15, ha="right", bold=True)
m.city(32.62, 46.64, None)
m.label(32.05, 45.75, "Kherson", size="small", colour=INK, fs=16.5)
m.ax.plot([32.12, 32.58], [45.84, 46.58], color=INK, lw=1.2, zorder=6.5)
m.city(30.73, 46.48, "Odesa", dx=-0.14, dy=0.2, ha="right")
m.city(33.52, 44.60, "Sevastopol", dx=-0.2, dy=-0.05, ha="right")
m.city(37.80, 48.00, "Donetsk", dx=0.2, dy=-0.17, ha="left")
m.ax.plot(38.65, 48.14, "X", ms=13, mfc=INK, mec=PAPER, mew=1.2, zorder=6)
m.label(40.4, 47.65, "airliner\nshot down,\n2014", size="small", colour=INK, fs=15)
m.ax.plot([39.85, 38.75], [47.75, 48.09], color=INK, lw=1.2, zorder=6.5)

m.label(28.6, 49.0, "U K R A I N E", fs=28)
m.label(35.6, 51.55, "RUSSIA", fs=24, colour="#5a534b")
m.label(27.6, 52.2, "BELARUS", fs=22, colour="#5a534b")
m.label(23.0, 51.7, "POLAND", fs=18, colour="#5a534b")
m.label(25.0, 46.4, "ROMANIA", fs=18, colour="#5a534b")
m.label(28.45, 47.45, "MOLDOVA", fs=15, colour="#5a534b")
m.label(34.3, 45.35, "CRIMEA", fs=18, colour=DARK)
m.label(39.35, 49.1, "DONBAS", fs=18, colour=DARK)
m.label(31.2, 44.65, "Black Sea", size="sea", fs=22)
m.label(36.75, 46.25, "Sea of\nAzov", size="sea", fs=16)
m.label(31.05, 49.15, "Dnieper", size="sea", fs=17, style="italic", rot=-38)
m.scale(200, lon=23.0, lat=44.55)
p1 = os.path.join(SCRATCH, "ch104_1.png"); m.save(p1)

# ================================================================ below: the alliance in Europe
W2 = 9.0
L = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
L = {r["name"]: r.geometry for _, r in L.iterrows()}
by1990 = ["Belgium", "Denmark", "France", "Germany", "Greece", "Iceland", "Italy", "Luxembourg", "Netherlands",
          "Norway", "Portugal", "Spain", "Turkey", "United Kingdom"]
by2004 = ["Czechia", "Hungary", "Poland", "Bulgaria", "Estonia", "Latvia", "Lithuania", "Romania", "Slovakia",
          "Slovenia"]
by2024 = ["Albania", "Croatia", "Montenegro", "North Macedonia", "Finland", "Sweden"]
n = ProjMap("+proj=laea +lat_0=53 +lon_0=15 +units=km", (-2300, 2700, -2000, 2350),
            lonlat_box=box(-30, 30, 100, 80), width=W2)
LANDN = n.land.buffer(0)
P = lambda g: n.proj(g.intersection(n.llclip)).buffer(0).intersection(LANDN)
for names_, col, a in [(by1990, BLUE, 0.62), (by2004, BLUE, 0.36), (by2024, BLUE, 0.16)]:
    n.paint(P(unary_union([L[k] for k in names_])), col, a, lw=0, hatch="///" if names_ is by2024 else None, edge=BLUE)
n.paint(P(UKR), FILL["gold"], 0.45, lw=0)
for g in list(L.values()):
    pg = P(g)
    for p in getattr(pg, "geoms", [pg]):
        if p.geom_type == "Polygon" and p.area > 300:
            xy = np.array(p.exterior.coords)
            n.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=1.6, zorder=2.3)
            n.ax.plot(xy[:, 0], xy[:, 1], color="#6c6156", lw=0.6, zorder=2.35)
n.label(31.0, 49.0, "UKRAINE", fs=15, colour=INK)
YR = dict(fs=15, colour=INK, size="small")
n.label(19.3, 52.2, "1999", **YR)
n.label(25.0, 45.9, "2004", **YR)
n.label(26.5, 63.0, "2023", **YR)
n.label(15.5, 62.5, "2024", **YR)
n.label(45.0, 57.5, "RUSSIA", fs=16, colour="#5a534b")
n.ax.text(0.03, 0.97, "THE ALLIANCE IN EUROPE", transform=n.ax.transAxes, ha="left", va="top", fontsize=17,
          fontweight="bold", color=INK, zorder=9, bbox=dict(boxstyle="square,pad=0.35", fc=PAPER, ec=INK, lw=1.2))
p2 = os.path.join(SCRATCH, "ch104_2.png"); n.save(p2)

# ---------------------------------------------------------------- the key, beside the alliance
img2 = mpimg.imread(p2)[:, :, :3]
k = plt.figure(figsize=(16.0 - W2 - 0.16, img2.shape[0] / 100.0), dpi=100)
k.patch.set_facecolor(PAPER)
handles = [Patch(fc=DARK + "4d", ec=DARK, hatch="///", label="held by Russia and its\nproxies from 2014"),
           Line2D([0], [0], color=INK, lw=3.2, label="line of contact,\n2015 to 2022"),
           Line2D([0], [0], color=BLUE, lw=3.4, ls=(0, (2.4, 1.2)), label="furthest Russian\nadvance, March 2022"),
           Patch(fc=RED + "52", ec=RED, label="held by Russia,\nend of 2025"),
           Line2D([0], [0], color=DARK, lw=3.6, label="front, end of 2025"),
           Patch(fc=BLUE + "9e", ec=BLUE, label="alliance members\nin 1990"),
           Patch(fc=BLUE + "5c", ec=BLUE, label="joined 1999\nand 2004"),
           Patch(fc=BLUE + "29", ec=BLUE, hatch="///", label="joined 2009\nto 2024")]
k.legend(handles=handles, loc="center", fontsize=17, frameon=False, labelspacing=0.8, handlelength=2.4,
         handleheight=1.5, title="lines of the war are approximate", title_fontproperties=dict(size=16, style="italic"))
p3 = os.path.join(SCRATCH, "ch104_key.png"); k.savefig(p3, dpi=100, facecolor=PAPER); plt.close(k)

top, key = mpimg.imread(p1)[:, :, :3], mpimg.imread(p3)[:, :, :3]
paper = np.array(lib.matplotlib.colors.to_rgb(PAPER))
h = img2.shape[0]
key = key[:h]
row = np.hstack([img2, np.ones((h, 1600 - img2.shape[1] - key.shape[1], 3)) * paper, key])
out = np.vstack([top, np.ones((16, 1600, 3)) * paper, row])
path = os.path.join(lib.ROOT, "chapters/104-ukraine/images/map_ukraine.png")
plt.imsave(path, out)
print("wrote", path, out.shape)
