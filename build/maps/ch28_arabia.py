#!/usr/bin/env python3
"""Chapter 28: Arabia about the year 600, between the Roman and Persian empires.

Replaces "Pre Islamic Arabia" by Javierfv1212 (Wikimedia Commons, public domain), whose labels were
too small to read. The two empires are traced roughly after that map: Rome held Egypt, Palestine and
Syria to the edge of the desert, and Persia held Iraq and Iran, with the frontier on the middle Euphrates.
Their edge in the desert was never a line, and the areas are soft. Yemen, under Persian overlords from
the 570s, is left unshaded and simply named, as the chapter names it. Positions from English Wikipedia.
"""
from lib import Map, INK
from tracing import states

rome = [(26.0, 39.5), (36.0, 39.5), (40.5, 39.0), (40.5, 37.6), (41.0, 36.3), (39.6, 35.4), (38.6, 34.0), (37.6, 32.8),
        (37.0, 31.0), (36.0, 29.8), (35.0, 28.2), (33.6, 27.6), (33.2, 25.0), (33.0, 23.6), (31.5, 23.6),
        (29.5, 24.5), (27.5, 27.5), (25.5, 30.0), (25.0, 31.8)]
persia = [(41.0, 36.6), (42.5, 37.6), (46.0, 38.6), (56.0, 38.5), (61.0, 37.5), (61.0, 25.2), (57.5, 25.6),
          (56.3, 27.0), (52.5, 27.6), (50.2, 29.6), (48.6, 29.9), (47.6, 30.0), (46.0, 30.8), (44.5, 31.6),
          (43.4, 32.6), (42.0, 33.8), (40.9, 34.6), (40.2, 35.3)]

m = Map(27.5, 60.0, 12.3, 38.2)
m.river("Nile", "Tigris", "Euphrates", "Firat", en=True)
states(m, [(rome, "purple"), (persia, "red")], alpha=0.38)

m.label(34.0, 37.5, "ROMAN EMPIRE", fs=24)
m.label(53.0, 33.6, "PERSIAN EMPIRE", fs=24)
m.label(30.0, 27.0, "EGYPT", size="land", fs=21, style="normal")
m.label(38.6, 35.3, "SYRIA", size="land", fs=21, style="normal")
m.label(44.4, 34.2, "IRAQ", size="land", fs=21, style="normal")
m.label(46.0, 23.0, "A R A B I A", size="land", fs=30, style="normal")
m.label(46.0, 14.8, "YEMEN", size="land", fs=22, style="normal")

m.city(39.83, 21.42, "Mecca", dx=0.5, dy=-0.25, star=True, bold=True, size=22)
m.city(39.61, 24.47, "Medina (Yathrib)", dx=0.5, dy=0.15, bold=True, size=21)
m.city(38.78, 23.73, "Badr", dx=-0.45, dy=-0.15, size=20)
m.city(35.23, 31.78, "Jerusalem", dx=-0.45, dy=0.05, size=20)
m.city(36.29, 33.51, "Damascus", dx=0.45, dy=0.05, size=20)

m.label(37.9, 19.6, "Red\nSea", size="sea", fs=22)
m.label(52.2, 26.4, "Persian\nGulf", size="sea", fs=21)
m.label(56.5, 16.0, "Arabian Sea", size="sea", fs=22)
m.label(30.8, 33.3, "Mediterranean Sea", size="sea", fs=21)
m.scale(500, lon=52.0, lat=13.0)
m.save("chapters/28-islam/images/map_arabia.png")
