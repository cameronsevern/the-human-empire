#!/usr/bin/env python3
"""Chapter 76: India in 1930, with the salt march in an enlarged inset. Delhi, Amritsar (1919), Bombay,
Calcutta, Ahmedabad, Porbandar (where Gandhi was born), and Bengal; in the inset, the march from Gandhi's
community at Ahmedabad to the beach at Dandi, 12 March to 6 April 1930, and the government salt works at
Dharasana, raided on 21 May 1930.

Drawn for this chapter, which had no map. No borders are drawn: British India and the princely states are
not told apart, and Burma, then governed as part of British India, is only named. Bengal is drawn roughly
as the province of the 1930s (modern West Bengal and Bangladesh). The march is simplified through its
main stops, after the route map in English Wikipedia's "Salt March": Sabarmati Ashram, Aslali, Nadiad,
Anand, Borsad, the Mahi crossing at Kankapura, Jambusar, Amod, Ankleshwar across the Narmada, the
outskirts of Surat, Navsari, Dandi. Positions from English Wikipedia (Dandi 20.886 N 72.801 E, Dharasana
20.683 N 72.917 E).
"""
import os
import matplotlib.image as mpimg
from matplotlib.patches import Polygon as MplPoly, Rectangle
from lib import Map, INK, FILL

SCRATCH = os.environ.get("SCRATCH", "/tmp")
march = [(72.58, 23.06), (72.59, 22.92), (72.86, 22.69), (72.95, 22.56), (72.90, 22.41), (72.85, 22.27),
         (72.80, 22.05), (72.87, 21.99), (73.00, 21.63), (72.88, 21.25), (72.92, 20.95), (72.80, 20.89)]
bengal = [(86.0, 22.0), (86.8, 21.6), (88.0, 21.5), (89.0, 21.7), (90.5, 21.9), (91.8, 22.2), (92.3, 21.0),
          (92.7, 22.5), (92.4, 24.2), (91.5, 24.6), (90.0, 25.2), (89.8, 26.0), (89.0, 26.5), (88.4, 27.1),
          (88.0, 26.4), (88.0, 25.4), (87.8, 24.9), (87.2, 24.0), (86.5, 23.5), (86.0, 22.8)]

# ---------------------------------------------------------------- the inset: the salt march
IW, IE, IS, IN = 71.4, 74.0, 20.35, 23.3
FX0, FY0, FW = 0.006, 0.008, 0.27
n = Map(IW, IE, IS, IN, width=16.0 * FW, lakes=False)
n.river("Mahi", "Narmada", "Tapi", lw=1.5)
n.route(march, colour="red", lw=3.4, arrow=False)
n.city(72.58, 23.03, "Ahmedabad", dx=0.12, dy=0.1, ha="left", bold=True)
n.city(72.80, 20.89, "Dandi", dx=-0.1, dy=0.08, ha="right", star=True, r=8, bold=True)
n.city(72.917, 20.683, "salt works,\nraided 21 May", dx=0.1, dy=0.0, ha="left", size=15)
n.label(71.5, 22.75, "SALT\nMARCH,\n1930", fs=16, ha="left")
n.label(73.5, 22.35, "12 March\nto 6 April", size="small", colour=INK, fs=15)
n.label(72.2, 21.65, "Gulf of\nCambay", size="sea", fs=15)
n.ax.add_patch(MplPoly([(IW, IS), (IE, IS), (IE, IN), (IW, IN)], closed=True, fc="none", ec=INK, lw=3, zorder=10))
pi = os.path.join(SCRATCH, "ch76_inset.png")
n.save(pi)

# ---------------------------------------------------------------- the main map
m = Map(60.0, 98.0, 6.0, 37.0)
m.region(bengal, "gold", alpha=0.45)
m.river("Indus", "Ganges", "Brahmaputra", lw=1.6)
m.route(march, colour="red", lw=2.4, arrow=False)
m.ax.add_patch(Rectangle((IW, IS), IE - IW, IN - IS, fc="none", ec=INK, lw=1.4, ls=(0, (4, 2)), zorder=5))

m.city(77.21, 28.61, "Delhi", dx=0.5, dy=0.3, bold=True)
m.city(74.87, 31.63, "Amritsar, 1919", dx=0.5, dy=0.3, bold=True)
m.city(72.88, 19.08, "Bombay", dx=0.5, dy=-0.2, bold=True)
m.city(88.36, 22.57, "Calcutta", dx=-0.5, dy=-0.3, bold=True)
m.city(69.61, 21.64, "Porbandar", dx=-0.4, dy=0.0)
m.label(89.6, 23.6, "BENGAL", fs=18)
m.label(79.0, 21.8, "I N D I A", fs=26)
m.label(96.0, 21.5, "BURMA", size="land", colour="#5a534b", fs=17, style="normal")
m.label(66.5, 33.5, "AFGHANISTAN", size="land", colour="#5a534b", fs=16, style="normal")
m.label(84.0, 31.6, "TIBET", size="land", colour="#5a534b", fs=16, style="normal")
m.label(85.0, 16.0, "Bay of\nBengal", size="sea", fs=19)
m.label(68.5, 18.6, "Arabian Sea", size="sea", fs=19)
m.label(71.6, 27.6, "Indus", size="sea", fs=16)
m.label(83.6, 26.3, "Ganges", size="sea", fs=16)
m.scale(500, lon=90.0, lat=8.0)

img = mpimg.imread(pi)
fh = m.fig.get_size_inches()[1]
ax = m.fig.add_axes([FX0, FY0, FW, img.shape[0] / 100.0 / fh])
ax.imshow(img)
ax.set_axis_off()
m.save("chapters/76-gandhi/images/map_india.png")
