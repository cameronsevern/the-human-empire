#!/usr/bin/env python3
"""Chapter 54: India about 1765, when the Mughal emperor gave the East India Company the right to collect
the land tax of Bengal and its neighbours. Bengal and Bihar shaded as the Company's; the three Company
towns (Calcutta, Madras, Bombay), Plassey, Delhi; the Maratha lands and Mysore as soft areas. An inset
shows the Spice Islands, from Batavia on Java to the Banda Islands.

Drawn for this chapter, which had no map. The extents are rough, after the maps of India in 1765 in
English Wikipedia's articles "Maratha Empire", "Kingdom of Mysore" and "Company rule in India" and the
Imperial Gazetteer atlas (1909) plate of India in 1765. The grant of 1765 named Bengal, Bihar and Orissa,
but most of Orissa had passed to the Marathas in 1751 and the Company got only the district of Midnapore,
so Orissa is not shaded as the Company's: the shaded area is Bengal (with Midnapore and Chittagong) and
Bihar. The Maratha lands are drawn as one area, the Peshwa's lands with those of the great Maratha
chiefs, including Nagpur and Cuttack. Positions from English Wikipedia.
"""
import os
import numpy as np
import matplotlib.image as mpimg
import lib
from lib import Map, INK, PAPER, FILL

SCRATCH = os.environ.get("SCRATCH", "/tmp")

# ---------------------------------------------------------------- inset: the Spice Islands
s = Map(104.0, 132.5, -9.6, 0.4, width=6.0, lakes=False)
s.city(106.85, -6.13, "Batavia", dx=0.0, dy=1.0, bold=True)
s.city(129.9, -4.53, "Banda\nIslands", dx=-0.6, dy=-1.6, ha="center", bold=True)
s.label(108.6, -8.75, "JAVA", size="land", fs=17, style="normal")
s.label(114.0, -0.5, "BORNEO", size="land", fs=16, style="normal")
s.label(112.0, -4.7, "Java Sea", size="sea", fs=16)
s.ax.text(131.9, -0.0, "The Spice Islands", ha="right", va="top", fontsize=19, color=INK, fontweight="bold",
          zorder=8, path_effects=lib.HALO)
ps = os.path.join(SCRATCH, "ch54_spice.png")
s.save(ps)

# ---------------------------------------------------------------- India
m = Map(66.0, 97.0, 5.5, 33.0)
m.river("Ganges", "Indus", "Yamuna")
company = [(83.4, 25.2), (83.7, 26.8), (84.4, 27.4), (86.0, 26.8), (88.1, 26.6), (89.5, 26.4), (90.5, 26.0),
           (92.0, 25.1), (92.3, 24.0), (92.4, 22.4), (92.3, 20.8), (90.0, 21.3), (87.0, 21.4), (86.6, 22.0),
           (85.8, 22.9), (84.2, 23.4), (83.5, 24.1)]
m.region(company, "red", alpha=0.5)
maratha = [(72.6, 21.2), (73.6, 23.4), (74.8, 25.0), (76.0, 26.2), (78.4, 26.6), (80.2, 25.2), (81.5, 24.0),
           (83.0, 23.0), (84.6, 22.3), (86.7, 21.3), (86.3, 19.8), (84.6, 19.4), (82.4, 20.6), (80.3, 20.6),
           (78.0, 20.3), (76.4, 19.2), (75.7, 17.0), (75.4, 15.4), (74.0, 15.4), (73.1, 17.5), (72.8, 19.4)]
m.region(maratha, "gold", alpha=0.42)
mysore = [(74.9, 13.9), (76.2, 14.7), (77.8, 14.4), (78.6, 13.1), (78.3, 11.5), (76.8, 11.2), (75.6, 11.9)]
m.region(mysore, "green", alpha=0.45)

m.label(90.4, 23.6, "BENGAL", fs=20)
m.label(85.6, 25.4, "BIHAR", fs=18)
m.label(88.6, 28.2, "taxed by the Company\nfrom 1765", size="small", colour=INK, fs=17)
m.label(78.5, 22.8, "MARATHAS", fs=22)
m.label(76.7, 12.7, "MYSORE", fs=18)

m.city(77.21, 28.61, "Delhi", dx=-0.5, dy=0.0, bold=True)
m.city(88.36, 22.57, "Calcutta", dx=-0.5, dy=-0.2, bold=True)
m.city(88.25, 23.80, "Plassey, 1757", dx=-0.5, dy=0.15, star=True, r=7)
m.city(80.27, 13.08, "Madras", dx=0.5, dy=0.0, bold=True)
m.city(72.83, 18.94, "Bombay", dx=-0.5, dy=0.0, bold=True)

m.label(70.2, 13.5, "Arabian\nSea", size="sea", fs=21)
m.label(88.0, 16.5, "Bay of Bengal", size="sea", fs=21)
m.label(70.0, 30.5, "Indus", size="sea", fs=16)
m.label(83.0, 26.0, "Ganges", size="sea", fs=16, rot=-15)
m.scale(500, lon=67.0, lat=7.0)
pm = os.path.join(SCRATCH, "ch54_india.png")
m.save(pm)

# ---------------------------------------------------------------- the inset in the lower right corner
ia, ib = mpimg.imread(pm), mpimg.imread(ps)
H, Wd = ib.shape[:2]
out = ia.copy()
pad = 3
y0, x0 = out.shape[0] - H - pad, out.shape[1] - Wd - pad
ink = np.array([int(INK[i:i + 2], 16) / 255 for i in (1, 3, 5)] + [1.0])
out[y0 - 3:y0 + H, x0 - 3:x0 + Wd] = ink
out[y0:y0 + H, x0:x0 + Wd] = ib
dest = os.path.join(lib.ROOT, "chapters/54-company/images/map_india_1765.png")
mpimg.imsave(dest, out)
print("wrote", dest, out.shape)
