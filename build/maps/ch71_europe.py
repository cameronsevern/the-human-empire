#!/usr/bin/env python3
"""Chapter 71: Europe in August 1914. The two camps (Germany and Austria-Hungary; France, Russia and Britain,
with Serbia, Montenegro and Belgium), the neutral states, Bosnia with Sarajevo, Serbia with Belgrade, the
German sweep through Belgium towards Paris, and the trench line of the end of 1914.

Drawn for this chapter, which had no map. The states of 1914 are built from the modern countries
(Natural Earth admin-0, as shipped with geopandas), with the pieces that changed hands since cut off and
moved by hand-drawn lines, so their borders are rough: Germany with Alsace-Lorraine, northern Schleswig,
the Memel strip, East Prussia, and western Poland (Posen, West Prussia, Silesia); Austria-Hungary with
Galicia and Bukovina, Transylvania and the Banat, the Vojvodina north of the Sava and Danube, Bosnia,
Trentino and the land round Trieste; Russia with Finland, the Baltic lands, central Poland and
Bessarabia; Serbia with Kosovo and Macedonia, as after 1913; Bulgaria with western Thrace and without
southern Dobruja. The 1914 borders follow the maps of Europe in 1914 in English Wikipedia ("Map of Europe
in 1914", "Partitions of Poland"). The Ottoman Empire, neutral until November, is shown as neutral; Italy,
allied to Germany on paper, stayed out. The sweep follows the arrows of the German right wing in English
Wikipedia's "Schlieffen Plan" and "Battle of the Frontiers"; the front of late 1914 runs Nieuport, Ypres,
Arras, Noyon, Soissons, Reims, Verdun, St Mihiel, the Vosges, to the Swiss border near Bonfol.
Positions from English Wikipedia.
"""
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from matplotlib.patches import Polygon as MplPoly
from lib import Map, INK, PAPER, FILL, smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
P = lambda pts: Polygon(pts).buffer(0)
U = lambda *names: unary_union([G[n] if isinstance(n, str) else n for n in names])

W, E, S, N = -10.5, 41.0, 35.0, 61.5
m = Map(W, E, S, N)
frame = box(W - 3, S - 3, E + 3, N + 3)

# ------------------------------------------------------------------ pieces that changed hands
kaliningrad = G["Russia"].intersection(box(19.0, 54.2, 23.0, 55.4))
memel = G["Lithuania"].intersection(P([(20.9, 55.25), (21.6, 55.25), (22.2, 55.07), (22.4, 55.6), (21.5, 56.0),
                                        (20.9, 56.0)]))
west_poland = G["Poland"].intersection(P([(14.0, 54.9), (19.6, 54.9), (22.9, 54.4), (22.8, 53.95), (22.2, 53.55),
    (21.0, 53.28), (20.0, 53.2), (19.35, 53.05), (18.95, 52.95), (18.7, 52.7), (18.4, 52.5), (17.9, 52.3),
    (17.95, 51.75), (18.1, 51.45), (18.5, 51.15), (18.95, 50.85), (19.1, 50.5), (19.17, 50.23), (19.15, 50.0),
    (18.85, 49.93), (18.55, 49.9), (14.0, 49.9)]))
galicia_pl = G["Poland"].intersection(P([(18.3, 48.8), (18.55, 49.9), (18.85, 49.93), (19.15, 50.0), (19.17, 50.23),
    (19.3, 50.08), (20.0, 50.13), (20.8, 50.25), (21.5, 50.5), (21.85, 50.68), (22.1, 50.55), (22.6, 50.35),
    (24.5, 50.4), (24.5, 48.5)])).difference(west_poland)
galicia_ua = G["Ukraine"].intersection(P([(21.5, 51.0), (22.6, 50.35), (24.1, 50.5), (25.2, 50.1), (25.9, 49.8),
    (26.1, 49.2), (26.2, 48.6), (26.3, 48.2), (25.0, 47.3), (21.5, 47.3)]))
alsace = G["France"].intersection(P([(5.85, 49.55), (6.0, 49.2), (6.25, 48.95), (6.6, 48.75), (7.05, 48.5),
    (7.1, 48.2), (6.95, 47.85), (7.05, 47.45), (8.5, 47.5), (8.5, 49.6)]))
schleswig = G["Denmark"].intersection(P([(8.0, 54.6), (10.1, 54.6), (10.1, 55.1), (9.65, 55.25), (9.6, 55.45),
                                          (8.0, 55.5)]))
old_romania = G["Romania"].intersection(P([(22.35, 44.6), (22.75, 45.2), (23.4, 45.35), (24.3, 45.5), (25.5, 45.45),
    (26.1, 45.7), (26.4, 45.95), (26.3, 46.3), (25.95, 46.95), (26.15, 47.4), (26.65, 47.65), (27.0, 48.0),
    (26.7, 48.35), (28.5, 48.5), (31.0, 45.5), (29.5, 43.0), (22.35, 43.0)]))
transylvania = G["Romania"].difference(old_romania)
s_dobruja = G["Bulgaria"].intersection(P([(26.5, 44.2), (26.55, 44.05), (26.9, 43.75), (27.6, 43.55), (28.1, 43.38),
                                           (29.0, 43.38), (29.0, 44.3)]))
w_thrace = G["Greece"].intersection(P([(24.3, 41.7), (24.5, 41.2), (24.75, 40.8), (26.1, 40.7), (26.4, 41.8)]))
vojvodina = G["Serbia"].intersection(P([(18.5, 46.5), (18.8, 44.95), (19.3, 44.92), (20.0, 44.85), (20.45, 44.83),
    (21.0, 44.78), (21.5, 44.78), (22.2, 44.55), (22.9, 44.6), (22.9, 46.5)]))
trentino = G["Italy"].intersection(P([(10.45, 46.6), (10.5, 46.3), (10.6, 46.0), (10.85, 45.8), (11.2, 45.85),
    (11.7, 45.95), (12.1, 46.15), (12.5, 46.4), (13.3, 46.5), (13.5, 46.1), (13.45, 45.65), (14.2, 45.4),
    (14.2, 47.2), (10.45, 47.2)]))

state = {
    "Germany": U("Germany", kaliningrad, memel, west_poland, alsace, schleswig),
    "Austria-Hungary": U("Austria", "Hungary", "Czechia", "Slovakia", "Slovenia", "Croatia", "Bosnia and Herz.",
                         galicia_pl, galicia_ua, transylvania, vojvodina, trentino),
    "France": G["France"].difference(alsace),
    "Britain": U("United Kingdom", "Ireland"),
    "Russia": U(G["Russia"].difference(kaliningrad), "Finland", "Estonia", "Latvia",
                G["Lithuania"].difference(memel), "Belarus", G["Ukraine"].difference(galicia_ua), "Moldova",
                G["Poland"].difference(west_poland).difference(galicia_pl)),
    "Belgium": U("Belgium", "Luxembourg"),
    "Serbia": U(G["Serbia"].difference(vojvodina), "Kosovo", "North Macedonia"),
    "Montenegro": G["Montenegro"],
    "Italy": G["Italy"].difference(trentino),
    "Romania": U(old_romania, s_dobruja),
    "Bulgaria": U(G["Bulgaria"].difference(s_dobruja), w_thrace),
    "Greece": G["Greece"].difference(w_thrace),
    "Ottoman": G["Turkey"],
}
for n in ["Netherlands", "Switzerland", "Spain", "Portugal", "Norway", "Sweden", "Albania"]:
    state[n] = G[n]
state["Denmark"] = G["Denmark"].difference(schleswig)

side = {"Germany": "red", "Austria-Hungary": "red", "France": "blue", "Britain": "blue", "Russia": "blue",
        "Belgium": "blue", "Serbia": "blue", "Montenegro": "blue"}


def paint(geom, colour, alpha, hatch=None):
    fc = FILL[colour]
    for p in getattr(geom, "geoms", [geom]):
        if p.is_empty or p.geom_type != "Polygon" or p.area < 2e-3:
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
        if hatch:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=0, alpha=0.7, zorder=2.05, hatch=hatch))
        m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=fc, lw=1.3, alpha=0.95, zorder=2.1))


taken = None
for name in ["Germany", "Austria-Hungary", "Russia", "France", "Belgium", "Serbia", "Montenegro", "Britain", "Italy",
             "Switzerland", "Netherlands", "Denmark", "Norway", "Sweden", "Spain", "Portugal", "Romania", "Bulgaria",
             "Greece", "Albania", "Ottoman"]:
    g = state[name].buffer(0.2).intersection(m.land).intersection(frame)
    if taken is not None:
        g = g.difference(taken)
    taken = g if taken is None else taken.union(g)
    if name in side:
        paint(g, side[name], 0.5)
    else:
        paint(g, "grey", 0.22, hatch="///")

# Bosnia, inside Austria-Hungary, outlined
bos = G["Bosnia and Herz."].intersection(m.land)
for p in getattr(bos, "geoms", [bos]):
    xy = np.array(p.exterior.coords)
    m.ax.plot(xy[:, 0], xy[:, 1], color=INK, lw=1.2, ls=(0, (2, 2)), zorder=2.4)

m.river("Danube", "Donau", lw=1.4)

# the German sweep, August 1914, and the front at the end of 1914
m.route([(6.4, 51.05), (5.2, 50.95), (4.1, 50.75), (3.1, 50.3), (2.55, 49.6)], colour=INK, lw=3.0)
m.route([(6.5, 49.95), (5.2, 49.75), (4.2, 49.35), (3.4, 48.95)], colour=INK, lw=3.0)
front = [(2.75, 51.15), (2.9, 50.85), (2.8, 50.5), (2.75, 50.25), (2.7, 49.95), (2.95, 49.55), (3.4, 49.4),
         (4.0, 49.3), (4.8, 49.2), (5.3, 49.2), (5.6, 48.9), (6.0, 48.9), (6.6, 48.6), (7.0, 48.2), (7.15, 47.5)]
c = smooth(front)
m.ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=7, solid_capstyle="round", zorder=4.4)
m.ax.plot(c[:, 0], c[:, 1], color=INK, lw=3.4, ls=(0, (1.2, 1.0)), zorder=4.5)

# cities
m.city(2.35, 48.86, "Paris", dx=-0.5, dy=-0.35, bold=True)
m.city(-0.13, 51.51, "London", dx=-0.5, dy=0.35, bold=True)
m.city(13.40, 52.52, "Berlin", dx=0.5, dy=0.35, bold=True)
m.city(16.37, 48.21, "Vienna", dx=-0.5, dy=0.35, bold=True)
m.city(30.32, 59.94, "St Petersburg", dx=0.6, dy=-0.4)
m.city(20.46, 44.82, "Belgrade", dx=0.55, dy=0.3)
m.city(18.41, 43.86, "Sarajevo", dx=-0.4, dy=-0.55, star=True, bold=True)

# names
m.label(10.3, 51.0, "GERMANY", fs=21)
m.label(21.0, 47.6, "AUSTRIA-\nHUNGARY", fs=20)
m.label(1.6, 46.6, "FRANCE", fs=21)
m.label(33.0, 54.0, "RUSSIA", fs=24, spaced=True)
m.label(-2.0, 53.9, "BRITAIN", fs=19)
m.label(17.2, 44.65, "BOSNIA", fs=15, ha="center")
m.label(21.2, 43.2, "SERBIA", fs=17, ha="left")
m.label(2.4, 53.0, "BELGIUM", fs=16, ha="center")
m.ax.plot([2.8, 4.3], [52.75, 50.95], color=INK, lw=1.1, zorder=6.5)
m.label(12.6, 42.6, "ITALY", size="land", colour="#5a534b", fs=17, style="normal")
m.label(-3.2, 41.2, "SPAIN", size="land", colour="#5a534b", fs=17, style="normal")
m.label(8.2, 46.8, "SWITZ.", size="land", colour="#5a534b", fs=15, style="normal")
m.label(5.8, 52.45, "NETH.", size="land", colour="#5a534b", fs=15, style="normal")
m.label(15.4, 62.2 - 3.0, "SWEDEN", size="land", colour="#5a534b", fs=16, style="normal")
m.label(8.6, 60.4, "NORWAY", size="land", colour="#5a534b", fs=16, style="normal")
m.label(9.2, 56.3, "DEN.", size="land", colour="#5a534b", fs=15, style="normal")
m.label(25.3, 44.75, "ROMANIA", size="land", colour="#5a534b", fs=16, style="normal")
m.label(25.3, 42.7, "BULGARIA", size="land", colour="#5a534b", fs=15, style="normal")
m.label(22.0, 39.3, "GREECE", size="land", colour="#5a534b", fs=15, style="normal")
m.label(33.0, 39.2, "OTTOMAN EMPIRE", size="land", colour="#5a534b", fs=17, style="normal")


m.label(3.0, 55.5, "North Sea", size="sea", fs=17)
m.label(-7.5, 46.5, "ATLANTIC\nOCEAN", size="sea", fs=17)
m.label(18.0, 37.0, "Mediterranean Sea", size="sea", fs=17)
m.label(19.5, 57.0, "Baltic\nSea", size="sea", fs=16)
m.label(34.5, 43.3, "Black Sea", size="sea", fs=17)

m.key([("red", "Germany and Austria-Hungary"), ("blue", "France, Russia, Britain\nand their allies"),
       (("hatch", "grey", "///"), "neutral in August 1914"),
       (("line", INK, "-"), "German plan, August 1914"), (("line", INK, (0, (1.2, 1.0))), "front, end of 1914")], loc="lower left", size=15)
m.save("chapters/71-sarajevo/images/map_europe_1914.png")
