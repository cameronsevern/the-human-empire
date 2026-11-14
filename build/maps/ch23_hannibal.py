#!/usr/bin/env python3
"""Chapter 23: Rome and Carthage when Hannibal set out, about 2,240 years ago (218 BCE), and his route.

One map in place of two. The lands of Rome, Syracuse and Carthage are drawn by eye after "Map of Rome
and Carthage at the start of the Second Punic War" (William Robert Shepherd, modified; Wikimedia
Commons, CC BY-SA 4.0) and checked against the Barrington Atlas and Lazenby, Hannibal's War (1978).
Rome's land in Italy ends at the line from the Arno to the Adriatic near Ariminum, as on the source;
the colonies being founded on the Po that year are left out. Carthage's Spain is the south and east
of the peninsula up to about the Ebro; its Africa is the land around the city and a strip of coast.

The route follows "Hannibal route of invasion" by Pinpin (Wikimedia Commons, CC BY-SA 3.0) and
Lazenby: along the coast to the Pyrenees, across the south of Gaul to the Rhone, over the Alps (the
pass is disputed, so the crossing is drawn between the candidates), down the Po valley, over the
Apennines past Lake Trasimene, down the Adriatic side to Cannae, and in 203 BCE by sea from Croton
back to Africa. Positions of towns and battlefields from English Wikipedia.
"""
from lib import Map, FILL, INK, PAPER
from tracing import hatched

rome_italy = [(9.8, 44.2), (11.3, 44.3), (12.6, 44.1), (13.6, 43.75), (14.6, 43.0), (16.6, 42.0), (19.0, 40.6),
              (18.8, 39.3), (17.2, 38.2), (16.0, 37.6), (15.2, 38.3), (12.5, 40.4), (10.6, 42.2), (9.9, 43.3)]
islands = [(8.0, 38.7), (9.9, 38.7), (10.0, 41.0), (9.8, 43.2), (8.3, 43.2), (8.1, 41.0)]
syracuse = [(14.55, 36.55), (14.5, 37.15), (14.95, 37.5), (15.4, 37.5), (15.6, 36.95), (15.2, 36.5)]
sicily = [(12.1, 38.1), (12.4, 36.9), (14.3, 36.5), (14.55, 36.55), (14.5, 37.15), (14.95, 37.5), (15.4, 37.5),
          (15.75, 38.35), (14.0, 38.3), (12.6, 38.35)]
spain = [(-9.6, 36.7), (-9.6, 38.9), (-7.8, 39.9), (-5.5, 40.7), (-3.2, 41.2), (-1.0, 41.6), (0.7, 40.8),
         (0.6, 39.0), (-0.3, 37.6), (-2.0, 36.5), (-5.6, 35.8)]
balearics = [(1.0, 38.5), (4.6, 39.6), (4.3, 40.3), (2.2, 39.9), (1.2, 39.2)]
africa = [(-6.6, 34.9), (-2.0, 35.0), (2.0, 35.8), (6.0, 36.2), (8.2, 36.2), (8.4, 35.1), (8.6, 34.1), (9.6, 33.4),
          (11.0, 33.1), (13.0, 32.6), (13.0, 35.0), (11.8, 37.4), (9.6, 37.8), (5.0, 37.3), (0.0, 36.4),
          (-6.6, 36.2)]

m = Map(-6.4, 18.9, 33.3, 47.0)
m.river("Po", "Ebro", "Rhône", "Tevere")
for pts in (rome_italy, islands, sicily):
    m.region(pts, "red", alpha=0.45)
hatched(m, syracuse, colour="red", alpha=0.2)
for pts in (spain, balearics, africa):
    m.region(pts, "purple", alpha=0.42)

march = [(-0.98, 37.60), (-0.6, 38.7), (-0.27, 39.68), (0.2, 40.5), (0.9, 40.8), (2.0, 41.4), (2.9, 42.3),
         (3.1, 43.1), (4.0, 43.6), (4.7, 44.0), (5.3, 44.9), (6.4, 45.1), (7.1, 45.0), (7.7, 45.05),
         (8.9, 45.15), (9.6, 45.0)]
south = [(9.6, 45.0), (10.4, 44.3), (11.0, 43.75), (12.05, 43.2), (13.0, 43.3), (13.9, 42.7), (14.6, 42.2),
         (15.5, 41.75), (16.13, 41.31)]
home = [(17.12, 39.08), (17.4, 37.9), (15.6, 36.4), (13.0, 35.7), (11.0, 35.7), (10.3, 35.9), (9.6, 36.2)]
m.route(march, colour="#2f2a26", lw=3.4, arrow=False)
m.route(south, colour="#2f2a26", lw=3.4)
m.route(home, colour="#2f2a26", lw=3.4, style=(0, (2.2, 1.4)))
for lon, lat in [(9.6, 45.0), (12.05, 43.2), (16.13, 41.31), (9.45, 36.25)]:
    m.ax.plot(lon, lat, marker="X", ms=19, mfc=INK, mec=PAPER, mew=1.6, zorder=6.5)

m.label(16.25, 40.5, "ROME", fs=24)
m.label(-4.0, 38.6, "CARTHAGINIAN\nSPAIN", fs=23)
m.label(9.5, 34.7, "CARTHAGE", fs=24)
m.city(12.48, 41.89, "Rome", dx=-0.3, dy=-0.25, star=True, bold=True, size=20)
m.city(10.32, 36.85, "Carthage", dx=0.35, dy=0.35, star=True, bold=True, size=20)
m.city(-0.98, 37.60, "New Carthage", dx=0.0, dy=-0.5, size=19)
m.city(-0.27, 39.68, "Saguntum", dx=0.35, dy=0.0, size=19)
m.city(14.25, 41.08, "Capua", dx=0.0, dy=-0.45, size=19)
m.city(15.29, 37.07, "Syracuse", dx=0.35, dy=-0.15, size=19)
m.label(9.6, 45.55, "Trebia", size="small", colour=INK, fs=19)
m.label(11.65, 43.3, "Lake Trasimene", size="small", colour=INK, fs=19, ha="right")
m.label(16.6, 41.75, "Cannae", size="small", colour=INK, fs=19, ha="left")
m.label(9.3, 35.75, "Zama", size="small", colour=INK, fs=19, ha="right")
m.label(13.4, 37.75, "Sicily", size="land", fs=19)
m.label(9.0, 40.0, "Sardinia", size="land", fs=19)
m.label(2.0, 45.0, "GAUL", size="land", fs=24, style="normal")
m.label(7.4, 46.3, "Alps", size="land", fs=21)
m.label(1.0, 42.75, "Pyrenees", size="land", fs=19)
m.label(5.5, 39.5, "Mediterranean Sea", size="sea", fs=22)
m.label(1.5, 34.3, "NUMIDIA", size="land", fs=21, style="normal")
m.scale(300, lon=-5.6, lat=33.9)
m.save("chapters/23-rome/images/map_hannibal.png")
