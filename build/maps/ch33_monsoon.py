#!/usr/bin/env python3
"""Chapter 33: the Indian Ocean and its two monsoon winds, with the places the chapter names.

Drawn for this chapter, which had no map. The arrows show the prevailing directions only: the summer
wind from the south-west (about June to September) and the winter wind from the north-east (about
November to February), over the Arabian Sea, the Bay of Bengal and the South China Sea; south of the
equator the winds turn, and the arrows are not a chart of them. Positions from English Wikipedia:
Srivijaya at Palembang, the Chola kingdom at its capital Thanjavur.
"""
from lib import Map, INK, FILL

m = Map(26.0, 122.0, -23.0, 31.0)
m.river("Zambezi", "Limpopo", "Mekong", "Ganges", "Indus", en=True)

SUMMER, WINTER = "red", "blue"
for a, b in [((55.0, 5.0), (66.0, 15.5)), ((82.5, 3.5), (89.5, 14.0)), ((108.0, 7.5), (113.5, 17.0))]:
    m.route([a, ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), b], colour=SUMMER, lw=4.6)
for a, b in [((71.0, 12.0), (60.5, 2.5)), ((96.0, 12.5), (89.5, 2.5)), ((118.5, 15.0), (112.0, 5.5))]:
    m.route([a, ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), b], colour=WINTER, lw=4.6, style=(0, (2.2, 1.3)))
m.label(52.0, 1.6, "summer wind\nfrom the south-west", size="small", colour=SUMMER, fs=19)
m.label(68.0, 0.6, "winter wind\nfrom the north-east", size="small", colour=WINTER, fs=19)

m.city(104.75, -2.99, "Srivijaya (Palembang)", dx=-0.8, dy=-0.9, size=19)
m.label(108.9, -2.8, "Belitung", size="small", colour=INK, fs=19, ha="left")
m.city(79.14, 10.79, "Thanjavur", dx=-0.8, dy=0.0, size=19)
m.label(78.4, 13.5, "CHOLA", fs=19, ha="center")
m.city(103.87, 13.41, "Angkor", dx=-0.8, dy=0.6, size=19)
m.city(110.20, -7.61, "Borobudur", dx=0.8, dy=-1.0, size=19)
m.city(39.52, -8.96, "Kilwa", dx=0.8, dy=0.0, size=19)
m.city(30.93, -20.27, "Great Zimbabwe", dx=0.8, dy=0.7, size=19)
m.city(113.26, 23.13, "Guangzhou", dx=-0.8, dy=0.4, size=19)
m.label(97.2, 4.0, "Strait of\nMalacca", size="sea", fs=18, ha="right")

m.label(46.0, 23.0, "ARABIA", size="land", fs=21, style="normal")
m.label(79.0, 22.0, "INDIA", size="land", fs=22, style="normal")
m.label(108.0, 27.5, "CHINA", size="land", fs=22, style="normal")
m.label(33.0, -4.0, "AFRICA", size="land", fs=22, style="normal")
m.label(100.4, 0.2, "Sumatra", size="land", fs=18)
m.label(110.5, -10.0, "Java", size="land", fs=18)
m.label(51.2, 27.2, "Persian\nGulf", size="sea", fs=18)
m.label(63.5, 19.6, "Arabian Sea", size="sea", fs=21)
m.label(87.0, 17.6, "Bay of\nBengal", size="sea", fs=20)
m.label(117.6, 19.6, "South China\nSea", size="sea", fs=19)
m.label(75.0, -12.0, "INDIAN OCEAN", size="sea", fs=24)
m.scale(1000, lon=90.0, lat=-21.0)
m.save("chapters/33-ocean/images/map_monsoon.png")
