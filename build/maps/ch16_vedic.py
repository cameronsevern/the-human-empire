#!/usr/bin/env python3
"""Chapter 16: northern India between about 3,100 and 2,500 years ago, the country of the
priests and their hymns, and its spread east along the Ganges.

The areas are drawn by eye after "Late Vedic Culture (1100-500 BCE)" by Avantiputra7
(Wikimedia Commons, CC BY-SA 3.0), the map this one replaces: its solid shading (the Punjab and
the upper Ganges plain, the lands of the Kurus and Panchalas) as the heartland, its dotted
outline as the wider area, and its arrow to Videha, which it dates to about 700 BCE. Checked
against the map of the later Vedic period in Witzel, "Early Sanskritization" (1995). They follow
rivers rather than coordinates and are rough.
"""
from lib import Map
from tracing import hatched

core = [(72.6, 33.3), (74.5, 33.0), (76.0, 31.9), (77.5, 30.6), (79.0, 29.7), (80.5, 28.7), (82.0, 27.7),
        (82.5, 26.7), (81.6, 25.7), (79.6, 25.0), (77.6, 24.7), (76.2, 25.4), (75.6, 26.9), (74.6, 28.6),
        (73.0, 29.4), (71.8, 30.4), (71.9, 32.0)]
outer = [(72.0, 34.2), (73.5, 34.0), (74.5, 33.0), (76.0, 31.9), (77.5, 30.6), (79.0, 29.7), (80.5, 28.7),
         (82.0, 27.7), (82.5, 26.7), (82.3, 25.4), (80.5, 24.5), (78.5, 23.6), (76.0, 23.0), (74.0, 22.6),
         (72.8, 22.9), (72.6, 24.5), (71.3, 27.0), (70.6, 28.8), (70.8, 30.6), (71.4, 32.6)]

m = Map(67.5, 89.0, 21.0, 35.0)
m.river("Indus", "Ganges", "Yamuna", "Jhelum", "Chenab", "Ravi", "Beas", "Sutlej", "Ghäghara", "Gandak")
hatched(m, outer, minus=[core], colour="brown")
m.region(core, "brown", alpha=0.45)
m.route([(82.3, 26.9), (83.4, 27.0), (84.4, 26.75)], colour="red", lw=4)

m.label(76.2, 28.2, "country of\nthe hymns", size="small", colour="#2f2a26", fs=19)
m.label(73.3, 31.7, "PUNJAB", fs=21)
m.label(86.2, 26.4, "VIDEHA")
m.label(83.6, 27.75, "about 2,700\nyears ago", size="small", colour="red", fs=17)
m.label(70.0, 27.3, "Indus", size="sea", fs=19, rot=60)
m.label(85.5, 24.9, "Ganges", size="sea", fs=19, rot=-10)
m.label(78.8, 26.6, "Yamuna", size="sea", fs=18, rot=-40)
m.label(82.0, 30.6, "H I M A L A Y A S", size="land", fs=19, rot=-22)
m.label(68.6, 22.0, "Arabian\nSea", size="sea", fs=19)
m.label(88.0, 21.4, "Bay of\nBengal", size="sea", fs=19)
m.label(70.0, 25.5, "desert", size="land", fs=18)
m.scale(300, lon=79.5, lat=21.6)
m.save("chapters/16-caste/images/map_vedic_india.png")
