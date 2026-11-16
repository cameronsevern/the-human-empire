#!/usr/bin/env python3
"""Chapter 81: aircraft built each year, 1939 to 1945, by the United States, the Soviet Union, Britain,
Germany and Japan, drawn in the style of the book's maps.

Figures as tabulated in English Wikipedia's "World War II aircraft production" (after John Ellis, The World
War II Databook, 1993; W. F. Craven and J. L. Cate, The Army Air Forces in World War II, vol. 6, 1955;
Richard Overy; and the US Strategic Bombing Survey). Military aircraft of all kinds; definitions differ a
little between the countries' own statistics.
"""
import matplotlib.pyplot as plt
import lib                                                     # house fonts and colours
from lib import INK, PAPER, SOFT, FILL, HALO

years = [1939, 1940, 1941, 1942, 1943, 1944, 1945]
data = {
    "United States": ([2141, 6086, 26277, 47836, 85898, 96318, 49761], "blue", "-"),
    "Soviet Union": ([10382, 10565, 15735, 25436, 34245, 40246, 20052], "red", "-"),
    "Britain": ([7940, 15049, 20094, 23672, 26263, 26461, 12070], "green", "--"),
    "Germany": ([8295, 10826, 11776, 15596, 25527, 39807, 7540], INK, "-"),
    "Japan": ([4467, 4768, 5088, 8861, 16693, 28180, 8263], "gold", "--"),
}
# where each name sits, beside the 1944 point or along the line
place = {"United States": (1944.1, 99000, "right"), "Soviet Union": (1944.15, 44500, "left"),
         "Germany": (1944.3, 35000, "left"), "Britain": (1940.3, 21000, "center"),
         "Japan": (1942.5, 5200, "center")}

fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.11, 0.1, 0.85, 0.8])
ax.set_facecolor(PAPER)
for name, (vals, col, ls) in data.items():
    c = FILL.get(col, col)
    ax.plot(years, vals, color=c, lw=4.2, ls=ls, marker="o", ms=10, mfc=c, mec=PAPER, mew=1.6, zorder=3)
    x, y, ha = place[name]
    ax.text(x, y, name, fontsize=21, color=c if col != INK else INK, ha=ha, va="center", fontweight="bold",
            path_effects=HALO, zorder=5)

ax.set_xlim(1938.6, 1945.4)
ax.set_ylim(0, 105000)
ax.set_xticks(years)
ax.set_yticks(range(0, 100001, 20000))
ax.set_yticklabels([f"{v:,}" for v in range(0, 100001, 20000)])
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.11, 0.95, "Aircraft built each year", fontsize=24, color=INK, fontweight="bold", ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/81-war/images/chart_aircraft.png")
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
