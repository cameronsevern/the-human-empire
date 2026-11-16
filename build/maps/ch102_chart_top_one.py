#!/usr/bin/env python3
"""Chapter 102: the share of income going to the richest one per cent of American families each year,
1913 to 2017, drawn in the style of the book's maps, with 1928, 1980 and 2007 marked (the years compared in
the chapter) and the crashes of 1929 and 2008.

Data: Thomas Piketty and Emmanuel Saez, "Income Inequality in the United States, 1913-1998", Quarterly
Journal of Economics 118 (2003), series updated by Saez to 2018 (spreadsheet TabFig2018prel.xls, saved
June 2019, downloaded from Saez's page at eml.berkeley.edu in November 2026), Table A3, "Top fractiles income
shares (including capital gains) in the United States", column P99-100. Income is pre-tax market income
reported on tax returns, including realised capital gains and excluding government transfers; the unit is
the tax unit (a single person or a couple, with dependants), the top one per cent being defined relative to
all tax units, filers or not. Rounded here to two decimals; nothing else is changed and no year is filled in.
The table's last row, a preliminary figure, is labelled 2017 a second time, so it is left out and the series
ends at 2017. The spike of 1986 is the rush to realise gains before the tax reform of that year.
"""
import matplotlib.pyplot as plt
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

years = list(range(1913, 2018))
# Piketty and Saez, Table A3 (including capital gains), P99-100, per cent; TabFig2018prel.xls
share = [17.96, 18.16, 17.58, 19.31, 17.74, 15.96, 16.41, 14.83, 15.64, 17.06,                        # 1913-22
         15.64, 17.42, 20.24, 19.91, 21.03, 23.94, 22.35, 17.22, 15.50, 15.56,                        # 1923-32
         16.46, 16.40, 16.68, 19.29, 17.15, 15.75, 16.18, 16.48, 15.79, 13.43,                        # 1933-42
         12.31, 11.28, 12.52, 13.28, 11.96, 12.24, 11.73, 12.82, 11.79, 10.79,                        # 1943-52
         9.90, 10.77, 11.06, 10.67, 10.16, 10.21, 10.65, 10.03, 10.64, 9.95,                           # 1953-62
         9.92, 10.48, 10.89, 10.18, 10.74, 11.21, 10.35, 9.03, 9.40, 9.64,                             # 1963-72
         9.16, 9.12, 8.87, 8.86, 9.03, 8.95, 9.96, 10.02, 10.02, 10.80,                                # 1973-82
         11.56, 11.99, 12.67, 15.92, 12.66, 15.49, 14.49, 14.33, 13.36, 14.67,                         # 1983-92
         14.24, 14.23, 15.23, 16.69, 18.02, 19.09, 20.04, 21.52, 18.22, 16.86,                         # 1993-2002
         17.53, 19.75, 21.92, 22.82, 23.50, 20.95, 18.12, 19.86, 19.65, 22.83,                         # 2003-12
         20.01, 21.52, 21.59, 20.70, 21.95]                                                            # 2013-17
assert len(share) == len(years)
S = dict(zip(years, share))

BLUE = FILL["blue"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.07, 0.1, 0.9, 0.8])
ax.set_facecolor(PAPER)

ax.fill_between(years, share, color=BLUE, alpha=0.22, lw=0, zorder=2)
ax.plot(years, share, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
ax.plot(years, share, color=BLUE, lw=4.2, solid_capstyle="round", zorder=4)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=6, linespacing=1.1)
for yr, text, tx, ty in [(1928, "1928:\n24 per cent", 1928.0, 26.6), (1980, "1980:\n10 per cent", 1980.0, 5.4),
                         (2007, "2007:\n23.5 per cent", 2004.0, 26.6)]:
    ax.plot(yr, S[yr], "o", ms=11, mfc=BLUE, mec=PAPER, mew=1.8, zorder=5.5)
    up = ty > S[yr]
    ax.plot([yr, tx], [S[yr] + (0.5 if up else -0.5), ty - (0.3 if up else -0.3)], color=INK, lw=1.4, zorder=5)
    ax.text(tx, ty, text, ha="center", va="bottom" if up else "top", **T)
# the two crashes: a leader from the falling line to an italic label
for (x0, y0), (x1, y1), text, va in [((1929.5, 20.0), (1933.2, 22.6), "crash,\n1929", "bottom"),
                                     ((2008.0, 20.2), (2006.0, 13.6), "crash,\n2008", "top")]:
    ax.plot([x0, x1], [y0, y1], color=INK, lw=1.4, zorder=5)
    ax.text(x1, y1 + (0.2 if va == "bottom" else -0.2), text, ha="center", va=va, style="italic", **T)

ax.set_xlim(1911.5, 2019)
ax.set_ylim(0, 30)
ax.set_xticks(range(1920, 2011, 10))
ax.set_yticks(range(0, 31, 5))
ax.set_yticklabels([f"{v}%" for v in range(0, 31, 5)])
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.07, 0.95, "Share of all income taken by the richest one per cent of Americans", fontsize=24,
         color=INK, fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/102-crash/images/chart_top_one.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
