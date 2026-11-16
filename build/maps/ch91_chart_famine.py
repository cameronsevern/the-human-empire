#!/usr/bin/env python3
"""Chapter 91: births and deaths per thousand people in China each year, 1950 to 1970, drawn in the style of
the book's maps, with the famine years of the Great Leap Forward marked.

Crude birth and death rates as published by China's State Statistical Bureau (now the National Bureau of
Statistics) in the China Statistical Yearbook and the China Population Statistical Yearbook, as tabulated in
English Wikipedia's "Demographics of China" (section "Births and deaths since 1949"); the 1958 and 1960
figures are the same as those quoted from the Yearbook in its "Great Chinese Famine". These are the official
figures, unsmoothed; the early-1950s figures are round numbers, and most demographers think that the deaths
of the famine years were under-recorded.
"""
import matplotlib.pyplot as plt
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

years = list(range(1950, 1971))
births = [37.00, 37.80, 37.00, 37.00, 37.97, 32.60, 31.90, 34.03, 29.22, 24.78, 20.86, 18.02, 37.01, 43.37,
          39.14, 37.88, 35.05, 33.96, 35.59, 34.11, 33.43]
deaths = [18.00, 17.80, 17.00, 14.00, 13.18, 12.28, 11.40, 10.80, 11.98, 14.59, 25.43, 14.24, 10.02, 10.04,
          11.50, 9.50, 8.83, 8.43, 8.21, 8.03, 7.60]
assert len(births) == len(deaths) == len(years)

BLUE, RED = FILL["blue"], FILL["red"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.08, 0.1, 0.88, 0.8])
ax.set_facecolor(PAPER)

ax.axvspan(1958.6, 1961.4, color="#e4d6bc", zorder=0.5, lw=0)
ax.text(1960.0, 47.2, "famine,\n1959 to 1961", fontsize=20, color=INK, ha="center", va="center",
        fontweight="bold", linespacing=1.1, zorder=5)

for vals, col, ls, mk in [(births, BLUE, "-", "o"), (deaths, RED, (0, (4, 1.6)), "s")]:
    ax.plot(years, vals, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
    ax.plot(years, vals, color=col, lw=4.2, ls=ls, marker=mk, ms=10, mfc=col, mec=PAPER, mew=1.6, zorder=4)

ax.text(1953.5, 40.6, "births", fontsize=22, color=BLUE, fontweight="bold", ha="center", va="center",
        path_effects=HALO, zorder=5)
ax.text(1953.0, 10.6, "deaths", fontsize=22, color=RED, fontweight="bold", ha="center", va="center",
        path_effects=HALO, zorder=5)
for x, v, dx, dy, ha in [(1960, 25.43, 0.25, 1.4, "left"), (1961, 18.02, 0.22, -1.6, "left"),
                         (1963, 43.37, 0.0, 2.0, "center")]:
    ax.text(x + dx, v + dy, f"{v:.1f}", fontsize=18, color=INK, ha=ha, va="center", path_effects=HALO, zorder=5)

ax.set_xlim(1949.5, 1970.5)
ax.set_ylim(0, 51)
ax.set_xticks(range(1950, 1971, 5))
ax.set_yticks(range(0, 51, 10))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.08, 0.95, "Births and deaths in China, per thousand people", fontsize=24, color=INK,
         fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/91-cultural-revolution/images/chart_famine.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
