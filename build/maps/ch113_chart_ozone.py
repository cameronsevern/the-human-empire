#!/usr/bin/env python3
"""Chapter 113: the size of the ozone hole over Antarctica each southern spring, 1979 to 2025, drawn in the style
of the book's maps, with the British report of 1985 and the Montreal agreement of 1987 marked.

Data: NASA Ozone Watch (Goddard Space Flight Center), "annual_data.txt" (ozonewatch.gsfc.nasa.gov/statistics/,
read November 2026): ozone hole area, the mean for 7 September to 13 October of each year, in millions of square
kilometres, from the TOMS, OMI and OMPS satellite instruments; NASA states that missing days are filled from the
MERRA, MERRA-2 and GEOS FP analyses. NASA gives no figure for 1995, when no TOMS instrument was in orbit; the year is
left empty here, not filled in. The ozone hole is the area where the ozone overhead is below 220 Dobson units.

For scale, the area of the United States: 9.8 million square kilometres (US Census Bureau, total area including
water, 9,833,517 sq km). The chapter says the satellite data, once examined, "showed a hole in the ozone layer the
size of the United States"; the means for 1984 and 1985 are 10.1 and 14.2.

The two low years, 2002 and 2019, were years of unusually warm air over Antarctica (NASA); they are not labelled,
since the chapter does not discuss them.
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

# NASA Ozone Watch, mean ozone hole area 7 Sep - 13 Oct, million km2 (no figure for 1995)
AREA = {1979: 0.1, 1980: 1.4, 1981: 0.6, 1982: 4.8, 1983: 7.9, 1984: 10.1, 1985: 14.2, 1986: 11.3, 1987: 19.3,
        1988: 10.0, 1989: 18.7, 1990: 19.2, 1991: 18.8, 1992: 22.3, 1993: 24.2, 1994: 23.6, 1996: 22.8,
        1997: 22.1, 1998: 25.9, 1999: 23.3, 2000: 24.8, 2001: 25.0, 2002: 12.0, 2003: 25.8, 2004: 19.5,
        2005: 24.4, 2006: 26.6, 2007: 22.0, 2008: 25.2, 2009: 22.0, 2010: 19.4, 2011: 24.7, 2012: 17.8,
        2013: 21.0, 2014: 20.9, 2015: 25.6, 2016: 20.7, 2017: 17.4, 2018: 22.9, 2019: 9.3, 2020: 23.5,
        2021: 23.3, 2022: 23.2, 2023: 23.1, 2024: 19.6, 2025: 18.7}
USA = 9.83

BLUE = FILL["blue"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.075, 0.1, 0.895, 0.8])
ax.set_facecolor(PAPER)

ax.bar(list(AREA), list(AREA.values()), width=0.72, color=BLUE, lw=0, zorder=3)
ax.axhline(USA, color=INK, lw=1.6, ls=(0, (4, 3)), zorder=4)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=7, linespacing=1.1)
ax.text(1978.3, USA + 0.3, "area of the\nUnited States", ha="left", va="bottom", style="italic", **T)
ax.text(1995, 0.6, "no measurement, 1995", ha="center", va="bottom", rotation=90, fontsize=16, color=INK,
        path_effects=HALO, zorder=7, style="italic")
ax.text(1981.6, 17.0, "British scientists\nreport the hole,\n1985", ha="center", va="bottom", **T)
ax.plot([1983.6, 1984.9], [16.8, 14.6], color=INK, lw=1.4, zorder=5)
ax.plot([1987, 1987], [AREA[1987] + 0.4, 24.3], color=INK, lw=1.4, zorder=5)
ax.text(1987, 24.6, "Montreal\nagreement,\n1987", ha="center", va="bottom", **T)
ax.text(2006, 27.0, "largest,\n2006", ha="center", va="bottom", **T)

ax.set_xlim(1977.5, 2026.5)
ax.set_ylim(0, 34)
ticks = [0, 5, 10, 15, 20, 25, 30]
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.set_xticks(range(1980, 2026, 5))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.075, 0.95, "The ozone hole over Antarctica each spring, in millions of square kilometres",
         fontsize=24, color=INK, fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/113-survival/images/chart_ozone.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
