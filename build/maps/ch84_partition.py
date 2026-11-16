#!/usr/bin/env python3
"""Chapter 84: British India divided in 1947: India, West Pakistan and East Pakistan; the partition lines
drawn by Radcliffe through Punjab and Bengal; the princely state of Kashmir and the ceasefire line of 1949;
the main flows of refugees; and the places named in the chapter (Delhi, Lahore, Amritsar, Rawalpindi,
Karachi, Bombay, Calcutta, Dhaka, Srinagar).

Drawn for this chapter, which had no map. The frontiers between India and Pakistan and between India and
East Pakistan are from OpenStreetMap (data/ch84_borders_osm.txt): the line between Punjab's two halves, from
the Ravi near Madhopur to the edge of Bahawalpur state near Fazilka, and the line through Bengal, west of
the Brahmaputra, are drawn as Radcliffe's lines; the rest of the frontier followed older boundaries of
provinces and princely states (Sindh against Rajputana, Assam and Tripura against east Bengal). In Kashmir
the OpenStreetMap line is the Line of Control, which follows the ceasefire line of 1 January 1949 (agreed at
Karachi that July) with small changes made in 1972; it is drawn as far as the point NJ9842, where the
line of 1949 stopped. The outer frontiers and the land west and east of the lines are Natural Earth
(admin-0, 110 m, as shipped with geopandas). The provinces of Punjab and Bengal and the state of Jammu and
Kashmir are drawn by hand as soft outlines, roughly, after the maps of English Wikipedia's "Partition of
India", "Punjab Province (British India)", "Bengal Presidency" and "Princely state of Jammu and Kashmir"
(Bengal as in ch76_india.py; the Sylhet district of Assam, which also went to East Pakistan, lies outside
it). Burma, which had been separated from British India in 1937, is only named. The refugee arrows are
schematic: Hindus and Sikhs east across Punjab and west across Bengal, and from Sindh by sea to Bombay;
Muslims west across Punjab, from Delhi to Karachi, and east across Bengal. Positions from English Wikipedia.
"""
import os
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, LineString, box
from shapely.ops import unary_union
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import lib
from lib import Map, INK, PAPER, FILL, SOFT, HALO, smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
GOLD, GREEN, RED = FILL["gold"], FILL["green"], FILL["red"]

B = {}
for line in open(os.path.join(lib.DATA, "ch84_borders_osm.txt")):
    if line.startswith("#") or ":" not in line:
        continue
    k, rest = line.strip().split(":", 1)
    B[k] = [LineString([tuple(map(float, p.split(","))) for p in piece.split()]) for piece in rest.split("|")]
pak = B["pak"][0]
                                   # north (the end of the Line of Control) to Sir Creek
ban = max(B["ban"], key=lambda l: l.length)         # the Sundarbans to the Burmese frontier

m = Map(60.5, 97.5, 7.0, 37.4)
LAND = m.land
whole = unary_union([G["India"], G["Pakistan"], G["Bangladesh"]]).buffer(0.02).intersection(LAND)
west_of = Polygon(list(pak.coords) + [(67.0, 22.5), (55.0, 22.5), (55.0, 40.0), (pak.coords[0][0], 40.0)]).buffer(0)
east_closed = list(ban.coords) + [(92.40, 21.40), (92.33, 21.0), (92.30, 20.4), (89.2, 20.4)]
east_pak = Polygon(east_closed).buffer(0).intersection(LAND)
west_pak = whole.intersection(west_of)
india = whole.difference(west_of).difference(east_pak)
m.region(india, GOLD, alpha=0.30, edge=False)
m.region(west_pak, GREEN, alpha=0.42, edge=False)
m.region(east_pak, GREEN, alpha=0.42, edge=False)

# Kashmir, the princely state of Jammu and Kashmir, roughly
kashmir = [(74.55, 32.55), (75.35, 32.35), (75.9, 32.6), (76.4, 33.05), (77.3, 32.85), (78.3, 32.5), (79.0, 32.4),
           (79.4, 33.1), (80.2, 34.3), (80.2, 35.3), (79.4, 35.6), (78.0, 35.5), (77.0, 35.9), (76.0, 36.3),
           (75.4, 36.9), (74.5, 37.05), (73.6, 36.9), (72.6, 36.4), (72.9, 35.6), (73.6, 35.0), (73.6, 34.5),
           (73.35, 34.0), (73.45, 33.55), (73.65, 33.0), (74.1, 32.85)]
m.region(kashmir, "grey", alpha=0.10, hatch="///", edge=True, smooth_n=10)

# Punjab and Bengal as they were before the partition, roughly: soft dotted outlines
punjab = [(71.8, 33.9), (72.6, 34.0), (73.4, 33.85), (73.7, 33.2), (74.2, 32.85), (74.55, 32.55), (75.35, 32.35),
          (75.9, 32.55), (76.6, 32.85), (77.5, 32.6), (77.85, 32.2), (77.7, 31.4), (77.9, 31.0), (77.6, 30.4),
          (77.3, 29.5), (77.25, 28.75), (77.45, 27.95), (76.5, 27.85), (75.4, 28.6), (74.5, 29.4), (73.95, 29.95),
          (73.2, 30.05), (72.0, 29.5), (71.0, 29.3), (70.5, 28.6), (69.6, 28.4), (70.0, 29.5), (69.7, 30.6),
          (70.4, 31.2), (71.2, 32.4), (71.6, 33.2)]
bengal = [(86.0, 22.0), (86.8, 21.6), (88.0, 21.5), (89.0, 21.7), (90.5, 21.9), (91.8, 22.2), (92.3, 21.0),
          (92.7, 22.5), (92.4, 24.2), (91.5, 24.6), (90.0, 25.2), (89.8, 26.0), (89.0, 26.5), (88.4, 27.1),
          (88.0, 26.4), (88.0, 25.4), (87.8, 24.9), (87.2, 24.0), (86.5, 23.5), (86.0, 22.8)]
for pts in (punjab, bengal):
    g = Polygon(smooth(pts, n=10, closed=True)).buffer(0).intersection(LAND)
    for p in getattr(g, "geoms", [g]):
        if p.geom_type == "Polygon" and p.area > 0.05:
            xy = np.array(p.exterior.coords)
            m.ax.plot(xy[:, 0], xy[:, 1], color="#6c6156", lw=2.0, ls=(0, (1, 1.6)), zorder=2.7)

m.river("Indus", "Ganges", "Brahmaputra", "Sutlej", "Ravi", lw=1.4)

# frontiers
def draw(geom, lw, style, colour=INK, halo=True, z=4.5):
    for l in getattr(geom, "geoms", [geom]):
        if l.is_empty or l.geom_type != "LineString":
            continue
        xy = np.array(l.coords)
        if halo:
            m.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=lw + 3, solid_capstyle="round", zorder=z - 0.1)
        m.ax.plot(xy[:, 0], xy[:, 1], color=colour, lw=lw, ls=style, solid_capstyle="round", zorder=z)

punjab_line = pak.intersection(box(73.3, 30.3, 75.6, 32.50))
ceasefire = pak.intersection(box(73.3, 32.85, 77.3, 35.02))
other_pak = pak.difference(box(73.3, 30.3, 75.6, 32.50).buffer(0.001)).difference(box(73.3, 32.85, 77.3, 40))
bengal_line = ban.intersection(box(88.0, 21.3, 89.95, 26.7)).intersection(LAND.buffer(0.02))
other_ban = ban.difference(box(88.0, 21.3, 89.95, 26.7).buffer(0.001))
outer = whole.boundary.intersection(LAND.buffer(-0.03))
draw(outer, 1.4, (0, (5, 2.5)), colour=SOFT, halo=False, z=2.6)
draw(other_pak, 2.0, "-", colour="#5a534b", halo=False, z=3.0)
draw(other_ban, 2.0, "-", colour="#5a534b", halo=False, z=3.0)
draw(punjab_line, 4.2, "-")
draw(bengal_line, 4.2, "-")
draw(ceasefire, 3.2, (0, (2.6, 1.3)))

# refugees: Hindus and Sikhs (solid) and Muslims (dashed)
HS = dict(colour=RED, lw=4.0)
MU = dict(colour="#3f6b3b", lw=4.0, style=(0, (2.2, 1.0)))
m.route([(72.0, 32.35), (73.4, 32.3), (75.2, 32.25), (77.0, 31.95)], **HS)                 # west Punjab east
m.route([(77.3, 29.75), (76.0, 30.2), (74.6, 30.55), (73.0, 30.85)], **MU)                # east Punjab west
m.route([(78.2, 27.7), (75.6, 26.6), (71.5, 25.6), (68.0, 24.95)], **MU)                  # Delhi and the north to Karachi
m.route([(66.3, 24.2), (67.6, 22.2), (70.0, 20.2), (72.3, 19.1)], **HS)                   # Sindh by sea to Bombay
m.route([(91.0, 24.2), (89.9, 23.9), (88.6, 23.1)], **HS)                                  # east Bengal west
m.route([(86.3, 24.9), (87.6, 25.1), (88.9, 24.9)], **MU)                                  # Bihar and west Bengal east

# places
m.city(77.21, 28.61, "Delhi", dx=0.45, dy=-0.45, ha="left", bold=True)
m.city(74.34, 31.55, "Lahore", dx=-0.4, dy=-0.05, ha="right")
m.city(74.87, 31.63, "Amritsar", dx=0.4, dy=-0.25, ha="left")
m.city(73.05, 33.60, "Rawalpindi", dx=-0.4, dy=0.25, ha="right")
m.city(67.01, 24.86, "Karachi", dx=-0.4, dy=-0.5, ha="right", bold=True)
m.city(72.88, 19.08, "Bombay", dx=0.45, dy=-0.2, ha="left")
m.city(88.36, 22.57, "Calcutta", dx=-0.45, dy=-0.35, ha="right")
m.city(90.41, 23.81, "Dhaka", dx=0.45, dy=-0.35, ha="left")
m.city(74.80, 34.08, "Srinagar", dx=0.45, dy=0.0, ha="left")

m.label(78.6, 21.5, "I N D I A", fs=28)
m.label(66.4, 28.4, "WEST\nPAKISTAN", fs=21)
m.label(90.4, 20.75, "EAST\nPAKISTAN", fs=17, ha="center")
m.label(76.9, 35.7, "KASHMIR", fs=18)
m.label(78.9, 34.15, "ceasefire\nline, 1949", size="small", colour=INK, fs=15, style="italic")
m.ax.plot([78.0, 76.75], [34.55, 35.05], color=INK, lw=1.2, zorder=6.5)
m.label(72.3, 30.05, "PUNJAB", fs=15, colour="#5a534b")
m.label(87.0, 23.65, "BENGAL", fs=15, colour="#5a534b")
m.label(68.6, 26.0, "SINDH", fs=15, colour="#5a534b")
m.label(65.6, 26.4, "BALUCHISTAN", fs=15, colour="#5a534b", ha="center")
G3 = dict(size="land", colour="#5a534b", style="normal", fs=16)
m.label(65.0, 33.5, "AFGHANISTAN", **G3)
m.label(85.0, 31.2, "TIBET", **G3)
m.label(84.3, 28.35, "NEPAL", fs=15, size="land", colour="#5a534b", style="normal")
m.label(95.6, 21.0, "BURMA", **G3)
m.label(86.6, 16.0, "Bay of\nBengal", size="sea", fs=19)
m.label(66.0, 15.5, "Arabian Sea", size="sea", fs=19)
m.scale(500, lon=90.5, lat=8.2)

handles = [Patch(fc=GOLD + "4d", ec=GOLD, label="India"),
           Patch(fc=GREEN + "6b", ec=GREEN, label="Pakistan"),
           Patch(fc="#8d857b1a", ec="#8d857b", hatch="///", label="Kashmir"),
           Line2D([0], [0], color=INK, lw=4.2, label="partition line, 1947"),
           Line2D([0], [0], color=INK, lw=3.2, ls=(0, (2.6, 1.3)), label="ceasefire line, 1949"),
           Line2D([0], [0], color=RED, lw=4.0, label="Hindus and Sikhs fleeing"),
           Line2D([0], [0], color="#3f6b3b", lw=4.0, ls=(0, (2.2, 1.0)), label="Muslims fleeing")]
leg = m.ax.legend(handles=handles, loc="lower left", fontsize=16, frameon=True, fancybox=False, edgecolor=INK,
                  facecolor=PAPER, framealpha=1, borderpad=0.7, labelspacing=0.45, handlelength=2.6)
leg.set_zorder(9); leg.get_frame().set_linewidth(1.2)
m.save("chapters/84-partition/images/map_partition.png")
