#!/usr/bin/env python3
"""Chapter 87: Africa and Asia, coloured by the decade in which each country left colonial rule, 1945 to 1980.

Drawn for this chapter, which had no map. Modern borders are shown, since the chapter is about the countries
that inherited them: Natural Earth admin-0 (110 m, as shipped with geopandas). Dates are those of
independence as given in English Wikipedia's "Decolonisation of Africa", "Decolonisation of Asia" and the
articles on each country, counted from the end of colonial rule over the land: Bangladesh is coloured with
Pakistan (1947) and South Sudan with Sudan (1956), whose parts they then were; Malaysia is split into Malaya
(1957) and the Borneo states (1963); Yemen into the north, never a colony, and the former British colony and
protectorates of Aden in the south (1967), along a roughly drawn line. Countries that passed after colonial
rule to the rule of a neighbour, and became independent after 1980 or not at all, are hatched (Namibia,
Eritrea, Western Sahara, East Timor, Palestine), with Brunei (1984). Countries already independent in 1945,
or never colonies, are grey; the Soviet Union and Europe are left plain. Island states too small for the
110 m data (Singapore, Mauritius, the Comoros and others) are not coloured.
"""
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, box
from shapely.ops import unary_union, split
from matplotlib.patches import Polygon as MplPoly, Patch
import lib
from lib import INK, PAPER, FILL
from projmap import ProjMap

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}

YEAR = {
    # 1945 to 1949
    "North Korea": 1945, "South Korea": 1945, "Philippines": 1946, "Jordan": 1946, "Syria": 1946,
    "India": 1947, "Pakistan": 1947, "Bangladesh": 1947, "Sri Lanka": 1948, "Myanmar": 1948, "Israel": 1948,
    "Indonesia": 1949,
    # 1950s
    "Libya": 1951, "Laos": 1953, "Cambodia": 1953, "Vietnam": 1954, "Sudan": 1956, "S. Sudan": 1956,
    "Morocco": 1956, "Tunisia": 1956, "Ghana": 1957, "Guinea": 1958,
    # 1960s
    "Cameroon": 1960, "Togo": 1960, "Madagascar": 1960, "Dem. Rep. Congo": 1960, "Somalia": 1960,
    "Somaliland": 1960, "Benin": 1960, "Niger": 1960, "Burkina Faso": 1960, "Côte d'Ivoire": 1960, "Chad": 1960,
    "Central African Rep.": 1960, "Congo": 1960, "Gabon": 1960, "Senegal": 1960, "Mali": 1960, "Nigeria": 1960,
    "Mauritania": 1960, "Cyprus": 1960, "N. Cyprus": 1960, "Sierra Leone": 1961, "Tanzania": 1961,
    "Kuwait": 1961, "Burundi": 1962, "Rwanda": 1962, "Uganda": 1962, "Algeria": 1962, "Kenya": 1963,
    "Malawi": 1964, "Zambia": 1964, "Gambia": 1965, "Botswana": 1966, "Lesotho": 1966, "eSwatini": 1968,
    "Eq. Guinea": 1968,
    # 1970 to 1980
    "Qatar": 1971, "United Arab Emirates": 1971, "Guinea-Bissau": 1974, "Angola": 1975, "Mozambique": 1975,
    "Papua New Guinea": 1975, "Djibouti": 1977, "Solomon Is.": 1978, "Zimbabwe": 1980,
}
LATER = ["Namibia", "Eritrea", "W. Sahara", "Timor-Leste", "Palestine", "Brunei"]
BEFORE = ["Egypt", "Ethiopia", "Liberia", "South Africa", "Saudi Arabia", "Oman", "Iraq", "Iran", "Turkey",
          "Afghanistan", "Nepal", "Bhutan", "Thailand", "China", "Taiwan", "Mongolia", "Japan", "Lebanon"]

# Malaysia: Malaya in 1957, Sabah and Sarawak in 1963.  Yemen: the south (Aden) in 1967, roughly.
malaya = G["Malaysia"].intersection(box(95, 0, 106, 8))
borneo_states = G["Malaysia"].intersection(box(106, 0, 120, 8))
aden_line = [(43.3, 12.4), (43.95, 12.9), (44.2, 13.35), (44.9, 13.75), (45.6, 14.25), (46.4, 15.0),
             (47.0, 16.0), (48.2, 17.2), (50.0, 18.4), (52.0, 19.0), (54.0, 19.5), (54.0, 10.0)]
south_yemen = G["Yemen"].intersection(Polygon(aden_line).buffer(0))
north_yemen = G["Yemen"].difference(south_yemen)

RAMP = {1940: "#f1d08a", 1950: "#e09a52", 1960: "#bf5b3c", 1970: "#7c2f24"}
GREY = "#b9b1a5"

lonlat = box(-30, -45, 175, 60)
m = ProjMap("+proj=robin +lon_0=65 +units=km", (-7900, 8250, -4000, 5150), lonlat_box=lonlat)


LAND = m.land.buffer(0)


def fill(geom, colour, alpha=0.85, hatch=None):
    g = m.proj(geom.intersection(lonlat)).buffer(0).intersection(LAND)
    for p in getattr(g, "geoms", [g]):
        if p.is_empty or p.geom_type != "Polygon":
            continue
        xy = np.array(p.exterior.coords)
        m.ax.add_patch(MplPoly(xy, closed=True, fc=colour, ec="none", alpha=alpha, zorder=2))
        if hatch:
            m.ax.add_patch(MplPoly(xy, closed=True, fc="none", ec="#6c6156", lw=0, alpha=0.8, zorder=2.05,
                                   hatch=hatch))


def borders(geom):
    g = m.proj(geom.intersection(lonlat))
    for p in getattr(g, "geoms", [g]):
        if p.geom_type == "Polygon":
            xy = np.array(p.exterior.coords)
            m.ax.plot(xy[:, 0], xy[:, 1], color=PAPER, lw=1.1, zorder=2.2)


parts = []
for name, y in YEAR.items():
    parts.append((G[name], RAMP[y // 10 * 10 if y < 1980 else 1970], None))
parts += [(malaya, RAMP[1950], None), (borneo_states, RAMP[1960], None), (south_yemen, RAMP[1960], None),
          (north_yemen, GREY, None)]
parts += [(G[n], "#e8dcc4", "///") for n in LATER]
parts += [(G[n], GREY, None) for n in BEFORE]
for geom, col, hatch in parts:
    fill(geom, col, hatch=hatch)
for geom, _, _ in parts:
    borders(geom)

# names and years: the countries the chapter dwells on
L = dict(size="region", fs=17, colour=INK)
m.label(2.7, 28.6, "ALGERIA\n1962", **L)
m.label(-0.6, 1.2, "GHANA\n1957", **L)
m.ax.plot(*zip(m.xy(-1.0, 3.3), m.xy(-1.2, 6.2)), color=INK, lw=1.4, zorder=6.5)
m.label(23.6, -2.5, "CONGO\n1960", **L)
m.label(37.9, 0.4, "KENYA\n1963", **L)
m.label(17.6, -12.4, "ANGOLA\n1975", **L)
m.label(43.5, -17.6, "MOZAMBIQUE\n1975", **L)
m.label(78.4, 22.0, "INDIA\n1947", **L)
m.label(96.6, 21.2, "BURMA\n1948", **L)
m.label(114.0, -4.6, "INDONESIA\n1949", **L)
m.label(127.0, 21.6, "PHILIPPINES\n1946", **L)
m.city(107.6, -6.9, "Bandung", dx=-90, dy=-170, size="small")
m.label(30.0, 27.5, "EGYPT", size="land", colour="#5a534b", fs=15, style="normal")
m.label(103.0, 33.5, "CHINA", size="land", colour="#5a534b", fs=17, style="normal")
m.label(80.0, 51.5, "SOVIET UNION", size="land", colour="#5a534b", fs=17, style="normal")
m.label(-6.0, -13.0, "Atlantic\nOcean", size="sea", fs=19)
m.label(80.0, -2.0, "Indian Ocean", size="sea", fs=19)

handles = [Patch(fc=RAMP[1940], ec="none", label="1945 to 1949"), Patch(fc=RAMP[1950], ec="none", label="1950s"),
           Patch(fc=RAMP[1960], ec="none", label="1960s"), Patch(fc=RAMP[1970], ec="none", label="1970 to 1980"),
           Patch(fc="#e8dcc4", ec="#6c6156", hatch="///", lw=0, label="after 1980, or not yet"),
           Patch(fc=GREY, ec="none", label="already independent")]
leg = m.ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.445, 0.035), fontsize=16,
                  title="Independence", title_fontsize=17, frameon=True, fancybox=False, edgecolor=INK,
                  facecolor=PAPER, framealpha=1, borderpad=0.7, labelspacing=0.45, handlelength=2.2,
                  handleheight=1.1)
leg.set_zorder(9); leg.get_frame().set_linewidth(1.2)
m.scale(2000, x=-7500, y=-3780)
m.save("chapters/87-independence/images/map_independence.png")
