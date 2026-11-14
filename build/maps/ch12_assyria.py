#!/usr/bin/env python3
"""Chapter 12: the Assyrian empire at its largest, about 2,650 years ago.

Both areas are traced by eye from "The Neo-Assyrian Empire" by Ennomus (Wikimedia Commons,
CC BY-SA 4.0): its darker "boundaries" as the provinces, its paler "clients" as the kings who
paid tribute. Checked against the map of the Assyrian empire in Van De Mieroop, A History of
the Ancient Near East. The tracing is in the source map's pixels, turned into degrees by a fit
to eleven cities (error under half a degree). Urartu and the Medes, which the source shades, are left out: they were
neighbours that Assyria fought or bargained with, not lands it ruled. City positions from
English Wikipedia.
"""
from lib import Map
from tracing import fit, hatched

deg = fit([((978, 381), (43.15, 36.36)), ((441, 350), (34.90, 36.92)), ((205, 795), (31.25, 29.85)),
           ((322, 1155), (32.90, 24.09)), ((1318, 643), (48.26, 32.19)), ((1167, 729), (46.10, 30.96)),
           ((556, 567), (36.29, 33.51)), ((405, 712), (34.47, 31.50)),
           ((1002, 243), (43.33, 38.50)), ((656, 347), (38.01, 36.83)), ((1063, 643), (44.42, 32.54))])

core = deg([(395, 372), (440, 300), (490, 215), (550, 232), (620, 218), (690, 236), (760, 262), (850, 272),
            (950, 285), (1050, 300), (1100, 340), (1140, 400), (1170, 480), (1185, 560), (1180, 600), (1130, 612),
            (1050, 585), (950, 562), (850, 522), (750, 482), (660, 445), (600, 520), (560, 600), (520, 640),
            (495, 672), (450, 690), (418, 730), (370, 720), (420, 600), (460, 470), (420, 400)])
outer = deg([(395, 372), (440, 300), (490, 215), (550, 232), (620, 218), (690, 236), (760, 262), (850, 272),
             (950, 285), (1050, 300), (1100, 340), (1140, 400), (1170, 480), (1185, 560), (1260, 590), (1380, 600),
             (1460, 660), (1495, 710), (1470, 760), (1350, 772), (1250, 776), (1100, 775), (900, 772), (700, 776),
             (560, 790), (490, 830), (440, 930), (420, 960), (440, 1080), (490, 1190), (320, 1205), (180, 1150),
             (70, 1030), (20, 880), (10, 720), (120, 690), (250, 700), (380, 722), (300, 530), (250, 470),
             (300, 430)])

m = Map(28.0, 50.6, 26.4, 39.5)
m.river("Nile", "Euphrates", "Tigris", en=True)
hatched(m, outer, minus=[core], colour="red")
m.region(core, "red", alpha=0.45)

m.label(40.6, 37.3, "ASSYRIA")
m.label(29.3, 28.0, "EGYPT")
m.label(48.0, 31.0, "ELAM", fs=21)
m.label(39.2, 31.0, "kings who\npaid tribute", size="small", colour="#2f2a26", fs=17)
m.label(36.6, 31.15, "JUDAH", fs=17)
m.label(47.7, 35.6, "Medes", size="land", fs=19)
m.label(31.2, 33.4, "Mediterranean Sea", size="sea", fs=19)
m.label(49.3, 28.6, "Persian\nGulf", size="sea")
m.label(35.6, 27.4, "Red\nSea", size="sea")
m.label(41.0, 28.0, "ARABIA", size="land", fs=19)
m.label(31.5, 38.3, "mountains of Turkey", size="land")
m.label(39.6, 36.0, "Euphrates", size="sea", rot=-28)
m.label(44.25, 34.6, "Tigris", size="sea", rot=-58)

m.city(43.153, 36.360, "Nineveh", dx=0.35, star=True, bold=True)
m.city(43.262, 35.456, "Ashur", dx=0.35)
m.city(44.421, 32.536, "Babylon", dx=-0.35)
m.city(48.258, 32.190, "Susa", dx=0.35)
m.city(36.29, 33.51, "Damascus", dx=0.35)
m.city(35.19, 32.28, "Samaria", dx=0.3, dy=0.12)
m.city(35.23, 31.78, "Jerusalem", dx=0.3, dy=-0.1)
m.city(34.85, 31.56, "Lachish", dx=-0.3, dy=-0.15)
m.city(31.25, 29.85, "Memphis", dx=-0.35)
m.scale(500)
m.save("chapters/12-assyria/images/map_assyria_empire.png")
