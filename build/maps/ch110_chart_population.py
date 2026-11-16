#!/usr/bin/env python3
"""Chapter 110: the number of people in the world, 1700 to 2100, drawn in the style of the book's maps, with the
United Nations' forecast to 2100 and the year in which each billion was reached.

Data: Our World in Data, "Population" (grapher population.csv, read November 2026), which joins HYDE 3.3 (2023)
for years before 1800, Gapminder v7 (2022) for 1800 to 1949, and the UN World Population Prospects 2024 for 1950
to 2023; forecast, 2024 to 2100: UN World Population Prospects 2024, medium variant (OWID grapher
population-with-un-projections.csv). Mid-year figures, in people; nothing is filled in. HYDE gives only one
figure a decade before 1800; for 1800 to 1949 one figure a decade is used, with the years either side of the
first two billions.

The year shown for each billion is the first year whose mid-year figure in this series reaches it. These differ
by a year in four places from the dates the UN announced at the time (from older revisions): 1 billion 1805
(usually given as 1804), 4 billion 1975 (1974), 6 billion 1998 (1999), 7 billion 2010 (2011).
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

# OWID population series (HYDE 3.3 to 1799; Gapminder v7 1800-1949; UN WPP 2024 from 1950)
past = {1700: 595456896, 1710: 617975872, 1720: 648184768, 1730: 670899968, 1740: 702227776,
        1750: 753279296, 1760: 788254976, 1770: 827951488, 1780: 900945152, 1790: 942261696,
        1800: 983104755, 1804: 996784263, 1805: 1000304675, 1810: 1020150076, 1820: 1089507052,
        1830: 1162497339, 1840: 1219617217, 1850: 1275602897, 1860: 1298027373, 1870: 1340168478,
        1880: 1414583216, 1890: 1520891633, 1900: 1627273655, 1910: 1767417985, 1920: 1895426673,
        1926: 1996813608, 1927: 2014848732, 1930: 2071786711, 1940: 2291979566,
        1950: 2493092852, 1951: 2536927034, 1952: 2584086340, 1953: 2634106241, 1954: 2685894857,
        1955: 2740213796, 1956: 2795409991, 1957: 2852618331, 1958: 2911249671, 1959: 2965950350,
        1960: 3015470889, 1961: 3064869675, 1962: 3123374312, 1963: 3192807826, 1964: 3264487343,
        1965: 3334533710, 1966: 3404041131, 1967: 3473412877, 1968: 3545187246, 1969: 3619491581,
        1970: 3694683794, 1971: 3769847867, 1972: 3844917684, 1973: 3920805041, 1974: 3996416100,
        1975: 4070735279, 1976: 4144246382, 1977: 4217863796, 1978: 4292097499, 1979: 4368539520,
        1980: 4447606240, 1981: 4528777306, 1982: 4612673415, 1983: 4697327573, 1984: 4782175518,
        1985: 4868943457, 1986: 4958072839, 1987: 5049746390, 1988: 5141992540, 1989: 5234431736,
        1990: 5327803106, 1991: 5418735886, 1992: 5505989815, 1993: 5591544802, 1994: 5675551258,
        1995: 5758878977, 1996: 5842055730, 1997: 5924787819, 1998: 6007066691, 1999: 6089006328,
        2000: 6171702992, 2001: 6254936464, 2002: 6337730343, 2003: 6420361633, 2004: 6503377774,
        2005: 6586970132, 2006: 6671452019, 2007: 6757308776, 2008: 6844457659, 2009: 6932766416,
        2010: 7021732143, 2011: 7110923773, 2012: 7201202478, 2013: 7291793585, 2014: 7381616239,
        2015: 7470491876, 2016: 7558554527, 2017: 7645617952, 2018: 7729902779, 2019: 7811293699,
        2020: 7887001289, 2021: 7954448387, 2022: 8021407196, 2023: 8091734933}
# UN WPP 2024, medium variant (forecast)
fore = {2023: 8091734933, 2025: 8231613067, 2030: 8569124917, 2035: 8885210180, 2040: 9177190199,
        2045: 9439639664, 2050: 9664378585, 2055: 9846237566, 2060: 9989232293, 2065: 10101849558,
        2070: 10189241950, 2075: 10250496436, 2080: 10283078027, 2084: 10289315239, 2085: 10288456610,
        2090: 10271565066, 2095: 10235403600, 2100: 10180160744}

py, pv = sorted(past), [past[y] / 1e9 for y in sorted(past)]
fy, fv = sorted(fore), [fore[y] / 1e9 for y in sorted(fore)]
billions = {}
for b in range(1, 9):
    billions[b] = min(y for y in py if past[y] >= b * 1e9)
print("first year at or above each billion:", billions)
# Labels use the dates the United Nations gives for each billion, which the text also uses;
# the dots sit where this series crosses each billion (within a year of those dates).
UN = {1: 1804, 2: 1927, 3: 1960, 4: 1974, 5: 1987, 6: 1999, 7: 2011, 8: 2022}

RED, BLUE = FILL["red"], FILL["blue"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.075, 0.1, 0.895, 0.8])
ax.set_facecolor(PAPER)

ax.axvspan(2023.5, 2101, color="#ece4d4", lw=0, zorder=0.5)
ax.plot(py, pv, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
ax.plot(py, pv, color=RED, lw=4.2, solid_capstyle="round", zorder=4)
ax.plot(fy, fv, color=RED, lw=3.6, ls=(0, (2.5, 1.6)), zorder=4)

T = dict(fontsize=17, color=INK, path_effects=HALO, zorder=7, linespacing=1.1)
# each billion: a dot and its year, to the left of the line
for b, yr in billions.items():
    ax.plot(yr, past[yr] / 1e9, "o", ms=9, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
    if b == 1:                                                 # below the line, clear of Malthus's leader
        ax.text(yr + 2, 0.72, f"{b} billion, {UN[b]}", ha="left", va="top", **T)
    else:
        ax.text(yr - 3.5, past[yr] / 1e9 + 0.02, f"{b} billion, {UN[b]}", ha="right", va="center", **T)
ax.plot(1700, past[1700] / 1e9, "o", ms=9, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
ax.text(1702, 0.95, "about 600\nmillion, 1700", ha="left", va="bottom", **T)
ax.plot(2084, fore[2084] / 1e9, "o", ms=10, mfc=PAPER, mec=RED, mew=2.4, zorder=6)
ax.text(2084, 10.55, "peak, about 10.3\nbillion, in 2084", ha="center", va="bottom", **T)
ax.text(2062, 7.4, "forecast\n(United Nations,\nmiddle estimate)", ha="center", va="center", style="italic", **T)
ax.text(1798, 2.2, "Malthus writes,\n1798", ha="center", va="bottom", **T)
ax.plot([1798, 1798], [past[1800] / 1e9 + 0.15, 2.15], color=INK, lw=1.4, zorder=5)

ax.set_xlim(1695, 2104)
ax.set_ylim(0, 11.6)
ticks = list(range(0, 12, 2))
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.set_yticklabels([f"{t}" for t in ticks])
ax.set_xticks(range(1700, 2101, 50))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.075, 0.95, "People in the world, in billions", fontsize=24, color=INK, fontweight="bold", ha="left",
         va="center")
out = lib.os.path.join(lib.ROOT, "chapters/110-eight-billion/images/chart_population.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
