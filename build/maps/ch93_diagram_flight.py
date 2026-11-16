#!/usr/bin/env python3
"""Chapter 93: the flight plan of a Moon landing (as flown by Apollo 11 in July 1969), drawn in the style of
the book's maps. Left, the rocket as it stood, with the parts that were dropped one after another; right, the
path out and back: launch, the first and second stages falling away, one and a half turns round the Earth,
the third stage firing for the Moon, the main ship turning round to dock with the landing craft and pull it
free, three days' coasting, orbit round the Moon, two men going down while one stays in orbit, the top half of
the landing craft climbing back to meet the main ship in lunar orbit, the engine firing behind the Moon for
home, and the engine section dropped before the cone comes down by parachute in the Pacific.

Not to scale: the Moon is about thirty Earth-widths away, and the stack is drawn schematically. Sequence and
times after NASA's Apollo 11 mission report and English Wikipedia's "Apollo 11" and "Saturn V".
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, FancyBboxPatch
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO, SOFT

W, H = 1600, 1000
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal"); ax.axis("off")

RED, BLUE, GOLD, GREY = FILL["red"], FILL["blue"], FILL["gold"], "#d6cdbd"
T = dict(color=INK, path_effects=HALO, zorder=8, va="center")


def bez(p0, p1, p2, p3, n=120):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2, p3 = map(np.array, (p0, p1, p2, p3))
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def path(xy, colour=RED, lw=3.4, style="-", arrow=True):
    ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=lw + 3, solid_capstyle="round", zorder=3)
    end = -3 if arrow else None
    ax.plot(xy[:end, 0], xy[:end, 1], color=colour, lw=lw, ls=style, solid_capstyle="round", zorder=4)
    if arrow:
        ax.annotate("", xy=xy[-1], xytext=xy[-6], zorder=5,
                    arrowprops=dict(arrowstyle="-|>,head_width=0.45,head_length=0.9", color=colour, lw=lw,
                                    shrinkA=0, shrinkB=0))


def num(x, y, n):
    ax.add_patch(Circle((x, y), 17, fc=INK, ec=PAPER, lw=2, zorder=9))
    ax.text(x, y - 1, str(n), ha="center", va="center", fontsize=17, fontweight="bold", color=PAPER, zorder=10)


def note(x, y, n, text, ha="left"):
    num(x, y, n)
    ax.text(x + (26 if ha == "left" else -26), y, text, ha=ha, fontsize=17, linespacing=1.15, **T)


# ------------------------------------------------------------------ the rocket, as it stood
sx, sw = 150, 64
parts = [("first stage", 0, 250, GREY), ("second stage", 250, 150, GREY), ("third stage", 400, 105, GREY),
         ("landing craft", 505, 55, GOLD), ("engine section", 560, 50, "#c9c2b5"), ("the cone", 610, 0, None)]
y0 = 120
for name, a, h, col in parts[:-1]:
    ax.add_patch(Rectangle((sx - sw / 2, y0 + a), sw, h, fc=col, ec=INK, lw=1.6, zorder=3))
# the cone, with its escape tower
ax.add_patch(Polygon([(sx - sw / 2, y0 + 610), (sx + sw / 2, y0 + 610), (sx, y0 + 660)], closed=True, fc=BLUE,
                     ec=INK, lw=1.6, zorder=3))
ax.plot([sx, sx], [y0 + 660, y0 + 720], color=INK, lw=2.2, zorder=3)
for x in (-1, 1):                                            # fins and engines
    ax.add_patch(Polygon([(sx + x * sw / 2, y0 + 50), (sx + x * (sw / 2 + 22), y0), (sx + x * sw / 2, y0)],
                         closed=True, fc=GREY, ec=INK, lw=1.4, zorder=3))
for name, mid, ly in [("first stage: dropped\nafter two and a half\nminutes", y0 + 125, y0 + 125),
                      ("second stage:\ndropped after\nnine minutes", y0 + 325, y0 + 325),
                      ("third stage", y0 + 452, y0 + 452), ("landing craft", y0 + 532, y0 + 540),
                      ("main ship: its\nengine section", y0 + 585, y0 + 625),
                      ("main ship: the cone,\nthe crew's cabin and\nthe only part to\ncome home", y0 + 635, y0 + 735)]:
    ax.plot([sx + sw / 2 + 4, sx + sw / 2 + 22, sx + sw / 2 + 34], [mid, mid, ly], color=INK, lw=1.2, zorder=4)
    ax.text(sx + sw / 2 + 40, ly, name, ha="left", fontsize=17, linespacing=1.1, **T)
ax.text(sx, 50, "the rocket, 110 metres", ha="center", fontsize=18, fontweight="bold", **T)
ax.plot([455, 455], [40, 960], color=SOFT, lw=1.2, ls=(0, (4, 3)), zorder=1)

# ------------------------------------------------------------------ Earth, Moon and the path
E, RE, RO = np.array([700, 470]), 95, 125          # Earth centre, radius, parking orbit
M, RM, RL = np.array([1250, 520]), 48, 82           # Moon centre, radius, lunar orbit
ax.add_patch(Circle(E, RE, fc="#9fb8c8", ec=INK, lw=1.8, zorder=2))
ax.add_patch(Circle(M, RM, fc="#d9d3c7", ec=INK, lw=1.8, zorder=2))
ax.text(*E, "Earth", ha="center", fontsize=20, fontweight="bold", **T)
ax.text(M[0], M[1], "Moon", ha="center", fontsize=17, fontweight="bold", **T)
a = np.linspace(0, 2 * np.pi, 200)
ax.plot(E[0] + RO * np.cos(a), E[1] + RO * np.sin(a), color=RED, lw=2.2, ls=(0, (2, 2.4)), zorder=3.5)
ax.plot(M[0] + RL * np.cos(a), M[1] + RL * np.sin(a), color=RED, lw=2.2, ls=(0, (2, 2.4)), zorder=3.5)

pol = lambda c, r, deg: c + r * np.array([np.cos(np.radians(deg)), np.sin(np.radians(deg))])
# launch: from the surface up to the parking orbit
launch = bez(pol(E, RE, 200), pol(E, RE + 20, 185), pol(E, RO - 5, 175), pol(E, RO, 160))
path(launch, lw=3.4)
# out: from the parking orbit, behind the Moon
out = bez(pol(E, RO, 60), (860, 830), (1180, 820), pol(M, RL, 95))
path(out)
# home: from behind the Moon back to the Earth
home = bez(pol(M, RL, -80), (1150, 170), (880, 170), pol(E, RE + 6, -45))
path(home)
# the landing: down from lunar orbit to the surface, and back up
down = bez(pol(M, RL, 20), pol(M, RL - 8, 0), pol(M, RM + 12, -10), pol(M, RM, -20))
path(down, colour=GOLD, lw=3.0)
ax.add_patch(Polygon([pol(M, RM, -25) + d for d in [(-9, -4), (9, -4), (0, 12)]], closed=True, fc=GOLD, ec=INK,
                     lw=1.2, zorder=6))

note(483, 470, 1, "launch")
note(500, 300, 2, "one and a half turns\nround the Earth")
note(500, 800, 3, "the third stage fires for the Moon;\nthe main ship turns round, docks\nwith the landing craft and pulls\nit free; the third stage is cast off")
note(1300, 830, 4, "three days' coasting,\nthen into orbit round\nthe Moon, behind it")
note(1365, 650, 5, "two men go down\nin the landing\ncraft; one stays\nin orbit")
note(1365, 410, 6, "the top half of the\nlanding craft climbs\nback to meet the\nmain ship, and is\nthen cast off")
note(900, 110, 7, "the engine fires behind the Moon:\ntwo and a half days home")
note(560, 190, 8, "the engine section is dropped;\nthe cone comes down by\nparachute in the Pacific")
ax.text(1590, 975, "not to scale", ha="right", fontsize=17, style="italic", **T)
out_path = lib.os.path.join(lib.ROOT, "chapters/93-moon/images/diagram_flight_plan.png")
lib.os.makedirs(lib.os.path.dirname(out_path), exist_ok=True)
fig.savefig(out_path, dpi=100, facecolor=PAPER)
print("wrote", out_path)
