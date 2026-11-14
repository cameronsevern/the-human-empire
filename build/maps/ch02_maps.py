#!/usr/bin/env python3
"""The two maps of chapter 2, drawn from the dates the chapter gives.

    uv run --python 3.12 --with 'geopandas<1' --with matplotlib build/maps/ch02_maps.py

Coastlines are Natural Earth (public domain), as bundled with geopandas 0.x.
Output: chapters/02-everywhere/images/migration_map.png and pacific_map.png
"""
import os, warnings
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPoly
from matplotlib import patheffects as pe
from shapely.geometry import box
from shapely.affinity import translate
warnings.filterwarnings("ignore")
import geopandas as gpd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "chapters", "02-everywhere", "images")
INK, PAPER, SOFT, ACC = "#2f2a26", "#faf6ee", "#8a8178", "#b5523b"
LAND, SEA, SHORE = "#e4d8bd", "#f3eee2", "#a89c86"
plt.rcParams["font.family"] = ["P052", "serif"]
HALO = [pe.withStroke(linewidth=3.2, foreground=PAPER)]

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
world = world[world.name != "Antarctica"]
LANDMASS = world.geometry.buffer(0.01).unary_union   # one shape, so no modern borders are drawn


def land(ax, west):
    """Draw the continents on a map whose left edge is longitude `west` (plain degrees, 360 wide)."""
    for geom in [LANDMASS]:
        east_part = geom.intersection(box(west, -90, 180, 90))
        west_part = translate(geom.intersection(box(-180, -90, west, 90)), xoff=360)
        for part in (east_part, west_part):
            polys = getattr(part, "geoms", [part])
            for p in polys:
                if p.is_empty or p.geom_type != "Polygon":
                    continue
                ax.add_patch(MplPoly(np.array(p.exterior.coords), closed=True, fc=LAND, ec=SHORE, lw=0.5, zorder=1))


def L(lon, west):
    """A longitude moved onto the map."""
    return lon + 360 if lon < west else lon


def smooth(pts, n=24):
    """A Catmull-Rom curve through the points."""
    p = np.array(pts, float)
    p = np.vstack([p[0], p, p[-1]])
    out = []
    for i in range(1, len(p) - 2):
        for t in np.linspace(0, 1, n, endpoint=False):
            a, b, c, d = p[i - 1], p[i], p[i + 1], p[i + 2]
            out.append(0.5 * ((2 * b) + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t * t + (-a + 3 * b - 3 * c + d) * t ** 3))
    out.append(p[-2])
    return np.array(out)


def route(ax, pts, west, lw=2.6, colour=ACC):
    c = smooth([(L(x, west), y) for x, y in pts])
    ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=lw + 2.2, solid_capstyle="round", zorder=3)
    ax.plot(c[:-3, 0], c[:-3, 1], color=colour, lw=lw, solid_capstyle="round", zorder=4)
    ax.annotate("", xy=c[-1], xytext=c[-6], zorder=5,
                arrowprops=dict(arrowstyle="-|>,head_width=0.34,head_length=0.7", color=colour, lw=lw, shrinkA=0, shrinkB=0))


def date(ax, lon, lat, text, west, size=13):
    ax.text(L(lon, west), lat, text, ha="center", va="center", fontsize=size, color=INK, fontweight="bold", zorder=7,
            bbox=dict(boxstyle="round,pad=0.28", fc=PAPER, ec=INK, lw=0.9))


def name(ax, lon, lat, text, west, size=10.5, ha="center", colour=SOFT, style="italic"):
    ax.text(L(lon, west), lat, text, ha=ha, va="center", fontsize=size, color=colour, style=style, zorder=6, path_effects=HALO)


def dot(ax, lon, lat, west, r=5):
    ax.plot(L(lon, west), lat, "o", ms=r, mfc=INK, mec=PAPER, mew=1, zorder=6)


def frame(west, east, south, north, width=16.0):
    h = width * (north - south) / (east - west)
    fig = plt.figure(figsize=(width, h), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(west, east); ax.set_ylim(south, north)
    ax.set_facecolor(SEA); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_edgecolor(INK); s.set_linewidth(1.6)
    land(ax, west)
    return fig, ax


# ---------------------------------------------------------------- the world
def world_map():
    W = -25
    fig, ax = frame(W, W + 360, -58, 78)
    # out of Africa, along the southern coast of Asia, and across the straits to Australia
    route(ax, [(36, 3), (41, 10), (45, 13.5), (55, 18.5), (61, 24.5), (70, 21), (76, 11), (83, 15), (92, 21),
               (99, 12), (104, 2), (112, -6.5), (123, -9.5), (131, -13.5), (134, -23)], W)
    # north along the Nile, into Europe
    route(ax, [(36, 3), (33, 15), (32, 26), (35, 32.5), (33, 38.5), (25, 43), (14, 46.5), (3, 46)], W)
    # across Asia to Siberia, over the land bridge and down the Americas
    route(ax, [(57, 25), (62, 36), (74, 45), (92, 53), (112, 60), (138, 66), (166, 67.5), (-168, 66), (-150, 63.5),
               (-128, 54), (-115, 43), (-107, 34), (-100, 22), (-88, 14), (-78, 3), (-72, -14), (-70, -30), (-72.5, -41)], W)
    # east Asia
    route(ax, [(101, 14), (107, 22), (114, 31), (120, 39)], W, lw=2.0)
    # the Pacific, much later
    P = "#5d6d7e"
    route(ax, [(124, 4), (138, -1), (152, -6), (166, -13), (178, -17.5), (-172, -14)], W, lw=2.0, colour=P)
    route(ax, [(-172, -14), (-160, -17), (-149.5, -17.5)], W, lw=2.0, colour=P)
    route(ax, [(-149.5, -17.5), (-151, 0), (-155.5, 19)], W, lw=2.0, colour=P)
    route(ax, [(-149.5, -17.5), (-130, -24), (-110.5, -27)], W, lw=2.0, colour=P)
    route(ax, [(-149.5, -17.5), (-165, -29), (178, -38.5)], W, lw=2.0, colour=P)

    for lon, lat in [(-155.5, 19.6), (-109.4, -27.1), (-149.5, -17.5), (178, -17.8), (-172, -13.8)]:
        dot(ax, lon, lat, W, r=4)

    date(ax, 22, 2, "300", W)
    date(ax, 47, 5, "70–50", W)
    date(ax, 10, 53, "45", W)
    date(ax, 121, -26, "50", W)
    date(ax, 118, 68.5, "30", W)
    date(ax, -122, 36, "20", W)
    date(ax, -58, -44, "14", W)
    date(ax, 172, -8, "3", W)
    date(ax, -143, -9, "1", W)
    date(ax, -168, 22, "0.8", W)
    date(ax, -98, -30, "0.8", W)
    date(ax, 162, -43, "0.7", W)

    name(ax, 20, 12, "AFRICA", W, size=13)
    name(ax, 85, 38, "ASIA", W, size=13)
    name(ax, 22, 59, "EUROPE", W, size=11)
    name(ax, 134, -30.5, "AUSTRALIA", W, size=11)
    name(ax, -100, 50, "NORTH\nAMERICA", W, size=11)
    name(ax, -57, -12, "SOUTH\nAMERICA", W, size=11)
    name(ax, -168, 60, "the land\nbridge", W, size=9.5)
    name(ax, -106, 28.5, "New Mexico", W, size=9.5, ha="left")
    name(ax, -150, 27, "Hawaii", W, size=9.5)
    name(ax, -109, -22, "Easter Island", W, size=9.5)
    name(ax, 177, -47.5, "New Zealand", W, size=9.5)
    name(ax, -150, -24, "Tahiti", W, size=9.5)
    name(ax, -150, 2, "P A C I F I C   O C E A N", W, size=10.5)

    # key
    ax.add_patch(plt.Rectangle((W + 6, -55), 96, 22, fc=PAPER, ec=INK, lw=1, zorder=8))
    ax.text(W + 10, -38.5, "First arrival, in thousands of years ago", fontsize=12.5, color=INK, fontweight="bold", va="center", zorder=9)
    ax.plot([W + 10, W + 22], [-45, -45], color=ACC, lw=2.6, zorder=9)
    ax.text(W + 25, -45, "on foot and along the coasts, in the ice age", fontsize=11, color=INK, va="center", zorder=9)
    ax.plot([W + 10, W + 22], [-50.5, -50.5], color=P, lw=2.0, zorder=9)
    ax.text(W + 25, -50.5, "by sailing canoe, in the last 3,000 years", fontsize=11, color=INK, va="center", zorder=9)
    fig.savefig(os.path.join(OUT, "migration_map.png"), dpi=100)
    plt.close(fig)


# ---------------------------------------------------------------- the Pacific
def pacific_map():
    W = 95
    fig, ax = frame(W, W + 205, -54, 36, width=16.0)
    islands = {  # name: (lon, lat, label dx, label dy, ha)
        "Fiji": (178, -17.8, -2, 3.6, "right"), "Tonga": (-175.2, -21.2, -1, -4.2, "center"),
        "Samoa": (-172, -13.8, 0, 3.8, "center"), "Tahiti": (-149.5, -17.5, 0, -4.2, "center"),
        "Marquesas": (-139.5, -9.5, 3, 2.8, "left"), "Hawaii": (-155.5, 19.6, 0, 4.2, "center"),
        "Easter Island": (-109.4, -27.1, 0, -4.2, "center"),
    }
    P = ACC
    # the first stage, about 3,000 years ago
    route(ax, [(122, 14), (128, 4), (140, -2), (152, -5), (162, -10), (168, -16), (178, -17.8)], W, lw=2.8, colour=P)
    route(ax, [(178, -17.8), (-177, -17), (-172.5, -14.3)], W, lw=2.4, colour=P)
    route(ax, [(178, -17.8), (-178, -20.5), (-175.6, -21)], W, lw=2.4, colour=P)
    # the open ocean, from about 1,000 years ago
    route(ax, [(-172, -13.8), (-165, -18), (-159.8, -21), (-154, -19), (-150, -17.6)], W, lw=2.8, colour=P)
    route(ax, [(-149.5, -17.5), (-144, -13), (-140, -9.9)], W, lw=2.4, colour=P)
    route(ax, [(-149.5, -17.5), (-152, -2), (-153, 9), (-155.2, 18.6)], W, lw=2.8, colour=P)
    route(ax, [(-149.5, -17.5), (-136, -23), (-122, -26), (-110.4, -27)], W, lw=2.8, colour=P)
    route(ax, [(-159.8, -21.2), (-168, -29), (-178, -35), (177, -38.2)], W, lw=2.8, colour=P)
    # contact with South America
    c = smooth([(L(x, W), y) for x, y in [(-139.5, -9.5), (-120, -6), (-100, -4), (-82, -3.5)]])
    ax.plot(c[:, 0], c[:, 1], color=INK, lw=1.5, ls=(0, (5, 4)), zorder=4)

    for k, (lon, lat, dx, dy, ha) in islands.items():
        dot(ax, lon, lat, W)
        name(ax, lon + dx, lat + dy, k, W, size=12, ha=ha, colour=INK, style="normal")
    name(ax, 172.5, -47, "New Zealand", W, size=12, colour=INK, style="normal")
    name(ax, 134, -25, "AUSTRALIA", W, size=13)
    name(ax, 143, -6.2, "New Guinea", W, size=10.5)
    name(ax, 117, 22, "Taiwan", W, size=10.5, ha="right")
    name(ax, 111, 5, "islands of\nsouth-east\nAsia", W, size=10.5)
    name(ax, -70, -12, "SOUTH\nAMERICA", W, size=13)
    name(ax, -99, 28, "NORTH\nAMERICA", W, size=13)
    name(ax, -128, 5, "P A C I F I C   O C E A N", W, size=12)
    name(ax, -103, -0.5, "sweet potato", W, size=10.5, colour=INK)

    date(ax, 166, -4.5, "about 3,000\nyears ago", W, size=12)
    date(ax, -150, -26, "about 1,000", W, size=12)
    date(ax, -171, 12, "about 800", W, size=12)
    date(ax, -124, -32.5, "about 800", W, size=12)
    date(ax, 160, -37, "about 700", W, size=12)

    ax.add_patch(plt.Rectangle((W + 4, -51.5), 62, 12, fc=PAPER, ec=INK, lw=1, zorder=8))
    ax.text(W + 7, -43, "The settlement of the Pacific", fontsize=13.5, color=INK, fontweight="bold", va="center", zorder=9)
    ax.text(W + 7, -48, "first arrivals, in years before today", fontsize=11.5, color=INK, va="center", zorder=9, style="italic")
    fig.savefig(os.path.join(OUT, "pacific_map.png"), dpi=100)
    plt.close(fig)


world_map()
pacific_map()
print("maps written to", OUT)
