#!/usr/bin/env python3
"""Chapter 97: the price of a barrel of crude oil each year, 1950 to 1991, in constant dollars, drawn in the
style of the book's maps, with the events named in the chapter marked.

Data: Energy Institute, Statistical Review of World Energy (2026), "Crude oil prices since 1861", as
reproduced by Our World in Data (chart "oil-prices-inflation-adjusted", variable 1295353, read in November
2026), in constant 2025 US dollars per cubic metre. Divided here by 6.28981, the number of barrels in a cubic
metre, to give 2025 dollars a barrel; nothing else is changed. The Review's series is the posted price of
Arabian Light at Ras Tanura from 1945 to 1983, and Brent from 1984; yearly averages.
"""
import matplotlib.pyplot as plt
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

years = list(range(1950, 1992))
per_m3 = [144.34303, 133.78676, 130.9145, 146.65259, 145.94333, 146.4883, 144.28783, 137.45204, 146.47624,
          145.01065, 130.55814, 122.37635, 120.92671, 119.44598, 117.93765, 116.09731, 112.69935, 109.65874,
          105.16625, 99.7192, 94.21849, 112.42359, 120.52507, 150.58719, 477.26913, 435.3992, 457.0979,
          466.74753, 436.77078, 885.14124, 908.2506, 803.062, 694.33136, 602.9389, 563.01514, 520.6869,
          267.54565, 329.72003, 256.4626, 298.7888, 369.02798, 298.45197]
assert len(per_m3) == len(years)
price = [v / 6.28981 for v in per_m3]
P = dict(zip(years, price))

RED = FILL["red"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.075, 0.1, 0.895, 0.8])
ax.set_facecolor(PAPER)

ax.plot(years, price, color=PAPER, lw=8.5, solid_capstyle="round", zorder=3.5)
ax.plot(years, price, color=RED, lw=4.2, marker="o", ms=8, mfc=RED, mec=PAPER, mew=1.4, zorder=4)

T = dict(fontsize=18, color=INK, va="center", path_effects=HALO, zorder=6, linespacing=1.1)
# events, each with a short leader line from the point to its label
for yr, text, tx, ty, lx, ly in [
        (1951, "Iran takes over\nits oil, 1951", 1951.0, 52, 1951.0, 43),
        (1960, "OPEC founded,\n1960", 1960.0, 48, 1960.0, 39),
        (1973, "war and\nembargo,\n1973", 1970.6, 58, 1971.6, 45),
        (1979, "revolution\nin Iran,\n1979", 1975.6, 116, 1977.3, 124),
        (1990, "Iraq invades\nKuwait, 1990", 1990.0, 86, 1990.0, 77)]:
    ax.plot([yr, lx], [P[yr], ly], color=INK, lw=1.4, zorder=5)
    ax.text(tx, ty, text, ha="center", **T)
for yr, dx, dy, ha in [(1970, 0.0, -6.5, "center"), (1974, 0.45, 4.5, "left"), (1980, 0.4, 4.5, "left"),
                       (1986, 0.0, -7.0, "center")]:
    ax.text(yr + dx, P[yr] + dy, f"${P[yr]:.0f}", fontsize=17, color=INK, ha=ha, va="center",
            path_effects=HALO, zorder=6)

ax.set_xlim(1949.3, 1991.7)
ax.set_ylim(0, 160)
ax.set_xticks(range(1950, 1991, 5))
ax.set_yticks(range(0, 161, 20))
ax.set_yticklabels([f"${v}" for v in range(0, 161, 20)])
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.075, 0.95, "The price of a barrel of crude oil, in dollars of 2025", fontsize=24, color=INK,
         fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/97-oil/images/chart_oil_price.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
