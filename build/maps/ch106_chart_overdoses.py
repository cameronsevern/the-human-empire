#!/usr/bin/env python3
"""Chapter 106: deaths from drug overdose in the United States each year, 1980 to 2024, drawn in the style of
the book's maps, with the three waves of the opioid epidemic: prescription painkillers (the pills), then heroin,
then fentanyl and other synthetic opioids.

Data, all from the National Center for Health Statistics (CDC), National Vital Statistics System:
- Total deaths, 1980 to 2023: NIDA, "Drug Overdose Deaths: Facts and Figures", workbook
  overdose_data_1999-2023_1.16.25.xlsx (January 2025), sheet "Historical Data" (NCHS, data table for "Age-adjusted
  drug overdose rate: United States, 1980-2023"). Deaths were classified under ICD-9 in 1980 to 1998 and under
  ICD-10 from 1999, so the two parts are not exactly comparable.
- Total deaths, 2024: NCHS Data Brief No. 549, "Drug Overdose Deaths in the United States, 2023-2024" (January
  2026): 79,384.
- Deaths by type of drug, 1999 to 2023: the same NIDA workbook, sheet "Number Drug OD Deaths" (CDC WONDER,
  Multiple Cause of Death): "Prescription Opioids" (ICD-10 T40.2-T40.3, natural and semi-synthetic opioids and
  methadone), "Heroin" (T40.1), "Synthetic Opioids other than Methadone (primarily fentanyl)" (T40.4). A death
  that involved more than one drug is counted under each, so the three lines do not add up to the total.
  The workbook stops at 2023, and Data Brief 549 does not give the prescription-opioid series in the same form for
  2024, so the three type lines end at 2023 rather than mixing definitions. Nothing is filled in.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

# NCHS via NIDA workbook (Jan 2025), sheet "Historical Data", 1980-2023; 2024 from NCHS Data Brief 549 (Jan 2026)
total = {1980: 6094, 1981: 6227, 1982: 6299, 1983: 6445, 1984: 6723, 1985: 7082, 1986: 7969, 1987: 7920,
         1988: 9031, 1989: 9275, 1990: 8413, 1991: 9392, 1992: 10604, 1993: 12133, 1994: 12714, 1995: 12779,
         1996: 13227, 1997: 14445, 1998: 15315, 1999: 16849, 2000: 17415, 2001: 19394, 2002: 23518, 2003: 25785,
         2004: 27424, 2005: 29813, 2006: 34425, 2007: 36010, 2008: 36450, 2009: 37004, 2010: 38329, 2011: 41340,
         2012: 41502, 2013: 43982, 2014: 47055, 2015: 52404, 2016: 63632, 2017: 70237, 2018: 67367, 2019: 70630,
         2020: 91799, 2021: 106699, 2022: 107941, 2023: 105007,
         2024: 79384}
# NIDA workbook (Jan 2025), sheet "Number Drug OD Deaths", 1999-2023
ty = list(range(1999, 2024))
pills = [3442, 3785, 4770, 6483, 7461, 8577, 9612, 11589, 12796, 13149, 13523, 14583, 15140, 14240, 14145, 14838,
         15281, 17087, 17029, 14975, 14139, 16416, 16706, 14716, 13026]
heroin = [1960, 1842, 1779, 2089, 2080, 1878, 2009, 2088, 2399, 3041, 3278, 3036, 4397, 5925, 8257, 10574, 12989,
          15469, 15482, 14996, 14019, 13165, 9173, 5871, 3984]
fent = [730, 782, 957, 1295, 1400, 1664, 1742, 2707, 2213, 2306, 2946, 3007, 2666, 2628, 3105, 5544, 9580, 19413,
        28466, 31335, 36359, 56516, 70601, 73838, 72776]
assert len(pills) == len(heroin) == len(fent) == len(ty)
print("deaths 1996-2024:", sum(v for y, v in total.items() if y >= 1996))
print("share involving an opioid, 2022:", 81806 / total[2022])

RED, BLUE, GOLD = FILL["red"], FILL["blue"], FILL["gold"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.085, 0.1, 0.885, 0.8])
ax.set_facecolor(PAPER)

yrs = sorted(total)
vals = [total[y] for y in yrs]
ax.fill_between(yrs, vals, color="#e3d6bd", alpha=0.6, lw=0, zorder=1)
ax.plot(yrs, vals, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
ax.plot(yrs, vals, color=INK, lw=4.2, solid_capstyle="round", zorder=4)


def line(v, colour, style, lw=3.6):
    ax.plot(ty, v, color=PAPER, lw=lw + 4, solid_capstyle="round", zorder=4.5)
    ax.plot(ty, v, color=colour, lw=lw, ls=style, solid_capstyle="round", dash_capstyle="round", zorder=5)


line(pills, GOLD, "-")
line(heroin, BLUE, (0, (5, 2.2)))
line(fent, RED, (0, (0.6, 1.6)), lw=5.0)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=7, linespacing=1.1)
ax.text(1987, 16500, "all drug overdoses", ha="center", va="bottom", fontweight="bold", **T)
C = {k: v for k, v in T.items() if k != "color"}
ax.text(2005.6, 14800, "first wave:\nprescription\npainkillers", ha="center", va="bottom", color="#8a6416", **C)
ax.text(2010.4, 4300, "second wave:\nheroin", ha="right", va="bottom", color="#2f5577", **C)
ax.text(2015.9, 30500, "third wave:\nfentanyl and\nother synthetic\nopioids", ha="right", va="center",
        color="#8a3b2a", **C)

# OxyContin goes on sale
ax.plot([1996, 1996], [0, 33000], color=INK, lw=1.4, ls=(0, (3, 3)), zorder=2)
ax.text(1995.6, 35500, "OxyContin goes\non sale, 1996", ha="center", va="bottom", **T)

for yr, text, dx, dy, ha in [(1980, "6,100\nin 1980", 0.0, 4500, "center"),
                             (1999, "16,800\nin 1999", 0.4, -9000, "left"),
                             (2022, "107,900\nin 2022", 0.0, 4500, "center"),
                             (2024, "79,400\nin 2024", 0.5, 3000, "left")]:
    ax.plot(yr, total[yr], "o", ms=10, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
    ax.text(yr + dx, total[yr] + dy, text, ha=ha, va="bottom", **T)

ax.set_xlim(1979, 2026.5)
ax.set_ylim(0, 122000)
ticks = [0, 20000, 40000, 60000, 80000, 100000, 120000]
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.set_yticklabels([f"{v:,}" for v in ticks])
ax.set_xticks(range(1980, 2025, 5))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.085, 0.95, "Deaths from drug overdose in the United States, each year", fontsize=24, color=INK,
         fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/106-drugs/images/chart_overdoses.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
