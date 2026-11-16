#!/usr/bin/env python3
"""Chapter 114: one step in training a small neural network, drawn in the style of the book's maps, in the
chapter's own words. A photograph that a person has labelled as a cat is turned into numbers, one for the
brightness of each dot; these are fed into a first layer of simple units; each unit multiplies its inputs by
numbers called weights, adds up the results, stays silent if the total is too small, and otherwise passes its
answer on to the next layer; out of the last layer comes a single number, the machine's estimate of how likely
the picture is to be a cat. The answer is compared with the label, and a piece of mathematics works backwards
through the layers, nudging each weight up or down so that the answer would have been a little less wrong. Then
the next picture is shown.

A schematic: the picture, the number of units, the brightness values, the guess of 0.3 and the nudges are
illustrative, not taken from any real network.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO, SOFT

W, H = 1600, 1000
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal"); ax.axis("off")

RED, BLUE, GOLD, GREEN = FILL["red"], FILL["blue"], FILL["gold"], FILL["green"]
UNIT = "#dbe4ea"
T = dict(color=INK, path_effects=HALO, zorder=8, va="center")


def num(x, y, n):
    ax.add_patch(Circle((x, y), 17, fc=INK, ec=PAPER, lw=2, zorder=9))
    ax.text(x, y - 1, str(n), ha="center", va="center", fontsize=17, fontweight="bold", color=PAPER, zorder=10)


def note(x, y, n, text):
    num(x, y, n)
    ax.text(x + 26, y + 14, text, ha="left", va="top", fontsize=17, linespacing=1.15, color=INK, zorder=8)


def arrow(xy, colour=INK, lw=3.0, ls="-"):
    xy = np.array(xy, float)
    seg = [np.linspace(a, b, 30, endpoint=False) for a, b in zip(xy[:-1], xy[1:])]
    xy = np.vstack(seg + [xy[-1:]])
    ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=lw + 4, solid_capstyle="round", zorder=3.5)
    ax.plot(xy[:-4, 0], xy[:-4, 1], color=colour, lw=lw, ls=ls, solid_capstyle="round", zorder=4)
    ax.annotate("", xy=xy[-1], xytext=xy[-8], zorder=5,
                arrowprops=dict(arrowstyle="-|>,head_width=0.5,head_length=1.0", color=colour, lw=lw,
                                shrinkA=0, shrinkB=0))


ax.text(40, 955, "One step in training a neural network", ha="left", fontsize=24, fontweight="bold", **T)

# ------------------------------------------------------------------ 1. the labelled picture, as dots
CAT = ["10000001", "11000011", "11111111", "12111121", "11111111", "11133111", "01111110", "00111100"]
shade = {"0": "#e9e1d2", "1": "#5a514a", "2": "#f4efe4", "3": "#b8a99a"}
cx0, cy0, cell = 70, 545, 24
for r, row in enumerate(CAT):
    for c, ch in enumerate(row[:8]):
        ax.add_patch(Rectangle((cx0 + c * cell, cy0 + (7 - r) * cell), cell - 2, cell - 2, fc=shade[ch], ec="none",
                               zorder=3))
ax.add_patch(Rectangle((cx0 - 6, cy0 - 6), 8 * cell + 10, 8 * cell + 10, fc="none", ec=INK, lw=1.4, zorder=3.5))
ax.text(cx0 + 4 * cell, cy0 + 8 * cell + 52, "a picture that a\nperson has labelled", ha="center", fontsize=17,
        linespacing=1.1, **T)
ax.add_patch(FancyBboxPatch((cx0 + 30, cy0 - 62), 136, 40, boxstyle="round,pad=0,rounding_size=8", fc="#f3e2b5",
                            ec=GOLD, lw=2, zorder=3))
ax.text(cx0 + 98, cy0 - 42, "label: cat", ha="center", fontsize=17, fontweight="bold", **T)
num(cx0 - 22, cy0 + 8 * cell + 52, 1)
arrow([(cx0 + 8 * cell + 14, 640), (360, 640)])

# ------------------------------------------------------------------ the network: three layers
L1 = [(420, y) for y in (840, 740, 640, 540, 440)]
L2 = [(700, y) for y in (790, 690, 590, 490)]
L3 = [(980, 640)]
R = 34
bright = ["0.9", "0.2", "0.1", "0.8", "0.3"]

for i, a in enumerate(L1):
    for j, b in enumerate(L2):
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#b9ad9b", lw=1.6, zorder=2)
for j, b in enumerate(L2):
    ax.plot([b[0], L3[0][0]], [b[1], L3[0][1]], color="#b9ad9b", lw=1.6, zorder=2)


def nudge(a, b, sign):
    colour = GREEN if sign == "+" else RED
    ax.plot([a[0], b[0]], [a[1], b[1]], color=colour, lw=4.2, zorder=2.5)
    m = (0.42 * a[0] + 0.58 * b[0], 0.42 * a[1] + 0.58 * b[1])
    ax.add_patch(Circle(m, 15, fc=PAPER, ec=colour, lw=2.2, zorder=6))
    ax.text(m[0], m[1] + 1, sign, ha="center", va="center", fontsize=20, fontweight="bold", color=INK, zorder=7)


nudge(L1[1], L2[0], "+")
nudge(L1[3], L2[3], "−")
nudge(L1[4], L2[1], "+")
nudge(L2[0], L3[0], "−")
nudge(L2[2], L3[0], "+")

for (x, y), v in zip(L1, bright):
    ax.add_patch(Circle((x, y), R, fc=UNIT, ec=INK, lw=1.8, zorder=5))
    ax.text(x, y, v, ha="center", fontsize=17, **T)
for x, y in L2:
    ax.add_patch(Circle((x, y), R, fc=UNIT, ec=INK, lw=1.8, zorder=5))
ax.add_patch(Circle(L3[0], R + 6, fc="#f3e2b5", ec=INK, lw=2.2, zorder=5))
ax.text(L3[0][0], L3[0][1], "0.3", ha="center", fontsize=19, fontweight="bold", **T)
ax.text(420, 395, "…", ha="center", fontsize=22, **T)

ax.text(420, 905, "first layer", ha="center", fontsize=19, fontweight="bold", **T)
ax.text(700, 905, "next layer", ha="center", fontsize=19, fontweight="bold", **T)
ax.text(980, 905, "last layer", ha="center", fontsize=19, fontweight="bold", **T)
ax.text(560, 868, "weights", ha="center", fontsize=17, style="italic", **T)
num(762, 840, 2)
num(980, 712, 3)

# ------------------------------------------------------------------ 4. compared with the label
arrow([(1026, 640), (1100, 640)])
bx, by, bw, bh = 1110, 500, 450, 280
ax.add_patch(FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0,rounding_size=14", fc="#efe8da", ec=INK,
                            lw=1.6, zorder=2))
num(bx + 30, by + bh - 34, 4)
ax.text(bx + 60, by + bh - 34, "compared with the label", ha="left", fontsize=19, fontweight="bold", **T)
ax.text(bx + 30, by + 175, "the guess:", ha="left", fontsize=18, **T)
ax.text(bx + 210, by + 175, "0.3", ha="left", fontsize=18, fontweight="bold", **T)
ax.text(bx + 30, by + 120, "the label:", ha="left", fontsize=18, **T)
ax.text(bx + 210, by + 120, "1 (it is a cat)", ha="left", fontsize=18, fontweight="bold", **T)
ax.plot([bx + 30, bx + bw - 30], [by + 88, by + 88], color=INK, lw=1.2, zorder=3)
ax.text(bx + 30, by + 52, "the error:", ha="left", fontsize=18, **T)
ax.text(bx + 210, by + 52, "0.7 too low", ha="left", fontsize=18, fontweight="bold", color="#8a3b2a",
        path_effects=HALO, zorder=8, va="center")

# ------------------------------------------------------------------ 5. backwards, nudging every weight
arrow([(1300, 490), (1300, 360), (560, 360), (560, 425)], colour=RED, lw=3.4, ls=(0, (4, 2.4)))
num(1210, 360, 5)
ax.text(810, 325, "working backwards through the layers, every weight is nudged up (+) or down (−)",
        ha="center", fontsize=17, style="italic", **T)

# ------------------------------------------------------------------ the notes
note(30, 245, 1, "The picture is turned\ninto numbers, one for\nthe brightness of\neach dot")
note(345, 245, 2, "Each unit multiplies its\ninputs by its weights,\nadds them up and, if the\ntotal is big enough,\npasses it on")
note(680, 245, 3, "Out of the last layer\ncomes a guess: how\nlikely the picture is\nto be a cat")
note(985, 245, 4, "The guess is\ncompared with\nthe label: here\nit is too low")
note(1255, 245, 5, "Every weight is nudged\nto make the answer a\nlittle less wrong.\nThen the next picture")
ax.text(1590, 18, "illustrative numbers; real networks have millions of weights", ha="right", fontsize=16,
        style="italic", **T)

out = lib.os.path.join(lib.ROOT, "chapters/114-machines/images/diagram_network.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
