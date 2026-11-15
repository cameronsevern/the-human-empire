#!/usr/bin/env python3
"""Chapter 48: the three Muslim empires in the middle of the 1600s, the Ottomans, the Safavids and the
Mughals, with the places the chapter names: Istanbul, Bosnia, Tabriz and the battlefield of Chaldiran,
Isfahan, Baghdad, Kabul, Panipat, Delhi, Agra, Burhanpur, Varanasi, Amritsar in the Punjab, and the
Portuguese town of Goa; and Vienna, for the Ottoman frontier in Europe.

Drawn for this chapter, which had no map. The three areas are soft and approximate, after the maps
usually drawn for the middle of the 1600s (English Wikipedia's articles "Ottoman Empire", "Safavid
Iran" and "Mughal Empire"): the Ottoman-Safavid border as settled in 1639, which runs much where the
border of Iran runs today, Baghdad Ottoman, Tabriz and Kandahar Safavid, Kabul and Kashmir Mughal, and
the Mughal border in the Deccan north of Bijapur and Golconda. Wallachia, Moldavia, Transylvania and
the Crimea, which paid tribute to the sultan but kept their own rulers, are left out of the Ottoman
area, as are the Venetian coast of Dalmatia and Crete. The middle of the 1600s is chosen because the
borders between the three changed often before 1639 (the Ottomans held Tabriz from 1585 to 1603).
Positions from English Wikipedia.
"""
import numpy as np
import lib
from lib import Map, INK, FILL
from tracing import states

ottoman = [(15.6, 45.0), (16.6, 45.6), (17.6, 46.0), (18.2, 46.8), (18.6, 47.6), (19.6, 48.1), (20.8, 48.1),
           (21.6, 47.4), (21.9, 46.4), (22.4, 45.2), (22.6, 44.5), (24.0, 43.75), (26.0, 43.7), (27.8, 44.2),
           (29.0, 45.2), (29.8, 45.3), (31.0, 44.0), (36.0, 42.6), (40.0, 41.8), (41.6, 42.2), (42.6, 42.2),
           (43.4, 41.6), (43.7, 40.7), (43.9, 39.9), (44.2, 39.4), (44.4, 38.6), (44.7, 37.9), (45.1, 37.0),
           (45.5, 36.1), (45.8, 35.2), (45.6, 34.4), (46.2, 33.6), (47.1, 32.7), (47.7, 31.6), (48.4, 30.4),
           (48.6, 29.9), (49.6, 28.3), (50.2, 26.6), (50.4, 25.0), (48.6, 25.0), (46.0, 28.6), (43.0, 30.6),
           (39.6, 28.4), (40.6, 24.6), (41.4, 21.2), (41.8, 19.2), (40.2, 19.0), (37.2, 22.0), (33.0, 21.8),
           (31.0, 21.8), (25.0, 22.0), (24.8, 29.0), (20.5, 29.0), (17.0, 28.5), (13.0, 29.5), (12.5, 33.0),
           (14.0, 35.5), (19.0, 37.0), (19.2, 40.0), (19.0, 42.0), (17.8, 43.0), (16.6, 43.6), (15.9, 44.3)]
safavid = [(43.0, 41.2), (44.5, 42.0), (46.5, 41.9), (48.4, 41.9), (49.5, 41.0), (49.5, 38.5), (51.0, 36.9),
           (54.0, 37.3), (56.5, 38.2), (59.0, 37.6), (61.0, 36.6), (62.5, 35.6), (64.5, 35.0), (66.4, 34.4),
           (67.5, 32.5), (67.2, 30.5), (66.5, 29.0), (64.0, 27.0), (61.8, 25.2), (60.0, 24.5), (56.0, 25.5),
           (52.0, 27.5), (50.0, 29.3), (48.6, 29.9), (48.0, 31.5), (46.8, 33.0), (45.3, 34.4), (45.2, 35.5),
           (44.6, 37.0), (44.0, 38.8), (43.4, 40.0)]
mughal = [(68.0, 35.8), (70.5, 36.2), (71.5, 35.6), (74.5, 35.3), (76.0, 34.8), (77.0, 33.4), (76.6, 32.3),
          (78.0, 31.0), (80.0, 29.5), (83.0, 27.5), (85.5, 27.0), (88.0, 26.5), (89.5, 26.3), (90.6, 25.5),
          (91.2, 23.6), (90.6, 22.0), (88.0, 21.0), (86.6, 20.0), (85.0, 19.6), (83.0, 20.6), (80.5, 20.0),
          (78.0, 18.9), (76.0, 18.0), (74.0, 18.2), (72.9, 18.9), (72.4, 20.5), (72.3, 21.6), (70.0, 20.6),
          (68.6, 22.4), (67.4, 24.0), (66.6, 25.6), (67.2, 28.0), (67.6, 30.4), (68.4, 31.8), (68.2, 33.0),
          (67.3, 34.1)]

m = Map(13.0, 90.0, 12.0, 50.0)
m.river("Danube", "Tigris", "Euphrates", "Nile", "Indus", "Ganges", "Yamuna", "Sutlej", "Chenab", "Ravi",
        en=True, lw=1.4)
states(m, [(ottoman, "green"), (safavid, "gold"), (mughal, "red")], alpha=0.42)

m.label(34.0, 38.7, "OTTOMAN\nEMPIRE", fs=22)
m.label(58.0, 33.2, "SAFAVID\nEMPIRE", fs=22)
m.label(81.6, 22.5, "MUGHAL\nEMPIRE", fs=22)

m.city(28.98, 41.01, "Istanbul", dx=-0.5, dy=0.8, bold=True)
m.city(16.37, 48.21, "Vienna", dx=0.6, dy=0.3)
m.label(18.4, 44.0, "Bosnia", size="small", colour=INK, fs=18)
m.city(44.37, 33.31, "Baghdad", dx=-0.7, dy=0.0)
m.city(46.29, 38.08, "Tabriz", dx=0.7, dy=0.2)
m.ax.plot(43.97, 39.14, "X", ms=16, mfc=INK, mec=lib.PAPER, mew=1.2, zorder=6)
m.label(44.6, 40.3, "Chaldiran 1514", size="small", colour=INK, fs=17)
m.city(51.67, 32.65, "Isfahan", dx=0.0, dy=-1.0, bold=True)
m.city(69.17, 34.53, "Kabul", dx=-0.7, dy=0.0)
m.city(74.87, 31.63, "Amritsar", dx=-0.7, dy=0.15)
m.label(71.6, 29.9, "PUNJAB", size="land", fs=17, style="normal")
m.ax.plot(76.97, 29.39, "X", ms=16, mfc=INK, mec=lib.PAPER, mew=1.2, zorder=6)
m.label(77.6, 29.75, "Panipat 1526", size="small", colour=INK, fs=17, ha="left")
m.city(77.21, 28.61, "Delhi", dx=-0.7, dy=-0.2)
m.city(78.01, 27.18, "Agra", dx=0.7, dy=-0.2, bold=True)
m.city(82.97, 25.32, "Varanasi", dx=0.7, dy=0.0)
m.city(76.23, 21.31, "Burhanpur", dx=-0.7, dy=-0.1)
m.city(73.83, 15.49, "Goa", dx=0.7, dy=0.0)

m.label(34.0, 43.4, "Black Sea", size="sea", fs=17)
m.label(51.0, 41.6, "Caspian\nSea", size="sea", fs=16)
m.label(23.0, 34.0, "Mediterranean", size="sea", fs=17)
m.label(64.0, 18.0, "Arabian Sea", size="sea", fs=18)
m.scale(500, lon=40.0, lat=14.0)
m.save("chapters/48-taj/images/map_three_empires.png")
