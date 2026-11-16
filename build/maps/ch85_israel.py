#!/usr/bin/env python3
"""Chapter 85: left, the United Nations partition plan of 29 November 1947 (the Jewish state, the Arab state in
three pieces joined at their corners, with Jaffa as an Arab enclave, and Jerusalem under the United Nations);
right, the armistice lines of 1949, with Israel, the West Bank held by Transjordan (Jordan), the Gaza strip
held by Egypt, and the places named in the chapter (Tel Aviv, Jaffa, Haifa, Lydda, Ramle, Deir Yassin, Gaza);
inset, divided Jerusalem, with the Old City and the Israeli enclave on Mount Scopus.

Drawn for this chapter, which had no map. The partition plan is traced from the Wikimedia Commons map
"1947-UN-Partition-Plan-1949-Armistice-Comparison.svg" (AnonMoos, public domain; outlines sampled from its
paths: data/ch85_partition_svg.txt), fitted to longitude and latitude by least squares on the extreme points
of the mandate (the south tip at the Gulf of Aqaba, the north tip at Metula, the coast at Rafah, the Yarmuk
corner); the fit is good to a few kilometres, so the plan's areas are drawn roughly, and the small Arab
enclave of Jaffa is enlarged by the tracing. The plan's areas are cut to the mandate as Natural Earth draws it
(admin-0, 110 m, as shipped with geopandas: Israel and Palestine, less the Golan heights). The West Bank and
the Gaza strip of 1949 are from OpenStreetMap (data/ch98_westbank_osm.txt, the West Bank as Jordan held it
from 1949 to 1967); the inset of Jerusalem from OpenStreetMap too (data/ch85_jerusalem_osm.txt: the same
relation in more detail, and the walls of the Old City). The demilitarised zones and no-man's-lands of 1949
are not shown. Positions from English Wikipedia.
"""
import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from matplotlib.patches import Polygon as MplPoly, Rectangle
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth
from tracing import fit

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
SCRATCH = os.environ.get("SCRATCH", "/tmp")
BLUE, RED, GREY = FILL["blue"], FILL["red"], "#8d857b"
G3 = dict(size="land", colour="#5a534b", style="normal")


def read(name, conv=lambda p: p):
    D = {}
    for line in open(os.path.join(lib.DATA, name)):
        if line.startswith("#") or ":" not in line:
            continue
        k, rest = line.strip().split(":", 1)
        if not rest:
            continue
        D.setdefault(k, []).extend([[conv(tuple(map(float, p.split(",")))) for p in piece.split()]
                                     for piece in rest.split("|")])
    return D


# ------------------------------------------------------------------ the plan of 1947, fitted
deg = fit([((179.9, 1012.6), (34.94, 29.50)),       # south tip, at the Gulf of Aqaba
           ((328.1, 12.0), (35.575, 33.285)),        # north tip, at Metula
           ((21.8, 528.5), (34.218, 31.322)),        # the coast at Rafah
           ((352.6, 168.6), (35.68, 32.69))])        # the Yarmuk corner
P = read("ch85_partition_svg.txt")
poly = lambda key: unary_union([Polygon(deg(pts)).buffer(0) for pts in P[key] if len(pts) > 3])
lib._load()
traced = unary_union([poly(k) for k in P]).buffer(0.002).buffer(-0.002)
# the traced outline, pushed out to the coast of Natural Earth where it falls a little short of it
coast = box(34.15, 31.33, 35.13, 33.12)
mandate = traced.union(traced.buffer(0.05).intersection(coast)).intersection(lib._land)
lakes = unary_union([g for g in lib._lakes[lib._lakes["name"].isin(["Dead Sea", "Sea of Galilee"])].geometry])
mandate = mandate.difference(lakes).buffer(0)
cs = unary_union([poly("magenta"), poly("grey")]).buffer(0.004)
arab47 = unary_union([poly("pink"), poly("green")]).buffer(0.003).difference(cs).intersection(mandate)
jewish47 = mandate.difference(arab47).difference(cs)
big = lambda g, a=0.002: unary_union([p for p in getattr(g, "geoms", [g]) if p.area > a])
jewish47, arab47 = big(jewish47), big(arab47, 0.0004)
cs = cs.intersection(mandate)

# ------------------------------------------------------------------ the lines of 1949 (OpenStreetMap)
D = read("ch98_westbank_osm.txt")
wb = Polygon(D["wb"][0], [D["wb"][1]]).buffer(0)
gaza = Polygon(D["gaza"][0]).buffer(0)
israel49 = big(mandate.difference(wb.buffer(0.004)).difference(gaza.buffer(0.004)), 0.01)
wb, gaza = wb.intersection(lib._land).difference(lakes), gaza.intersection(lib._land)
J = read("ch85_jerusalem_osm.txt")
scopus = unary_union([Polygon(p).buffer(0) for p in J["scopus"]])
jwb = unary_union([Polygon(p).buffer(0) for p in J["jwb"]]).difference(scopus)
oldcity = Polygon(J["oldcity"][0])


def paint(m, geom, colour, alpha=0.45, hatch=None, lw=1.6, edge=None, z=2):
    for p in getattr(geom, "geoms", [geom]):
        if p.is_empty or p.geom_type != "Polygon" or p.area < 1e-5:
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=colour, ec="none", alpha=alpha, zorder=z))
        if hatch:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=edge or colour, lw=0, alpha=0.8, zorder=z + 0.05,
                                   hatch=hatch))
        if lw:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=edge or colour, lw=lw, alpha=0.95, zorder=z + 0.1))


def edge(m, geom, lw=2.6, colour=INK, z=3.6):
    for p in getattr(geom, "geoms", [geom]):
        if p.geom_type == "Polygon" and p.area > 1e-5:
            xy = np.array(p.exterior.coords)
            m.ax.plot(xy[:, 0], xy[:, 1], color=colour, lw=lw, zorder=z)


def countries(m, names):
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            e = G[a].boundary.intersection(G[b].buffer(0.02)).intersection(m.land.buffer(-0.01))
            for line in getattr(e, "geoms", [e]):
                if line.is_empty or line.geom_type != "LineString":
                    continue
                xy = np.array(line.coords)
                m.ax.plot(xy[:, 0], xy[:, 1], color=SOFT, lw=1.6, ls=(0, (5, 2.5)), zorder=2.6)
    e = mandate.boundary.intersection(m.land.buffer(-0.01))          # the frontier of the mandate
    for line in getattr(e, "geoms", [e]):
        if line.geom_type == "LineString":
            xy = np.array(line.coords)
            m.ax.plot(xy[:, 0], xy[:, 1], color=SOFT, lw=1.6, ls=(0, (5, 2.5)), zorder=2.6)


def title(m, text):
    m.ax.text(0.04, 0.988, text, transform=m.ax.transAxes, ha="left", va="top", fontsize=20, fontweight="bold",
              color=INK, zorder=9, bbox=dict(boxstyle="square,pad=0.35", fc=PAPER, ec=INK, lw=1.2))


def leader(m, a, b):
    m.ax.plot([a[0], b[0]], [a[1], b[1]], color=INK, lw=1.2, zorder=6.5)


FRAME = (33.95, 36.05, 29.40, 33.42)
W = 7.9

# ================================================================ left: the plan of 1947
L = Map(*FRAME, width=W)
countries(L, ["Egypt", "Jordan", "Syria", "Lebanon"])
paint(L, jewish47, BLUE)
paint(L, arab47, RED, alpha=0.5)
paint(L, cs, GREY, alpha=0.35, hatch="///", edge=INK, lw=1.4)
L.label(34.95, 30.25, "JEWISH\nSTATE", fs=19)
L.label(34.27, 31.88, "ARAB\nSTATE", fs=16, ha="center")
L.ax.plot([34.36, 34.56], [31.81, 31.68], color=INK, lw=1.2, zorder=6.5)
L.label(35.27, 32.12, "ARAB\nSTATE", fs=17)
L.label(35.23, 32.98, "ARAB\nSTATE", fs=15, ha="right")
leader(L, (35.24, 32.93), (35.30, 32.83))
L.label(35.84, 32.98, "JEWISH\nSTATE", fs=15, ha="left")
leader(L, (35.84, 32.98), (35.62, 33.05))
L.city(35.22, 31.78, None, r=7)
L.label(35.36, 31.66, "JERUSALEM,\nunder the\nUnited Nations", fs=15, ha="left")
leader(L, (35.37, 31.70), (35.28, 31.76))
L.city(34.78, 32.08, "Tel Aviv", dx=-0.07, dy=0.06, ha="right")
L.city(34.75, 32.05, "Jaffa", dx=-0.07, dy=-0.05, ha="right")
L.city(34.99, 32.79, "Haifa", dx=-0.07, dy=0.03, ha="right")
L.city(34.45, 31.50, "Gaza", dx=-0.07, dy=0.03, ha="right")
L.label(34.30, 32.75, "Mediterranean\nSea", size="sea", fs=17)
L.label(36.0, 31.0, "TRANS-\nJORDAN", fs=15, ha="right", **G3)
L.label(36.0, 33.30, "SYRIA", fs=15, ha="right", **G3)
L.label(35.42, 33.36, "LEBANON", fs=15, ha="right", **G3)
L.label(34.0, 30.0, "EGYPT", fs=15, ha="left", **G3)
L.label(35.62, 31.30, "Dead\nSea", size="sea", fs=15, ha="left")
title(L, "1947: the United Nations plan")
p1 = os.path.join(SCRATCH, "ch85_1.png"); L.save(p1)

# ================================================================ right: the lines of 1949
R = Map(*FRAME, width=W)
countries(R, ["Egypt", "Jordan", "Syria", "Lebanon"])
paint(R, israel49, BLUE)
paint(R, wb, RED, alpha=0.5)
paint(R, gaza, RED, alpha=0.5)
edge(R, wb, 2.4); edge(R, gaza, 2.4)
R.label(34.80, 30.85, "ISRAEL", fs=20)
R.label(35.33, 32.08, "WEST\nBANK", fs=17)
R.label(35.34, 31.99, "held by Jordan", size="small", colour=INK, fs=15)
R.label(34.10, 31.86, "GAZA\nSTRIP", fs=15, ha="center")
R.label(34.10, 31.70, "held by\nEgypt", size="small", colour=INK, fs=15, ha="center")
leader(R, (34.20, 31.62), (34.37, 31.46))
R.city(34.78, 32.08, "Tel Aviv", dx=-0.07, dy=0.06, ha="right")
R.city(34.75, 32.05, "Jaffa", dx=-0.07, dy=-0.02, ha="right")
R.city(34.99, 32.79, "Haifa", dx=-0.07, dy=0.03, ha="right")
R.city(34.45, 31.50, None, r=7)
R.city(34.895, 31.95, "Lydda", dx=-0.035, dy=0.035, ha="right")
R.city(34.87, 31.93, "Ramle", dx=-0.03, dy=-0.04, ha="right")
R.city(35.22, 31.78, None, r=7)
R.label(35.25, 31.875, "Jerusalem", size="city", colour=INK, fs=16.5, ha="center")
R.label(34.30, 32.75, "Mediterranean\nSea", size="sea", fs=17)
R.label(36.0, 31.0, "JORDAN", fs=15, ha="right", **G3)
R.label(36.0, 33.30, "SYRIA", fs=15, ha="right", **G3)
R.label(35.42, 33.36, "LEBANON", fs=15, ha="right", **G3)
R.label(34.0, 30.0, "EGYPT", fs=15, ha="left", **G3)
R.label(35.62, 31.30, "Dead\nSea", size="sea", fs=15, ha="left")
R.scale(50, lon=35.35, lat=29.62)
title(R, "1949: the armistice lines")

# ---------------------------------------------------------------- inset: divided Jerusalem
IW, IE, IS, IN = 35.155, 35.295, 31.735, 31.835
IWID = 4.1
ins = Map(IW, IE, IS, IN, width=IWID, lakes=False)
paint(ins, box(IW - 0.1, IS - 0.1, IE + 0.1, IN + 0.1).difference(jwb), BLUE, lw=0)
paint(ins, jwb, RED, alpha=0.5, lw=0)
paint(ins, scopus, BLUE, alpha=0.6, lw=0)
edge(ins, jwb.intersection(box(IW, IS, IE, IN)), 2.6)
edge(ins, scopus, 1.8)
ins.ax.add_patch(MplPoly(np.array(oldcity.exterior.coords), closed=True, fc="#e7cdbf", ec=INK, lw=2.2, zorder=4))
ins.label(35.234, 31.7665, "Old City", size="small", colour=INK, fs=15)
ins.label(35.19, 31.757, "WEST\n(Israel)", fs=15)
ins.label(35.268, 31.752, "EAST\n(Jordan)", fs=15)
ins.label(35.258, 31.808, "Mount\nScopus", size="small", colour=INK, fs=15, ha="left")
ins.city(35.178, 31.786, None, r=7)
ins.label(35.178, 31.796, "Deir Yassin", size="small", colour=INK, fs=15, ha="center")
ins.ax.text(0.04, 0.965, "JERUSALEM, 1949", transform=ins.ax.transAxes, ha="left", va="top", fontsize=15,
            fontweight="bold", color=INK, zorder=9, path_effects=HALO)
ins.ax.add_patch(Rectangle((0, 0), 1, 1, transform=ins.ax.transAxes, fc="none", ec=INK, lw=3, zorder=10))
pi = os.path.join(SCRATCH, "ch85_inset.png"); ins.save(pi)
img = mpimg.imread(pi)
fw, fh = R.fig.get_size_inches()
ax = R.fig.add_axes([1 - IWID / fw - 0.012, 0.012, IWID / fw, img.shape[0] / 100.0 / fh])
ax.imshow(img); ax.set_axis_off(); ax.set_zorder(20)
# where the inset is
R.ax.add_patch(Rectangle((IW, IS), IE - IW, IN - IS, fc="none", ec=INK, lw=1.4, zorder=5))
p2 = os.path.join(SCRATCH, "ch85_2.png"); R.save(p2)

ims = [mpimg.imread(p)[:, :, :3] for p in (p1, p2)]
paper = np.array(lib.matplotlib.colors.to_rgb(PAPER))
hgt = max(i.shape[0] for i in ims)
ims = [np.vstack([i, np.ones((hgt - i.shape[0], i.shape[1], 3)) * paper]) for i in ims]
gap = np.ones((hgt, 1600 - sum(i.shape[1] for i in ims), 3)) * paper
out = np.hstack([ims[0], gap, ims[1]])
path = os.path.join(lib.ROOT, "chapters/85-israel/images/map_partition.png")
plt.imsave(path, out)
print("wrote", path, out.shape)
