#!/usr/bin/env python3
"""Chapter 95: the American South and the places of the civil rights campaign, 1955 to 1968: Montgomery
(the bus boycott), Nashville (the workshops), Greensboro (the first sit-in), Albany, Birmingham, Selma and
the march to Montgomery, Memphis, Washington (the march of 1963), and the route of the bus rides of 1961.

Drawn for this chapter, which had no map. The route of the 1961 rides is simplified, roughly, after English
Wikipedia's "Freedom Riders": from Washington through Virginia and the Carolinas to Atlanta, then into Alabama,
where a bus was burned outside Anniston and riders were beaten in Birmingham and Montgomery, and on to
Jackson, Mississippi, where they were arrested. The state borders are not drawn: the states are named in
grey. Positions from English Wikipedia.
"""
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO

m = Map(-93.0, -75.3, 29.6, 39.6)
m.river("Mississippi", "Tennessee", "Alabama", lw=1.6)

# the bus rides of 1961: Washington, Richmond, Lynchburg, Danville, Greensboro, Charlotte, Rock Hill, Sumter,
# Augusta, Athens, Atlanta, Anniston, Birmingham, Montgomery, Jackson
rides = [(-77.04, 38.91), (-77.44, 37.54), (-79.14, 37.41), (-79.40, 36.59), (-79.79, 36.07), (-80.84, 35.23),
         (-81.03, 34.92), (-80.34, 33.92), (-81.97, 33.47), (-83.38, 33.96), (-84.39, 33.75), (-85.83, 33.66),
         (-86.81, 33.52), (-86.30, 32.38), (-90.18, 32.30)]


def dense(pts, step=0.12):
    """Points every step degrees along straight legs, so that the smoothing in route() cannot overshoot."""
    import numpy as np
    out = []
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        n = max(2, int(np.hypot(x1 - x0, y1 - y0) / step))
        out += [(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t) for t in np.linspace(0, 1, n, endpoint=False)]
    return out + [pts[-1]]


m.route(dense(rides), colour="red", lw=3.2, style=(0, (4, 1.8)))
m.route([(-87.02, 32.41), (-86.66, 32.36), (-86.36, 32.37)], colour="blue", lw=3.6, arrow=True)   # Selma march

m.city(-86.30, 32.38, "Montgomery", dx=0.25, dy=-0.28, bold=True)
m.city(-87.02, 32.41, "Selma", dx=-0.2, dy=0.25)
m.city(-86.81, 33.52, "Birmingham", dx=-0.3, dy=0.18)
m.city(-85.83, 33.66, "Anniston:\nbus burned", dx=0.0, dy=0.5, ha="center")
m.city(-84.39, 33.75, "Atlanta", dx=0.25, dy=-0.25)
m.city(-84.16, 31.58, "Albany", dx=0.25, dy=0.0)
m.city(-86.78, 36.16, "Nashville", dx=0.25, dy=0.15)
m.city(-90.05, 35.15, "Memphis", dx=0.25, dy=0.12)
m.city(-90.18, 32.30, "Jackson", dx=-0.25, dy=0.22)
m.city(-79.79, 36.07, "Greensboro", dx=0.25, dy=0.22)
m.city(-77.04, 38.91, "Washington", dx=0.25, dy=0.15, bold=True)

G = dict(size="land", colour="#5a534b", fs=17)
m.label(-89.6, 33.3, "MISSISSIPPI", **G)
m.label(-86.7, 31.3, "ALABAMA", **G)
m.label(-83.4, 32.4, "GEORGIA", **G)
m.label(-86.2, 35.55, "TENNESSEE", **G)
m.label(-78.7, 35.45, "NORTH CAROLINA", **G)
m.label(-80.4, 33.2, "SOUTH\nCAROLINA", **G)
m.label(-78.6, 37.75, "VIRGINIA", **G)
m.label(-92.2, 34.6, "ARKANSAS", **G)
m.label(-91.7, 31.2, "LOUISIANA", **G)
m.label(-83.6, 30.25, "FLORIDA", **G)
m.label(-87.6, 29.95, "Gulf of Mexico", size="sea", fs=19)
m.label(-76.3, 33.0, "Atlantic\nOcean", size="sea", fs=19)

m.label(-80.85, 35.85, "bus rides, 1961", size="small", colour=FILL["red"], fs=17, ha="right", style="italic")
m.label(-87.15, 32.02, "march, 1965", size="small", colour=FILL["blue"], fs=16, ha="center", style="italic")
m.scale(200, lon=-92.6, lat=30.2)
m.save("chapters/95-civil-rights/images/map_south.png")
