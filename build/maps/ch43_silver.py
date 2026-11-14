#!/usr/bin/env python3
"""Chapter 43: the roads of the silver about 1600, on a world map centred on the Americas, so that the
Pacific crossing is unbroken (Asia on the left, Europe on the right). From Potosi down to the coast and
by sea to Lima and Panama, across the isthmus and by the Caribbean and the Atlantic fleets to Seville,
and on to Genoa and Antwerp; from Zacatecas to Mexico City, and from Mexico City to the Caribbean and to
Acapulco, and by the galleon to Manila, out in the tropics and home far to the north; from Manila to the
coast of Fujian. Two panels below show Mexico (Zacatecas, Mexico City, Acapulco) and the Andes
(Cajamarca, Lima, Huancavelica, Cuzco, Potosi) closer.

Drawn for this chapter, which had no map. The routes are simplified, after the routes usually drawn for
the Spanish treasure fleets and the Manila galleon about 1600 (as on the maps in English Wikipedia's
articles "Spanish treasure fleet" and "Manila galleon"): Potosi to the port of Arica and by sea to
Callao, the port of Lima; Panama to Portobelo across the isthmus; the fleets meeting at Havana and
sailing home by the Florida strait and the Azores. Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import lib
from lib import Map, INK, PAPER, FILL

SCRATCH = os.environ.get("SCRATCH", "/tmp")


def X(lon):
    """Longitudes west of 90 east are drawn 360 degrees over, to the right of the Pacific."""
    return lon if lon >= 90 else lon + 360


def P(pts):
    return [(X(a), b) for a, b in pts]


# ---------------------------------------------------------------- below: Mexico and the Andes, closer
PW = 7.93                        # inches: two panels and a gap make 1600 px
PH = 5.10


def panel(west, east, mid):
    """A frame PW by PH inches, true to shape at its middle latitude."""
    dlat = PH * (east - west) * np.cos(np.radians(mid)) / PW
    return west, east, mid - dlat / 2, mid + dlat / 2


MX = panel(-112.0, -89.0, 19.6)
AN = panel(-87.0, -59.0, -12.3)

c = Map(*MX, width=PW)
c.route([(-102.57, 22.77), (-100.8, 21.0), (-99.13, 19.43)], colour="red", lw=3.2, arrow=False)
c.route([(-99.13, 19.43), (-97.6, 19.6), (-96.14, 19.19), (-94.0, 20.6), (-91.0, 22.3), (-89.2, 23.3)],
        colour="red", lw=3.2)
c.route([(-99.13, 19.43), (-99.6, 18.0), (-99.88, 16.85)], colour="red", lw=3.2, arrow=False)
c.route([(-99.88, 16.85), (-104.0, 15.4), (-108.0, 14.4), (-111.8, 13.9)], colour="red", lw=3.2)
c.route([(-111.8, 24.4), (-108.5, 21.8), (-105.6, 19.2), (-102.6, 17.6), (-100.25, 17.0)], colour=INK, lw=2.4,
        style=(0, (4, 2.5)))
c.city(-102.57, 22.77, "Zacatecas", dx=0.6, dy=0.5, bold=True)
c.city(-99.13, 19.43, "Mexico City", dx=0.75, dy=-0.85, bold=True)
c.city(-99.88, 16.85, "Acapulco", dx=0.7, dy=-0.55, bold=True)
c.label(-109.6, 15.75, "to Manila", size="small", colour=FILL["red"], fs=17)
c.label(-109.5, 24.4, "from Manila", size="small", colour=INK, fs=17, ha="left")
c.label(-91.0, 20.0, "to Havana\nand Seville", size="small", colour=FILL["red"], fs=17)
c.label(-101.0, 25.8, "MEXICO", size="land", fs=17, style="normal", spaced=True)
c.label(-108.6, 18.4, "Pacific", size="sea", fs=17)
c.label(-93.5, 24.6, "Gulf of\nMexico", size="sea", fs=16)
c.scale(500, lon=-95.5, lat=MX[2] + 0.6)
pc = os.path.join(SCRATCH, "ch43_mexico.png")
c.save(pc)

b = Map(*AN, width=PW)
b.route([(-65.75, -19.59), (-68.0, -19.2), (-70.32, -18.48)], colour="red", lw=3.2, arrow=False)
b.route([(-70.32, -18.48), (-71.6, -17.6), (-74.5, -15.9), (-76.6, -13.6), (-77.25, -12.05), (-79.0, -9.0),
         (-80.8, -6.2), (-81.6, -4.0), (-81.0, -1.0), (-80.6, AN[3] - 0.2)], colour="red", lw=3.2)
b.city(-78.52, -7.16, "Cajamarca", dx=0.6, dy=0.0)
b.city(-77.03, -12.05, "Lima", dx=-0.7, dy=0.0)
b.city(-74.97, -12.79, "Huancavelica", dx=0.55, dy=0.9)
b.city(-71.97, -13.53, "Cuzco", dx=0.6, dy=-0.35)
b.city(-65.75, -19.59, "Potosí", dx=0.6, dy=0.0, bold=True)
b.label(-84.2, -4.4, "to Panama", size="small", colour=FILL["red"], fs=17)
b.label(-79.5, -18.0, "Pacific", size="sea", fs=17)
b.label(-66.0, -8.0, "ANDES", size="land", fs=17, style="normal", spaced=True)
b.scale(500, lon=-86.0, lat=AN[2] + 0.7)
pb = os.path.join(SCRATCH, "ch43_andes.png")
b.save(pb)

# ---------------------------------------------------------------- the world
W, E, S, N = 98.0, 392.0, -44.0, 61.0
m = Map(W, E, S, N)
pxdeg = 1600 / (E - W)

# the Atlantic fleets
silver = dict(colour="red", lw=3.2)
m.route(P([(-65.75, -19.59), (-70.32, -18.48), (-74.5, -15.9), (-77.25, -12.05), (-80.6, -6.0),
           (-81.0, 0.5), (-79.6, 7.0), (-79.52, 8.95)]), arrow=False, **silver)
m.route(P([(-79.52, 8.95), (-79.66, 9.55), (-76.5, 11.5), (-80.0, 17.0), (-82.36, 23.13), (-79.5, 26.5),
           (-72.0, 33.0), (-55.0, 38.0), (-30.0, 38.6), (-15.0, 37.5), (-6.4, 36.8)]), **silver)
m.route(P([(-102.57, 22.77), (-99.13, 19.43)]), arrow=False, **silver)
m.route(P([(-99.13, 19.43), (-96.14, 19.19), (-91.0, 22.4), (-85.0, 23.6), (-82.6, 23.3)]), arrow=False, **silver)
m.route(P([(-6.0, 36.6), (-5.6, 35.95), (0.0, 37.2), (5.0, 40.0), (8.4, 43.9)]), **silver)
m.route(P([(-6.4, 36.9), (-9.6, 38.5), (-9.8, 43.5), (-5.0, 47.6), (0.0, 50.0), (3.4, 51.6)]), **silver)
# the galleon: out with the trade winds, home far to the north
m.route(P([(-99.13, 19.43), (-99.88, 16.85)]), arrow=False, **silver)
m.route(P([(-99.88, 16.85), (-110.0, 14.0), (-140.0, 13.0), (170.0, 13.4), (144.7, 13.4), (130.0, 13.2),
           (124.5, 12.6), (121.6, 13.6), (120.98, 14.6)]), **silver)
m.route(P([(121.2, 15.8), (125.0, 22.0), (135.0, 32.0), (150.0, 37.0), (180.0, 40.0), (-150.0, 41.0),
           (-127.0, 40.0), (-117.0, 32.0), (-106.0, 22.0), (-100.6, 17.6)]), colour=INK, lw=2.4,
        style=(0, (4, 2.5)))
m.route([(120.6, 15.2), (119.8, 19.5), (118.6, 23.6)], **silver)

for ext in (MX, AN):
    m.ax.add_patch(Rectangle((X(ext[0]), ext[2]), ext[1] - ext[0], ext[3] - ext[2], fc="none", ec=INK, lw=1.3,
                             ls=(0, (3, 2)), zorder=5))

# places
m.city(X(-79.52), 8.95, "Panama", dx=-1.6, dy=-0.4)
m.city(X(-5.98), 37.39, "Seville", dx=-1.0, dy=-4.6, bold=True)
m.city(X(8.93), 44.41, "Genoa", dx=1.4, dy=0.0)
m.city(X(4.40), 51.22, "Antwerp", dx=1.4, dy=1.0)
m.city(120.98, 14.60, "Manila", dx=1.6, dy=-1.0, bold=True)
m.label(113.0, 26.5, "FUJIAN", fs=17)
m.label(109.5, 35.0, "CHINA", size="land", fs=19, style="normal")

m.label(X(-160.0), 18.4, "the galleon from Acapulco", size="small", colour=FILL["red"], fs=18)
m.label(X(-170.0), 45.6, "the galleon home", size="small", colour=INK, fs=18)
m.label(X(-45.0), 42.2, "the treasure fleets", size="small", colour=FILL["red"], fs=18)
m.label(X(-160.0), 29.0, "PACIFIC OCEAN", size="sea", fs=22)
m.label(X(-38.0), 18.0, "ATLANTIC\nOCEAN", size="sea", fs=20)
pa = os.path.join(SCRATCH, "ch43_world.png")
m.save(pa)

# ---------------------------------------------------------------- the world above, the two panels below
ia, ic, ib = (mpimg.imread(p) for p in (pa, pc, pb))
h = min(ic.shape[0], ib.shape[0])
paper = np.array([int(lib.PAPER[i:i + 2], 16) / 255 for i in (1, 3, 5)] + [1.0])
row = np.hstack([ic[:h], np.tile(paper, (h, 1600 - ic.shape[1] - ib.shape[1], 1)), ib[:h]])
out = np.vstack([ia, np.tile(paper, (14, 1600, 1)), row])
dest = os.path.join(lib.ROOT, "chapters/43-silver/images/map_silver_routes.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
