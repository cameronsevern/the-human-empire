#!/usr/bin/env python3
"""Chapter 79: the Nazi party's share of the vote at each national (Reichstag) election from 1928 to March
1933, with the share of German workers unemployed in each year, drawn in the style of the book's maps.

Votes: the official results, as tabulated in English Wikipedia's articles on each Reichstag election
(20 May 1928, 14 September 1930, 31 July 1932, 6 November 1932, 5 March 1933).
Unemployment: registered unemployed as a share of employees, annual averages, from D. Petzina,
W. Abelshauser and A. Faust, Sozialgeschichtliches Arbeitsbuch III (1978), p. 119; the same series as the
chart in chapter 77. Each year's figure is drawn at the middle of the year.
"""
import matplotlib.pyplot as plt
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

RED = FILL["red"]
elections = [(1928 + 140 / 366, 2.6, "May\n1928"), (1930 + 256 / 365, 18.3, "Sept.\n1930"),
             (1932 + 212 / 366, 37.3, "July\n1932"), (1932 + 310 / 366, 33.1, "Nov.\n1932"),
             (1933 + 63 / 365, 43.9, "March\n1933")]
jobless = [(1928, 6.3), (1929, 8.5), (1930, 14.0), (1931, 21.9), (1932, 29.9), (1933, 25.9)]

fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.09, 0.13, 0.87, 0.77])
ax.set_facecolor(PAPER)
for x, v, when in elections:
    ax.bar(x, v, width=0.21, color=RED, alpha=0.85, ec=PAPER, lw=1.5, zorder=2)
    ax.text(x, v + 0.9, f"{v:.0f}%" if v >= 10 else f"{v}%", ha="center", va="bottom", fontsize=20,
            fontweight="bold", color=RED, path_effects=HALO, zorder=5)
xs = [y + 0.5 for y, _ in jobless]
ys = [v for _, v in jobless]
ax.plot(xs, ys, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
ax.plot(xs, ys, color=INK, lw=4.2, ls=(0, (4, 1.6)), marker="o", ms=11, mfc=INK, mec=PAPER, mew=1.6, zorder=4)
for (x, v), (dx, dy, ha) in zip(zip(xs, ys), [(0, 2.4, "center")] * 2 + [(-0.07, 1.6, "right"), (0, 2.4, "center"), (-0.1, 2.0, "right"), (0.09, 0, "left")]):
    ax.text(x + dx, v + dy, f"{int(x)}: {int(v + 0.5)}%", ha=ha, va="center", fontsize=17, color=INK, path_effects=HALO,
            zorder=5)

ax.text(1930.9, 41.0, "Nazi share of the vote,\nat each national election", fontsize=20, color=RED,
        fontweight="bold", ha="center", va="center", path_effects=HALO, zorder=5, linespacing=1.1)
ax.text(1929.0, 18.0, "share of workers\nunemployed, each year", fontsize=20, color=INK, fontweight="bold",
        ha="center", va="center", path_effects=HALO, zorder=5, linespacing=1.1)

ax.set_xlim(1927.9, 1934.1)
ax.set_ylim(0, 50)
ax.set_xticks([e[0] for e in elections])
ax.set_xticklabels([e[2] for e in elections])
ax.set_yticks(range(0, 51, 10))
ax.set_yticklabels([f"{v}%" for v in range(0, 51, 10)])
ax.tick_params(labelsize=17, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.09, 0.95, "Votes and unemployment in Germany, 1928 to 1933", fontsize=24, color=INK,
         fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/79-hitler/images/chart_votes.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
