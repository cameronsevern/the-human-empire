#!/usr/bin/env python3
"""Chapter 111: carbon dioxide in the air, from the year 1000 to 2025, drawn in the style of the book's maps: the
air in bubbles in the Antarctic ice (Law Dome) from 1000 to 1957, then Keeling's measurements on Mauna Loa from
March 1958 to December 2025, with an enlargement of the Mauna Loa record showing the yearly rise and fall.

Data (in build/maps/data, each file naming its source and edition):
- ch111_co2_law_dome.txt: Law Dome ice cores, CSIRO spline fit (October 2008), NOAA NCEI law2006.txt
  (MacFarling Meure et al. 2006), one value every ten years.
- ch111_co2_mauna_loa_monthly.txt: NOAA Global Monitoring Laboratory co2_mm_mlo.txt (created 9 October 2026),
  monthly means, Scripps (Keeling) to April 1974 and NOAA after. Missing months were interpolated by NOAA, as
  that file states; nothing else is filled in here.

The chapter's figures: "two hundred and eighty when James Watt improved the steam engine" (Law Dome spline, 1769:
277.1, which rounds to 280); "In 2025 the reading passed four hundred and thirty" (monthly mean, May 2025:
430.51). The chapter's "first reading was three hundred and thirteen" is a single reading of March 1958; the first
monthly mean in the NOAA file is 315.71, so the chart does not label the first value.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO


def load(name):
    rows = [l.split() for l in open(lib.os.path.join(lib.DATA, name)) if l.strip() and not l.startswith("#")]
    return [[float(x) for x in r] for r in rows]


ice = load("ch111_co2_law_dome.txt")
iy, iv = [r[0] for r in ice], [r[1] for r in ice]
ml = load("ch111_co2_mauna_loa_monthly.txt")
my = [r[0] + (r[1] - 0.5) / 12 for r in ml]
mv = [r[2] for r in ml]
watt = dict(zip(iy, iv))[1769]
may25 = [r[2] for r in ml if r[0] == 2025 and r[1] == 5][0]
print("Law Dome 1769:", watt, " Mauna Loa May 2025:", may25, " max 2025:", max(r[2] for r in ml if r[0] == 2025))

RED, BLUE = FILL["red"], FILL["blue"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.075, 0.1, 0.895, 0.8])
ax.set_facecolor(PAPER)

ax.plot(iy, iv, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
ax.plot(iy, iv, color=BLUE, lw=4.2, solid_capstyle="round", zorder=4)
ax.plot(my, mv, color=PAPER, lw=7, solid_capstyle="round", zorder=3.5)
ax.plot(my, mv, color=RED, lw=3.0, solid_capstyle="round", zorder=4)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=7, linespacing=1.1)
C = {k: v for k, v in T.items() if k != "color"}
ax.text(1330, 286, "air trapped in the Antarctic ice\n(Law Dome)", ha="center", va="bottom", color="#2f5577", **C)
ax.plot(1769, watt, "o", ms=10, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
ax.text(1769, 297, "about 280 when\nJames Watt improved\nthe steam engine, 1769", ha="center", va="bottom", **T)
ax.plot([1769, 1769], [watt + 3, 295.5], color=INK, lw=1.4, zorder=5)
ax.text(1945, 375, "measured on\nMauna Loa,\nfrom 1958", ha="right", va="center", color="#8a3b2a", **C)
ax.plot(2025.375, may25, "o", ms=10, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
ax.text(1995, 433, "passes 430\nin 2025", ha="right", va="center", **T)

# enlargement: Mauna Loa, 1958 to 2025, showing the planet breathing
ins = fig.add_axes([0.13, 0.5, 0.36, 0.34])
ins.set_facecolor("#f3ecdf")
ins.plot(my, mv, color=RED, lw=1.6, zorder=4)
ins.set_xlim(1956, 2027)
ins.set_ylim(305, 440)
ins.set_xticks([1960, 1980, 2000, 2020])
ins.set_yticks([320, 360, 400, 440])
ins.tick_params(labelsize=16, colors=INK, length=0, pad=6)
ins.grid(axis="y", color="#d8cdb8", lw=1.0, zorder=0)
for s in ins.spines.values():
    s.set_color(INK)
    s.set_linewidth(1.2)
ins.text(1958, 432, "Mauna Loa, enlarged:\nthe zigzag of the seasons", ha="left", va="top", fontsize=17, color=INK,
         path_effects=HALO, zorder=7, linespacing=1.1)

ax.set_xlim(985, 2045)
ax.set_ylim(255, 445)
ticks = [260, 280, 300, 320, 340, 360, 380, 400, 420, 440]
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.set_xticks(range(1000, 2001, 100))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.075, 0.95, "Carbon dioxide in the air, in parts per million", fontsize=24, color=INK,
         fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/111-climate/images/chart_co2.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
