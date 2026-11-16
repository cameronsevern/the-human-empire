#!/usr/bin/env python3
"""Chapter 100: the end of the Soviet empire. The six satellite states of eastern Europe, whose communist
governments fell in 1989, and the fifteen republics of the Soviet Union, with the year in which each declared
itself independent; the cities and places named in the chapter (Berlin, Leipzig, Gdansk, Prague, Moscow,
Kyiv, Chernobyl, Vilnius, the forest lodge where the Union was dissolved, the Crimea, Chechnya).

Drawn for this chapter, which had no map. The states are built from the modern ones (Natural Earth admin-0,
110 m, as shipped with geopandas), whose borders are those of the Soviet republics and of the satellites, apart
from Germany, divided along the line drawn by hand in ch88_europe.py, roughly, and Czechoslovakia, the union
of the Czech Republic and Slovakia. Above, eastern Europe and the western republics; below, Central Asia, with Russia cut at about 95 degrees east (it ran on to the Pacific). Years: for the
satellites, the year their communist governments fell (Poland, Hungary, East Germany, Czechoslovakia, Bulgaria
and Romania, all in 1989; East Germany joined West Germany on 3 October 1990); for the republics, the year of
the declaration of independence, after English Wikipedia's "Dissolution of the Soviet Union": Lithuania on
11 March 1990; Georgia on 9 April 1991; Estonia and Latvia in August 1991 (Latvia had declared a transition to
independence in May 1990); Ukraine, Belarus, Moldova, Azerbaijan, Kyrgyzstan, Uzbekistan, Tajikistan, Armenia
and Turkmenistan between August and October 1991; Russia and Kazakhstan in December 1991. The forest lodge is
Viskuli in the Belovezha forest. Positions from English Wikipedia.
"""
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import lib
from lib import INK, PAPER, FILL, SOFT, HALO
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from projmap import ProjMap

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}

border = [(10.88, 54.10), (10.88, 53.96), (10.95, 53.80), (10.76, 53.62), (10.84, 53.45), (10.60, 53.38),
          (10.85, 53.30), (11.20, 53.15), (11.58, 53.04), (11.38, 52.92), (11.05, 52.88), (10.76, 52.84),
          (10.93, 52.62), (11.03, 52.38), (10.95, 52.18), (10.78, 52.02), (10.62, 51.90), (10.56, 51.72),
          (10.40, 51.62), (10.22, 51.50), (10.05, 51.40), (9.92, 51.30), (10.05, 51.18), (10.03, 51.00),
          (9.94, 50.88), (9.96, 50.70), (10.07, 50.55), (10.40, 50.40), (10.73, 50.35), (10.86, 50.27),
          (11.16, 50.32), (11.40, 50.50), (11.60, 50.40), (11.88, 50.38), (12.10, 50.32)]
east_side = Polygon(border + [(13.0, 49.5), (16.5, 50.0), (16.5, 55.5), (10.88, 55.5)]).buffer(0)
SAT = {"EAST GERMANY": G["Germany"].intersection(east_side), "POLAND": G["Poland"],
       "CZECHOSLOVAKIA": unary_union([G["Czechia"], G["Slovakia"]]), "HUNGARY": G["Hungary"],
       "ROMANIA": G["Romania"], "BULGARIA": G["Bulgaria"]}
REP = {"RUSSIA": "Russia", "UKRAINE": "Ukraine", "BELARUS": "Belarus", "ESTONIA": "Estonia", "LATVIA": "Latvia",
       "LITHUANIA": "Lithuania", "MOLDOVA": "Moldova", "GEORGIA": "Georgia", "ARMENIA": "Armenia",
       "AZERBAIJAN": "Azerbaijan", "KAZAKHSTAN": "Kazakhstan", "UZBEKISTAN": "Uzbekistan",
       "TURKMENISTAN": "Turkmenistan", "KYRGYZSTAN": "Kyrgyzstan", "TAJIKISTAN": "Tajikistan"}

SCRATCH = os.environ.get("SCRATCH", "/tmp")
BLUE, RED = FILL["blue"], FILL["red"]


def base(m, minarea=100):
    LAND = m.land.buffer(0)
    P = lambda g: m.proj(g.intersection(m.llclip)).buffer(0).intersection(LAND)
    for g in SAT.values():
        m.paint(P(g), BLUE, 0.45, lw=0)
    for name, n in REP.items():
        m.paint(P(G[n]), RED, 0.20 if name != "LITHUANIA" else 0.45, lw=0)
    for g in list(SAT.values()) + [G[n] for n in REP.values()]:
        pg = P(g)
        for p in getattr(pg, "geoms", [pg]):
            if p.geom_type == "Polygon" and p.area > minarea:
                xy = np.array(p.exterior.coords)
                m.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=2.6, zorder=2.3)
                m.ax.plot(xy[:, 0], xy[:, 1], color="#6c6156", lw=0.9, zorder=2.35)
    ussr = P(unary_union([G[n] for n in REP.values()]).buffer(0.03))
    for p in getattr(ussr, "geoms", [ussr]):
        if p.geom_type == "Polygon" and p.area > 5 * minarea:
            xy = np.array(p.exterior.coords)
            m.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=2.2, zorder=2.5)


def namer(m):
    def name(lon, lat, text, year, fs=15, ha="center", lead=None, colour=INK):
        m.label(lon, lat, f"{text}\n{year}", fs=fs, ha=ha, colour=colour)
        if lead:
            a, b = m.xy(*lead[0]), m.xy(*lead[1])
            m.ax.plot([a[0], b[0]], [a[1], b[1]], color=INK, lw=1.2, zorder=6.5)
    return name


G3 = dict(size="land", colour="#5a534b", style="normal", fs=15)

# ================================================================ above: eastern Europe and the western republics
m = ProjMap("+proj=lcc +lat_1=45 +lat_2=58 +lat_0=50 +lon_0=30 +units=km", (-1480, 1820, -1330, 1150),
            lonlat_box=box(-10, 30, 75, 75))
base(m)
name = namer(m)
name(19.6, 52.0, "POLAND", 1989, fs=17)
name(13.0, 55.6, "EAST GERMANY", 1989, lead=((13.0, 55.0), (12.9, 53.9)))
name(16.6, 49.3, "CZECHOSLOVAKIA", 1989)
name(19.3, 46.9, "HUNGARY", 1989)
name(24.9, 45.8, "ROMANIA", 1989)
name(25.3, 42.75, "BULGARIA", 1989)
name(32.0, 49.0, "UKRAINE", 1991, fs=18)
name(28.0, 53.5, "BELARUS", 1991, fs=16)
name(20.2, 58.9, "ESTONIA", 1991, lead=((22.0, 58.9), (25.2, 58.8)))
name(18.6, 57.2, "LATVIA", 1991, lead=((20.2, 57.15), (24.4, 56.9)))
name(17.4, 55.35, "LITHUANIA", 1990, lead=((20.4, 55.3), (23.5, 55.35)))
name(30.4, 44.7, "MOLDOVA", 1991, lead=((30.0, 45.3), (28.7, 47.0)))
name(39.0, 40.3, "GEORGIA", 1991, ha="center", lead=((40.6, 41.2), (43.3, 42.0)))
name(43.6, 39.0, "ARMENIA", 1991, ha="right", lead=((43.5, 39.6), (44.8, 40.25)))
name(50.6, 38.9, "AZERBAIJAN", 1991, ha="right", lead=((48.5, 39.6), (47.7, 40.3)))
name(44.5, 54.5, "RUSSIA", 1991, fs=24)

m.city(13.40, 52.52, "Berlin", dx=-45, dy=-45, ha="right", bold=True)
m.city(12.37, 51.34, "Leipzig", dx=-45, dy=-15, ha="right")
m.city(18.65, 54.35, "Gdańsk", dx=0, dy=45, ha="center")
m.city(14.42, 50.09, "Prague", dx=-45, dy=-25, ha="right")
m.city(37.62, 55.75, "Moscow", dx=45, dy=30, ha="left", bold=True)
m.city(30.52, 50.45, "Kyiv", dx=40, dy=-25, ha="left")
m.city(30.10, 51.39, None, r=7)
m.label(30.6, 51.75, "Chernobyl", size="small", colour=INK, fs=15, ha="left")
m.city(25.28, 54.69, "Vilnius", dx=40, dy=-15, ha="left")
m.ax.plot(*m.xy(23.9, 52.65), "^", ms=14, mfc=INK, mec=PAPER, mew=1.4, zorder=6)
m.label(23.2, 51.3, "forest lodge,\nDecember 1991", size="small", colour=INK, fs=15, ha="center")
m.label(34.2, 45.25, "Crimea", size="small", colour=INK, fs=15, ha="center")
m.city(45.70, 43.32, None, r=7)
m.label(46.4, 43.9, "Chechnya", size="small", colour=INK, fs=15, ha="left")
m.label(34.5, 42.9, "Black Sea", size="sea", fs=18)
m.label(50.8, 42.0, "Caspian\nSea", size="sea", fs=16)
m.label(18.2, 60.6, "Baltic Sea", size="sea", fs=16)
m.label(15.2, 63.2, "SWEDEN", **G3)
m.label(26.5, 62.5, "FINLAND", **G3)
m.label(34.0, 39.5, "TURKEY", **G3)
m.label(19.4, 44.0, "YUGO-\nSLAVIA", **G3)
m.label(14.2, 47.3, "AUSTRIA", **G3)
m.scale(300, x=1400, y=-1270)
p1 = os.path.join(SCRATCH, "ch100_1.png"); m.save(p1)

# ================================================================ below: Central Asia
W2 = 10.0
n = ProjMap("+proj=lcc +lat_1=40 +lat_2=55 +lat_0=47 +lon_0=66 +units=km", (-1700, 2350, -1330, 1250),
            lonlat_box=box(30, 25, 110, 75), width=W2)
base(n, minarea=400)
name = namer(n)
name(68.0, 48.3, "KAZAKHSTAN", 1991, fs=17)
name(63.4, 42.0, "UZBEKISTAN", 1991)
name(58.6, 39.3, "TURKMENISTAN", 1991)
name(74.7, 41.55, "KYRGYZSTAN", 1991, ha="center")
name(71.0, 38.65, "TAJIKISTAN", 1991, ha="center")
name(70.0, 56.6, "RUSSIA", 1991, fs=19)
n.label(85.5, 55.6, "to the\nPacific", size="small", colour=INK, fs=15, style="italic", ha="left")
n.ax.annotate("", xy=n.xy(93.5, 54.6), xytext=n.xy(88.0, 54.4), zorder=8,
              arrowprops=dict(arrowstyle="-|>,head_width=0.3,head_length=0.6", color=INK, lw=1.6))
n.label(51.0, 43.5, "Caspian\nSea", size="sea", fs=15)
n.label(59.5, 33.5, "IRAN", **G3)
n.label(66.5, 33.4, "AFGHANISTAN", **G3)
n.label(84.0, 43.0, "CHINA", **G3)
n.ax.text(0.02, 0.975, "CENTRAL ASIA", transform=n.ax.transAxes, ha="left", va="top", fontsize=16,
          fontweight="bold", color=INK, zorder=9, bbox=dict(boxstyle="square,pad=0.3", fc=PAPER, ec=INK, lw=1.2))
n.scale(500, x=1700, y=-1180)
p2 = os.path.join(SCRATCH, "ch100_2.png"); n.save(p2)

# ---------------------------------------------------------------- the key, in the space beside Central Asia
k = plt.figure(figsize=(16.0 - W2 - 0.16, 1), dpi=100)
k.patch.set_facecolor(PAPER)
handles = [Patch(fc=BLUE + "73", ec=BLUE, label="satellite states:\nyear communist\nrule ended"),
           Patch(fc=RED + "33", ec=RED, label="Soviet republics:\nyear of declared\nindependence"),
           Patch(fc=RED + "73", ec=RED, label="Lithuania, the\nfirst, in 1990"),
           Line2D([0], [0], color=INK, lw=2.2, label="frontier of the\nSoviet Union"),
           Line2D([0], [0], ls="none", marker="^", ms=13, mfc=INK, mec=PAPER,
                  label="where the Union\nwas dissolved")]
leg = k.legend(handles=handles, loc="center", fontsize=17, frameon=False, labelspacing=0.9, handlelength=2.2,
               handleheight=1.6)
img2 = mpimg.imread(p2)[:, :, :3]
k.set_size_inches(16.0 - W2 - 0.16, img2.shape[0] / 100.0)
p3 = os.path.join(SCRATCH, "ch100_key.png"); k.savefig(p3, dpi=100, facecolor=PAPER); plt.close(k)

top, key = mpimg.imread(p1)[:, :, :3], mpimg.imread(p3)[:, :, :3]
paper = np.array(lib.matplotlib.colors.to_rgb(PAPER))
h = img2.shape[0]
key = key[:h]
row = np.hstack([img2, np.ones((h, 1600 - img2.shape[1] - key.shape[1], 3)) * paper, key])
out = np.vstack([top, np.ones((16, 1600, 3)) * paper, row])
path = os.path.join(lib.ROOT, "chapters/100-soviet-collapse/images/map_breakup.png")
plt.imsave(path, out)
print("wrote", path, out.shape)
