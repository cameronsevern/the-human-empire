#!/usr/bin/env python3
"""Chapter 107: how a message is sent in packets, drawn in the style of the book's maps, in the chapter's own
words. The message is chopped into small pieces; each piece carries the address it is going to and a number
giving its place in the sequence; each is sent off separately through a mesh of connected machines, each of
which passes it on to a neighbour closer to the destination; the pieces go by different routes, round a machine
that is busy or broken, and arrive out of order; the receiving machine puts them back together.

A schematic, not a map of any real network. The message, "LO AND BEHOLD", is the phrase the chapter ends on;
the address "SRI" is the research institute at the other end of the first link in 1969.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO, SOFT

W, H = 1600, 1000
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal"); ax.axis("off")

RED, BLUE, GREEN, GREY = FILL["red"], FILL["blue"], FILL["green"], "#cfc5b3"
T = dict(color=INK, path_effects=HALO, zorder=8, va="center")
COL = {1: RED, 2: BLUE, 3: GREEN}
STY = {1: "-", 2: (0, (5, 2.2)), 3: (0, (1.2, 1.6))}
WORD = {1: "LO", 2: "AND", 3: "BEHOLD"}


def num(x, y, n):
    ax.add_patch(Circle((x, y), 17, fc=INK, ec=PAPER, lw=2, zorder=9))
    ax.text(x, y - 1, str(n), ha="center", va="center", fontsize=17, fontweight="bold", color=PAPER, zorder=10)


def note(x, y, n, text):
    num(x, y, n)
    ax.text(x + 26, y, text, ha="left", fontsize=17, linespacing=1.15, **T)


def packet(x, y, n, w=200, h=76):
    """A packet with its lower-left corner at (x, y): a header (address, place) and a piece of the message."""
    ax.add_patch(Rectangle((x, y), w, h, fc=PAPER, ec=INK, lw=1.8, zorder=6))
    ax.add_patch(Rectangle((x, y + h * 0.52), w, h * 0.48, fc=COL[n], alpha=0.35, ec="none", zorder=6.1))
    ax.plot([x, x + w], [y + h * 0.52, y + h * 0.52], color=INK, lw=1.2, zorder=6.2)
    ax.text(x + w / 2, y + h * 0.76, f"to SRI, {n} of 3", ha="center", va="center", fontsize=15, color=INK,
            zorder=7)
    ax.text(x + w / 2, y + h * 0.26, WORD[n], ha="center", va="center", fontsize=19, fontweight="bold",
            color=INK, zorder=7)


def arrow(xy, colour=INK, lw=3.0, style="-"):
    xy = np.array(xy, float)
    seg = [np.linspace(a, b, 30, endpoint=False) for a, b in zip(xy[:-1], xy[1:])]
    xy = np.vstack(seg + [xy[-1:]])
    ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=lw + 4, solid_capstyle="round", zorder=3.5)
    ax.plot(xy[:-4, 0], xy[:-4, 1], color=colour, lw=lw, ls=style, solid_capstyle="round",
            dash_capstyle="round", zorder=4)
    ax.annotate("", xy=xy[-1], xytext=xy[-8], zorder=5,
                arrowprops=dict(arrowstyle="-|>,head_width=0.5,head_length=1.0", color=colour, lw=lw,
                                shrinkA=0, shrinkB=0))


# ------------------------------------------------------------------ the sending computer and its packets
ax.add_patch(FancyBboxPatch((20, 610), 290, 120, boxstyle="round,pad=0,rounding_size=14", fc="#e3d6bd", ec=INK,
                            lw=1.8, zorder=3))
ax.text(165, 700, "sending computer", ha="center", fontsize=17, style="italic", **T)
ax.text(165, 650, "LO AND BEHOLD", ha="center", fontsize=20, fontweight="bold", **T)
for n, y in [(1, 500), (2, 395), (3, 290)]:
    packet(65, y, n)
ax.plot([165, 165], [606, 584], color=INK, lw=1.6, zorder=3)
note(30, 900, 1, "The message is\nchopped into\nsmall pieces:\npackets")
note(30, 175, 2, "Each carries the address\nit is going to and its\nplace in the order")

# ------------------------------------------------------------------ the mesh of machines
N = {"A": (440, 640), "B": (440, 330), "C": (680, 770), "D": (680, 490), "E": (680, 230),
     "F": (900, 640), "G": (900, 360), "H": (1120, 770), "I": (1120, 500), "J": (1120, 230)}
links = ["AC", "AD", "BD", "BE", "CF", "DF", "DG", "EG", "FH", "FI", "GI", "GJ", "CH", "EJ", "AB"]
S0, S1 = (265, 540), (265, 330)                      # where the packets leave the sender's stack
R = (1300, 500)                                      # the receiving computer's left edge
for a, b in links:
    ax.plot(*zip(N[a], N[b]), color=GREY, lw=7, solid_capstyle="round", zorder=1)
for p in [N["H"], N["I"], N["J"]]:
    ax.plot(*zip(p, R), color=GREY, lw=7, solid_capstyle="round", zorder=1)
for k, (x, y) in N.items():
    broken = k == "D"
    ax.add_patch(Circle((x, y), 28, fc="#efe6d4" if broken else "#9fb8c8", ec=INK, lw=1.8, zorder=2))
    if broken:
        for s in (1, -1):
            ax.plot([x - 20, x + 20], [y - 20 * s, y + 20 * s], color="#8a3b2a", lw=4.5, solid_capstyle="round",
                    zorder=2.5)
ax.text(718, 490, "busy or\nbroken", ha="left", fontsize=17, style="italic", color="#8a3b2a", path_effects=HALO,
        zorder=8, va="center", linespacing=1.05)

# the three routes; packets sharing a link are drawn side by side
off = {1: np.array([0, 0]), 2: np.array([0, -10]), 3: np.array([0, 10])}
routes = {1: [(265, 538), N["A"], N["C"], N["H"], R],
          2: [(265, 433), N["B"], N["E"], N["J"], R],
          3: [(265, 328), N["B"], N["E"], N["G"], N["I"], R]}
for n, pts in routes.items():
    pts = [np.array(p, float) + off[n] for p in pts]
    pts[-1] = pts[-1] + np.array([-6, {1: 26, 2: -26, 3: 0}[n]])
    arrow(pts, colour=COL[n], lw=3.4, style=STY[n])
# a small tag on each route, naming its packet
for n, (x, y) in {1: (790, 810), 2: (900, 190), 3: (1010, 395)}.items():
    ax.add_patch(FancyBboxPatch((x - 72, y - 19), 144, 38, boxstyle="round,pad=0,rounding_size=6", fc=PAPER,
                                ec=COL[n], lw=2.2, zorder=7))
    ax.text(x, y, f"{n}: {WORD[n]}", ha="center", fontsize=16, fontweight="bold", **T)
note(440, 940, 3, "Each machine passes a packet on to a neighbour closer to\nthe destination; the pieces may go by different routes")
note(440, 70, 4, "If part of the mesh is busy or broken, the pieces go another way")

# ------------------------------------------------------------------ the receiving computer
ax.add_patch(FancyBboxPatch((1300, 420), 270, 160, boxstyle="round,pad=0,rounding_size=14", fc="#e3d6bd", ec=INK,
                            lw=1.8, zorder=3))
ax.text(1435, 545, "receiving computer", ha="center", fontsize=17, style="italic", **T)
ax.text(1435, 470, "LO AND BEHOLD", ha="center", fontsize=20, fontweight="bold", **T)
ax.text(1435, 870, "they arrive\nout of order:", ha="center", fontsize=17, style="italic", linespacing=1.1, **T)
for n, y in [(2, 760), (3, 670), (1, 590)]:
    packet(1335, y, n, h=70)
note(1290, 330, 5, "It puts them back\nin order by their\nnumbers")
out = lib.os.path.join(lib.ROOT, "chapters/107-internet/images/diagram_packets.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)
