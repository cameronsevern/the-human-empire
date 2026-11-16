#!/usr/bin/env python3
"""Chapter 102: how a pile of house loans became a top-rated bond, drawn in the style of the book's maps, in
the chapter's own words. Brokers lend to several thousand families and are paid for each loan signed; an
investment bank gathers the loans into a pool and sells the right to the monthly payments in layers; the top
layer is paid first and loses nothing unless a very large share of the borrowers stop paying, the bottom layer
takes the first losses and pays a higher return; rating agencies, paid by the banks, stamp the top layers with
the highest grade, the grade of the American government's debt; investors round the world buy the layers, the
bank keeps many itself with money borrowed for a day or a week, and an insurer guarantees them against loss.

A schematic: the number of houses and the heights of the layers are not to scale. Sequence after the chapter
and English Wikipedia's "Collateralized debt obligation" and "Mortgage-backed security".
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, FancyBboxPatch
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO, SOFT

W, H = 1600, 1080
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal"); ax.axis("off")

RED, BLUE, GOLD, GREEN = FILL["red"], FILL["blue"], FILL["gold"], FILL["green"]
T = dict(color=INK, path_effects=HALO, zorder=8, va="center")


def arrow(xy, colour=INK, lw=3.0):
    xy = np.array(xy, float)
    if len(xy) < 20:                                           # resample a polyline so the head sits on its end
        seg = [np.linspace(a, b, 20, endpoint=False) for a, b in zip(xy[:-1], xy[1:])]
        xy = np.vstack(seg + [xy[-1:]])
    ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=lw + 3, solid_capstyle="round", zorder=3)
    ax.plot(xy[:-3, 0], xy[:-3, 1], color=colour, lw=lw, solid_capstyle="round", zorder=4)
    ax.annotate("", xy=xy[-1], xytext=xy[-6], zorder=5,
                arrowprops=dict(arrowstyle="-|>,head_width=0.45,head_length=0.9", color=colour, lw=lw,
                                shrinkA=0, shrinkB=0))


def bez(p0, p1, p2, p3, n=80):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2, p3 = map(np.array, (p0, p1, p2, p3))
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def num(x, y, n):
    ax.add_patch(Circle((x, y), 17, fc=INK, ec=PAPER, lw=2, zorder=9))
    ax.text(x, y - 1, str(n), ha="center", va="center", fontsize=17, fontweight="bold", color=PAPER, zorder=10)


def note(x, y, n, text):
    num(x, y, n)
    ax.text(x + 26, y, text, ha="left", va="top", fontsize=17, linespacing=1.15, color=INK, zorder=8)


# ------------------------------------------------------------------ 1. the houses
def house(x, y, s=34):
    ax.add_patch(Polygon([(x, y), (x + s, y), (x + s, y + 0.62 * s), (x + s / 2, y + s), (x, y + 0.62 * s)],
                         closed=True, fc="#e3d6bd", ec=INK, lw=1.2, zorder=3))
    ax.add_patch(Rectangle((x + 0.4 * s, y), 0.2 * s, 0.34 * s, fc=INK, ec="none", zorder=3.1))


for i in range(7):
    for j in range(8):
        house(55 + i * 48, 330 + j * 56)
ax.text(215, 290, "several thousand loans", ha="center", fontsize=17, style="italic", **{k: v for k, v in T.items()})
note(40, 1050, 1, "Brokers lend to families\nto buy houses, and are\npaid for each loan signed")

# ------------------------------------------------------------------ 2. the pool
px0, px1, py0, py1 = 470, 680, 400, 700
ax.add_patch(FancyBboxPatch((px0, py0), px1 - px0, py1 - py0, boxstyle="round,pad=0,rounding_size=40",
                            fc="#c9d6de", ec=INK, lw=1.8, zorder=3))
ax.text((px0 + px1) / 2, (py0 + py1) / 2, "the pool", ha="center", fontsize=20, fontweight="bold", **T)
for y in (420, 545, 670):
    arrow([(398, y), (430, (y + 550) / 2), (462, 550 + (y - 545) * 0.35)], lw=2.6)
note(430, 1050, 2, "An investment\nbank gathers\nthe loans into\na pool")

# ------------------------------------------------------------------ 3. the layers
sx0, sx1 = 830, 1090
layers = [("bottom layer", 200, 300, RED), ("middle\nlayers", 300, 430, GOLD), ("top layer", 430, 760, BLUE)]
for name, y0, y1, col in layers:
    ax.add_patch(Rectangle((sx0, y0), sx1 - sx0, y1 - y0, fc=col, alpha=0.45, ec="none", zorder=2.5))
    ax.add_patch(Rectangle((sx0, y0), sx1 - sx0, y1 - y0, fc="none", ec=INK, lw=1.8, zorder=3))
ax.text((sx0 + sx1) / 2, 600, "TOP LAYER", ha="center", fontsize=19, fontweight="bold", **T)
ax.text((sx0 + sx1) / 2, 510, "paid first; loses\nnothing unless\nvery many families\nstop paying", ha="center",
        fontsize=17, linespacing=1.1, **T)
ax.text((sx0 + sx1) / 2, 365, "middle layers", ha="center", fontsize=17, fontweight="bold", **T)
ax.text((sx0 + sx1) / 2, 265, "BOTTOM LAYER", ha="center", fontsize=17, fontweight="bold", **T)
ax.text((sx0 + sx1) / 2, 228, "takes the first losses;\npays more", ha="center", fontsize=15, linespacing=1.0, **T)

# monthly payments: from the pool, over the top, into the top layer
arrow(bez((575, 705), (590, 860), (930, 880), (960, 772)), colour=GREEN, lw=3.4)
ax.text(760, 868, "monthly payments", ha="center", fontsize=17, style="italic", color=GREEN, path_effects=HALO,
        zorder=8, va="center")
# money down the right side, top first; losses up the left side, bottom first
arrow([(1112, 740), (1112, 470), (1112, 215)], colour=GREEN, lw=3.0)
ax.text(1134, 480, "paid out from the top down", rotation=-90, ha="center", fontsize=17, style="italic", color=GREEN,
        path_effects=HALO, zorder=8, va="center", linespacing=1.1)
arrow([(808, 215), (808, 470), (808, 745)], colour=RED, lw=3.0)
ax.text(786, 300, "losses\nstrike from\nthe bottom\nup", ha="right", fontsize=17, style="italic", color="#8a3b2a",
        path_effects=HALO, zorder=8, va="center", linespacing=1.1)

# the stamp of the rating agencies on the top layer
cx, cy = 1012, 690
ax.add_patch(Circle((cx, cy), 64, fc=PAPER, ec="#8a3b2a", lw=3.2, zorder=6))
ax.add_patch(Circle((cx, cy), 56, fc="none", ec="#8a3b2a", lw=1.4, zorder=6))
ax.text(cx, cy, "HIGHEST\nGRADE", ha="center", va="center", fontsize=15, fontweight="bold", color="#8a3b2a",
        rotation=12, linespacing=1.0, zorder=7)
note(800, 1050, 3, "It sells the right to the payments\nin layers. Rating agencies, paid\nby the banks, give the top layers\nthe highest grade, the grade of\nthe American government's debt")

# ------------------------------------------------------------------ 4. the buyers
bx = 1310
buyers = ["pension funds\nin Norway", "banks in\nGermany", "town councils\nin Australia",
          "the investment bank\nitself, with money\nborrowed for a\nday or a week"]
ys = [720, 610, 500, 360]
for text, y in zip(buyers, ys):
    arrow([(1160, 520), (1225, (520 + y) / 2), (bx - 14, y)], lw=2.4)
    ax.text(bx, y, text, ha="left", fontsize=17, linespacing=1.1, **T)
note(1250, 1050, 4, "Investors all over\nthe world buy the\nlayers as bonds")
ax.add_patch(FancyBboxPatch((1240, 80), 330, 120, boxstyle="round,pad=6,rounding_size=10", fc=PAPER, ec=INK,
                            lw=1.4, zorder=6))
num(1262, 178, 5)
ax.text(1290, 140, "An insurance company\nguarantees the bonds,\nand sets nothing aside", ha="left", fontsize=17,
        linespacing=1.1, **T)
ax.text(1590, 25, "not to scale", ha="right", fontsize=17, style="italic", **T)

out = lib.os.path.join(lib.ROOT, "chapters/102-crash/images/diagram_mortgage_bond.png")
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
