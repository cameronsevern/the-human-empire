#!/usr/bin/env python3
"""Chapter 96: South Africa under apartheid: the ten "homelands" (the four declared independent, Transkei,
Bophuthatswana, Venda and Ciskei, and the six others), Cape Town and Robben Island, Johannesburg, Pretoria,
Durban and Natal; inset: the country round Johannesburg, with Soweto and Sharpeville.

Drawn for this chapter, which had no map. The homelands are traced from the Wikimedia Commons map "Bantustans
in South Africa.svg" (outlines sampled from its paths: data/ch96_homelands_svg.txt), fitted to longitude and
latitude by least squares on the extreme points of South Africa (the mouth of the Orange, Kosi Bay, Cape
Agulhas), Lesotho and Swaziland; the fit is good to about a tenth of a degree, so the homelands are roughly
placed, and the smallest pieces are left out. The borders of the neighbouring states are Natural Earth
admin-0 (110 m, as shipped with geopandas). Positions from English Wikipedia.
"""
import os
import numpy as np
import geopandas as gpd
import matplotlib.image as mpimg
from shapely.geometry import Polygon
from shapely.ops import unary_union
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
SCRATCH = os.environ.get("SCRATCH", "/tmp")

# ------------------------------------------------------------------ fit SVG pixels to degrees
full = [((25.1, 371.9), (16.45, -28.63)), ((782.0, 278.6), (32.89, -26.86)), ((200.8, 685.9), (20.00, -34.83))]
lon_only = [((506.7, 412.7), 27.01), ((617.7, 399.6), 29.46), ((684.9, 264.9), 30.79), ((746.8, 275.1), 32.14)]
lat_only = [((582.2, 358.3), -28.57), ((555.2, 466.8), -30.68), ((716.8, 215.2), -25.72), ((737.0, 299.7), -27.32)]
row = lambda x, y: [x / 1000, y / 1000, 1.0]
A_lon = np.array([row(*p) for p, _ in full] + [row(*p) for p, _ in lon_only])
b_lon = np.array([ll[0] for _, ll in full] + [v for _, v in lon_only])
A_lat = np.array([row(*p) for p, _ in full] + [row(*p) for p, _ in lat_only])
b_lat = np.array([ll[1] for _, ll in full] + [v for _, v in lat_only])
k_lon, *_ = np.linalg.lstsq(A_lon, b_lon, rcond=None)
k_lat, *_ = np.linalg.lstsq(A_lat, b_lat, rcond=None)
print("fit: worst error lon %.2f, lat %.2f degrees" % (np.abs(A_lon @ k_lon - b_lon).max(), np.abs(A_lat @ k_lat - b_lat).max()))
deg = lambda x, y: (float(np.dot(row(x, y), k_lon)), float(np.dot(row(x, y), k_lat)))

homes, border_lines = {}, []
for line in open(os.path.join(lib.DATA, "ch96_homelands_svg.txt")):
    if line.startswith("#") or ":" not in line:
        continue
    name, rest = line.strip().split(":", 1)
    if name == "border":
        border_lines = [[deg(*map(float, p.split(","))) for p in piece.split()] for piece in rest.split("|")]
        continue
    g = Polygon()
    for piece in rest.split("|"):
        pts = [deg(*map(float, p.split(","))) for p in piece.split()]
        if len(pts) >= 4:
            g = g.symmetric_difference(Polygon(pts).buffer(0))
    homes[name] = g


def borders(m, lw=1.6):
    for pts in border_lines:
        xy = np.array(pts)
        m.ax.plot(xy[:, 0], xy[:, 1], color=SOFT, lw=lw, ls=(0, (5, 2.5)), zorder=2.6)


GREY = dict(size="land", colour="#5a534b", style="normal")

# ------------------------------------------------------------------ inset: round Johannesburg
I = Map(26.9, 29.0, -27.05, -25.3, width=5.6)
borders(I)
for g in homes.values():
    I.region(g, "brown", alpha=0.55)
I.city(28.05, -26.20, "Johannesburg", dx=0.07, dy=0.07, bold=True)
I.city(27.86, -26.27, "Soweto", dx=-0.07, dy=-0.03)
I.city(27.87, -26.69, "Sharpeville", dx=0.07, dy=0.0)
I.city(28.19, -25.75, "Pretoria", dx=0.07, dy=0.05)
I.label(27.15, -25.45, "BOPHUTHATSWANA", fs=15, ha="left")
I.label(28.72, -25.45, "KWA-\nNDEBELE", fs=15)
I.ax.text(0.03, 0.03, "round Johannesburg", transform=I.ax.transAxes, ha="left", va="bottom", fontsize=17,
          fontweight="bold", color=INK, zorder=9, path_effects=HALO)
pin = os.path.join(SCRATCH, "ch96_inset.png")
I.save(pin)

# ------------------------------------------------------------------ South Africa
m = Map(16.3, 33.2, -35.0, -22.0)
borders(m)
for g in homes.values():
    m.region(g, "brown", alpha=0.55)
m.ax.add_patch(lib.Rectangle((26.9, -27.05), 2.1, 1.75, fc="none", ec=INK, lw=1.4, zorder=5))

R = dict(fs=15)
for x, y, t, ha in [(28.6, -31.6, "TRANSKEI", "center"), (25.8, -32.95, "CISKEI", "right"),
                    (24.3, -25.95, "BOPHUTHATSWANA", "center"), (29.75, -22.45, "VENDA", "right"),
                    (31.65, -23.55, "GAZANKULU", "left"), (28.6, -23.75, "LEBOWA", "right"),
                    (32.35, -25.0, "KA-\nNGWANE", "center"), (31.75, -28.25, "KWAZULU", "left"),
                    (28.7, -27.8, "QWAQWA", "center"), (29.15, -25.75, "KWANDEBELE", "left")]:
    m.label(x, y, t, ha=ha, **R)
# leaders from a label to its homeland where the label stands off it
for a, b in [((29.8, -22.45), (30.45, -22.6)), ((31.62, -23.55), (31.25, -23.45)),
             ((29.13, -25.72), (28.85, -25.3)), ((28.7, -27.92), (28.65, -28.3))]:
    m.ax.plot(*zip(a, b), color=INK, lw=1.2, zorder=6.5)

m.city(18.42, -33.92, "Cape Town", dx=0.2, dy=-0.12, bold=True)
m.city(18.37, -33.80, "Robben Island", dx=-0.2, dy=0.12, r=7)
m.city(31.03, -29.86, "Durban", dx=0.2, dy=-0.15)
m.label(30.3, -29.0, "Natal", size="land", colour=INK, fs=17)
m.label(22.0, -31.0, "SOUTH AFRICA", fs=24)
m.label(28.25, -29.6, "LESOTHO", fs=15, **GREY)
m.label(31.5, -26.5, "SWAZI-\nLAND", fs=15, **GREY)
m.label(23.2, -23.1, "BOTSWANA", fs=17, **GREY)
m.label(32.55, -22.55, "MOZAM-\nBIQUE", fs=15, **GREY)
m.label(17.6, -31.5, "Atlantic\nOcean", size="sea", fs=19)
m.label(28.5, -34.0, "Indian Ocean", size="sea", fs=19)
m.key([("brown", "homeland, roughly")], loc="lower right")
m.scale(300, lon=22.0, lat=-33.4)

img = mpimg.imread(pin)
H = m.fig.get_size_inches()[1] * 100
h, w = img.shape[:2]
ia = m.fig.add_axes([10 / 1600, (H - h - 10) / H, w / 1600, h / H])
ia.imshow(img); ia.axis("off")
m.save("chapters/96-apartheid/images/map_homelands.png")
