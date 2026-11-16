#!/usr/bin/env python3
"""Chapter 113: nuclear warheads in the world, 1945 to 2025, drawn in the style of the book's maps: the stockpiles
of the United States, of the Soviet Union and then Russia, and of all other countries together, and the world's
total including warheads retired and awaiting dismantling.

Data: Federation of American Scientists (Hans Kristensen, Matt Korda and colleagues), "Estimated Global Nuclear
Warhead Inventories", as published by Our World in Data, grapher "nuclear-warhead-stockpiles" (FAS 2026 release,
OWID update of 13 May 2026; read November 2026), years 1945 to 2025; 2026 left out. The country figures are
stockpiles: warheads assigned to military forces, excluding retired warheads awaiting dismantling. The world line
is FAS's total inventory, which includes those retired warheads (OWID: "Retired warheads are only included in the
global total"); in a few early years it is slightly lower than the sum of the stockpiles, because the two come from
different FAS tables. All figures are estimates, since the true numbers are secret. "All others" is the sum of
China, France, the United Kingdom, India, Pakistan, Israel, North Korea and South Africa (which held a few in the
1980s and dismantled them).

Against the chapter: peak 70,374 in 1986 (the 1980s); 12,241 in 2025, "about twelve thousand", a fall of 83 per cent
("more than four fifths"). "Russia and the United States hold nearly nine tenths": of the total inventory in FAS's
2025 figures (5,459 and 5,177 of 12,241, 87 per cent); of the stockpiles shown by country here, 83 per cent.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

YEARS = list(range(1945, 2026))
# FAS via OWID, stockpiles by country, and world total inventory (including retired), 1945-2025
US = [
    2, 9, 13, 50, 170, 299, 438, 841, 1169, 1703, 2422, 3692, 5543, 7345, 12298, 18638, 22229, 25540, 28133,
    29463, 31139, 31175, 31255, 29561, 27552, 26008, 25830, 26516, 27835, 28537, 27519, 25914, 25542, 24418,
    24138, 24104, 23208, 22886, 23305, 23459, 23368, 23317, 23575, 23205, 22217, 21392, 19008, 13708, 11511,
    10979, 10904, 11011, 10903, 10732, 10685, 10577, 10526, 10457, 10027, 8570, 8360, 7853, 5709, 5273, 5113,
    5066, 4897, 4881, 4804, 4717, 4571, 4018, 3822, 3785, 3805, 3750, 3713, 3768, 3748, 3708, 3700]
RU = [
    0, 0, 0, 0, 1, 5, 25, 50, 120, 150, 200, 426, 660, 863, 1048, 1627, 2492, 3346, 4259, 5242, 6144, 7091,
    8400, 9490, 10671, 11736, 13279, 14600, 15878, 17286, 19235, 22165, 24281, 26169, 28258, 30665, 32146,
    33486, 35130, 36825, 38582, 40159, 38107, 36538, 35078, 32980, 29154, 26734, 24403, 21339, 18179, 15942,
    15442, 14368, 13188, 12188, 11152, 10114, 9076, 8038, 7000, 6643, 6286, 5929, 5527, 5215, 4858, 4750, 4650,
    4600, 4500, 4490, 4300, 4350, 4330, 4310, 4495, 4477, 4489, 4380, 4309]
OTHERS = [
    0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 10, 50, 58, 60, 78, 105, 155, 211, 256, 276, 308, 337, 418, 392, 398, 494,
    568, 636, 781, 832, 888, 914, 932, 951, 959, 986, 1017, 913, 918, 893, 977, 976, 1047, 1042, 1047, 1140,
    1180, 1082, 1069, 1056, 1031, 951, 951, 995, 1008, 1081, 977, 990, 1003, 1016, 1027, 1003, 1020, 990, 1015,
    1015, 1035, 1055, 1070, 1075, 1105, 1120, 1150, 1185, 1200, 1280, 1320, 1345, 1379, 1497, 1605]
WORLD = [
    6, 11, 32, 110, 236, 374, 665, 1055, 1557, 2218, 3267, 5094, 7162, 10751, 16606, 22144, 26752, 30920, 33953,
    36553, 38419, 39466, 39990, 39015, 38278, 38799, 40616, 43026, 45695, 47182, 47769, 47698, 49698, 51170,
    53499, 55352, 56530, 58570, 60818, 62678, 64408, 70374, 68387, 65623, 63657, 61229, 58326, 52463, 48830,
    45580, 42366, 39484, 36776, 35387, 34677, 34004, 33190, 31902, 30820, 29627, 28358, 27061, 25533, 23855,
    22524, 21234, 20035, 18855, 17680, 16370, 15795, 15228, 14540, 14470, 13865, 13145, 13100, 12705, 12512,
    12121, 12241]

for s in (US, RU, OTHERS, WORLD):
    assert len(s) == len(YEARS)
W = dict(zip(YEARS, WORLD))
pk = max(W, key=W.get)
print("world peak:", pk, W[pk], " 2025:", W[2025], " fall:", round(1 - W[2025] / W[pk], 3))

RED, BLUE, GOLD = FILL["red"], FILL["blue"], FILL["gold"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.085, 0.1, 0.885, 0.8])
ax.set_facecolor(PAPER)


def line(v, colour, style, lw=4.0, z=4):
    ax.plot(YEARS, v, color=PAPER, lw=lw + 4.5, solid_capstyle="round", zorder=z - 0.5)
    ax.plot(YEARS, v, color=colour, lw=lw, ls=style, solid_capstyle="round", dash_capstyle="round", zorder=z)


line(WORLD, INK, (0, (1.2, 1.8)), lw=3.4, z=5)
line(US, BLUE, "-")
line(RU, RED, (0, (5, 2.2)))
line(OTHERS, GOLD, "-", lw=4.6)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=7, linespacing=1.1)
C = {k: v for k, v in T.items() if k != "color"}
ax.text(1960.5, 33500, "United States", ha="right", va="center", color="#2f5577", **C)
ax.text(1980.5, 37500, "Soviet Union,\nthen Russia", ha="right", va="center", color="#8a3b2a", **C)
ax.text(1975, 1900, "all other countries", ha="center", va="bottom", color="#8a6416", **C)
ax.text(1999, 42000, "all warheads, including\nthose retired and\nawaiting dismantling", ha="left", va="bottom",
        **T)
ax.plot(pk, W[pk], "o", ms=10, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
ax.text(pk - 2, W[pk] + 600, "about 70,000\nin 1986", ha="right", va="bottom", **T)
ax.plot(2025, W[2025], "o", ms=10, mfc=INK, mec=PAPER, mew=1.6, zorder=6)
ax.text(2025, W[2025] + 2800, "about\n12,000\nin 2025", ha="center", va="bottom", **T)

ax.set_xlim(1943, 2029)
ax.set_ylim(0, 78000)
ticks = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000]
ax.yaxis.set_major_locator(FixedLocator(ticks))
ax.set_yticklabels([f"{t:,}" for t in ticks])
ax.set_xticks(range(1945, 2026, 10))
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
ax.grid(axis="y", color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(INK)
ax.spines["bottom"].set_linewidth(1.6)
fig.text(0.085, 0.95, "Nuclear warheads in the world, estimated", fontsize=24, color=INK, fontweight="bold",
         ha="left", va="center")
out = lib.os.path.join(lib.ROOT, "chapters/113-survival/images/chart_warheads.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
