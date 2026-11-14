#!/usr/bin/env python3
"""Chapter 42: central Mexico in 1519-21, in two panels. Above: the Gulf coast where Cortes landed at
Veracruz in 1519 and his march inland to Tlaxcala and on to Tenochtitlan. Below, closer: the last stage
of the march, from Tlaxcala by Cholula and Huejotzingo over the pass between the two volcanoes, and the
lake, with Tenochtitlan on its island, its three causeways to Tepeyac, Tlacopan and Iztapalapa, and
Texcoco on the eastern shore.

Drawn for this chapter, which had no map. Natural Earth has no lake here, since the lake was drained
after the conquest, so its shore is drawn by hand: roughly, after the usual reconstructions of the
lakes of the Valley of Mexico about 1519 (as on the map in English Wikipedia's article "Lake Texcoco"),
using the old lakeside towns as fixed points: Azcapotzalco, Tlacopan and Chapultepec on the west shore,
Tepeyac and Ecatepec in the north, Atenco, Texcoco and Chimalhuacan in the east, the Iztapalapa
peninsula, and Coyoacan, Xochimilco, Cuitlahuac and Chalco on the southern lakes. The island and the
causeways follow the same reconstructions. The route is simplified, after the route usually drawn for
1519: Veracruz, Xalapa, the high plain north of the Cofre de Perote, Tlaxcala, Cholula, Huejotzingo,
the pass between Popocatepetl and Iztaccihuatl, Amecameca, Iztapalapa. Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
from matplotlib.patches import Polygon as MplPoly, Rectangle
import lib
from lib import Map, INK, PAPER, SEA, SHORE, FILL, smooth

SCRATCH = os.environ.get("SCRATCH", "/tmp")

# the lakes about 1519 (roughly): Texcoco, joined to Xochimilco and Chalco in the south
lake = [(-99.180, 19.488), (-99.150, 19.492), (-99.120, 19.497), (-99.088, 19.512), (-99.068, 19.550),
        (-99.052, 19.590), (-99.036, 19.615), (-99.000, 19.617), (-98.966, 19.592), (-98.938, 19.556),
        (-98.920, 19.520), (-98.925, 19.480), (-98.942, 19.450), (-98.962, 19.432), (-98.958, 19.400),
        (-98.966, 19.374), (-98.995, 19.364), (-99.035, 19.363), (-99.070, 19.365), (-99.098, 19.361),
        (-99.116, 19.354), (-99.119, 19.344), (-99.098, 19.331), (-99.050, 19.318), (-99.005, 19.305),
        (-98.965, 19.302), (-98.932, 19.298), (-98.900, 19.288), (-98.878, 19.268), (-98.892, 19.246),
        (-98.940, 19.232), (-98.990, 19.244), (-99.040, 19.250), (-99.090, 19.255), (-99.128, 19.266),
        (-99.152, 19.290), (-99.160, 19.320), (-99.157, 19.345), (-99.168, 19.375), (-99.180, 19.420),
        (-99.181, 19.455), (-99.182, 19.475)]
xaltocan = [(-99.085, 19.640), (-99.030, 19.636), (-98.985, 19.660), (-98.962, 19.700), (-98.980, 19.760),
            (-99.040, 19.800), (-99.100, 19.800), (-99.130, 19.750), (-99.112, 19.690)]
island = [(-99.160, 19.426), (-99.150, 19.416), (-99.130, 19.414), (-99.116, 19.424), (-99.114, 19.440),
          (-99.124, 19.459), (-99.140, 19.466), (-99.155, 19.457), (-99.163, 19.440)]
causeways = [
    [(-99.134, 19.462), (-99.127, 19.478), (-99.120, 19.496)],                    # north, to Tepeyac
    [(-99.161, 19.446), (-99.171, 19.450), (-99.182, 19.455)],                    # west, to Tlacopan
    [(-99.133, 19.414), (-99.134, 19.395), (-99.135, 19.378)],                    # south
    [(-99.135, 19.378), (-99.147, 19.366), (-99.158, 19.352)],                    # to Coyoacan
    [(-99.135, 19.378), (-99.118, 19.368), (-99.095, 19.362)],                    # to Iztapalapa
]
VOLCANOES = [(-98.622, 19.023), (-98.642, 19.179)]
route = [(-96.14, 19.19), (-96.42, 19.42), (-96.92, 19.54), (-97.35, 19.62), (-97.82, 19.62), (-98.05, 19.46),
         (-98.237, 19.318), (-98.303, 19.063), (-98.405, 19.159), (-98.55, 19.12), (-98.65, 19.09),
         (-98.765, 19.125), (-98.86, 19.22), (-98.97, 19.30), (-99.04, 19.35), (-99.095, 19.362),
         (-99.135, 19.378), (-99.134, 19.410)]


def draw_lakes(m, lw=1.0):
    for pts in (lake, xaltocan):
        m.ax.add_patch(MplPoly(smooth(pts, n=6, closed=True), closed=True, fc=SEA, ec=SHORE, lw=lw, zorder=1.3))


def volcanoes(m, ms):
    for lon, lat in VOLCANOES:
        m.ax.plot(lon, lat, "^", ms=ms, mfc=FILL["brown"], mec=INK, mew=1.2, zorder=6)


# ---------------------------------------------------------------- above: from the coast
W, E, S, N = -99.80, -95.92, 18.86, 19.86
a = Map(W, E, S, N, lakes=False)
draw_lakes(a, lw=0.8)
BX0, BX1, BY0, BY1 = -99.33, -97.98, 18.955, 19.645       # the lower panel
a.ax.add_patch(Rectangle((BX0, BY0), BX1 - BX0, BY1 - BY0, fc="none", ec=INK, lw=1.4, ls=(0, (4, 2)), zorder=4))
a.route(route[:7], colour="red", lw=3.4, arrow=False)
a.route(route[6:], colour="red", lw=3.4)
volcanoes(a, 12)
a.label(-97.25, 19.76, "Cortés's march, 1519", size="small", colour=FILL["red"], fs=20)
a.city(-99.133, 19.433, "Tenochtitlan", dx=-0.08, dy=0.0, bold=True)
a.city(-98.237, 19.318, "Tlaxcala", dx=0.07, dy=0.0, bold=True)
a.city(-96.14, 19.19, "Veracruz", dx=-0.07, dy=0.02, bold=True)
a.label(-96.21, 19.10, "landing, 1519", size="small", colour=INK, fs=17, ha="right")
a.label(-96.55, 19.84 - 0.12, "Gulf of\nMexico", size="sea", fs=20)
a.label(-97.20, 18.95, "M E X I C A N   H I G H L A N D S", size="land", fs=16)
a.scale(50, lon=-97.40, lat=19.20)
pa = os.path.join(SCRATCH, "ch42_a.png")
a.save(pa)

# ---------------------------------------------------------------- below: the valley and the lake
b = Map(BX0, BX1, BY0, BY1, lakes=False)
draw_lakes(b, lw=1.4)
b.ax.add_patch(MplPoly(smooth(island, n=6, closed=True), closed=True, fc=FILL["gold"], ec=INK, lw=1.4, alpha=0.8,
                       zorder=3))
b.route(route[6:-2], colour="red", lw=3.6)
for pts in causeways:
    c = np.array(pts)
    b.ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=8, solid_capstyle="round", zorder=4.5)
    b.ax.plot(c[:, 0], c[:, 1], color=INK, lw=4, solid_capstyle="round", zorder=4.6)
volcanoes(b, 20)

b.label(-99.000, 19.545, "Lake\nTexcoco", size="sea", fs=21)
b.label(-99.105, 19.440, "Tenochtitlan", size="small", colour=INK, fs=19, ha="left", style="normal")
b.city(-99.120, 19.496, "Tepeyac", dx=0.0, dy=0.022, size=17)
b.city(-99.188, 19.457, "Tlacopan", dx=-0.012, dy=0.0, size=17)
b.city(-99.090, 19.358, "Iztapalapa", dx=0.0, dy=-0.050, size=17)
b.city(-98.882, 19.514, "Texcoco", dx=0.014, dy=0.0, size=17, bold=True)
b.city(-98.237, 19.318, "Tlaxcala", dx=0.016, dy=0.012, bold=True, size=18)
b.city(-98.303, 19.063, "Cholula", dx=0.016, dy=-0.012, size=18)
b.city(-98.405, 19.159, "Huejotzingo", dx=0.0, dy=0.034, size=18)
b.label(-98.622, 18.985, "Popocatépetl", size="small", colour=INK, fs=17)
b.label(-98.642, 19.222, "Iztaccíhuatl", size="small", colour=INK, fs=17)
b.label(-98.70, 19.580, "the Valley of Mexico, 1519", size="small", colour=INK, fs=19)
b.scale(10, lon=-98.20, lat=BY0 + 0.02)
pb = os.path.join(SCRATCH, "ch42_b.png")
b.save(pb)

# ---------------------------------------------------------------- one above the other
ia, ib = mpimg.imread(pa), mpimg.imread(pb)
gap = np.ones((14, 1600, 4))
gap[:, :, :3] = np.array([int(PAPER[i:i + 2], 16) / 255 for i in (1, 3, 5)])
out = np.vstack([ia, gap, ib])
dest = os.path.join(lib.ROOT, "chapters/42-aztecs/images/map_mexico_1519.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
