#!/usr/bin/env python3
"""Chapter 36: the Maya country close up, with the cities the chapter names (Tikal, Copán, Quiriguá,
Yaxchilán) and Teotihuacan to the west. The hemisphere map is ch36_americas.py.

Drawn for this chapter, which had no map. The lowlands are a soft, approximate area, as in English
Wikipedia's article on the Maya civilization: the forest of northern Guatemala, Belize and southern
Mexico and the Yucatán peninsula, with the valley of the Motagua, where Copán and Quiriguá stand, at
its south-eastern edge. Positions from English Wikipedia.
"""
from lib import Map, INK
from tracing import states

maya = [(-92.9, 17.3), (-91.6, 18.7), (-90.7, 19.9), (-90.45, 21.2), (-88.0, 21.75), (-86.6, 21.5),
        (-87.4, 18.4), (-88.3, 15.9), (-88.9, 14.65), (-89.6, 15.0), (-90.8, 15.95), (-92.1, 16.3)]

m = Map(-99.8, -86.2, 13.4, 22.2)
m.river("Usumacinta", "Motagua", "Grijalva", en=True, lw=2.0)
states(m, [(maya, "green")], alpha=0.42)

m.label(-89.2, 19.6, "MAYA\nLOWLANDS", fs=25)
m.city(-89.62, 17.22, "Tikal", dx=0.25, dy=0.22, size=22, bold=True)
m.city(-90.97, 16.90, "Yaxchilán", dx=-0.25, dy=0.2, size=21)
m.city(-89.14, 14.84, "Copán", dx=-0.25, dy=-0.15, size=21)
m.city(-89.04, 15.27, "Quiriguá", dx=0.25, dy=0.1, size=21)
m.city(-98.84, 19.69, "Teotihuacan", dx=0.0, dy=0.42, size=22, bold=True)
m.label(-98.2, 19.2, "near modern Mexico City", size="small", fs=17)

m.label(-95.4, 17.6, "MEXICO", size="land", fs=20, style="normal")
m.label(-91.3, 14.75, "GUATEMALA", size="land", fs=18, style="normal")
m.label(-88.55, 17.15, "BELIZE", size="land", fs=17, style="normal", ha="left")
m.label(-87.5, 14.6, "HONDURAS", size="land", fs=18, style="normal")
m.label(-92.0, 17.75, "Usumacinta", size="sea", fs=17, rot=-50)
m.label(-94.4, 21.0, "Gulf of Mexico", size="sea", fs=22)
m.label(-86.9, 19.4, "Caribbean\nSea", size="sea", fs=19)
m.label(-95.0, 14.6, "PACIFIC OCEAN", size="sea", fs=21)
m.scale(200, lon=-99.0, lat=13.9)
m.save("chapters/36-americas/images/map_maya.png")
