#!/usr/bin/env python3
"""Chapter 60: Spanish and Portuguese America about 1800, and the countries of South America in 1830.

The main map: the four viceroyalties (New Spain, New Granada, Peru and Río de la Plata) and Portuguese
Brazil, with Venezuela and Chile named within them; Mexico City, Caracas, Bogotá, Quito, Lima, Cuzco,
Santiago, Buenos Aires and Rio de Janeiro; Bolívar's road from Angostura over the Andes to Bogotá (1819)
and on by Quito and Guayaquil to Lima and Ayacucho (1824); San Martín's from Mendoza over the Andes to
Santiago (1817) and by sea to Lima (1821). The inset: South America in 1830, after Bolívar's Colombia had
broken into Venezuela, New Granada and Ecuador.

Drawn for this chapter, which had no map. All borders are rough. The viceroyalties are drawn after the
maps in English Wikipedia's articles on each viceroyalty and "Spanish Empire"; Central America, under a
captain-general who answered to the viceroy of New Spain, is shaded with New Spain, and the islands are
left out. The borders of 1830 are drawn after English Wikipedia's maps of South America in 1830 and
"Gran Colombia": Bolivia still has its Pacific coast and Peru reaches south to the Loa; the Chaco and the
far south (Patagonia), outside any state's control, are left unshaded; boundaries in the Amazon were
undefined, and are drawn near the later ones. The routes follow the usual lines of the campaigns.
Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
from matplotlib.patches import Polygon as MplPoly
from shapely.geometry import Polygon
from shapely.ops import unary_union
from lib import Map, INK, PAPER, FILL

SCRATCH = os.environ.get("SCRATCH", "/tmp")


def P(pts):
    return Polygon(pts).buffer(0)


VEN = P([(-71.3, 12.5), (-71.3, 11.8), (-72.3, 11.0), (-72.4, 8.4), (-72.4, 7.4), (-70.1, 7.0), (-67.8, 6.2),
         (-67.5, 4.5), (-67.8, 2.0), (-67.2, 1.2), (-66.0, 0.8), (-64.8, 2.2), (-64.0, 4.0), (-62.8, 4.0),
         (-60.7, 5.2), (-60.0, 8.5), (-59.5, 9.5), (-62.0, 11.5), (-68.0, 12.8)])
NGR = P([(-82.9, 7.5), (-82.9, 8.05), (-82.6, 9.6), (-80.0, 10.5), (-75.0, 11.5), (-71.3, 12.5), (-71.3, 11.8),
         (-72.3, 11.0), (-72.4, 8.4), (-72.4, 7.4), (-70.1, 7.0), (-67.8, 6.2), (-67.5, 4.5), (-67.8, 2.0),
         (-67.2, 1.2), (-69.5, -1.0), (-74.0, -0.5), (-75.6, -0.1), (-77.4, 0.8), (-79.0, 1.4), (-80.5, 1.5),
         (-80.5, 7.0)])
ECU = P([(-79.0, 1.4), (-77.4, 0.8), (-75.6, -0.1), (-75.2, -1.0), (-75.6, -1.6), (-77.0, -2.8), (-78.4, -3.4),
         (-78.6, -4.6), (-79.5, -4.5), (-80.3, -3.4), (-81.3, -2.0), (-80.5, 1.5)])
PER = P([(-80.3, -3.4), (-79.5, -4.5), (-78.6, -4.6), (-78.4, -3.4), (-77.0, -2.8), (-75.6, -1.6), (-75.2, -1.0),
         (-75.6, -0.1), (-74.0, -0.5), (-69.5, -1.0), (-70.0, -4.4), (-73.0, -7.5), (-72.7, -9.4), (-70.5, -11.0),
         (-69.6, -10.9), (-68.7, -12.6), (-69.5, -14.2), (-69.0, -15.5), (-69.3, -16.0), (-69.5, -17.5),
         (-68.6, -19.0), (-68.5, -21.0), (-70.1, -21.4), (-75.0, -17.0), (-81.5, -6.0), (-81.3, -3.0)])
BOL = P([(-70.1, -21.4), (-68.5, -21.0), (-68.6, -19.0), (-69.5, -17.5), (-69.3, -16.0), (-69.0, -15.5),
         (-69.5, -14.2), (-68.7, -12.6), (-69.6, -10.9), (-66.3, -9.8), (-65.3, -10.9), (-63.3, -12.6),
         (-61.8, -13.5), (-60.4, -13.5), (-60.2, -15.1), (-58.4, -16.3), (-57.5, -18.2), (-58.0, -20.2),
         (-59.0, -22.5), (-62.6, -22.2), (-64.3, -22.8), (-65.7, -22.1), (-66.3, -21.8), (-67.2, -22.8),
         (-67.9, -22.8), (-68.3, -24.5), (-68.5, -25.4), (-70.5, -25.4), (-71.5, -23.0)])
CHI = P([(-70.5, -25.4), (-68.5, -25.4), (-68.4, -27.0), (-69.0, -28.5), (-70.0, -30.5), (-70.0, -33.0),
         (-70.3, -35.0), (-71.0, -37.5), (-71.4, -40.0), (-71.8, -42.0), (-72.0, -44.0), (-76.0, -44.0),
         (-73.0, -30.0), (-71.5, -25.4)])
ARG = P([(-67.9, -22.8), (-67.2, -22.8), (-66.3, -21.8), (-65.7, -22.1), (-64.3, -22.8), (-62.6, -22.2),
         (-57.6, -25.3), (-58.6, -27.3), (-56.0, -27.4), (-54.6, -25.6), (-53.8, -27.1), (-56.0, -28.6),
         (-57.6, -30.2), (-58.1, -32.0), (-58.4, -33.9), (-56.0, -36.0), (-57.5, -38.2), (-62.3, -38.8),
         (-66.0, -36.8), (-70.0, -36.6), (-70.3, -35.0), (-70.0, -33.0), (-70.0, -30.5), (-69.0, -28.5),
         (-68.4, -27.0), (-68.5, -25.4), (-68.3, -24.5)])
PAR = P([(-57.6, -25.3), (-58.6, -27.3), (-56.0, -27.4), (-54.6, -25.6), (-54.3, -24.0), (-55.5, -22.3),
         (-57.9, -22.1)])
URU = P([(-57.6, -30.2), (-55.5, -30.9), (-53.9, -31.9), (-53.2, -32.6), (-53.4, -33.75), (-53.0, -35.0),
         (-58.0, -35.0), (-58.4, -33.9), (-58.1, -32.0)])
CHACO = P([(-57.9, -22.1), (-57.6, -25.3), (-62.6, -22.2), (-59.0, -22.5), (-58.0, -20.2)])
GUI = P([(-60.0, 8.5), (-60.7, 5.2), (-59.6, 3.5), (-59.9, 1.3), (-58.5, 1.4), (-56.0, 1.9), (-54.5, 2.3),
         (-52.5, 2.2), (-51.6, 4.3), (-51.0, 5.5), (-57.0, 8.0)])
BRA = P([(-60.7, 5.2), (-62.8, 4.0), (-64.0, 4.0), (-64.8, 2.2), (-66.0, 0.8), (-67.2, 1.2), (-69.5, -1.0),
         (-70.0, -4.4), (-73.0, -7.5), (-72.7, -9.4), (-70.5, -11.0), (-69.6, -10.9), (-66.3, -9.8),
         (-65.3, -10.9), (-63.3, -12.6), (-61.8, -13.5), (-60.4, -13.5), (-60.2, -15.1), (-58.4, -16.3),
         (-57.5, -18.2), (-58.0, -20.2), (-57.9, -22.1), (-55.5, -22.3), (-54.3, -24.0), (-54.6, -25.6),
         (-53.8, -27.1), (-56.0, -28.6), (-57.6, -30.2), (-55.5, -30.9), (-53.9, -31.9), (-53.2, -32.6),
         (-53.4, -33.75), (-50.0, -36.0), (-30.0, -36.0), (-30.0, 6.0), (-51.0, 5.5), (-51.6, 4.3),
         (-52.5, 2.2), (-54.5, 2.3), (-56.0, 1.9), (-58.5, 1.4), (-59.9, 1.3), (-59.6, 3.5)])
# New Spain with Central America: Mexico north of the frame, down to the border of Panama
NSP = P([(-125.0, 34.0), (-125.0, 20.0), (-100.0, 12.0), (-84.0, 6.0), (-82.9, 7.5), (-82.9, 8.05), (-82.6, 9.6),
         (-81.0, 13.0), (-84.0, 16.5), (-86.5, 22.0), (-90.0, 24.0), (-96.5, 26.5), (-93.8, 29.7), (-93.8, 34.0)])

# ---------------------------------------------------------------- the inset: South America in 1830
IW, IE, IS, IN = -85.5, -33.5, -56.0, 13.5
FX0, FY0, FW = 0.008, 0.006, 0.42
n = Map(IW, IE, IS, IN, width=16.0 * FW, lakes=False)
for g, c in ((VEN, "gold"), (NGR, "green"), (ECU, "purple"), (PER, "red"), (BOL, "blue"), (CHI, "gold"),
             (ARG, "green"), (PAR, "purple"), (URU, "red"), (BRA, "brown")):
    n.region(g, c, alpha=0.42)
n.label(-58.0, 10.6, "South America\nin 1830", size="small", colour=INK, fs=19, ha="left")
n.label(-66.0, 7.3, "VENEZUELA", fs=15)
n.label(-74.0, 4.0, "NEW\nGRANADA", fs=15)
n.label(-80.7, 0.6, "ECUADOR", fs=15, ha="center")
n.label(-75.0, -9.0, "PERU", fs=16)
n.label(-64.5, -16.5, "BOLIVIA", fs=16)
n.label(-77.2, -30.0, "CHILE", fs=16, rot=0)
n.label(-64.5, -31.0, "ARGENTINA", fs=16)
n.label(-56.0, -23.6, "PARAGUAY", fs=15)
n.label(-55.8, -33.2, "URUGUAY", fs=15)
n.label(-50.0, -10.0, "BRAZIL", fs=19)
n.label(-58.0, -47.0, "Patagonia", size="land", fs=16)
n.ax.add_patch(MplPoly([(IW, IS), (IE, IS), (IE, IN), (IW, IN)], closed=True, fc="none", ec=INK, lw=3, zorder=10))
pi = os.path.join(SCRATCH, "ch60_inset.png")
n.save(pi)

# ---------------------------------------------------------------- the main map: about 1800
m = Map(-118.0, -33.0, -56.0, 33.0)
m.region(NSP, "gold", alpha=0.40)
m.region(unary_union([VEN, NGR, ECU]), "green", alpha=0.40)
m.region(unary_union([PER, CHI]), "red", alpha=0.36)
m.region(unary_union([BOL, ARG, PAR, URU, CHACO]), "blue", alpha=0.38)
m.region(BRA, "brown", alpha=0.36)

BOLIVAR = [(-63.55, 8.13), (-67.5, 7.0), (-71.0, 5.9), (-73.4, 5.45), (-74.07, 4.71), (-76.5, 2.5),
           (-78.47, -0.18), (-79.89, -2.19), (-79.6, -6.5), (-77.04, -12.05), (-74.55, -12.95)]
SANMARTIN = [(-68.83, -32.89), (-70.65, -33.45), (-71.62, -33.05), (-73.5, -28.0), (-74.5, -20.0), (-77.2, -13.5),
             (-77.3, -12.3)]
m.route(BOLIVAR, colour="red", lw=3.6)
m.route(SANMARTIN, colour=INK, lw=3.2, style=(0, (4, 2)))
m.label(-62.5, 5.2, "Bolívar\n1819 to 1824", size="small", colour=FILL["red"], fs=18)
m.label(-77.6, -30.5, "San Martín\n1817 to 1821", size="small", colour=INK, fs=18)

m.label(-103.0, 24.5, "NEW SPAIN", fs=22)
m.label(-71.5, 1.0, "NEW GRANADA", fs=20)
m.label(-73.8, -8.5, "PERU", fs=22)
m.label(-63.0, -27.0, "RÍO DE LA PLATA", fs=20)
m.label(-50.0, -10.0, "BRAZIL", fs=24)
m.label(-50.0, -12.6, "Portuguese", size="land", fs=17)
m.label(-66.0, 9.6, "Venezuela", size="land", fs=16)
m.label(-73.0, -37.0, "Chile", size="land", fs=16, ha="right")
m.label(-57.0, 2.8, "Guianas", size="land", fs=15)
m.label(-75.0, 15.0, "Caribbean Sea", size="sea", fs=18)
m.label(-40.0, 5.0, "ATLANTIC\nOCEAN", size="sea", fs=20)
m.label(-98.0, 4.0, "PACIFIC OCEAN", size="sea", fs=22)

m.city(-99.13, 19.43, "Mexico City", dx=0.0, dy=-1.6, bold=True)
m.city(-66.90, 10.50, "Caracas", dx=0.0, dy=1.4)
m.city(-74.07, 4.71, "Bogotá", dx=-1.0, dy=0.6, bold=True)
m.city(-78.47, -0.18, "Quito", dx=-1.0, dy=0.3)
m.city(-79.89, -2.19, "Guayaquil, 1822", dx=-1.0, dy=-0.5)
m.city(-77.04, -12.05, "Lima", dx=-1.0, dy=0.0, bold=True)
m.city(-71.97, -13.53, "Cuzco", dx=1.0, dy=0.0)
m.city(-74.20, -13.10, None, star=True, r=7)
m.label(-71.2, -15.6, "Ayacucho, 1824", size="small", colour=INK, fs=16.5, style="normal")
m.city(-63.55, 8.13, "Angostura", dx=1.0, dy=-0.6)
m.city(-68.83, -32.89, "Mendoza", dx=1.0, dy=0.0)
m.city(-70.65, -33.45, "Santiago", dx=0.9, dy=-1.3)
m.city(-58.38, -34.60, "Buenos Aires", dx=1.0, dy=-0.3, bold=True)
m.city(-43.20, -22.90, "Rio de Janeiro", dx=0.0, dy=-1.4)
m.scale(1000, lon=-48.0, lat=-52.0)

img = mpimg.imread(pi)
fh = m.fig.get_size_inches()[1]
ax = m.fig.add_axes([FX0, FY0, FW, img.shape[0] / 100.0 / fh])
ax.imshow(img)
ax.set_axis_off()
m.save("chapters/60-bolivar/images/map_viceroyalties.png")
