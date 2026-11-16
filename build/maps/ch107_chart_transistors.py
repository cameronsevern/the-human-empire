#!/usr/bin/env python3
"""Chapter 107: the number of transistors on a chip, 1971 to 2024, drawn in the style of the book's maps, on a
scale on which each step up multiplies the count by ten, so that a steady doubling is a straight line.

Data: English Wikipedia, "Transistor count", table of microprocessors (read November 2026), which gives the
count for each named chip with its sources. Two kinds of chip are shown: the main chips of Intel's personal
computers, 1971 to 2008, and the chips Apple designed for its telephones, 2013 to 2023, with Apple's M4 (2024),
for tablets and computers, as the last point. No point is filled in between. The table gives the Intel 4004 as
2,250 transistors; Intel's own long-quoted figure is 2,300. Apple has not published a count for its 2024
telephone chip (A18), so 2024 is shown by the M4.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

# Wikipedia, "Transistor count", microprocessors table (November 2026)
intel = [(1971, 2_250, "Intel 4004"), (1974, 6_000, "Intel 8080"), (1978, 29_000, "Intel 8086"),
         (1982, 134_000, "Intel 80286"), (1985, 275_000, "Intel 80386"), (1989, 1_180_235, "Intel 80486"),
         (1993, 3_100_000, "Pentium"), (1997, 7_500_000, "Pentium II"), (2000, 42_000_000, "Pentium 4"),
         (2006, 291_000_000, "Core 2 Duo"), (2008, 731_000_000, "Core i7")]
apple = [(2013, 1_000_000_000, "Apple A7"), (2015, 2_000_000_000, "Apple A9"), (2017, 4_300_000_000, "Apple A11"),
         (2018, 6_900_000_000, "Apple A12"), (2019, 8_500_000_000, "Apple A13"), (2020, 11_800_000_000, "Apple A14"),
         (2021, 15_000_000_000, "Apple A15"), (2022, 16_000_000_000, "Apple A16"),
         (2023, 19_000_000_000, "Apple A17")]
m4 = (2024, 28_000_000_000, "Apple M4")

BLUE, RED = FILL["blue"], FILL["red"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.13, 0.1, 0.84, 0.8])
ax.set_facecolor(PAPER)
ax.set_yscale("log")

xi, yi = [p[0] for p in intel], [p[1] for p in intel]
xa, ya = [p[0] for p in apple], [p[1] for p in apple]
ax.plot(xi, yi, color=BLUE, lw=2.4, zorder=3)
ax.plot(xa, ya, color=RED, lw=2.4, ls=(0, (4, 2)), zorder=3)
ax.plot(xi, yi, "o", ms=13, mfc=BLUE, mec=PAPER, mew=1.8, zorder=5)
ax.plot(m4[0], m4[1], "o", ms=13, mfc=BLUE, mec=PAPER, mew=1.8, zorder=5)
ax.plot(xa, ya, "s", ms=12, mfc=RED, mec=PAPER, mew=1.8, zorder=5)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=7, linespacing=1.1)
# labels: (year, count, text, x offset in years, y factor, ha, va)
for yr, n, text, dx, f, ha, va in [
        (1971, 2_250, "Intel 4004, 1971:\n2,250", 0.9, 0.8, "left", "top"),
        (1978, 29_000, "Intel 8086, 1978:\n29,000", -0.8, 1.15, "right", "bottom"),
        (1989, 1_180_235, "Intel 80486, 1989:\n1.2 million", -0.8, 1.2, "right", "bottom"),
        (2000, 42_000_000, "Pentium 4, 2000:\n42 million", 0.8, 0.85, "left", "top"),
        (2013, 1_000_000_000, "Apple A7, 2013:\n1 billion", 0.8, 0.75, "left", "top"),
        (2023, 19_000_000_000, "Apple A17, 2023:\n19 billion", -0.6, 1.4, "right", "bottom"),
        (2024, 28_000_000_000, "Apple M4,\n2024:\n28 billion", 1.1, 0.55, "center", "top")]:
    ax.text(yr + dx, n * f, text, ha=ha, va=va, **T)
ax.text(1985.5, 2.6e7, "chips for personal\ncomputers (Intel)", ha="center", va="center", fontweight="bold",
        color="#2f5577", **{k: v for k, v in T.items() if k != "color"})
ax.text(2012.3, 6.0e9, "chips for telephones\n(Apple)", ha="right", va="center", fontweight="bold",
        color="#8a3b2a", **{k: v for k, v in T.items() if k != "color"})

ax.set_xlim(1968.5, 2028)
ticks = [1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11]
names = ["1,000", "10,000", "100,000", "1 million", "10 million", "100 million", "1 billion", "10 billion",
         "100 billion"]
ax.set_ylim(260, 1.4e11)
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.yaxis.set_minor_locator(NullLocator())
ax.set_yticklabels(names)
ax.set_xticks(range(1970, 2025, 10))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.13, 0.95, "Transistors on a chip", fontsize=24, color=INK, fontweight="bold", ha="left", va="center")
fig.text(0.97, 0.95, "each line up is ten times as many", fontsize=17, color=INK, style="italic", ha="right",
         va="center")
out = lib.os.path.join(lib.ROOT, "chapters/107-internet/images/chart_transistors.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
