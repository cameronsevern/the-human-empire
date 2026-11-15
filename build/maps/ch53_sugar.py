#!/usr/bin/env python3
"""Chapter 53: the sugar islands of the Caribbean about 1750, with the power that held each: Spain (Cuba,
Puerto Rico, Santo Domingo, the eastern part of Hispaniola), Britain (Jamaica, Antigua, Barbados) and
France (Saint-Domingue, the western part of Hispaniola, Guadeloupe and Martinique). An inset in the lower left shows the
sugar coast of north-east Brazil, around Recife and Salvador, with the stretch the Dutch held from 1630
to 1654.

Drawn for this chapter, which had no map. Each island is filled whole from the Natural Earth coastline.
The line between Saint-Domingue and Santo Domingo was not fixed by treaty until 1777; it is drawn roughly
where it then ran, close to the modern border. Dutch Brazil is drawn roughly as the coast from the Sao
Francisco river to Rio Grande do Norte, after the map in English Wikipedia's article "Dutch Brazil"; at
its widest it reached further north. Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
from shapely.geometry import Point, box
from matplotlib.patches import Polygon as MplPoly
import lib
from lib import Map, INK, PAPER, FILL, SOFT

SCRATCH = os.environ.get("SCRATCH", "/tmp")
OWNER = {"Spanish": "gold", "British": "red", "French": "blue"}


def island(m, lon, lat, owner, cut=None, alpha=0.6):
    """Fill the land polygon under (lon, lat) in the owner's colour; cut is an optional box to keep."""
    hit = [p for p in getattr(m.land, "geoms", [m.land]) if p.contains(Point(lon, lat))]
    if not hit:
        hit = [min(getattr(m.land, "geoms", [m.land]), key=lambda p: p.distance(Point(lon, lat)))]
        print("nearest polygon used for", lon, lat)
    g = hit[0] if cut is None else hit[0].intersection(box(*cut))
    col = FILL[OWNER[owner]]
    for p in getattr(g, "geoms", [g]):
        if p.geom_type != "Polygon":
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=col, ec=col, lw=1.6, alpha=alpha, zorder=2))


def name(m, lon, lat, text, owner, ha="center"):
    m.label(lon, lat, text, size="small", colour=INK, fs=19, ha=ha, style="normal")
    m.ax.text(lon, lat - 0.62, owner, ha=ha, va="center", fontsize=17, color=SOFT, style="italic", zorder=7,
              path_effects=lib.HALO)


# ---------------------------------------------------------------- inset: north-east Brazil
b = Map(-41.6, -34.2, -13.6, -4.6, width=4.0)
b.region([(-36.3, -10.6), (-37.0, -10.0), (-35.9, -8.2), (-35.6, -6.0), (-35.6, -5.2), (-34.9, -5.0), (-34.5, -6.5),
          (-34.6, -8.2), (-35.4, -9.6)], "purple", alpha=0.55)
b.river("São Francisco", en=True)
b.city(-34.88, -8.05, "Recife", dx=-0.35, dy=0.0)
b.city(-38.51, -12.97, "Salvador", dx=0.4, dy=0.0)
b.label(-37.9, -7.0, "held by the\nDutch,\n1630-1654", size="small", colour=INK, fs=17)
b.label(-39.0, -11.3, "BRAZIL", size="land", fs=18, style="normal")
b.ax.text(-41.4, -4.85, "North-east Brazil", ha="left", va="top", fontsize=19, color=INK, fontweight="bold",
          zorder=8, path_effects=lib.HALO)
pb = os.path.join(SCRATCH, "ch53_brazil.png")
b.save(pb)

# ---------------------------------------------------------------- the Caribbean
W, E, S, N = -87.5, -57.0, 7.4, 24.6
m = Map(W, E, S, N)
island(m, -79.0, 21.8, "Spanish")                                  # Cuba
island(m, -66.5, 18.2, "Spanish")                                  # Puerto Rico
island(m, -77.3, 18.1, "British")                                  # Jamaica
island(m, -61.80, 17.08, "British", alpha=0.85)                    # Antigua
island(m, -59.55, 13.17, "British", alpha=0.85)                    # Barbados
island(m, -61.68, 16.15, "French", alpha=0.85)                     # Guadeloupe
island(m, -61.42, 16.32, "French", alpha=0.85)
island(m, -61.02, 14.65, "French", alpha=0.85)                     # Martinique
island(m, -72.5, 19.0, "French", cut=(-75.0, 17.5, -71.72, 20.2))    # Saint-Domingue
island(m, -70.0, 18.8, "Spanish", cut=(-71.72, 17.5, -68.0, 20.2))   # Santo Domingo
m.ax.plot([-71.72, -71.72], [18.05, 19.7], color=INK, lw=1.4, ls=(0, (3, 2)), zorder=3)

name(m, -79.3, 21.05, "Cuba", "Spanish")
name(m, -77.3, 17.2, "Jamaica", "British")
name(m, -73.7, 17.3, "Saint-Domingue", "French")
name(m, -69.5, 17.3, "Santo Domingo", "Spanish")
name(m, -66.4, 19.55, "Puerto Rico", "Spanish")
name(m, -61.15, 17.65, "Antigua", "British", ha="left")
name(m, -62.15, 16.25, "Guadeloupe", "French", ha="right")
name(m, -61.55, 14.7, "Martinique", "French", ha="right")
name(m, -59.55, 12.55, "Barbados", "British")

m.label(-71.5, 14.0, "Caribbean Sea", size="sea", fs=24)
m.label(-62.0, 22.0, "ATLANTIC\nOCEAN", size="sea", fs=20)
m.label(-73.0, 9.2, "SOUTH AMERICA", size="land", fs=18, style="normal")
m.scale(300, lon=-64.5, lat=8.2)
pa = os.path.join(SCRATCH, "ch53_caribbean.png")
m.save(pa)

# ---------------------------------------------------------------- the inset in the lower right corner
ia, ib = mpimg.imread(pa), mpimg.imread(pb)
H, Wd = ib.shape[:2]
out = ia.copy()
pad = 3
y0, x0 = out.shape[0] - H - pad, pad + 3
ink = np.array([int(INK[i:i + 2], 16) / 255 for i in (1, 3, 5)] + [1.0])
out[y0 - 3:y0 + H, x0:x0 + Wd + 3] = ink
out[y0:y0 + H, x0:x0 + Wd] = ib
dest = os.path.join(lib.ROOT, "chapters/53-sugar/images/map_sugar_islands.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
