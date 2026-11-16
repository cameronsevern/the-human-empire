#!/usr/bin/env python3
"""Chapter 82: Europe in 1942. The land ruled by Germany, its allies and the countries they occupied; the
Warsaw ghetto; the six killing centres (Chelmno, Treblinka, Sobibor, Majdanek, Belzec, Auschwitz); the
area of the mass shootings in the occupied Soviet lands, 1941 and 1942; and the main railway routes of the
deportations, from Amsterdam, Paris, Salonika, Budapest and Warsaw.

Drawn for this chapter, which had no map. The Axis area and the front of November 1942 are as in
ch81_furthest.py (the modern countries west of the front, without the neutrals and Britain). The area of the
mass shootings is the German-occupied Soviet land of 1941 and 1942, from the Baltic states and the
borderlands taken by the Soviet Union in 1939 to the front, after the maps in English Wikipedia's "Einsatzgruppen"
and "The Holocaust" and in the United States Holocaust Memorial Museum's Holocaust Encyclopedia, roughly.
The railway routes are simplified to their main junctions, after the Holocaust Encyclopedia's deportation
maps: Westerbork, Bremen, Hanover and Breslau for the Dutch trains; Metz, Frankfurt and Dresden for the
French; Skopje, Belgrade and Vienna for the Greek; Kassa (Kosice) and Zilina for the Hungarian of 1944;
Malkinia for Warsaw to Treblinka. Positions of the camps and cities from English Wikipedia. Only the cities
the chapter names are named, with the six camps; Paris and Salonika are marked "from France" and "from
Greece".
"""
import os
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, box
from shapely.ops import unary_union
from matplotlib.patches import Polygon as MplPoly, Rectangle
import matplotlib.image as mpimg
import lib
from lib import Map, INK, PAPER, FILL, smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}


def paint(m, geom, colour, alpha, hatch=None, lw=1.3, hatch_colour=None):
    fc = FILL.get(colour, colour)
    for p in getattr(geom, "geoms", [geom]):
        if p.is_empty or p.geom_type != "Polygon" or p.area < 2e-3:
            continue
        xy = np.array(p.exterior.coords)
        if alpha:
            m.ax.add_patch(MplPoly(xy, closed=True, fc=fc, ec="none", alpha=alpha, zorder=2))
        if hatch:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=hatch_colour or fc, lw=0, alpha=0.8, zorder=2.05,
                                   hatch=hatch))
        if lw:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec=hatch_colour or fc, lw=lw, alpha=0.95, zorder=2.1))


m = Map(-3.0, 46.0, 36.0, 60.0)
front = [(31.2, 69.6), (32.0, 68.0), (30.6, 67.0), (31.6, 65.9), (32.6, 64.0), (34.4, 62.9), (35.3, 61.6),
         (33.6, 60.9), (32.6, 60.5), (31.0, 60.0), (31.6, 59.9), (32.0, 59.4), (31.6, 58.7), (31.4, 58.2),
         (32.0, 57.8), (33.4, 57.6), (32.6, 57.0), (31.1, 56.6), (30.6, 56.3), (32.0, 55.9), (33.6, 56.3),
         (34.4, 56.2), (35.1, 55.6), (35.3, 54.8), (34.6, 54.0), (35.6, 53.6), (36.6, 53.1), (37.3, 52.3),
         (38.1, 51.9), (39.2, 51.7), (40.0, 50.6), (41.5, 49.9), (43.0, 49.3), (44.5, 48.75), (44.4, 47.9),
         (44.9, 46.5), (44.8, 44.9), (44.6, 43.8), (43.6, 43.4), (42.4, 43.4), (40.6, 43.7), (39.2, 44.25),
         (37.8, 44.7)]
fc = smooth(front, n=8)
west_of_front = Polygon(list(map(tuple, fc)) + [(37.0, 44.3), (34.0, 43.6), (29.0, 42.0), (25.0, 38.0),
                                                (-30.0, 36.0), (-30.0, 72.0), (31.2, 72.0)]).buffer(0)
europe = unary_union([r.geometry for _, r in C.iterrows() if r["continent"] == "Europe"])
neutral = unary_union([G[n] for n in ["Spain", "Portugal", "Switzerland", "Sweden", "Ireland", "Turkey"]])
allied = unary_union([G["United Kingdom"], G["Iceland"]])
axis = unary_union([europe.intersection(west_of_front), G["Libya"], G["Tunisia"]])
axis = axis.buffer(0.15).difference(neutral.buffer(0.02)).difference(allied.buffer(0.3)).intersection(m.land)


def draw(m, names):
    paint(m, axis, "brown", 0.4)

    # the mass shootings: the occupied Soviet lands, from the borderlands of 1939 to the front
    shoot_west = [(21.0, 55.4), (22.6, 55.1), (22.9, 54.4), (23.5, 54.0), (23.9, 53.0), (23.2, 52.3), (23.7, 51.6),
                  (24.0, 50.5), (22.8, 49.3), (24.0, 48.4), (26.6, 48.3), (28.5, 47.6), (29.9, 46.5), (30.6, 45.5),
                  (36.5, 43.0)]
    shoot = Polygon(list(reversed(shoot_west)) + [(19.5, 58.0), (23.5, 60.0), (30.0, 60.2)]
                    + [tuple(p) for p in fc if p[1] < 60.2]).buffer(0).intersection(m.land).intersection(axis.buffer(0.1)).intersection(box(-30, 30, 60, 59.75))
    paint(m, shoot, INK, 0, hatch="///", lw=0, hatch_colour="#5a4a3a")
    c = fc[[p[1] < 60.4 for p in fc]]
    m.ax.plot(c[:, 0], c[:, 1], color=PAPER, lw=5.5, zorder=4.4)
    m.ax.plot(c[:, 0], c[:, 1], color=INK, lw=2.6, zorder=4.5)

    # deportation railways
    R = dict(colour=INK, lw=3.0, style=(0, (4, 1.5)))
    m.route([(4.9, 52.37), (6.6, 52.85), (8.8, 53.0), (9.8, 52.35), (12.5, 52.0), (17.0, 51.12), (18.95, 50.17)], **R)
    m.route([(2.35, 48.86), (6.2, 49.1), (8.7, 50.05), (11.2, 50.75), (13.7, 50.98), (16.2, 50.55), (18.9, 50.06)], **R)
    m.route([(22.94, 40.64), (21.45, 42.0), (21.0, 43.6), (20.46, 44.8), (18.0, 45.5), (16.0, 45.9), (15.4, 47.1),
             (16.4, 48.2), (17.6, 49.4), (19.02, 49.93)], **R)
    m.route([(19.04, 47.5), (20.4, 48.0), (21.25, 48.72), (20.3, 49.1), (19.0, 49.3), (19.17, 49.88)], **R)
    m.route([(21.01, 52.23), (21.6, 52.55), (21.9, 52.62)], colour=INK, lw=3.0, style=(0, (4, 1.5)))

    camps = {"Chełmno": (18.73, 52.15, 0.17, 0.0), "Treblinka": (22.05, 52.63, 0.17, 0.0),
             "Sobibór": (23.59, 51.45, 0.17, 0.0), "Majdanek": (22.60, 51.22, -0.17, 0.0),
             "Bełżec": (23.46, 50.37, 0.17, 0.0), "Auschwitz": (19.18, 50.03, 0.17, 0.02)}
    for name, (x, y, dx, dy) in camps.items():
        m.ax.plot(x, y, "s", ms=14, mfc=INK, mec=PAPER, mew=1.6, zorder=6.5)
        if names:
            m.label(x + dx, y + dy, name, size="city", colour=INK, fs=17, ha="left" if dx > 0 else "right" if dx < 0 else "center",
                    style=None)
    m.city(21.01, 52.23, None)
    if names:
        m.label(21.17, 52.09, "Warsaw ghetto", size="city", colour=INK, fs=16.5, ha="left")

# ================================================================ the enlargement of occupied Poland
SCRATCH = os.environ.get("SCRATCH", "/tmp")
IW, IE, IS, IN = 18.0, 25.0, 49.4, 53.2
inset = Map(IW, IE, IS, IN, width=5.4)
draw(inset, True)
inset.label(18.15, 53.0, "THE KILLING CENTRES", fs=15, ha="left")
inset.river("Vistula", "Bug", lw=1.4)
inset.scale(100, lon=21.2, lat=49.55)
pin = os.path.join(SCRATCH, "ch82_inset.png")
inset.save(pin)

# ================================================================ Europe
draw(m, False)
m.ax.add_patch(Rectangle((IW, IS), IE - IW, IN - IS, fc="none", ec=INK, lw=1.8, zorder=8))
m.city(4.90, 52.37, "Amsterdam", dx=-0.4, dy=0.35)
m.city(19.04, 47.50, "Budapest", dx=0.4, dy=-0.25)
m.city(13.40, 52.52, "Berlin", dx=0.0, dy=0.5)
m.city(30.52, 50.45, "Kyiv", dx=0.45, dy=0.0)
m.city(2.35, 48.86, None)
m.city(22.94, 40.64, None)
m.label(2.6, 48.2, "from France", size="small", colour=INK, fs=16)
m.label(23.2, 40.1, "from Greece", size="small", colour=INK, fs=16, ha="left")
m.label(9.5, 51.35, "deportation trains", size="small", colour=INK, fs=16, style="italic")

m.label(30.0, 54.0, "mass shootings,\n1941 and 1942", fs=18, ha="center")
m.label(40.2, 51.4, "front,\nlate 1942", size="small", colour=INK, fs=15, ha="left")
m.label(2.6, 46.9, "GERMANY, ITS ALLIES AND\nTHE LANDS THEY OCCUPIED", fs=15, ha="center")
m.label(19.6, 46.6, "HUNGARY", size="land", colour="#5a534b", fs=15, style="normal")
m.label(25.2, 42.7, "BULGARIA", size="land", colour="#5a534b", fs=15, style="normal")
m.label(7.9, 56.6, "DENMARK", size="land", colour="#5a534b", fs=15, style="normal", ha="right")
m.label(15.0, 59.0, "SWEDEN", size="land", colour="#5a534b", fs=15, style="normal")
m.label(20.6, 53.75, "POLAND", size="land", colour="#5a534b", fs=15, style="normal")
m.label(41.0, 57.0, "SOVIET UNION", size="land", colour="#5a534b", fs=16, style="normal")
m.label(0.0, 54.5, "BRITAIN", size="land", colour="#5a534b", fs=15, style="normal")
m.label(34.0, 43.4, "Black Sea", size="sea", fs=17)
m.label(19.0, 38.3, "Mediterranean\nSea", size="sea", fs=17)
m.label(4.0, 56.2, "North Sea", size="sea", fs=17)
m.scale(500, lon=34.0, lat=37.6)
img = mpimg.imread(pin)
H = m.fig.get_size_inches()[1] * 100
h, w = img.shape[:2]
ia = m.fig.add_axes([10 / 1600, 10 / H, w / 1600, h / H])
ia.imshow(img); ia.axis("off")
m.save("chapters/82-holocaust/images/map_europe_1942.png")
