#!/usr/bin/env python3
"""Chapter 44: the winds of the Atlantic and the voyages that used them. The great wind circles, clockwise
in the North Atlantic and anticlockwise in the South; the Portuguese turn of the sea, the loop home from
West Africa by way of the Azores; Columbus's voyage of 1492-93, out from the Canaries with the trade wind
and back by the north; and da Gama's voyage of 1497-98, with its great arc through the South Atlantic to
the Cape of Good Hope and on by Malindi to Calicut.

Drawn for this chapter, which had no map. The wind circles are schematic. The routes are simplified,
following the tracks usually drawn for the two voyages (da Gama's track in the open South Atlantic is not known exactly, only that he swung far out and was
ninety-three days out of sight of land). The turn of the sea is drawn as a typical loop, not as any one
voyage. Positions from English Wikipedia.
"""
from lib import Map, INK, FILL

m = Map(-82.0, 80.0, -42.0, 47.0)

WIND = "#7f98a8"
def wind(pts):
    m.route(pts, colour=WIND, lw=2.4)

# North Atlantic: clockwise
wind([(-28.0, 12.5), (-42.0, 12.0), (-56.0, 14.5)])
wind([(-64.0, 37.0), (-56.0, 42.5), (-44.0, 44.5), (-32.0, 44.5)])
# South Atlantic: anticlockwise
wind([(-1.0, -26.0), (-4.0, -16.0), (-14.0, -9.0)])
wind([(-30.0, -10.0), (-37.0, -18.0), (-38.0, -27.0)])
wind([(-30.0, -36.0), (-18.0, -37.5), (-6.0, -35.5)])
m.label(-47.0, 17.2, "winds turn\nclockwise", size="sea", fs=19, colour=WIND)
m.label(-15.0, -23.0, "winds turn\nanticlockwise", size="sea", fs=19, colour=WIND)

# the turn of the sea (Portuguese, 1400s)
m.route([(-16.0, 12.0), (-21.0, 17.5), (-28.0, 24.0), (-33.0, 31.0), (-30.0, 36.4), (-22.0, 38.6), (-14.0, 39.0),
         (-9.6, 38.8)], colour="gold", lw=3.4, style=(0, (1.2, 1.4)))
m.label(-36.5, 22.6, "the turn\nof the sea", size="small", colour=INK, fs=19)

# Columbus 1492-93
m.route([(-6.9, 37.2), (-11.0, 33.0), (-17.2, 28.1)], colour="red", lw=3.2, arrow=False)
m.route([(-17.2, 28.1), (-35.0, 27.6), (-55.0, 26.0), (-67.0, 25.2), (-74.3, 24.1)], colour="red", lw=3.2)
m.route([(-71.0, 20.0), (-62.0, 29.0), (-50.0, 36.5), (-38.0, 38.3), (-25.1, 37.0), (-15.0, 38.2), (-9.4, 38.7)],
        colour="red", lw=3.2, style=(0, (5, 2.5)))
m.label(-56.0, 22.6, "Columbus 1492", size="small", colour=FILL["red"], fs=20)
m.label(-55.5, 31.8, "Columbus 1493", ha="left", size="small", colour=FILL["red"], fs=20)

# da Gama 1497-98
m.route([(-9.4, 38.5), (-14.0, 33.0), (-16.5, 28.0), (-18.0, 22.0), (-23.5, 15.0), (-22.5, 6.0), (-24.0, -6.0),
         (-29.0, -18.0), (-26.0, -29.0), (-12.0, -36.0), (5.0, -36.5), (18.47, -34.9), (26.0, -34.8),
         (35.6, -26.0), (40.7, -15.0), (40.6, -3.6)], colour="blue", lw=3.4, arrow=False, style=(0, (7, 2.5, 1.5, 2.5)))
m.route([(40.6, -3.6), (50.0, 3.0), (62.0, 8.0), (75.6, 11.2)], colour="blue", lw=3.4,
        style=(0, (7, 2.5, 1.5, 2.5)))
m.label(-37.0, -6.5, "da Gama\n1497-98", size="small", colour=FILL["blue"], fs=20)

# places
m.city(-9.14, 38.72, "Lisbon", dx=0.0, dy=2.1, bold=True)
m.city(-5.32, 35.89, "Ceuta", dx=1.0, dy=-0.5, ha="left")
m.city(-16.95, 32.65, "Madeira", dx=-1.2, dy=0.6, ha="right")
m.city(-25.5, 37.75, "Azores", dx=-1.0, dy=2.4, ha="right")
m.city(-15.6, 28.1, "Canaries", dx=1.3, dy=-0.3, ha="left")
m.city(-14.5, 26.13, None)
m.label(-13.2, 24.4, "Cape Bojador", size="small", colour=INK, fs=18, ha="left")
m.city(-23.6, 15.1, "Cape Verde\nIslands", dx=-1.4, dy=0.2, ha="right")
m.city(-74.5, 24.05, "Bahamas", dx=0.0, dy=6.8, ha="center")
m.label(-74.5, 27.9, "landfall 1492", size="small", fs=17)
m.city(18.47, -34.36, "Cape of\nGood Hope", dx=-0.4, dy=-4.0, ha="center")
m.city(40.12, -3.22, "Malindi", dx=1.4, dy=-0.6, ha="left")
m.city(75.78, 11.25, "Calicut", dx=0.0, dy=2.4, bold=True)

m.label(-35.0, 4.0, "ATLANTIC OCEAN", size="sea", fs=22)
m.label(68.0, -18.0, "INDIAN\nOCEAN", size="sea", fs=22)
m.label(15.0, 8.0, "AFRICA", size="land", fs=24, style="normal")
m.label(-58.0, -10.0, "SOUTH\nAMERICA", size="land", fs=21, style="normal")
m.label(12.0, 43.5, "EUROPE", size="land", fs=21, style="normal")
m.scale(1000, lon=50.0, lat=-38.0)
m.save("chapters/44-columbus/images/map_atlantic.png")
