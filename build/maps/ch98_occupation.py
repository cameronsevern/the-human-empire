#!/usr/bin/env python3
"""Chapter 98: Israel and the territories it took in June 1967 (Sinai and the Gaza strip from Egypt, the West
Bank and East Jerusalem from Jordan, the Golan heights from Syria), with Sinai marked as returned to Egypt
under the treaty of 1979; right, the West Bank about 2005, with the 1949 armistice line, the Palestinian
cities, the larger Israeli settlements, and the route of the barrier, roughly.

Drawn for this chapter, which had no map. The West Bank (with East Jerusalem) and the Gaza strip are from
OpenStreetMap (data/ch98_westbank_osm.txt): the West Bank as Jordan held it from 1949 to 1967, whose western
edge is the armistice line of 1949. Israel within the 1949 lines, Egypt, Jordan, Syria and Lebanon are
Natural Earth admin-0 (110 m, as shipped with geopandas). The Golan heights are the part of that file's Israel
east of the 1949 line with Syria, which is drawn by hand along the upper Jordan and the east shore of the Sea
of Galilee, roughly. Sinai is Egypt east of the Suez Canal and the Gulf of Suez. The barrier is the
OpenStreetMap route, which its mappers mark as rough and which does not tell built from planned stretches:
it is drawn as a rough line, with gaps where the data has them. Cities and settlements from OpenStreetMap and
English Wikipedia. Settlements shown: the four largest towns (Modi'in Illit, Beitar Illit, Ma'ale Adumim,
Ariel) and Kiryat Arba, the town above Hebron.
"""
import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from shapely.geometry import Polygon, LineString
from shapely.ops import unary_union
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
SCRATCH = os.environ.get("SCRATCH", "/tmp")
BLUE, RED, BROWN = FILL["blue"], FILL["red"], FILL["brown"]

D = {}
for line in open(os.path.join(lib.DATA, "ch98_westbank_osm.txt")):
    if line.startswith("#") or ":" not in line:
        continue
    k, rest = line.strip().split(":", 1)
    D[k] = [[tuple(map(float, p.split(","))) for p in piece.split()] for piece in rest.split("|")]
wb = Polygon(D["wb"][0], [D["wb"][1]]).buffer(0)                  # the Mount Scopus enclave is a hole
gaza = Polygon(D["gaza"][0]).buffer(0)
syria_line = [(35.66, 33.40), (35.66, 33.25), (35.64, 33.12), (35.62, 33.00), (35.635, 32.90), (35.645, 32.82),
              (35.64, 32.74), (35.60, 32.68)]
golan = G["Israel"].intersection(Polygon(syria_line + [(36.2, 32.6), (36.2, 33.5)]).buffer(0))
israel = unary_union([G["Israel"], G["Palestine"]]).difference(golan).difference(wb.buffer(0.004))
israel = israel.difference(gaza.buffer(0.004))
suez = [(32.32, 31.6), (32.30, 31.26), (32.33, 30.6), (32.55, 29.97), (32.65, 29.6), (33.2, 28.5), (33.9, 27.4),
        (34.5, 27.0)]
sinai = G["Egypt"].intersection(Polygon(suez + [(35.5, 27.0), (35.5, 31.6)]).buffer(0))
G3 = dict(size="land", colour="#5a534b", style="normal")


def edge(m, geom, lw=2.6):
    for p in getattr(geom, "geoms", [geom]):
        if p.geom_type == "Polygon":
            xy = np.array(p.exterior.coords)
            m.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=lw, zorder=3.6)


def countries(m, names):
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            e = G[a].boundary.intersection(G[b].buffer(0.02)).intersection(m.land.buffer(-0.01))
            for line in getattr(e, "geoms", [e]):
                if line.is_empty or line.geom_type != "LineString":
                    continue
                xy = np.array(line.coords)
                m.ax.plot(xy[:, 0], xy[:, 1], color=SOFT, lw=1.6, ls=(0, (5, 2.5)), zorder=2.6)


def title(m, text):
    m.ax.text(0.03, 0.985, text, transform=m.ax.transAxes, ha="left", va="top", fontsize=20, fontweight="bold",
              color=INK, zorder=9, bbox=dict(boxstyle="square,pad=0.35", fc=PAPER, ec=INK, lw=1.2))


# ================================================================ left: 1967
L = Map(32.2, 36.3, 27.6, 33.5, width=7.77)
countries(L, ["Egypt", "Jordan", "Syria", "Lebanon", "Saudi Arabia"])
L.region(israel, "blue", alpha=0.42, lakes_out=True)
for g in (wb, gaza, golan):
    L.region(g, "red", alpha=0.5, lakes_out=True)
L.region(sinai, "red", alpha=0.18, hatch="//")
edge(L, wb, 2.2); edge(L, gaza, 2.2)
L.ax.plot(*np.array(smooth(suez[:4])).T, color=lib.WATER, lw=2.4, zorder=2.5)
L.label(34.85, 30.75, "ISRAEL", fs=17)
L.label(33.85, 29.35, "SINAI\ntaken 1967,\nreturned to\nEgypt under\nthe treaty\nof 1979", fs=16)
L.label(35.95, 32.35, "WEST\nBANK", fs=15, ha="left")
L.ax.plot([35.35, 35.9], [32.05, 32.3], color=INK, lw=1.2, zorder=6.5)
L.label(33.65, 31.65, "Gaza\nstrip", fs=15, ha="center")
L.ax.plot([34.0, 34.35], [31.55, 31.42], color=INK, lw=1.2, zorder=6.5)
L.label(36.2, 33.15, "Golan\nheights", fs=15, ha="right")
L.city(35.23, 31.78, "Jerusalem", dx=0.12, dy=-0.18, ha="left")
L.city(34.78, 32.08, "Tel Aviv", dx=-0.1, dy=0.0)
L.city(34.95, 29.56, None, r=7)
L.label(35.1, 29.45, "Eilat", size="small", colour=INK, fs=15, ha="left")
L.label(32.9, 32.7, "Mediterranean\nSea", size="sea", fs=17)
L.label(35.85, 30.4, "JORDAN", fs=15, **G3)
L.label(36.2, 33.4, "SYRIA", fs=15, ha="right", **G3)
L.label(35.15, 33.38, "LEBANON", fs=15, ha="right", **G3)
L.label(32.5, 28.4, "EGYPT", fs=15, ha="left", **G3)
L.label(32.65, 30.65, "Suez\nCanal", size="sea", fs=15, ha="left")
L.label(34.6, 28.2, "Red\nSea", size="sea", fs=15, ha="left")
title(L, "1967")
p1 = os.path.join(SCRATCH, "ch98_1.png"); L.save(p1)

# ================================================================ right: the West Bank about 2005
R = Map(34.70, 35.65, 31.30, 32.60, width=8.06)
R.region(israel, "blue", alpha=0.32, lakes_out=True)
R.region(wb, "red", alpha=0.32, lakes_out=True)
R.river("Jordan", lw=2.0)
edge(R, wb, 3.0)
for _, r in lib._lakes[lib._lakes["name"] == "Dead Sea"].iterrows():      # the Dead Sea over the edge
    for p in getattr(r.geometry, "geoms", [r.geometry]):
        R.ax.add_patch(lib.MplPoly(np.array(p.exterior.coords), closed=True, fc=lib.SEA, ec=lib.SHORE, lw=0.8,
                                   zorder=3.65))
for piece in D["barrier"]:
    if len(piece) < 2:
        continue
    xy = np.array(piece)
    R.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=5.4, zorder=3.7)
    R.ax.plot(xy[:, 0], xy[:, 1], color=BROWN, lw=3.0, ls=(0, (2.2, 1.2)), zorder=3.8)
for x, y, name, dx, dy, ha in [(35.298, 32.462, "Jenin", 0.03, 0.0, "left"), (35.257, 32.221, "Nablus", 0.03, 0.0, "left"),
                               (35.028, 32.311, "Tulkarm", 0.03, 0.02, "left"),
                               (34.968, 32.188, "Qalqilya", -0.03, 0.01, "right"),
                               (35.195, 31.903, "Ramallah", 0.03, 0.0, "left"),
                               (35.460, 31.856, "Jericho", 0.0, 0.035, "center"),
                               (35.202, 31.705, "Bethlehem", 0.03, -0.01, "left"),
                               (35.094, 31.529, "Hebron", -0.03, 0.0, "right")]:
    R.city(x, y, name, dx=dx, dy=dy, ha=ha)
R.city(35.226, 31.779, "Jerusalem", dx=0.035, dy=0.02, ha="left", bold=True)
R.city(34.78, 32.08, "Tel Aviv", dx=0.0, dy=0.035, ha="center")
for x, y, name, dx, dy, ha in [(35.185, 32.106, "Ariel", 0.03, 0.0, "left"),
                               (35.298, 31.771, "Ma'ale Adumim", 0.025, -0.025, "left"),
                               (35.043, 31.932, "Modi'in Illit", -0.03, 0.015, "right"),
                               (35.114, 31.699, "Beitar Illit", -0.03, 0.0, "right"),
                               (35.120, 31.533, "Kiryat Arba", 0.03, -0.02, "left")]:
    R.ax.plot(x, y, "s", ms=11, mfc=RED, mec=INK, mew=1.4, zorder=6)
    R.ax.text(x + dx, y + dy, name, ha=ha, va="center", fontsize=15, color=INK, style="italic", zorder=7,
              path_effects=HALO)
R.label(35.33, 32.35, "WEST BANK", fs=19)
R.label(34.86, 31.75, "ISRAEL", fs=19)
R.label(35.58, 32.0, "Jordan", size="sea", fs=15, rot=90)
R.label(35.555, 31.56, "Dead\nSea", size="sea", fs=15)
R.label(34.90, 32.48, "armistice line\nof 1949", size="small", colour=INK, fs=15, ha="center")
R.ax.plot([34.96, 35.04], [32.445, 32.40], color=INK, lw=1.2, zorder=6.5)
from matplotlib.lines import Line2D
h = [Line2D([0], [0], color=INK, lw=3, label="armistice line of 1949"),
     Line2D([0], [0], color=BROWN, lw=3, ls=(0, (2.2, 1.2)), label="barrier, roughly"),
     Line2D([0], [0], ls="none", marker="s", ms=10, mfc=RED, mec=INK, label="Israeli settlement"),
     Line2D([0], [0], ls="none", marker="o", ms=8, mfc=INK, mec=PAPER, label="Palestinian city")]
leg = R.ax.legend(handles=h, loc="lower right", fontsize=15, frameon=True, fancybox=False, edgecolor=INK,
                  facecolor=PAPER, framealpha=1, borderpad=0.6, labelspacing=0.45)
leg.set_zorder(9); leg.get_frame().set_linewidth(1.2)
R.scale(10, lon=34.74, lat=31.47)
title(R, "The West Bank, about 2005")
p2 = os.path.join(SCRATCH, "ch98_2.png"); R.save(p2)

ims = [mpimg.imread(p)[:, :, :3] for p in (p1, p2)]
paper = np.array(lib.matplotlib.colors.to_rgb(PAPER))
hgt = max(i.shape[0] for i in ims)
ims = [np.vstack([i, np.ones((hgt - i.shape[0], i.shape[1], 3)) * paper]) for i in ims]
gap = np.ones((hgt, 1600 - sum(i.shape[1] for i in ims), 3)) * paper
out = np.hstack([ims[0], gap, ims[1]])
path = os.path.join(lib.ROOT, "chapters/98-occupation/images/map_occupation.png")
plt.imsave(path, out)
print("wrote", path, out.shape)
