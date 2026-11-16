#!/usr/bin/env python3
"""Chapter 77: unemployment in the United States, Britain and Germany, 1928 to 1939, with the point at
which each country left gold, drawn in the style of the book's maps.

Figures, per cent of the workforce, annual averages:
- United States: Stanley Lebergott's series, as in Historical Statistics of the United States (series D 86).
- Britain: insured workers unemployed (Ministry of Labour), as in W. Galenson and A. Zellner, "International
  Comparison of Unemployment Rates" (NBER, 1957), table 1, and B. R. Mitchell's British Historical Statistics.
- Germany: registered unemployed as a share of employees, from D. Petzina, W. Abelshauser and A. Faust,
  Sozialgeschichtliches Arbeitsbuch III (1978), p. 119.
The three series are measured differently, so the levels are only roughly comparable; the shapes are what
matter. Gold: Germany kept the gold value of the mark on paper but imposed exchange controls in July 1931,
which cut it loose in practice; Britain left on 21 September 1931; the United States in April 1933.
"""
import matplotlib.pyplot as plt
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

years = list(range(1928, 1940))
data = {
    "United States": ([4.2, 3.2, 8.7, 15.9, 23.6, 24.9, 21.7, 20.1, 16.9, 14.3, 19.0, 17.2], "blue", "-"),
    "Britain": ([10.8, 10.4, 16.1, 21.3, 22.1, 19.9, 16.7, 15.5, 13.1, 10.8, 12.9, 10.5], "green", "--"),
    "Germany": ([6.3, 8.5, 14.0, 21.9, 29.9, 25.9, 13.5, 10.3, 7.4, 4.1, 1.9, 0.5], INK, "-"),
}
place = {"United States": (1935.2, 23.3, "left"), "Britain": (1928.2, 13.4, "left"),
         "Germany": (1932.15, 31.6, "center")}
# where each country left gold: (date, text, label x, label y, ha)
gold = {"Germany": (1931.5, "Germany: exchange\ncontrols, July 1931", 1929.4, 25.5, "center"),
        "Britain": (1931.72, "Britain leaves gold,\nSeptember 1931", 1932.55, 12.0, "center"),
        "United States": (1933.28, "United States leaves\ngold, April 1933", 1935.0, 28.6, "center")}

fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.09, 0.1, 0.87, 0.8])
ax.set_facecolor(PAPER)
for name, (vals, col, ls) in data.items():
    c = FILL.get(col, col)
    ax.plot(years, vals, color=c, lw=4.2, ls=ls, marker="o", ms=10, mfc=c, mec=PAPER, mew=1.6, zorder=3)
    x, y, ha = place[name]
    ax.text(x, y, name, fontsize=21, color=c, ha=ha, va="center", fontweight="bold", path_effects=HALO, zorder=5)
    gx, text, lx, ly, lha = gold[name]
    gy = vals[int(gx) - 1928] + (vals[int(gx) - 1927] - vals[int(gx) - 1928]) * (gx - int(gx))
    ax.plot(gx, gy, "D", ms=17, mfc=PAPER, mec=c, mew=3.2, zorder=4)
    ax.annotate(text, xy=(gx, gy), xytext=(lx, ly), fontsize=17, color=INK, ha=lha, va="center", zorder=6,
                path_effects=HALO, linespacing=1.1,
                arrowprops=dict(arrowstyle="-", color=INK, lw=1.3, shrinkA=6, shrinkB=11))

ax.set_xlim(1927.6, 1939.4)
ax.set_ylim(0, 34)
ax.set_xticks(years)
ax.set_xticklabels([str(y) if y % 2 == 0 else "" for y in years])
ax.set_yticks(range(0, 31, 10))
ax.set_yticklabels([f"{v}%" for v in range(0, 31, 10)])
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.09, 0.95, "Share of workers unemployed", fontsize=24, color=INK, fontweight="bold", ha="left",
         va="center")
fig.text(0.96, 0.95, "◇  the point at which each country left gold", fontsize=17, color=INK, ha="right",
         va="center")
out = lib.os.path.join(lib.ROOT, "chapters/77-depression/images/chart_unemployment.png")
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
