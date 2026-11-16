#!/usr/bin/env python3
"""Chapter 101: income per person in China each year, 1960 to 2020, in US dollars at 2015 prices, drawn in the
style of the book's maps, with the events named in the chapter marked: the famine, the start of the reforms in
1978, the killings in Beijing in 1989, Deng's southern tour of 1992 and entry to the World Trade Organization
in 2001.

Data: World Bank, World Development Indicators, series NY.GDP.PCAP.KD, "GDP per capita (constant 2015 US$)",
China, read through the World Bank API in November 2026 (database last updated 11 November 2026). Rounded here
to the nearest cent; nothing else is changed, and no year is filled in. The series begins in 1960, so the first
year of the famine (1959) is not on it.

The vertical scale is logarithmic: each step up the scale doubles the income, so that equal rates of growth
look equally steep, and the famine of 1959 to 1961 can be seen at all beside the incomes of 2020.
For comparison (same series), Africa south of the Sahara in 1978: $1,475, against China's $386.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

years = list(range(1960, 2021))
# World Bank WDI, NY.GDP.PCAP.KD, China, constant 2015 US dollars (read November 2026)
gdp = [241.38, 177.35, 166.09, 178.74, 206.39, 235.70, 253.63, 232.93, 217.62, 247.61,          # 1960-69
       287.35, 299.31, 303.17, 319.32, 320.01, 341.83, 331.29, 351.55, 386.17, 409.99,          # 1970-79
       436.63, 453.12, 486.79, 531.49, 604.25, 676.13, 725.72, 797.42, 872.73, 895.61,          # 1980-89
       917.19, 989.59, 1117.30, 1258.34, 1406.97, 1545.08, 1681.46, 1819.08, 1944.47, 2076.93,  # 1990-99
       2237.30, 2405.99, 2610.66, 2856.85, 3127.91, 3465.73, 3883.27, 4409.70, 4811.34, 5237.79,  # 2000-09
       5764.65, 6275.72, 6723.09, 7197.94, 7686.37, 8175.33, 8679.23, 9221.35, 9798.58, 10356.29,  # 2010-19
       10573.38]                                                                                    # 2020
assert len(gdp) == len(years)
G = dict(zip(years, gdp))

RED = FILL["red"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.095, 0.1, 0.875, 0.8])
ax.set_facecolor(PAPER)
ax.set_yscale("log")

ax.axvspan(1959.3, 1961.5, color="#d8cdb8", alpha=0.55, lw=0, zorder=1)
ax.plot(years, gdp, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
ax.plot(years, gdp, color=RED, lw=4.2, solid_capstyle="round", zorder=4)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=6, linespacing=1.1)
ax.text(1962.0, 140, "famine, 1959 to 1961", ha="left", va="center", **T)
# events: a dot on the line, a leader, and the label above (va bottom) or below (va top) the leader's end
for yr, text, tx, ty, va in [
        (1978, "reforms begin,\n1978", 1976.6, 620, "bottom"),
        (1989, "the army clears\nthe square in\nBeijing, 1989", 1987.2, 1500, "bottom"),
        (1992, "Deng's southern\ntour, 1992", 1995.6, 900, "top"),
        (2001, "China joins the\nWorld Trade\nOrganization, 2001", 2005.0, 1900, "top")]:
    ax.plot([yr, tx], [G[yr], ty], color=INK, lw=1.4, zorder=5)
    ax.plot(yr, G[yr], "o", ms=10, mfc=RED, mec=PAPER, mew=1.6, zorder=5.5)
    ax.text(tx, ty * (1.03 if va == "bottom" else 0.97), text, ha="center", va=va, **T)
for yr, dx, f, ha in [(1960, 0.0, 1.22, "center"), (1978, -0.6, 1.0, "right"), (2001, -0.6, 1.07, "right"),
                      (2020, 0.0, 1.22, "center")]:
    ax.text(yr + dx, G[yr] * f, f"${G[yr]:,.0f}", fontsize=17, color=INK, ha=ha, va="bottom" if f > 1.05 else "center",
            path_effects=HALO, zorder=6)

ax.set_xlim(1958.8, 2021.5)
ticks = [125, 250, 500, 1000, 2000, 4000, 8000, 16000]
ax.set_ylim(110, 17000)
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.yaxis.set_minor_locator(NullLocator())
ax.set_yticklabels([f"${v:,}" for v in ticks])
ax.set_xticks(range(1960, 2021, 10))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.095, 0.95, "Income per person in China, in US dollars at 2015 prices", fontsize=24, color=INK,
         fontweight="bold", ha="left", va="center")
fig.text(0.97, 0.95, "each line up doubles the income", fontsize=17, color=INK, style="italic", ha="right",
         va="center")
out = lib.os.path.join(lib.ROOT, "chapters/101-china-rise/images/chart_income.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
