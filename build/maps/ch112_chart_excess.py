#!/usr/bin/env python3
"""Chapter 112: excess deaths in the world each week, 2020 to 2023, as estimated by The Economist, drawn in the
style of the book's maps: how many more people died, of all causes, than would have been expected in ordinary
years.

Data: build/maps/data/ch112_excess_deaths_world_weekly.csv, from Our World in Data's copy of The Economist's
excess-mortality model (covid-19-data repository, excess_mortality_economist_estimates.csv, updated 18 June 2024),
entity "World". The model gives the average daily figure for each week; it is multiplied by seven here to give
deaths per week. The shading is the model's 95% interval. These are estimates throughout, and labelled as such.

Waves are named only as the chapter names them: northern Italy and New York in March and April 2020, and India in
the spring of 2021. The winter wave of 2020-21 and that of early 2022 are not named in the chapter and are left
unlabelled. Cumulative central estimate by 1 May 2023 (the week in which the World Health Organization declared
the emergency over, 5 May): about 23.3 million (chapter: "well over twenty million"); by the end of 2021, about
15.7 million (the chapter quotes the World Health Organization's separate estimate, about fifteen million).
"""
import csv
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FixedLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

rows = [r for r in csv.reader(open(lib.os.path.join(lib.DATA, "ch112_excess_deaths_world_weekly.csv")))
        if r and not r[0].startswith("#") and r[0] != "date"]
d = [dt.date.fromisoformat(r[0]) for r in rows]
mid, top, bot = (np.array([float(r[i]) * 7 / 1000 for r in rows]) for i in (1, 2, 3))
cum = {r[0]: float(r[4]) for r in rows}
print("cumulative 2021-12-27:", cum["2021-12-27"], " 2023-05-01:", cum["2023-05-01"])
k = int(np.argmax(mid))
print("peak week:", d[k], round(mid[k], 1), "thousand")

RED = FILL["red"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.075, 0.1, 0.895, 0.8])
ax.set_facecolor(PAPER)

ax.fill_between(d, bot, top, color="#ecd3c8", lw=0, zorder=1)
ax.plot(d, mid, color=PAPER, lw=8, solid_capstyle="round", zorder=3.5)
ax.plot(d, mid, color=RED, lw=3.8, solid_capstyle="round", zorder=4)
ax.axhline(0, color=INK, lw=1.6, zorder=2)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=7, linespacing=1.1)
D = dt.date


def mark(day, y0, y1, text, ty, ha="center"):
    ax.plot([day, day], [y0, y1], color=INK, lw=1.4, ls=(0, (3, 3)), zorder=2.5)
    ax.text(day, ty, text, ha=ha, va="bottom", **T)


mark(D(2020, 12, 8), -20, 470, "vaccination begins\nin Britain,\n8 December 2020", 478)
mark(D(2023, 5, 5), -20, 300, "emergency\ndeclared over,\nMay 2023", 308)
ax.text(D(2020, 4, 10), 115, "Bergamo and\nNew York,\nspring 2020", ha="center", va="bottom", **T)
ax.plot([D(2020, 4, 10), D(2020, 4, 10)], [62, 112], color=INK, lw=1.4, zorder=5)
ax.text(D(2021, 7, 12), 400, "India,\nspring 2021", ha="left", va="bottom", **T)
ax.plot([D(2021, 5, 24), D(2021, 7, 8)], [362, 412], color=INK, lw=1.4, zorder=5)
ax.text(D(2022, 3, 1), 440, "About 23 million more deaths than\nin ordinary years by May 2023\n(estimate)",
        ha="left", va="bottom", fontsize=18, fontweight="bold", color=INK, path_effects=HALO, zorder=7,
        linespacing=1.1)
ax.text(D(2022, 3, 1), 395, "the shading shows the range\nof the estimate", ha="left", va="top", style="italic",
        **T)

ax.set_xlim(D(2019, 12, 10), D(2024, 1, 20))
ax.set_ylim(-60, 620)
ticks = [0, 100, 200, 300, 400, 500, 600]
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.set_yticklabels([f"{t},000" if t else "0" for t in ticks])
ax.xaxis.set_major_locator(mdates.YearLocator())                # year boundaries: short ticks, no labels
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=7, bymonthday=1))   # year names centred on each year
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%Y"))
ax.tick_params(axis="x", which="major", length=10, width=1.6, color=INK)
ax.tick_params(axis="x", which="minor", length=0, labelsize=18, colors=INK, pad=10)
ax.tick_params(axis="y", labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.075, 0.95, "Excess deaths in the world each week, estimated", fontsize=24, color=INK,
         fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/112-pandemic/images/chart_excess_deaths.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
