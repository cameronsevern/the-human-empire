#!/usr/bin/env python3
"""Chapter 58: the island of Hispaniola about 1791. French Saint-Domingue in the western third and Spanish
Santo Domingo in the east, with the frontier between them; the northern plain, the sugar country where the
rising of 1791 began; Cap-Français and Port-au-Prince. An inset places the island in the Caribbean, with
Cuba, Jamaica and Louisiana.

Drawn for this chapter, which had no map. The frontier is the line of the Treaty of Aranjuez (1777), drawn
roughly after the maps of colonial Saint-Domingue in English and French Wikipedia ("Saint-Domingue",
"Traité d'Aranjuez (1777)"): from the mouth of the Massacre river south to the mouth of the Pedernales,
but bending west round the central plateau (Saint-Raphaël, Saint-Michel, Hinche), which was then Spanish.
The northern plain is drawn roughly as the lowland between Limbé, Cap-Français and Fort-Dauphin.
Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
from matplotlib.patches import Polygon as MplPoly
from lib import Map, INK, PAPER, FILL

SCRATCH = os.environ.get("SCRATCH", "/tmp")

m = Map(-74.65, -68.15, 17.35, 21.6)

BORDER = [(-71.73, 19.71), (-71.72, 19.55), (-71.95, 19.48), (-72.20, 19.47), (-72.42, 19.40), (-72.42, 19.22),
          (-72.22, 19.02), (-72.02, 18.88), (-71.93, 18.70), (-71.80, 18.55), (-71.78, 18.30), (-71.74, 18.03)]
west = BORDER + [(-71.6, 17.2), (-75.5, 17.2), (-75.5, 18.9), (-74.0, 19.6), (-73.6, 20.1), (-71.8, 20.3)]
east = BORDER + [(-71.6, 17.2), (-67.5, 17.2), (-67.5, 20.4), (-71.8, 20.4)]
m.region(west, "blue", alpha=0.36, smooth_n=1)
m.region(east, "gold", alpha=0.36, smooth_n=1)
m.line(BORDER, colour=INK, lw=2.4, style=(0, (5, 2.5)), curved=False)

# the northern plain
m.region([(-72.48, 19.70), (-72.25, 19.80), (-71.95, 19.76), (-71.76, 19.68), (-71.80, 19.55), (-72.05, 19.53),
          (-72.35, 19.57)], "green", alpha=0.55, hatch="//")
m.ax.annotate("northern plain", xy=(-72.3, 19.66), xytext=(-72.75, 19.74), fontsize=17, color=INK, style="italic",
              ha="right", va="center", zorder=7, path_effects=__import__("lib").HALO,
              arrowprops=dict(arrowstyle="-", color=INK, lw=1.0, shrinkA=2, shrinkB=0))

m.city(-72.20, 19.76, "Cap-Français", dx=0.0, dy=0.17, bold=True)
m.city(-72.34, 18.54, "Port-au-Prince", dx=0.1, dy=-0.17, ha="center", bold=True)

m.label(-73.45, 18.38, "SAINT-DOMINGUE", fs=21)
m.label(-73.45, 18.02, "French", size="land", fs=17)
m.label(-70.45, 18.95, "SANTO DOMINGO", fs=21)
m.label(-70.45, 18.72, "Spanish", size="land", fs=17)
m.label(-71.6, 20.45, "ATLANTIC OCEAN", size="sea", fs=20)
m.label(-72.7, 17.62, "CARIBBEAN SEA", size="sea", fs=20)
m.label(-74.4, 20.55, "Cuba", size="land", fs=17)
m.label(-72.78, 20.2, "Tortuga", size="land", fs=15)
m.scale(100, lon=-69.6, lat=17.55)

# ---------------------------------------------------------------- the inset: the Caribbean and Louisiana
IW, IE, IS, IN = -96.0, -64.0, 15.0, 34.0
FX0, FY0, FW = 0.633, 0.655, 0.355
n = Map(IW, IE, IS, IN, width=16.0 * FW, lakes=False)
n.river("Mississippi")
n.ax.add_patch(MplPoly([(-74.6, 17.4), (-68.2, 17.4), (-68.2, 21.1), (-74.6, 21.1)], closed=True, fc="none",
                       ec=FILL["red"], lw=2.2, zorder=6))
n.city(-90.07, 29.95, None, r=6)
n.label(-91.5, 32.3, "LOUISIANA", size="land", fs=15, style="normal")
n.label(-80.5, 24.0, "Cuba", size="land", fs=15, style="normal")
n.label(-77.4, 16.6, "Jamaica", size="land", fs=15, style="normal")
n.label(-71.3, 22.6, "Hispaniola", size="small", colour=FILL["red"], fs=15)
n.ax.add_patch(MplPoly([(IW, IS), (IE, IS), (IE, IN), (IW, IN)], closed=True, fc="none", ec=INK, lw=3, zorder=10))
pi = os.path.join(SCRATCH, "ch58_inset.png")
n.save(pi)

img = mpimg.imread(pi)
fh = m.fig.get_size_inches()[1]
ax = m.fig.add_axes([FX0, FY0, FW, img.shape[0] / 100.0 / fh])
ax.imshow(img)
ax.set_axis_off()
m.save("chapters/58-haiti/images/map_hispaniola.png")
