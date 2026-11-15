#!/usr/bin/env python3
"""Chapter 36: a plan of a typical manor about 1100, seen from above. Not a real place: a diagram, drawn in
the same colours, fonts and line weights as the maps. The castle (a mound with a tower, a ditch round it
and a fenced yard beside it), the village street with its houses and church, the three great open
fields, each divided into blocks of long narrow strips and labelled with this year's use, the lord's own
land, the watermill on the stream, the meadow, the common pasture and the woodland. A few strips are
picked out to show that one family's holding lay scattered through all three fields.

After the usual textbook plans of an open-field manor (as in English Wikipedia's article "Open-field
system"), simplified.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPoly, Circle, Rectangle, Ellipse, FancyBboxPatch
from shapely.geometry import Polygon, LineString, box
import lib
from lib import INK, PAPER, SOFT, ACC, LAND, SEA, SHORE, WATER, FILL, HALO, smooth

W, H = 160.0, 112.0
fig = plt.figure(figsize=(16, 16 * H / W), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal")
ax.set_xticks([]); ax.set_yticks([])
ax.set_facecolor(LAND)
for s in ax.spines.values():
    s.set_edgecolor(INK); s.set_linewidth(1.8)

rng = np.random.default_rng(7)


def text(x, y, s, fs=19, bold=False, colour=INK, style="normal", ha="center", rot=0, z=9):
    ax.text(x, y, s, fontsize=max(15, fs), ha=ha, va="center", color=colour, fontweight="bold" if bold else "normal",
            style=style, rotation=rot, zorder=z, path_effects=HALO, linespacing=1.1)


def area(pts, colour, alpha=0.35, edge=True, z=1.5, smooth_it=True):
    xy = smooth(pts, n=10, closed=True) if smooth_it else np.array(pts, float)
    ax.add_patch(MplPoly(xy, closed=True, fc=FILL.get(colour, colour), ec="none", alpha=alpha, zorder=z))
    if edge:
        ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=FILL.get(colour, colour), lw=1.8, alpha=0.95, zorder=z + 0.1))
    return Polygon(xy).buffer(0)


def strips(poly, block, angle, gap=1.8, colour=SHORE, lw=1.0, pick=()):
    """Parallel strip boundaries across one block (a furlong) of a field, clipped to the field.
    pick: indexes of strips to fill as one family's holding."""
    b = box(*block).intersection(poly)
    if b.is_empty:
        return
    cx, cy = (block[0] + block[2]) / 2, (block[1] + block[3]) / 2
    a = np.radians(angle)
    d = np.array([np.cos(a), np.sin(a)])           # along the strips
    nrm = np.array([-d[1], d[0]])                  # across them
    L = 200
    ks = np.arange(-60, 61)
    for k in ks:
        p0 = np.array([cx, cy]) + nrm * k * gap
        ln = LineString([p0 - d * L, p0 + d * L]).intersection(b)
        for g in getattr(ln, "geoms", [ln]):
            if g.is_empty or g.geom_type != "LineString":
                continue
            xy = np.array(g.coords)
            ax.plot(xy[:, 0], xy[:, 1], color=colour, lw=lw, zorder=2.2, solid_capstyle="butt")
    for k in pick:
        p0 = np.array([cx, cy]) + nrm * k * gap
        band = Polygon([p0 - d * L, p0 + d * L, p0 + d * L + nrm * gap, p0 - d * L + nrm * gap]).intersection(b)
        for g in getattr(band, "geoms", [band]):
            if g.geom_type == "Polygon" and not g.is_empty:
                ax.add_patch(MplPoly(np.array(g.exterior.coords), closed=True, fc=ACC, ec=INK, lw=0.8, alpha=0.9,
                                     zorder=2.4))
    # the block edge: a headland, where the plough turned
    for g in getattr(b, "geoms", [b]):
        if g.geom_type == "Polygon":
            ax.add_patch(MplPoly(np.array(g.exterior.coords), closed=True, fc="none", ec=SOFT, lw=1.6, zorder=2.3))


def trees(region, n, r=1.9):
    minx, miny, maxx, maxy = region.bounds
    placed = 0
    pts = []
    while placed < n:
        x, y = rng.uniform(minx, maxx), rng.uniform(miny, maxy)
        if not region.buffer(-r).contains(Polygon([(x, y), (x + 0.01, y), (x, y + 0.01)])):
            continue
        if any((x - a) ** 2 + (y - b) ** 2 < (2.0 * r) ** 2 for a, b in pts):
            continue
        pts.append((x, y))
        placed += 1
    for x, y in sorted(pts, key=lambda p: -p[1]):
        ax.add_patch(Circle((x, y), r, fc=FILL["green"], ec="#4d6e49", lw=1.0, alpha=0.95, zorder=2.6))


# ---------------------------------------------------------------- woodland, pasture, meadow, stream
wood_n = area([(-2, 98), (40, 101), (80, 99), (118, 101), (128, 114), (-2, 114)], "green", alpha=0.25, edge=False)
wood_e = area([(142, -2), (162, -2), (162, 46), (150, 44), (141, 30), (139, 12)], "green", alpha=0.25, edge=False)
trees(wood_n, 70)
trees(wood_e, 26)

pasture = area([(132, 50), (147, 49), (162, 52), (162, 114), (134, 114), (131, 96), (133, 72)], "olive", alpha=0.22,
               edge=False)
for i in range(46):                                   # tufts of rough grass
    x, y = rng.uniform(136, 158), rng.uniform(54, 92)
    ax.plot([x - 0.6, x, x + 0.6], [y, y + 1.0, y], color="#7b7a3c", lw=1.1, zorder=2.2)

meadow = area([(113, -2), (138, -2), (137, 20), (134, 38), (130, 45), (117, 44), (112, 30), (110, 10)], "teal",
              alpha=0.20, edge=False)
for i in range(40):
    x, y = rng.uniform(112, 136), rng.uniform(2, 40)
    if meadow.buffer(-1).contains(Polygon([(x, y), (x + .01, y), (x, y + .01)])):
        ax.plot([x - 0.5, x + 0.5], [y, y], color=FILL["teal"], lw=1.6, zorder=2.2)
        ax.plot([x - 0.3, x, x + 0.3], [y + 0.3, y + 1.0, y + 0.3], color=FILL["teal"], lw=1.0, zorder=2.2)

stream = smooth([(126, 114), (127, 100), (124, 88), (128, 74), (126, 62), (124, 52), (125, 40), (122, 26), (125, 12),
                 (123, -2)], n=12)
ax.plot(stream[:, 0], stream[:, 1], color=PAPER, lw=11, zorder=3, solid_capstyle="round")
ax.plot(stream[:, 0], stream[:, 1], color=WATER, lw=7, zorder=3.1, solid_capstyle="round")

# the mill: a pond held back above the mill, and the mill house with its wheel
ax.add_patch(Ellipse((125.0, 53.5), 7.0, 5.0, fc=SEA, ec=WATER, lw=2.4, zorder=3.2))
ax.add_patch(Rectangle((118.0, 44.4), 5.2, 4.6, fc=FILL["brown"], ec=INK, lw=1.4, zorder=4))
ax.add_patch(Circle((124.2, 46.7), 2.0, fc=PAPER, ec=INK, lw=1.6, zorder=4.1))
for a in np.linspace(0, np.pi, 4, endpoint=False):
    ax.plot([124.2 - 2 * np.cos(a), 124.2 + 2 * np.cos(a)], [46.7 - 2 * np.sin(a), 46.7 + 2 * np.sin(a)],
            color=INK, lw=1.0, zorder=4.2)

# ---------------------------------------------------------------- the three fields
west = area([(3, 6), (40, 5), (43, 36), (44, 66), (38, 92), (3, 92)], "gold", alpha=0.30)
north = area([(44, 76), (78, 77), (114, 76), (117, 94), (78, 96), (42, 94)], "olive", alpha=0.30)
south = area([(46, 4), (78, 3), (108, 4), (109, 18), (106, 29), (76, 30), (48, 29)], "brown", alpha=0.22)

strips(west, (0, 0, 44, 30), 0, pick=(2,))
strips(west, (0, 30, 22, 66), 90)
strips(west, (22, 30, 46, 66), 0)
strips(west, (0, 66, 46, 96), 90, pick=(5,))
strips(north, (40, 70, 70, 100), 0)
strips(north, (70, 70, 96, 100), 90, pick=(-3,))
strips(north, (96, 70, 120, 100), 0)
strips(south, (44, 0, 74, 40), 90)
strips(south, (74, 0, 112, 18), 0, pick=(-3,))
strips(south, (74, 18, 112, 40), 0)

# ---------------------------------------------------------------- the lord's own land, by the castle
lord = area([(48, 56.5), (66, 56), (74, 57.5), (74, 72.5), (48, 73)], "red", alpha=0.25, smooth_it=False)
strips(lord, (46, 52, 76, 74), 90, gap=3.0, colour=FILL["red"], lw=1.0)

# ---------------------------------------------------------------- the castle: mound, ditch, tower, yard
MX, MY = 100.0, 65.2
yard = smooth([(77.5, 58.0), (88, 57.0), (93.0, 59.5), (93.0, 70.5), (88, 72.5), (77.5, 72.0), (76.5, 65.0)], n=8,
              closed=True)
ax.add_patch(MplPoly(yard, closed=True, fc="#ddd1b4", ec="none", zorder=3.3))
ax.add_patch(MplPoly(yard, closed=True, fc="none", ec=INK, lw=2.6, ls=(0, (1.2, 0.6)), zorder=3.4))   # fence
for x, y, w, h in ((80.0, 67.6, 8.0, 3.0), (79.0, 58.8, 3.6, 2.4), (87.6, 58.8, 3.4, 2.4)):            # hall, stables
    ax.add_patch(Rectangle((x, y), w, h, fc="#bfa98a", ec=INK, lw=1.2, zorder=3.5))
ax.add_patch(Circle((MX, MY), 9.0, fc=WATER, ec="none", alpha=0.45, zorder=3.3))                     # ditch
ax.add_patch(Circle((MX, MY), 6.6, fc="#cbb994", ec=INK, lw=1.4, zorder=3.4))                       # mound
ax.add_patch(Circle((MX, MY), 3.2, fc="#d9cba9", ec=INK, lw=2.4, ls=(0, (1.2, 0.6)), zorder=3.5))   # fence on top
ax.add_patch(Rectangle((MX - 1.6, MY - 1.6), 3.2, 3.2, fc=FILL["brown"], ec=INK, lw=1.6, zorder=3.6))  # tower
ax.plot([92.8, 93.8], [65.6, 65.4], color=INK, lw=3, zorder=3.6)                                   # bridge

# ---------------------------------------------------------------- the village
street = smooth([(42, 43.5), (60, 44.5), (80, 44.0), (100, 43.2), (117, 45.5)], n=10)
ax.plot(street[:, 0], street[:, 1], color="#cdbd9c", lw=13, zorder=3.0, solid_capstyle="round")
ax.plot(street[:, 0], street[:, 1], color="#e7dcc3", lw=10, zorder=3.05, solid_capstyle="round")
for x in np.arange(46, 113, 6.2):                       # houses with their garden plots
    for side in (1, -1):
        if side == -1 and 58 <= x <= 72:
            continue                                     # the churchyard
        yc = np.interp(x, street[:, 0], street[:, 1]) + side * 4.3
        gy = yc + side * 1.6 if side == 1 else yc - 6.2
        ax.add_patch(Rectangle((x - 2.6, gy), 5.2, 4.6 if side == 1 else 4.6, fc="none", ec=SOFT, lw=1.0, zorder=3.1))
        ax.add_patch(Rectangle((x - 1.7, yc - 1.1), 3.4, 2.2, fc="#bfa98a", ec=INK, lw=1.1, zorder=3.2))
# church and churchyard
ax.add_patch(Rectangle((58.0, 31.0), 14.0, 6.6, fc="#ddd1b4", ec=SOFT, lw=1.4, zorder=3.1))
ax.add_patch(Rectangle((61.0, 32.7), 8.4, 3.2, fc="#a99a84", ec=INK, lw=1.4, zorder=3.3))
ax.add_patch(Rectangle((59.0, 33.1), 2.4, 2.4, fc="#a99a84", ec=INK, lw=1.4, zorder=3.3))
ax.plot([65.2, 65.2], [33.1, 35.5], color=PAPER, lw=1.6, zorder=3.4)
ax.plot([63.8, 66.6], [34.3, 34.3], color=PAPER, lw=1.6, zorder=3.4)

# ---------------------------------------------------------------- labels
text(21, 50, "WEST FIELD", fs=22, bold=True)
text(21, 44.5, "sown in autumn:\nwheat or rye", fs=18)
text(79, 89.5, "NORTH FIELD", fs=22, bold=True)
text(79, 83.5, "sown in spring: oats, peas and beans", fs=18)
text(77, 19.5, "SOUTH FIELD", fs=22, bold=True)
text(77, 13.5, "resting this year", fs=18)
text(61, 63.5, "the lord's\nown land", fs=18)
text(110.3, 69.8, "castle mound\nand tower", fs=17, ha="left")
text(85.0, 63.6, "castle yard", fs=17)
text(110.3, 60.6, "ditch", fs=16, ha="left")
text(65, 27.0, "church", fs=17)
text(89.6, 43.75, "village street", fs=16, style="italic")
text(120.5, 40.6, "watermill", fs=17)
text(126.5, 22, "meadow", fs=19, style="italic", rot=0)
text(145.5, 76, "common\npasture", fs=20, style="italic")
text(60, 106, "woodland", fs=21, style="italic")
text(151, 22, "woodland", fs=18, style="italic", rot=90)
text(129.5, 88, "stream", fs=17, style="italic", colour="#5d7686", rot=-80)

# one family's strips
ax.add_patch(Rectangle((0.6, 0.0), 58.0, 4.8, fc=PAPER, ec=INK, lw=1.2, zorder=8.8))
ax.add_patch(Rectangle((2.0, 1.2), 3.2, 2.4, fc=ACC, ec=INK, lw=0.8, zorder=9))
text(6.2, 2.4, "one family's strips, scattered through all three fields", fs=16, ha="left")

fig.savefig(lib.ROOT + "/chapters/36-castles/images/plan_manor.png", dpi=100)
print("wrote plan_manor.png")
