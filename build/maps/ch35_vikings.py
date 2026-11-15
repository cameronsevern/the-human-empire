#!/usr/bin/env python3
"""Chapter 35: the Viking world, in two panels. Above: the North Atlantic, with the voyages west from
Norway to Iceland (about 870), Greenland (about 985) and Newfoundland (about 1000), the two Greenland
settlements and L'Anse aux Meadows. Below: Europe from Ireland to the Caspian, with the homelands
(Norway, Denmark, Sweden), the raids and settlements in the west by sea (Lindisfarne, the Danish part of
England with York, Dublin, the Seine to Paris and Normandy), and the river roads of the Rus in the east,
from Sweden to Novgorod, down the Dnieper by Kiev to the Black Sea and Constantinople, and down the Volga
to the Caspian, where the merchants of the caliphate of Baghdad came to buy.

Drawn for this chapter, which had no map. The routes are simplified, after the routes usually drawn for
the Viking age (as on the maps in English Wikipedia's articles "Viking expansion", "Trade route from the
Varangians to the Greeks" and "Volga trade route"). The Danish part of England is drawn roughly, as the
land north and east of the line agreed between Alfred and the Danes (the Thames, the Lea and Watling
Street) up to the Tees; Normandy roughly as it was about 933. Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
import lib
from lib import Map, INK, PAPER, FILL

SCRATCH = os.environ.get("SCRATCH", "/tmp")
SEA_R = dict(colour="red", lw=3.4)                        # west, by sea: solid
RIV_R = dict(colour="blue", lw=3.6, style=(0, (2.2, 1.3)))  # east, by river: dashed

# ---------------------------------------------------------------- above: the North Atlantic
a = Map(-62.0, 12.0, 48.0, 67.5, lakes=False)
a.region([(5.0, 58.0), (7.5, 57.9), (11.0, 59.0), (12.5, 61.5), (13.5, 64.5), (16.0, 68.5), (10.0, 68.5),
          (6.0, 64.0), (4.5, 61.5)], "gold")
a.route([(5.0, 61.2), (0.0, 62.0), (-7.0, 62.3), (-12.0, 63.6), (-13.8, 64.5)], **SEA_R)
a.route([(-22.0, 63.8), (-30.0, 62.6), (-38.0, 60.6), (-43.2, 59.6), (-45.6, 60.6)], **SEA_R)
a.route([(-47.5, 60.2), (-51.0, 57.5), (-54.0, 54.5), (-55.3, 52.0)], **SEA_R)

a.city(-55.53, 51.60, "L'Anse aux Meadows", dx=0.0, dy=-1.15, bold=True)
a.city(-45.50, 61.15, "Eastern\nSettlement", dx=1.2, dy=0.3)
a.city(-50.30, 64.40, "Western\nSettlement", dx=1.2, dy=0.0)
a.label(-18.6, 64.95, "ICELAND", fs=21)
a.label(-40.0, 66.0, "GREENLAND", fs=21)
a.label(8.6, 62.0, "NORWAY", fs=17)
a.label(-57.5, 59.3, "NORTH\nAMERICA", size="land", fs=18, style="normal")
a.label(-27.0, 53.5, "Atlantic Ocean", size="sea", fs=22)
a.label(-6.5, 64.4, "about 870", size="small", colour=INK, fs=17)
a.label(-31.5, 60.5, "about 985", size="small", colour=INK, fs=17)
a.label(-50.6, 55.2, "about 1000", size="small", colour=INK, fs=17, ha="left")
a.scale(500, lon=-20.0, lat=49.6)
pa = os.path.join(SCRATCH, "ch35_atlantic.png")
a.save(pa)

# ---------------------------------------------------------------- below: Europe and the rivers
b = Map(-11.0, 56.0, 31.0, 64.0)
b.river("Seine", "Volga", "Volkhov", "Neva", "Thames")
b.river("Dnieper", en=True)
# the homelands
b.region([(5.0, 58.0), (7.5, 57.9), (10.0, 58.9), (11.4, 58.0), (12.4, 56.3), (14.3, 55.4), (16.3, 56.4),
          (16.8, 58.2), (19.0, 59.6), (18.0, 62.5), (17.5, 65.5), (5.0, 65.5), (4.6, 61.0)], "gold")
b.region([(8.0, 54.6), (12.6, 54.6), (12.9, 56.3), (10.6, 58.0), (8.0, 57.2)], "gold")
# the Danish part of England, roughly
b.region([(-0.1, 51.5), (1.9, 51.6), (1.9, 53.0), (0.2, 53.6), (-0.6, 54.6), (-1.3, 54.7), (-2.4, 54.4),
          (-2.6, 53.2), (-1.4, 52.4), (-0.4, 51.9)], "red")
# Normandy, roughly
b.region([(-1.95, 49.75), (-1.6, 48.6), (0.0, 48.45), (1.75, 49.1), (1.6, 50.0), (0.1, 49.75), (-1.0, 49.5)], "red")

# west, by sea
b.route([(5.0, 60.3), (1.5, 58.9), (-0.9, 57.3), (-1.6, 56.0)], **SEA_R)                     # to Lindisfarne
b.route([(4.8, 60.8), (-1.0, 60.9), (-5.8, 59.7), (-8.4, 57.8), (-7.1, 56.2), (-5.85, 55.45), (-5.2, 54.5), (-5.65, 53.5)], **SEA_R)  # to Dublin
b.route([(8.0, 55.8), (4.5, 54.4), (1.6, 53.6), (0.3, 53.6)], **SEA_R)                       # to England
b.route([(8.0, 55.2), (5.4, 53.8), (3.0, 52.0), (1.2, 50.6), (0.15, 49.55)], **SEA_R)        # to the Seine
b.route([(0.15, 49.55), (0.9, 49.35), (1.6, 49.15), (2.25, 48.95)], colour="red", lw=3.0,
        style=(0, (2.2, 1.3)))                                                                 # up the Seine
# east, by river
nov = [(17.8, 59.4), (21.5, 59.6), (25.5, 59.9), (29.8, 59.95), (31.6, 60.2), (32.3, 59.6), (31.8, 58.9), (31.3, 58.55)]
b.route(nov, arrow=False, **RIV_R)
b.route([(31.3, 58.5), (31.4, 57.2), (31.6, 55.6), (32.0, 54.8), (30.6, 53.0), (30.5, 50.5), (31.6, 48.6),
         (34.0, 47.6), (32.6, 46.6), (31.4, 44.6), (29.6, 42.0), (29.05, 41.2)], **RIV_R)      # the Dnieper
b.route([(31.3, 58.5), (34.0, 57.4), (36.0, 56.9), (39.9, 57.6), (44.0, 56.3), (49.0, 55.8), (49.6, 53.4),
         (46.2, 51.6), (45.0, 49.0), (47.0, 47.4), (48.4, 46.2), (49.6, 45.0)], **RIV_R)       # the Volga

b.city(-1.80, 55.68, "Lindisfarne, 793", dx=0.6, dy=-0.35, bold=True)
b.city(-1.08, 53.96, "York", dx=-0.55, dy=-0.15)
b.city(-6.26, 53.35, "Dublin", dx=-0.6, dy=0.0)
b.city(2.35, 48.86, "Paris, 845", dx=0.6, dy=-0.2)
b.city(31.27, 58.52, "Novgorod", dx=0.9, dy=0.0, bold=True)
b.city(30.52, 50.45, "Kiev", dx=-0.8, dy=0.0, bold=True)
b.city(28.98, 41.01, "Constantinople", dx=-0.8, dy=-0.3, bold=True)
b.city(44.37, 33.31, "Baghdad", dx=0.8, dy=0.0, bold=True)

b.label(8.5, 61.4, "NORWAY", fs=20)
b.label(15.3, 60.2, "SWEDEN", fs=20)
b.label(9.15, 56.15, "DENMARK", fs=16, rot=90)
b.label(-0.75, 53.0, "DANES", fs=15)
b.label(-0.5, 48.0, "NORMANDY, 911", fs=17)
b.label(2.5, 46.6, "FRANKS", size="land", fs=19, style="normal")
b.label(38.0, 53.5, "the Rus", size="land", fs=21, style="normal")
b.label(44.5, 36.0, "THE CALIPHATE", size="land", fs=17, style="normal")
b.label(33.6, 51.6, "Dnieper", size="sea", fs=17, rot=-70)
b.label(46.7, 52.2, "Volga", size="sea", fs=17, rot=58)
b.label(4.6, 57.1, "North\nSea", size="sea", fs=19)
b.label(19.0, 56.6, "Baltic\nSea", size="sea", fs=20)
b.label(34.5, 43.3, "Black Sea", size="sea", fs=20)
b.label(51.0, 42.0, "Caspian\nSea", size="sea", fs=18)
b.label(18.0, 35.0, "Mediterranean Sea", size="sea", fs=20)
b.label(-7.0, 46.0, "Atlantic\nOcean", size="sea", fs=20)
b.label(-3.3, 61.5, "by sea", size="small", colour=FILL["red"], fs=19, style="italic")
b.label(26.0, 61.3, "by river", size="small", colour=FILL["blue"], fs=19, style="italic")
b.scale(500, lon=-9.5, lat=33.0)
pb = os.path.join(SCRATCH, "ch35_europe.png")
b.save(pb)

# ---------------------------------------------------------------- one above the other
ia, ib = mpimg.imread(pa), mpimg.imread(pb)
gap = np.ones((14, 1600, 4))
gap[:, :, :3] = np.array([int(PAPER[i:i + 2], 16) / 255 for i in (1, 3, 5)])
out = np.vstack([ia, gap, ib])
dest = os.path.join(lib.ROOT, "chapters/35-vikings/images/map_vikings.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
