#!/usr/bin/env python3
"""Chapter 111: the world's average surface temperature each year, 1850 to 2025, compared with the average of
1850 to 1900 (the chapter's "second half of the nineteenth century"), drawn in the style of the book's maps.

Data: HadCRUT5 analysis, version HadCRUT.5.2.0.0 (Met Office Hadley Centre and Climatic Research Unit),
global annual series, in build/maps/data/ch111_hadcrut5_global_annual.csv. HadCRUT gives anomalies from
1961-1990; here the average of 1850-1900 in the same series is subtracted from every year, which changes no
year's position relative to another. The shading is HadCRUT's own 95% range for each year.

Against the chapter: 2024 is 1.55 above 1850-1900 in this series, the first year above 1.5 (agrees). The average
of the last ten years, 2016-2025, is 1.29 (the chapter: "about one and a third degrees"). The ten warmest years in
this series are 2015, 2016, 2017 and 2019 to 2025: 2018 ranks eleventh, below 2015, so "the ten hottest years in
the record are the last ten" is not quite true of HadCRUT5; the eleven warmest years are the last eleven.
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

rows = [r for r in csv.reader(open(lib.os.path.join(lib.DATA, "ch111_hadcrut5_global_annual.csv")))
        if r and not r[0].startswith("#") and r[0] != "year"]
yrs = np.array([int(r[0]) for r in rows])
raw = np.array([[float(x) for x in r[1:]] for r in rows])
base = raw[(yrs >= 1850) & (yrs <= 1900), 0].mean()
val, lo, hi = raw[:, 0] - base, raw[:, 1] - base, raw[:, 2] - base
V = dict(zip(yrs, val))
order = sorted(V, key=V.get, reverse=True)
print("base (1961-90 units):", round(base, 3), " 2024:", round(V[2024], 2), " 2025:", round(V[2025], 2))
print("ten warmest:", sorted(order[:10]), " 2016-2025 mean:", round(np.mean([V[y] for y in range(2016, 2026)]), 2))

RED, BLUE = FILL["red"], FILL["blue"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.085, 0.1, 0.885, 0.8])
ax.set_facecolor(PAPER)

ax.fill_between(yrs, lo, hi, color="#e3d6bd", lw=0, zorder=1)
ax.bar(yrs, val, width=0.75, color=[RED if v > 0 else BLUE for v in val], lw=0, zorder=3)
ax.axhline(0, color=INK, lw=1.6, zorder=4)
ax.axhline(1.5, color=INK, lw=1.6, ls=(0, (4, 3)), zorder=2)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=7, linespacing=1.1)
ax.text(1852, 1.53, "one and a half degrees above the old level", ha="left", va="bottom", style="italic", **T)
ax.text(1935, -0.3, "zero: the average of 1850 to 1900", ha="left", va="center", style="italic", **T)
ax.plot(2024, V[2024], "o", ms=10, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
ax.text(2021.5, 1.72, "2024: the first\nyear above 1.5", ha="right", va="bottom", **T)
ax.plot([2022, 2023.6], [1.76, 1.6], color=INK, lw=1.4, zorder=5)
ax.text(1880, 0.75, "Each bar is one year. The shading shows\nthe range within which each year's figure\n"
        "lies, nineteen times in twenty.", ha="left", va="center", fontsize=17, color=INK, path_effects=HALO,
        zorder=7, linespacing=1.15)

ax.set_xlim(1848, 2028)
ax.set_ylim(-0.6, 1.95)
ticks = [-0.5, 0, 0.5, 1.0, 1.5]
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.set_yticklabels(["−0.5", "0", "+0.5", "+1.0", "+1.5"])
ax.set_xticks(range(1850, 2026, 25))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left", "bottom"]:
    ax.spines[s].set_visible(False)
fig.text(0.085, 0.95, "The world's average temperature, in degrees above or below 1850 to 1900", fontsize=24,
         color=INK, fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/111-climate/images/chart_temperature.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
