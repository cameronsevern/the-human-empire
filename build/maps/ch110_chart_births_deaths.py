#!/usr/bin/env python3
"""Chapter 110: births and deaths per thousand people in the world each year, 1950 to 2023, drawn in the style of
the book's maps, with the gap between them, by which the population grows, shaded.

Data: UN World Population Prospects 2024, crude birth rate and crude death rate, World, estimates 1950 to 2023
(read through Our World in Data's grapher birth-rate-vs-death-rate.csv, November 2026; OWID last updated the
series 12 July 2024). Values as published, to three decimals; nothing filled in. The world series begins in 1950.
The rise in deaths in 1959 to 1961 is the famine in China; that in 2020 and 2021 is the Covid pandemic.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

years = list(range(1950, 2024))
# UN WPP 2024, World, crude birth rate per 1,000 people, 1950-2023
birth = [36.831, 36.464, 37.681, 36.935, 37.301, 37.131, 36.402, 37.165, 35.945, 34.39,      # 1950-59
         33.951, 32.938, 35.871, 37.523, 35.93, 35.338, 34.439, 33.661, 34.364, 33.769,      # 1960-69
         33.599, 32.824, 32.134, 31.515, 30.705, 29.732, 29.275, 28.637, 28.457, 28.614,     # 1970-79
         28.655, 28.643, 28.878, 28.094, 28.097, 28.009, 28.096, 27.991, 27.419, 27.176,     # 1980-89
         26.927, 25.524, 24.808, 24.257, 23.811, 23.416, 22.992, 22.614, 22.283, 22.017,     # 1990-99
         21.997, 21.644, 21.364, 21.136, 21.004, 20.824, 20.755, 20.709, 20.711, 20.622,     # 2000-09
         20.416, 20.233, 20.282, 19.887, 19.68, 19.321, 19.164, 18.782, 18.155, 17.743,      # 2010-19
         17.081, 16.777, 16.515, 16.327]                                                    # 2020-23
# UN WPP 2024, World, crude death rate per 1,000 people, 1950-2023
death = [19.448, 18.99, 18.337, 17.934, 17.373, 17.019, 16.627, 16.434, 15.979, 17.102,      # 1950-59
         18.111, 16.287, 14.747, 14.693, 14.343, 14.459, 14.054, 13.695, 13.435, 13.211,     # 1960-69
         13.036, 13.1, 12.424, 12.134, 11.88, 11.699, 11.512, 11.183, 11.019, 10.75,         # 1970-79
         10.646, 10.482, 10.332, 10.263, 10.127, 10.017, 9.811, 9.636, 9.565, 9.395,         # 1980-89
         9.346, 9.247, 9.132, 9.091, 9.15, 8.927, 8.8, 8.681, 8.632, 8.57,                   # 1990-99
         8.464, 8.382, 8.324, 8.267, 8.178, 8.105, 7.987, 7.904, 7.888, 7.807,               # 2000-09
         7.729, 7.676, 7.609, 7.555, 7.525, 7.537, 7.509, 7.53, 7.477, 7.471,                # 2010-19
         8.057, 8.766, 7.764, 7.619]                                                         # 2020-23
assert len(birth) == len(death) == len(years)
B, D = dict(zip(years, birth)), dict(zip(years, death))

RED, BLUE = FILL["red"], FILL["blue"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.075, 0.1, 0.895, 0.8])
ax.set_facecolor(PAPER)

ax.fill_between(years, death, birth, color=FILL["gold"], alpha=0.35, lw=0, zorder=1)
for v, col, ls in [(birth, BLUE, "-"), (death, INK, (0, (5, 2.2)))]:
    ax.plot(years, v, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
    ax.plot(years, v, color=col, lw=4.2, ls=ls, solid_capstyle="round", dash_capstyle="round", zorder=4)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=7, linespacing=1.1)
ax.text(1985, 30.3, "births", ha="center", va="bottom", fontweight="bold", color="#2f5577",
        **{k: v for k, v in T.items() if k != "color"})
ax.text(1985, 8.2, "deaths", ha="center", va="top", fontweight="bold", **T)
ax.text(1990, 18.0, "the gap: the population grows", ha="center", va="center", fontsize=20, style="italic",
        color=INK, path_effects=HALO, zorder=7)
# the famine and the pandemic, with leaders down to the death line
for yr, text, tx, ty, ha in [(1960, "famine in\nChina, 1959\nto 1961", 1962.0, 23.5, "left"),
                             (2021, "Covid, 2020\nand 2021", 2013.0, 5.4, "center")]:
    ax.plot([yr, tx], [D[yr] + (0.5 if ty > D[yr] else -0.5), ty - (0.4 if ty > D[yr] else -0.3)], color=INK,
            lw=1.3, zorder=5)
    ax.text(tx, ty, text, ha=ha, va="bottom" if ty > D[yr] else "top", fontsize=17, color=INK, path_effects=HALO,
            zorder=7, linespacing=1.1)
for yr, v, text, dx, dy, ha, va in [(1950, B[1950], "37 in 1950", -0.9, 0, "right", "center"),
                                    (2023, B[2023], "16 in 2023", 0, 0.8, "center", "bottom"),
                                    (1950, D[1950], "19 in 1950", -0.9, 0, "right", "center"),
                                    (2023, D[2023], "8 in 2023", 0, -0.8, "center", "top")]:
    ax.plot(yr, v, "o", ms=9, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
    ax.text(yr + dx, v + dy, text, ha=ha, va=va, **T)

ax.set_xlim(1940, 2027)
ax.set_ylim(0, 42)
ticks = [0, 10, 20, 30, 40]
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.set_xticks(range(1950, 2021, 10))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.075, 0.95, "Births and deaths in the world, per thousand people each year", fontsize=24, color=INK,
         fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/110-eight-billion/images/chart_births_deaths.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
