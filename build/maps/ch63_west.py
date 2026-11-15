#!/usr/bin/env python3
"""Chapter 63: the growth of the United States, 1783 to 1853, each area labelled with its year and how it
was got: 1783 (recognised by Britain), 1803 (Louisiana, bought from France), 1819 (Florida, from Spain),
1845 (Texas, annexed), 1846 (Oregon, divided with Britain), 1848 (taken from Mexico), 1853 (bought from
Mexico). With the Cherokee homeland and the road of 1838 to Indian Territory, the range of the Comanche
about 1750 to 1850, and the railway finished in 1869.

Drawn for this chapter, which had no map. The areas follow the usual map of the territorial growth of the
United States (the National Atlas map "Territorial Acquisitions of the United States", and English
Wikipedia, "Territorial evolution of the United States"), simplified: Texas is drawn as annexed with its
claim to the upper Rio Grande; West Florida, taken in pieces from 1810, is shown with Florida; the
Red River basin, settled with Britain in 1818, is shown with Louisiana; the Canadian border of 1842 in
Maine is shown as it is today. The Cherokee homeland is the Cherokee Nation of about 1830 in Georgia,
Tennessee, North Carolina and Alabama; the route is the northern road of 1838 by Nashville, Kentucky,
southern Illinois and Missouri; the Comanche range is a rough area after the maps of Comancheria in
Pekka Hämäläinen's "The Comanche Empire" (2008) and English Wikipedia. The railway runs from Council
Bluffs and Omaha to Promontory Summit and Sacramento. Positions from English Wikipedia.
"""
from matplotlib.patches import Polygon as MplPoly
from shapely.geometry import Polygon
from lib import Map, INK, FILL, PAPER, smooth, course

m = Map(-126.0, -66.0, 24.0, 50.0)
m.river("Mississippi", "Missouri", "Ohio", "Rio Grande", "Columbia", "Arkansas")


def P(pts):
    return Polygon(pts).buffer(0)


MISS = course("Mississippi", (-95.2, 47.3), (-91.64, 31.0))
RIO = course("Rio Grande", (-107.4, 37.8), (-106.53, 31.78))
LOWER_RIO = course("Rio Grande", (-106.53, 31.78), (-97.15, 25.95))[1:]

RED = [(-93.85, 29.7), (-93.75, 31.0), (-94.04, 32.0), (-94.04, 33.55), (-95.5, 33.9), (-97.0, 33.8), (-98.5, 34.1),
       (-100.0, 34.56), (-100.0, 37.75), (-102.0, 38.0), (-104.0, 38.25), (-106.0, 38.8), (-106.3, 39.2)]

US1783 = P([(-66.9, 44.8), (-67.8, 47.1), (-69.2, 47.45), (-70.0, 46.0), (-71.5, 45.0), (-74.7, 45.0), (-76.3, 44.2),
            (-79.0, 43.4), (-79.2, 42.6), (-83.1, 42.0), (-82.4, 43.0), (-82.5, 45.3), (-84.4, 46.5), (-89.5, 48.0),
            (-95.2, 49.0)] + MISS + [(-89.6, 31.0), (-85.0, 31.0), (-84.9, 30.7), (-82.2, 30.6), (-81.45, 30.7),
                                     (-78.0, 31.0), (-74.0, 36.0), (-68.0, 41.0), (-66.0, 43.5)])
LOU = P([(-95.2, 49.0)] + MISS + [(-89.6, 31.0), (-89.4, 28.8)] + RED + [(-106.3, 42.0), (-108.5, 42.0), (-109.5, 43.0),
                                                             (-110.5, 44.2), (-111.5, 44.5), (-113.0, 45.7),
                                                             (-113.5, 47.0), (-114.0, 48.0), (-114.0, 49.0)])
FLA = P([(-89.6, 31.0), (-85.0, 31.0), (-84.9, 30.7), (-82.2, 30.6), (-81.45, 30.7), (-79.0, 30.0), (-79.5, 24.0),
         (-83.0, 24.0), (-88.0, 29.5), (-89.4, 28.8)])
TEX = P(RED + [(-106.3, 42.0), (-107.5, 42.0)] + RIO + LOWER_RIO + [(-96.0, 27.5), (-94.0, 29.0)])
ORE = P([(-125.5, 42.0), (-125.5, 48.3), (-124.7, 48.5), (-123.2, 48.3), (-123.2, 49.0), (-114.0, 49.0),
         (-114.0, 48.0), (-113.5, 47.0), (-113.0, 45.7), (-111.5, 44.5), (-110.5, 44.2), (-109.5, 43.0),
         (-108.5, 42.0)])
GILA = [(-108.7, 32.9), (-109.5, 33.0), (-110.5, 33.1), (-112.0, 33.0), (-113.5, 32.95), (-114.6, 32.73)]
MEX = P([(-125.5, 42.0), (-107.5, 42.0)] + RIO[:-1] + [(-108.2, 32.45)] + GILA + [(-117.12, 32.53), (-118.0, 32.0),
                                                                                (-126.0, 35.0)])
GAD = P([(-106.75, 32.45), (-106.53, 31.78), (-108.2, 31.78), (-108.2, 31.33), (-111.07, 31.33), (-114.8, 32.49)]
        + GILA[::-1] + [(-108.2, 32.45)])

for g, c in ((US1783, "olive"), (LOU, "gold"), (FLA, "pink"), (TEX, "red"), (ORE, "green"), (MEX, "blue"),
             (GAD, "purple")):
    m.region(g, c, alpha=0.36, lakes_out=True)

m.label(-84.0, 39.4, "1783", fs=22)
m.label(-84.0, 38.5, "recognised by Britain", size="small", colour=INK, fs=16)
m.label(-101.5, 44.8, "1803", fs=22)
m.label(-101.5, 43.9, "Louisiana, bought from France", size="small", colour=INK, fs=16)
m.label(-81.4, 28.4, "1819", fs=18)
m.label(-81.4, 27.5, "Florida,\nfrom Spain", size="small", colour=INK, fs=15)
m.label(-98.8, 31.2, "1845", fs=22)
m.label(-98.8, 30.3, "Texas, annexed", size="small", colour=INK, fs=16)
m.label(-119.0, 46.3, "1846", fs=22)
m.label(-119.0, 45.1, "Oregon, divided\nwith Britain", size="small", colour=INK, fs=16)
m.label(-116.3, 36.9, "1848", fs=22)
m.label(-116.3, 36.0, "taken from Mexico", size="small", colour=INK, fs=16)
m.ax.plot([-110.0, -110.4], [31.9, 30.1], color=INK, lw=1.0, zorder=6.5)
m.label(-110.4, 29.5, "1853", fs=18)
m.label(-110.4, 28.65, "bought from Mexico", size="small", colour=INK, fs=15)

# the Comanche range
COM = smooth([(-104.5, 38.5), (-100.5, 38.8), (-98.2, 37.0), (-97.6, 34.5), (-97.6, 31.0), (-99.5, 29.6),
              (-102.0, 30.0), (-104.0, 31.5), (-105.5, 34.0), (-105.3, 36.5)], closed=True)
m.ax.add_patch(MplPoly(COM, closed=True, fc="none", ec=FILL["brown"], lw=2.6, ls=(0, (2, 1.6)), zorder=3.2))
m.label(-101.6, 35.2, "Comanche", size="land", fs=19, colour="#6d5233")

# the Cherokee and their road west
m.region([(-85.95, 34.6), (-85.4, 35.2), (-84.8, 35.6), (-84.0, 35.6), (-83.2, 35.4), (-83.0, 35.0), (-83.6, 34.6),
          (-84.3, 34.0), (-85.1, 33.9), (-85.7, 34.0)], "teal", alpha=0.75, hatch="//")
m.label(-82.6, 33.7, "Cherokee", size="small", colour=INK, fs=17, ha="left")
m.route([(-84.8, 35.3), (-86.8, 36.16), (-87.5, 36.87), (-88.5, 37.36), (-89.5, 37.3), (-91.5, 37.5), (-93.3, 37.2),
         (-94.16, 36.06), (-94.9, 35.9)], colour="teal", lw=3.2, style=(0, (3, 1.6)))
m.label(-91.4, 38.3, "1838", size="small", colour=FILL["teal"], fs=17)
m.label(-95.3, 34.3, "Indian\nTerritory", size="land", fs=16)

# the railway of 1869
RAIL = [(-95.94, 41.26), (-98.3, 40.9), (-100.77, 41.12), (-104.82, 41.14), (-105.6, 41.3), (-107.2, 41.8),
        (-109.5, 41.5), (-111.97, 41.22), (-112.55, 41.62), (-114.96, 41.11), (-115.76, 40.83), (-117.7, 40.97),
        (-119.8, 39.53), (-121.49, 38.58)]
m.line(RAIL, colour=INK, lw=3.0, curved=False)
m.line(RAIL, colour=PAPER, lw=1.2, style=(0, (3, 3)), curved=False)
m.label(-103.0, 42.5, "railway, 1869", size="small", colour=INK, fs=17)
m.city(-112.55, 41.62, None, star=True, r=7)
m.label(-112.4, 42.35, "Promontory", size="small", colour=INK, fs=15)
m.city(-121.49, 38.58, "Sacramento", dx=0.3, dy=-0.65)
m.city(-95.94, 41.26, "Omaha", dx=0.4, dy=0.4)
m.city(-90.07, 29.95, "New Orleans", dx=-0.2, dy=-1.45)

m.label(-104.0, 27.2, "MEXICO", size="land", fs=19, style="normal", spaced=True)
m.label(-80.5, 48.6, "BRITISH NORTH AMERICA", size="land", fs=16, style="normal")
m.label(-90.0, 26.2, "Gulf of Mexico", size="sea", fs=18)
m.label(-71.5, 33.5, "ATLANTIC\nOCEAN", size="sea", fs=20)
m.label(-123.5, 33.5, "PACIFIC\nOCEAN", size="sea", fs=20)
m.scale(500, lon=-79.5, lat=25.3)
m.save("chapters/63-west/images/map_growth.png")
