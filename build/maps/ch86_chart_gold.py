#!/usr/bin/env python3
"""Chapter 86: the gold held by the United States at the end of each year, 1938 to 1971, in tonnes, drawn in the
style of the book's maps, with the conference of 1944 and the suspension of August 1971 marked.

Data: the monetary gold stock of the United States at the end of each year, in millions of dollars, from
Historical Statistics of the United States, Millennial Edition (Cambridge University Press, 2006), table Cj1-6,
"U.S. monetary gold stock: 1879-1971", series Cj1 (Michael D. Bordo), read in November 2026. For 1941 to 1960
the figures agree exactly with the Federal Reserve's own "Analysis of changes in U.S. gold stock, 1941-60"
(Supplement to Banking and Monetary Statistics, section 14, Gold, table 1, total gold stock). The dollar
figures value gold at the official price of $35 a fine troy ounce, which held from January 1934 until 1972,
so they convert exactly to weight: millions of dollars / 35 = millions of troy ounces; a troy ounce is
31.1034768 grams. Nothing else is changed, and no year is filled in.
"""
import matplotlib.pyplot as plt
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

years = list(range(1938, 1972))
# Historical Statistics of the United States, Millennial Edition, series Cj1: millions of dollars, end of year
dollars = [14592.0, 17800.0, 22042.0, 22762.0, 22739.0, 21981.0, 20631.0, 20083.0, 20706.0, 22868.0,   # 1938-47
           24399.0, 24563.0, 22820.0, 22873.0, 23252.0, 22091.0, 21793.0, 21753.0, 22058.0, 22857.0,   # 1948-57
           20582.0, 19507.0, 17804.0, 16947.0, 16057.0, 15596.0, 15471.0, 13806.0, 13235.0, 12065.0,   # 1958-67
           10892.0, 11859.0, 11072.0, 10206.0]                                                          # 1968-71
assert len(dollars) == len(years)
TONNES_PER_MILLION_DOLLARS = 31.1034768 / 35.0                 # a million dollars at $35 an ounce, in tonnes
tonnes = [v * TONNES_PER_MILLION_DOLLARS for v in dollars]
T = dict(zip(years, tonnes))

GOLD = "#b8862f"
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.085, 0.1, 0.885, 0.8])
ax.set_facecolor(PAPER)

ax.fill_between(years, tonnes, color=FILL["gold"], alpha=0.28, lw=0, zorder=2)
ax.plot(years, tonnes, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
ax.plot(years, tonnes, color=GOLD, lw=4.2, marker="o", ms=8, mfc=GOLD, mec=PAPER, mew=1.4, zorder=4)

TX = dict(fontsize=18, color=INK, va="center", path_effects=HALO, zorder=6, linespacing=1.1)
for yr, text, tx, ty, lx, ly in [
        (1944, "Bretton Woods\nconference,\nJuly 1944", 1942.3, 13600, 1943.4, 15300),
        (1971, "dollars no longer\nexchanged for gold,\nAugust 1971", 1968.6, 5600, 1970.4, 7500)]:
    ax.plot([yr, lx], [T[yr], ly], color=INK, lw=1.4, zorder=5)
    ax.text(tx, ty, text, ha="center", **TX)
for yr, dx, dy, ha in [(1938, 0.35, -1100, "left"), (1945, 0.25, -950, "center"), (1949, 0.0, 1000, "center"),
                       (1960, 0.35, 850, "left"), (1971, 0.0, 1000, "center")]:
    ax.text(yr + dx, T[yr] + dy, f"{round(T[yr], -2):,.0f}", fontsize=17, color=INK, ha=ha, va="center",
            path_effects=HALO, zorder=6)

ax.set_xlim(1937.3, 1971.8)
ax.set_ylim(0, 24000)
ax.set_xticks(range(1940, 1971, 5))
ax.set_yticks(range(0, 24001, 4000))
ax.set_yticklabels([f"{v:,}" for v in range(0, 24001, 4000)])
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.085, 0.95, "Gold held by the United States, in tonnes, at the end of each year", fontsize=24,
         color=INK, fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/86-dollar/images/chart_gold.png")
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
for y in (1945, 1949, 1971):
    print(y, round(T[y]))
