#!/usr/bin/env python3
"""Chapter 109: how a feed is ranked, drawn in the style of the book's maps, in the chapter's own words.
Several thousand new items might be shown to one person; for each, the ranking system calculates a score, its
estimate of how likely she is to react (to click, watch to the end, press the button that signals approval,
comment, pass it on), made from the record of how she and millions of people like her have reacted to similar
things; the items are sorted by score and the top few shown; her reactions are recorded and fed back, and the
next estimate is a little better; the company's engineers tell the system what to aim for, usually more
reactions and more time spent.

A schematic: the number of items, the lengths of the score bars and the number shown are illustrative, not
measured from any real system.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Ellipse
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO, SOFT

W, H = 1600, 1000
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal"); ax.axis("off")

RED, BLUE, GOLD, GREEN = FILL["red"], FILL["blue"], FILL["gold"], FILL["green"]
CARD, PALE = "#e3d6bd", "#efe8da"
T = dict(color=INK, path_effects=HALO, zorder=8, va="center")


def num(x, y, n):
    ax.add_patch(Circle((x, y), 17, fc=INK, ec=PAPER, lw=2, zorder=9))
    ax.text(x, y - 1, str(n), ha="center", va="center", fontsize=17, fontweight="bold", color=PAPER, zorder=10)


def note(x, y, n, text):
    num(x, y, n)
    ax.text(x + 26, y + 14, text, ha="left", va="top", fontsize=17, linespacing=1.15, color=INK, zorder=8)


def arrow(xy, colour=INK, lw=3.0):
    xy = np.array(xy, float)
    seg = [np.linspace(a, b, 30, endpoint=False) for a, b in zip(xy[:-1], xy[1:])]
    xy = np.vstack(seg + [xy[-1:]])
    ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=lw + 4, solid_capstyle="round", zorder=3.5)
    ax.plot(xy[:-4, 0], xy[:-4, 1], color=colour, lw=lw, solid_capstyle="round", zorder=4)
    ax.annotate("", xy=xy[-1], xytext=xy[-8], zorder=5,
                arrowprops=dict(arrowstyle="-|>,head_width=0.5,head_length=1.0", color=colour, lw=lw,
                                shrinkA=0, shrinkB=0))


def card(x, y, w, h, fc=CARD, lw=1.0):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=INK, lw=lw, zorder=4))


# ------------------------------------------------------------------ 1. the items that might be shown
for i in range(9):
    for j in range(13):
        card(48 + i * 31, 320 + j * 33, 24, 26, fc=CARD, lw=0.8)
ax.text(185, 790, "several thousand items", ha="center", fontsize=17, style="italic", **T)
arrow([(340, 530), (405, 530)])

# ------------------------------------------------------------------ 2. a score for each
scores = [0.35, 0.82, 0.15, 0.6, 0.95, 0.25, 0.5, 0.72, 0.42]
bx0, by0, step = 420, 690, 44
ax.add_patch(FancyBboxPatch((410, 300), 320, 440, boxstyle="round,pad=0,rounding_size=16", fc="#dbe4ea", ec=INK,
                            lw=1.8, zorder=2))
ax.text(570, 770, "the ranking system", ha="center", fontsize=19, fontweight="bold", **T)


def rows(x0, ys, vals, shown=0):
    for k, (y, s) in enumerate(zip(ys, vals)):
        top = k < shown
        card(x0, y - 15, 30, 30, fc=CARD if (top or not shown) else PALE, lw=1.0)
        ax.add_patch(Rectangle((x0 + 44, y - 9), 210 * s, 18, fc=RED if (top or not shown) else "#d9b3a6",
                               ec="none", zorder=4))
        ax.add_patch(Rectangle((x0 + 44, y - 9), 210, 18, fc="none", ec=SOFT, lw=1.0, zorder=4.1))


ys = [bx0 - 10 - k * step for k in range(len(scores))]
ys = [by0 - k * step for k in range(len(scores))]
rows(bx0 + 10, ys, scores)
arrow([(740, 520), (795, 520)])
ax.text(767, 560, "sorted", ha="center", fontsize=17, style="italic", **T)

# ------------------------------------------------------------------ 3. sorted; the top few shown
sx0 = 820
ax.add_patch(FancyBboxPatch((sx0 - 12, by0 - 2 * step - 28), 290, 3 * step + 12, boxstyle="round,pad=0,rounding_size=10",
                            fc="#f3e2b5", ec=GOLD, lw=2.4, zorder=2))
rows(sx0, ys, sorted(scores, reverse=True), shown=3)
yline = by0 - 2.5 * step - 4
ax.text(sx0 + 290, by0 + 10, "shown", ha="left", fontsize=17, fontweight="bold", **T)
ax.text(sx0 + 290, by0 - 5.5 * step, "not\nshown", ha="left", fontsize=17, style="italic", color=SOFT,
        path_effects=HALO, zorder=8, va="center", linespacing=1.05)
arrow([(1115, by0 - step), (1238, by0 - step - 20)])

# ------------------------------------------------------------------ 4. her feed
px0, px1, py0, py1 = 1250, 1470, 300, 760
ax.add_patch(FancyBboxPatch((px0, py0), px1 - px0, py1 - py0, boxstyle="round,pad=0,rounding_size=28", fc=INK,
                            ec=INK, lw=1.8, zorder=2))
ax.add_patch(Rectangle((px0 + 14, py0 + 40), px1 - px0 - 28, py1 - py0 - 80, fc=PAPER, ec="none", zorder=2.5))
for k in range(3):
    y = py1 - 70 - k * 125
    card(px0 + 30, y - 85, px1 - px0 - 60, 95, fc=CARD, lw=1.0)
    for d, w in [(20, 0.8), (42, 0.6), (64, 0.7)]:
        ax.plot([px0 + 44, px0 + 44 + (px1 - px0 - 88) * w], [y - d + 0, y - d + 0], color=SOFT, lw=3, zorder=4.5)
ax.text((px0 + px1) / 2, 790, "her feed", ha="center", fontsize=19, fontweight="bold", **T)

# ------------------------------------------------------------------ the loop: reactions recorded and fed back
cx, cy, cw, ch, cd = 1010, 950, 320, 40, 120
ax.add_patch(Rectangle((cx - cw / 2, cy - cd), cw, cd, fc="#c9d6de", ec="none", zorder=2))
ax.plot([cx - cw / 2, cx - cw / 2], [cy - cd, cy], color=INK, lw=1.8, zorder=2.2)
ax.plot([cx + cw / 2, cx + cw / 2], [cy - cd, cy], color=INK, lw=1.8, zorder=2.2)
ax.add_patch(Ellipse((cx, cy - cd), cw, ch, fc="#c9d6de", ec=INK, lw=1.8, zorder=2.1))
ax.add_patch(Ellipse((cx, cy), cw, ch, fc="#dbe4ea", ec=INK, lw=1.8, zorder=2.3))
ax.text(cx, cy - 66, "the record of how she,\nand millions like her,\nreacted before", ha="center", va="center",
        fontsize=16, linespacing=1.05, color=INK, zorder=8)
arrow([(1360, 800), (1360, 880), (1185, 880)], colour=GREEN, lw=3.4)
ax.text(1376, 840, "her reactions", ha="left", fontsize=17, style="italic", color="#3f6b3a", path_effects=HALO,
        zorder=8, va="center")
arrow([(835, 880), (700, 880), (640, 792)], colour=GREEN, lw=3.4)

# the engineers set the aim
ax.add_patch(FancyBboxPatch((30, 850), 370, 110, boxstyle="round,pad=0,rounding_size=12", fc=PAPER, ec=INK,
                            lw=1.4, zorder=6))
num(52, 938, 5)
ax.text(78, 905, "The company's engineers\nset the aim: more reactions,\nmore time spent", ha="left", fontsize=17,
        linespacing=1.1, **T)
arrow([(405, 900), (470, 900), (500, 792)], lw=2.6)

# ------------------------------------------------------------------ the notes
note(40, 225, 1, "Several thousand new\nitems might be shown\nto one person")
note(410, 225, 2, "For each, a score: how likely\nshe is to click, watch to the\nend, approve, comment or\npass it on")
note(820, 225, 3, "The items are sorted\nby score, and the top\nfew are shown")
note(1210, 225, 4, "Her reactions are recorded\nand fed back; the next\nestimate is a little better")
ax.text(1590, 25, "not to scale", ha="right", fontsize=17, style="italic", **T)

out = lib.os.path.join(lib.ROOT, "chapters/109-feed/images/diagram_feed.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
