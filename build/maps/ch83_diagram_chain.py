#!/usr/bin/env python3
"""Chapter 83: a chain reaction, drawn in the style of the book's maps. A neutron strikes a uranium nucleus,
which splits in two, releases energy and throws out two neutrons; each of those splits another nucleus, and
so on: one split, then two, then four, and eight neutrons going on. (A real fission gives off two or three
neutrons; two keeps the picture simple and matches the doubling described in the text.)
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

W, H = 1600, 900
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal"); ax.axis("off")

FLASH, FRAG, NEUT = "#f1d48a", FILL["brown"], INK


def split(x, y):
    """A nucleus at the moment of splitting: a burst of energy and two fragments flying apart."""
    a = np.linspace(0, 2 * np.pi, 25)[:-1]
    r = np.where(np.arange(24) % 2 == 0, 82, 52)
    ax.add_patch(Polygon(np.c_[x + r * np.cos(a), y + r * np.sin(a)], closed=True, fc=FLASH, ec="#d9a441",
                         lw=1.6, zorder=2))
    for dx, dy in [(-20, 17), (20, -17)]:
        ax.add_patch(Circle((x + dx, y + dy), 30, fc=FRAG, ec=PAPER, lw=2.2, zorder=3))


def neutron(x0, y0, x1, y1, gap0=70, gap1=70):
    """A neutron flying from one point to the next: a dot and an arrow."""
    v = np.array([x1 - x0, y1 - y0], float)
    d = np.hypot(*v); u = v / d
    a, b = np.array([x0, y0]) + u * gap0, np.array([x1, y1]) - u * gap1
    ax.annotate("", xy=b, xytext=a, zorder=4,
                arrowprops=dict(arrowstyle="-|>,head_width=0.45,head_length=0.9", color=INK, lw=2.6,
                                shrinkA=0, shrinkB=0))
    m = a + (b - a) * 0.42
    ax.add_patch(Circle(m, 10, fc=NEUT, ec=PAPER, lw=1.8, zorder=5))


g1 = [(430, 450)]
g2 = [(800, 250), (800, 650)]
g3 = [(1170, 140), (1170, 350), (1170, 550), (1170, 760)]
for p in g1 + g2 + g3:
    split(*p)
neutron(70, 450, *g1[0], gap0=0, gap1=88)
for i, p in enumerate(g2):
    neutron(*g1[0], *p, gap1=88)
for i, p in enumerate(g3):
    neutron(*g2[i // 2], *p, gap1=88)
for x, y in g3:
    for dy in (-62, 62):
        neutron(x, y, 1395, y + dy * 0.85, gap0=80, gap1=0)

T = dict(color=INK, path_effects=HALO, zorder=7, va="center")
for x, text in [(430, "1 split"), (800, "2 splits"), (1170, "4 splits"), (1470, "8 neutrons")]:
    ax.text(x, 868, text, fontsize=22, fontweight="bold", ha="center", **T)
ax.text(95, 505, "a neutron", fontsize=19, ha="left", **T)
ax.text(430, 300, "a uranium nucleus\nsplits in two,\ngiving off energy\nand two neutrons", fontsize=19,
        ha="center", linespacing=1.15, **T)
ax.text(1500, 450, "and so on:\neighty steps\ntake about a\nmillionth of\na second", fontsize=18, ha="center",
        linespacing=1.15, **T)
out = lib.os.path.join(lib.ROOT, "chapters/83-bomb/images/diagram_chain_reaction.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
