#!/usr/bin/env python3
"""Chapter 72: the Western Front, 1914 to 1918. The trench line as it stood for most of 1915 and 1916, the
ground held by Germany behind it, the furthest German advance of 1918, Ypres, the Somme, Verdun, Paris,
the Marne, and Compiègne, where the armistice was signed in a railway carriage in the forest.

Drawn for this chapter, which had no map. The small world inset of the outline is left out: it would
crowd the map. The front line follows the maps in English Wikipedia's "Western Front (World War I)",
"Battle of the Somme", "Battle of Verdun" and "German spring offensive", and is simplified: Nieuport, east
of Ypres, Loos, east of Arras, east of Albert, Noyon, north of Soissons and Reims, north of Verdun, the
St Mihiel salient, Pont-a-Mousson, the Vosges, the Swiss border near Bonfol. The 1918 line joins the
furthest points of the spring offensives: the Lys (Kemmel), Villers-Bretonneux and Montdidier, and the
Marne at Chateau-Thierry. The national frontiers of 1914 are drawn from Natural Earth's small-scale
admin-0 countries, smoothed, with Alsace-Lorraine (German from 1871) cut off by a hand-drawn line; the
Belgian-German frontier is the modern one, which differs from that of 1914 only by Eupen and Malmedy.
The Somme, which is not in Natural Earth, is traced by hand through Ham, Peronne, Corbie, Amiens and
Abbeville. Positions from English Wikipedia.
"""
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, LineString, box
from shapely.ops import unary_union, linemerge
from lib import Map, INK, PAPER, FILL, WATER, smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
P = lambda pts: Polygon(pts).buffer(0)

W, E, S, N = 0.6, 8.6, 47.25, 51.55
m = Map(W, E, S, N)
frame = box(W - 1, S - 1, E + 1, N + 1)

alsace = G["France"].intersection(P([(5.85, 49.55), (6.0, 49.2), (6.25, 48.95), (6.6, 48.75), (7.05, 48.5),
    (7.1, 48.2), (6.95, 47.85), (7.05, 47.45), (8.5, 47.5), (8.5, 49.6)]))
states = [G["France"].difference(alsace).intersection(frame), G["Germany"].union(alsace).intersection(frame),
          G["Belgium"], G["Luxembourg"], G["Netherlands"], G["Switzerland"]]

front = [(2.75, 51.15), (2.85, 50.97), (2.97, 50.85), (2.88, 50.65), (2.82, 50.46), (2.82, 50.3), (2.72, 50.12),
         (2.72, 50.0), (2.85, 49.78), (2.98, 49.58), (3.3, 49.43), (3.62, 49.4), (3.95, 49.32), (4.15, 49.3),
         (4.5, 49.22), (4.9, 49.2), (5.2, 49.25), (5.45, 49.22), (5.6, 49.1), (5.58, 48.98), (5.54, 48.89),
         (5.75, 48.86), (6.05, 48.9), (6.5, 48.66), (7.0, 48.3), (7.05, 48.0), (7.1, 47.7), (7.15, 47.5)]
fc = smooth(front)

# ground held by Germany, 1915 to 1916
held = Polygon(list(map(tuple, fc)) + [(7.6, 47.3), (9.5, 47.3), (9.5, 52.5), (2.7, 52.5)]).buffer(0)
held = held.intersection(m.land).difference(unary_union([states[1], G["Netherlands"], G["Switzerland"]]))
m.region(held, "red", alpha=0.32, hatch="//")

# frontiers of 1914
lines = unary_union([s.boundary for s in states]).intersection(m.land.buffer(-0.04)).intersection(frame)
for ln in getattr(linemerge(lines), "geoms", [linemerge(lines)]):
    xy = np.array(ln.coords)
    if len(xy) < 2:
        continue
    c = smooth(xy, n=6) if len(xy) > 2 else xy
    m.ax.plot(c[:, 0], c[:, 1], color="#6d655c", lw=1.4, ls=(0, (4, 2.5)), zorder=2.3)

m.river("Marne", "Seine", lw=1.6)
m.river("Maas", "Rhine", "Rhein", "Mosel", lw=1.6)
somme = smooth([(3.40, 49.88), (3.25, 49.80), (3.07, 49.75), (2.97, 49.85), (2.93, 49.93), (2.75, 49.92),
                (2.6, 49.94), (2.51, 49.91), (2.40, 49.9), (2.30, 49.89), (2.10, 49.98), (1.95, 50.05), (1.83, 50.10),
                (1.63, 50.18)], n=6)
m.ax.plot(somme[:, 0], somme[:, 1], color=WATER, lw=1.6, solid_capstyle="round", zorder=2.5)

# furthest German advance, 1918
adv = [(2.97, 50.85), (2.78, 50.78), (2.58, 50.7), (2.6, 50.58), (2.78, 50.48), (2.82, 50.3), (2.62, 50.08),
       (2.5, 49.9), (2.45, 49.76), (2.57, 49.64), (2.78, 49.55), (2.98, 49.48), (3.1, 49.3), (3.22, 49.12),
       (3.4, 49.03), (3.65, 49.07), (3.85, 49.12), (3.95, 49.22), (4.15, 49.3)]
m.line(adv, colour=INK, lw=3.0, style=(0, (4, 2)))

# the front, 1915 to 1916
m.ax.plot(fc[:, 0], fc[:, 1], color=PAPER, lw=8, solid_capstyle="round", zorder=4.4)
m.ax.plot(fc[:, 0], fc[:, 1], color=INK, lw=4.2, solid_capstyle="round", zorder=4.5)

m.city(2.35, 48.86, "Paris", dx=-0.1, dy=-0.15, ha="right", bold=True)
m.city(2.885, 50.85, "Ypres", dx=0.14, dy=0.1, ha="left", bold=True)
m.city(5.39, 49.16, "Verdun, 1916", dx=-0.12, dy=-0.12, ha="right", bold=True)
m.city(2.83, 49.42, "Compiègne:\narmistice, 1918", dx=-0.12, dy=0.0, ha="right")
m.city(2.75, 51.13, None)
m.label(2.5, 51.25, "Nieuport", size="city", colour=INK, fs=16, ha="right")
m.city(2.7, 50.02, "Somme, 1916", dx=-0.14, dy=0.12, ha="right", star=True, r=8, bold=True)

m.label(5.3, 50.55, "BELGIUM", fs=21)
m.label(2.6, 47.95, "FRANCE", fs=23, spaced=True)
m.label(7.6, 49.9, "GERMANY", fs=21)
m.label(5.6, 51.35, "NETHERLANDS, neutral", size="land", colour="#5a534b", fs=16, style="normal")
m.label(7.95, 47.4, "SWITZ.", size="land", colour="#5a534b", fs=16, style="normal")
m.label(6.15, 49.7, "LUX.", size="land", colour="#5a534b", fs=15, style="normal")
m.label(6.8, 48.9, "ALSACE-\nLORRAINE", size="small", colour=INK, fs=15)
m.label(1.3, 51.3, "North Sea", size="sea", fs=17)
m.label(1.15, 50.55, "English\nChannel", size="sea", fs=16)
m.label(3.95, 48.88, "Marne", size="sea", fs=16)
m.label(1.75, 49.35, "Seine", size="sea", fs=16)
m.label(7.9, 48.55, "Rhine", size="sea", fs=16, rot=75)
m.label(5.05, 49.75, "Meuse", size="sea", fs=16, rot=-60)

m.label(3.95, 50.05, "held by Germany,\n1914 to 1918", size="small", colour=INK, fs=16)
m.note(1.55, 49.75, "furthest German\nadvance, 1918", size=15)
m.ax.plot([2.1, 2.48], [49.75, 49.8], color=INK, lw=1.0, zorder=6.5)
m.note(4.15, 48.62, "front line,\n1915 to 1916", size=15)
m.ax.plot([4.2, 4.3], [48.75, 49.22], color=INK, lw=1.0, zorder=6.5)
m.scale(100, lon=0.9, lat=47.45)
m.save("chapters/72-trenches/images/map_western_front.png")
