#!/usr/bin/env python3
"""Chapter 56: eastern North America in 1775. The thirteen colonies, shaded together and named; the line of
1763 along the mountains, beyond which the colonists were forbidden to settle, and some of the Native
nations whose lands lay beyond it; Canada, British since 1763, with Quebec; the Ohio and the Mississippi;
and Boston, New York, Philadelphia, Saratoga (1777) and Yorktown (1781).

Drawn for this chapter, which had no map. The colonies are shaded as one rough area, without the borders
between them, many of which were disputed; their names sit on or beside them. The line of 1763 is drawn
roughly, as it is usually drawn on maps of the Royal Proclamation (English Wikipedia, "Royal
Proclamation of 1763"): along the Appalachian divide from New York to Georgia and down to the border of
Florida. The Native nations are placed roughly where their main towns lay about 1775. Positions from
English Wikipedia.
"""
from lib import Map, INK, FILL, PAPER

m = Map(-92.0, -63.0, 29.2, 47.9)
m.river("Ohio", "Mississippi", "Hudson", "Delaware", "Susquehanna", "Potomac", "St. Lawrence", "Tennessee")

LINE = [(-73.4, 45.0), (-74.2, 44.0), (-75.0, 43.0), (-75.4, 42.0), (-77.0, 41.3), (-78.4, 40.4), (-79.3, 39.4),
        (-80.0, 38.4), (-81.0, 37.3), (-82.0, 36.3), (-83.0, 35.2), (-83.3, 34.5), (-82.7, 33.4), (-82.3, 32.2),
        (-82.1, 30.8)]
colonies = LINE + [(-81.4, 30.6), (-76.0, 34.5), (-75.0, 37.0), (-73.5, 40.4), (-69.5, 41.2), (-66.9, 44.7),
                   (-68.0, 46.2), (-70.3, 45.6), (-71.5, 45.0)]
m.region(colonies, "gold", alpha=0.35, smooth_n=4)
m.line(LINE, colour="red", lw=3.2, style=(0, (5, 2.5)))
m.label(-80.6, 39.7, "line of 1763", size="small", colour=FILL["red"], fs=19, rot=48, style="italic")

# the colonies
on_land = [(-75.4, 44.3, "NEW YORK", 0), (-77.3, 40.95, "PENNSYLVANIA", 0), (-79.0, 37.75, "VIRGINIA", 0),
           (-78.7, 35.6, "NORTH CAROLINA", 0), (-80.6, 33.85, "SOUTH\nCAROLINA", 0), (-82.6, 31.6, "GEORGIA", 0)]
for lon, lat, t, r in on_land:
    m.label(lon, lat, t, fs=15, rot=r)
beside = [((-71.6, 43.7), (-68.6, 42.5), "NEW HAMPSHIRE"), ((-72.3, 42.4), (-68.6, 41.45), "MASSACHUSETTS"),
          ((-71.55, 41.75), (-68.6, 40.75), "RHODE ISLAND"), ((-72.7, 41.6), (-68.6, 40.05), "CONNECTICUT"),
          ((-74.5, 40.1), (-71.0, 38.55), "NEW JERSEY"), ((-75.5, 39.0), (-72.6, 37.75), "DELAWARE"),
          ((-76.7, 39.3), (-73.6, 36.95), "MARYLAND")]
for (x0, y0), (x1, y1), t in beside:
    m.ax.plot([x0, x1 - 0.15], [y0, y1], color=INK, lw=1.0, zorder=6.5)
    m.ax.plot(x0, y0, "o", ms=3.5, color=INK, zorder=6.5)
    m.label(x1, y1, t, fs=15, ha="left")

# beyond the line
for lon, lat, t in [(-76.6, 42.55, "Iroquois"), (-83.3, 39.6, "Shawnee"), (-84.6, 35.5, "Cherokee"),
                    (-85.8, 32.6, "Creek")]:
    m.label(lon, lat, t, size="land", fs=17)
m.label(-87.5, 37.6, "lands of the\nNative nations", size="land", fs=18)

m.city(-71.21, 46.81, "Quebec", dx=-0.35, dy=0.15, bold=True)
m.city(-71.06, 42.36, None)
m.label(-70.75, 42.62, "Boston", size="small", colour=INK, fs=16.5, ha="left", style="normal")
m.city(-74.0, 40.71, None)
m.city(-75.17, 39.95, "Philadelphia", dx=-0.3, dy=-0.2)
m.city(-73.64, 43.0, "Saratoga, 1777", dx=0.3, dy=0.0, star=True, r=7)
m.city(-76.51, 37.24, "Yorktown, 1781", dx=-0.3, dy=-0.3, star=True, r=7)
m.ax.annotate("New York", xy=(-74.0, 40.71), xytext=(-73.3, 39.9), fontsize=16.5, color=INK, zorder=7,
              ha="left", va="center", path_effects=__import__("lib").HALO,
              arrowprops=dict(arrowstyle="-", color=INK, lw=1.0, shrinkA=0, shrinkB=4))

m.label(-77.0, 46.6, "CANADA", size="land", fs=19, style="normal")
m.label(-77.0, 45.9, "British from 1763", size="land", fs=15)
m.label(-89.6, 31.0, "Mississippi", size="sea", fs=16, rot=-80)
m.label(-86.0, 38.35, "Ohio", size="sea", fs=16)
m.label(-70.0, 34.5, "ATLANTIC OCEAN", size="sea", fs=22)
m.label(-87.5, 44.0, "Lake\nMichigan", size="sea", fs=15)
m.scale(300, lon=-67.5, lat=30.4)
m.save("chapters/56-america/images/map_colonies_1775.png")
