#!/usr/bin/env python3
"""Chapter 9: Babylon's land when Hammurabi became king, about 3,800 years ago, and when he
died, about 3,750 years ago.

Both areas are traced by eye from "Hammurabi's Babylonia" by MapMaster (Wikimedia Commons,
CC BY-SA 4.0), by way of the cities each one takes in, and checked against the map of
Hammurabi's conquests in Van De Mieroop, King Hammurabi of Babylon (2005). They are rough.
Coastline and rivers are modern; city positions from English Wikipedia.
"""
from lib import Map, INK

m = Map(39.6, 49.0, 29.6, 36.0, lakes=False)
m.river("Euphrates", "Tigris", en=True)
big = [(40.4, 34.95), (41.3, 34.85), (42.5, 34.3), (43.6, 34.05), (44.6, 34.1), (45.3, 33.6), (46.0, 32.9),
       (46.8, 32.2), (47.4, 31.4), (47.6, 30.85), (47.1, 30.4), (46.2, 30.6), (45.5, 30.95), (45.0, 31.5),
       (44.3, 32.05), (43.6, 32.7), (42.7, 33.4), (41.7, 34.0), (40.7, 34.3)]
small = [(44.0, 33.2), (44.45, 33.25), (44.85, 32.65), (45.0, 32.25), (44.6, 32.05), (44.2, 32.25), (44.0, 32.7)]
m.region(big, "gold", alpha=0.35)
m.region(small, "red", alpha=0.55, hatch="//")

m.city(44.421, 32.536, "Babylon", dx=-0.15, bold=True, size="region")
m.city(44.252, 33.059, "Sippar", dx=-0.15)
m.city(40.887, 34.550, "Mari", dx=0.0, dy=0.3)
m.city(45.853, 31.286, "Larsa", dx=0.15, dy=0.08)
m.city(46.103, 30.963, "Ur", dx=0.15, dy=-0.05)
m.city(45.233, 32.127, "Nippur", dx=0.15)
m.city(44.727, 33.484, "Eshnunna", dx=0.15, dy=0.1)
m.city(43.262, 35.456, "Assur", dx=0.15)
m.city(48.258, 32.190, "Susa", dx=0.15)

m.label(43.55, 31.75, "Babylon's land\nwhen Hammurabi\nbecame king", size="small", colour=INK, fs=16.5, ha="right")
m.ax.plot([43.6, 44.45], [31.85, 32.2], color=INK, lw=1.4, zorder=6)
m.label(46.05, 31.78, "Babylon's land\nwhen he died", size="small", colour=INK, fs=16.5)
m.label(47.9, 33.3, "ELAM", size="region")
m.label(48.72, 29.85, "Gulf", size="sea")
m.label(42.0, 34.95, "Euphrates", size="sea", rot=-25)
m.label(43.7, 34.75, "Tigris", size="sea", rot=-65)
m.label(42.0, 31.0, "desert", size="land")
m.scale(100, lon=40.0, lat=29.9)
m.save("chapters/09-law/images/map_hammurabi.png")
