#!/usr/bin/env python3
"""Chapter 94: Vietnam, Laos and Cambodia during the American war: the line of 1954 near the seventeenth
parallel dividing North from South Vietnam, Hanoi, Saigon, Dien Bien Phu, My Lai, the Gulf of Tonkin, the
Mekong delta, and the supply trails from the North through Laos and Cambodia.

Drawn for this chapter, which had no map. The countries are the modern ones (Natural Earth admin-0, 1:10
million, public domain; cut to the frame and simplified: data/ch94_indochina_ne10m.geojson), whose borders are
those of French Indochina. The dividing line follows the Ben Hai
river, just south of the seventeenth parallel, from the coast to the border of Laos. The trails are a
simplified version of the "Ho Chi Minh trail" in English Wikipedia and the US Army Center of Military
History's maps, roughly: from the North through the passes at Mu Gia and Ban Karai, south through eastern
Laos past Tchepone and Attapeu, and into north-eastern Cambodia towards the country north-west of Saigon,
with branches east into South Vietnam. Positions from English Wikipedia. Hue and Da Nang are left out: the
chapter does not name them.
"""
import os
import numpy as np
import geopandas as gpd
from shapely.geometry import box, Polygon, LineString
from shapely.ops import unary_union, linemerge
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth

C = gpd.read_file(os.path.join(lib.DATA, "ch94_indochina_ne10m.geojson"))
G = {r["NAME"]: r.geometry for _, r in C.iterrows()}

m = Map(100.3, 110.2, 8.2, 23.6)
viet = G["Vietnam"].buffer(0.08).difference(unary_union([G[n] for n in ["Laos", "Cambodia", "China"]]))
viet = viet.intersection(m.land)
ben_hai = [(107.14, 17.09), (106.95, 17.00), (106.75, 16.98), (106.55, 16.95), (106.30, 16.95)]
north = Polygon([(100, 16.95)] + ben_hai[::-1][1:] + [(111, 17.09), (111, 24), (100, 24)])
south_cut = viet.difference(north)
m.region(viet.intersection(north), "red", alpha=0.36)
m.region(south_cut, "blue", alpha=0.36)
m.river("Mekong", lw=2.0)

# borders: the shared edges of the admin-0 polygons, clipped to the land
names = ["Vietnam", "Laos", "Cambodia", "Thailand", "China", "Myanmar"]
for i, a in enumerate(names):
    for b in names[i + 1:]:
        edge = G[a].boundary.intersection(G[b].buffer(0.01)).intersection(m.land.buffer(-0.02))
        parts = [l for l in getattr(edge, "geoms", [edge]) if l.geom_type == "LineString" and not l.is_empty]
        edge = linemerge(parts) if parts else edge
        for line in getattr(edge, "geoms", [edge]):
            if line.is_empty or line.geom_type != "LineString":
                continue
            xy = np.array(line.coords)
            m.ax.plot(xy[:, 0], xy[:, 1], color=SOFT, lw=1.6, ls=(0, (5, 2.5)), zorder=2.6)

line = viet.buffer(0.02).intersection(LineString(smooth(ben_hai, n=8)))
for l in getattr(line, "geoms", [line]):
    m.line(list(l.coords), colour=INK, lw=3.6, curved=False)

# the trails: a main line and branches
trail = [(105.65, 18.75), (105.80, 17.70), (106.15, 16.80), (106.40, 15.85), (106.80, 14.85), (107.15, 13.95),
         (106.95, 12.95), (106.55, 12.05), (106.20, 11.35)]
m.route(trail, colour="brown", lw=3.2, style=(0, (3, 1.6)))
for b in [[(106.15, 16.80), (106.75, 16.45), (107.25, 16.15)], [(106.80, 14.85), (107.45, 14.95), (108.0, 15.05)],
          [(107.15, 13.95), (107.65, 13.55), (108.0, 13.2)]]:
    m.route(b, colour="brown", lw=2.6, style=(0, (3, 1.6)))

m.city(105.85, 21.03, "Hanoi", dx=0.22, dy=0.2, bold=True)
m.city(106.70, 10.78, "Saigon", dx=0.25, dy=0.12, bold=True)
m.city(103.02, 21.39, "Dien Bien Phu", dx=0.0, dy=0.38)
m.city(108.87, 15.18, "My Lai", dx=0.25, dy=0.0)

m.label(104.6, 22.3, "NORTH\nVIETNAM", fs=19)
m.label(108.25, 12.45, "SOUTH\nVIETNAM", fs=19)
m.label(103.6, 19.2, "LAOS", fs=22)
m.label(104.6, 12.75, "CAMBODIA", fs=22)
m.label(101.6, 15.4, "THAILAND\n(Siam)", size="land", colour="#5a534b", fs=17, style="normal")
m.label(107.0, 23.1, "CHINA", size="land", colour="#5a534b", fs=18, style="normal")
m.label(107.65, 19.55, "Gulf of\nTonkin", size="sea", fs=18)
m.label(108.5, 9.7, "South China\nSea", size="sea", fs=18)
m.label(102.2, 9.3, "Gulf of\nSiam", size="sea", fs=17)
m.label(105.55, 9.65, "Mekong\ndelta", size="land", colour=INK, fs=16)
m.label(107.35, 17.15, "line of 1954", size="small", colour=INK, fs=16, ha="left")
m.label(105.6, 16.35, "supply\ntrails", size="small", colour=FILL["brown"], fs=17, style="italic")
m.scale(200, lon=100.7, lat=14.1)
m.save("chapters/94-vietnam/images/map_vietnam.png")
