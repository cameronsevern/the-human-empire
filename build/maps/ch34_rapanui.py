#!/usr/bin/env python3
"""Chapter 34: Rapa Nui. The triangular island with its three volcanoes (Terevaka in the north, Poike in
the east, the crater of Rano Kau in the south-west), the statue quarry of Rano Raraku, the red-stone
quarry of Puna Pau, Ahu Tongariki, Anakena, Tahai and the modern town of Hanga Roa, and the main statue
roads leading from the quarry. An inset shows the Polynesian triangle.

Drawn for this chapter, which had no map. Natural Earth gives the island as a six-sided outline, so the
coast is drawn by hand from coordinates of points along it, and checked by overlaying a modern
coastline (OpenStreetMap, used only for the check and not drawn). The statue roads are drawn roughly,
after Routledge's account (The Mystery of Easter Island, 1919) of a long southern road that follows
the south coast westward, a western road across the middle of the island, and a short northern road
that fades out after about a mile; their exact courses are not shown. Positions from English Wikipedia,
Wikidata and OpenStreetMap.

Set CHECK=path/to/osm_coast.json to overlay the modern coastline in red for checking.
"""
import os, json
import numpy as np
import matplotlib.image as mpimg
from matplotlib.patches import Polygon as MplPoly, Circle, Ellipse
import lib
from lib import Map, INK, PAPER, LAND, SEA, SHORE, FILL, smooth

SCRATCH = os.environ.get("SCRATCH", "/tmp")
COS = np.cos(np.radians(27.13))

# the coast, clockwise from the northern point
coast = [(-109.374, -27.0545), (-109.364, -27.0592), (-109.355, -27.0595), (-109.346, -27.0598),
         (-109.338, -27.0650), (-109.331, -27.0700), (-109.325, -27.0728), (-109.320, -27.0703),
         (-109.315, -27.0700), (-109.3128, -27.0730), (-109.310, -27.0775), (-109.304, -27.0815),
         (-109.298, -27.0880), (-109.289, -27.0878), (-109.281, -27.0930), (-109.275, -27.0915),
         (-109.257, -27.0905), (-109.248, -27.0930), (-109.239, -27.0922), (-109.232, -27.0975),
         (-109.2275, -27.1050), (-109.2295, -27.1130), (-109.2345, -27.1205), (-109.242, -27.1215),
         (-109.2505, -27.1208), (-109.260, -27.1225), (-109.2675, -27.1240), (-109.274, -27.1238),
         (-109.2758, -27.1275), (-109.2755, -27.1315), (-109.281, -27.1355), (-109.2875, -27.1405),
         (-109.2935, -27.1400), (-109.300, -27.1400), (-109.308, -27.1375), (-109.318, -27.1388),
         (-109.326, -27.1435), (-109.335, -27.1490), (-109.341, -27.1540), (-109.3485, -27.1600),
         (-109.3515, -27.1640), (-109.358, -27.1648), (-109.3645, -27.1680), (-109.370, -27.1685),
         (-109.3765, -27.1665), (-109.384, -27.1685), (-109.391, -27.1698), (-109.3975, -27.1690),
         (-109.4040, -27.1740), (-109.4075, -27.1830), (-109.4110, -27.1905), (-109.4180, -27.1945),
         (-109.4250, -27.1966), (-109.4320, -27.1965), (-109.4400, -27.1935), (-109.4460, -27.1895),
         (-109.4490, -27.1820), (-109.4492, -27.1760), (-109.4455, -27.1700), (-109.4420, -27.1640),
         (-109.4400, -27.1580), (-109.4395, -27.1530), (-109.4355, -27.1495), (-109.4310, -27.1478),
         (-109.4278, -27.1420), (-109.4272, -27.1340), (-109.4235, -27.1260), (-109.4225, -27.1190),
         (-109.4200, -27.1080), (-109.4150, -27.1010), (-109.4115, -27.0950), (-109.4065, -27.0835),
         (-109.4015, -27.0730), (-109.3960, -27.0650), (-109.3900, -27.0595), (-109.3830, -27.0555)]

# the statue roads, roughly
south_road = [(-109.2895, -27.1280), (-109.297, -27.1345), (-109.310, -27.1345), (-109.325, -27.1385),
              (-109.340, -27.1475), (-109.355, -27.1590), (-109.372, -27.1640), (-109.392, -27.1655)]
west_road = [(-109.2925, -27.1225), (-109.310, -27.1215), (-109.330, -27.1215), (-109.350, -27.1210),
             (-109.368, -27.1195)]
north_road = [(-109.2895, -27.1170), (-109.2915, -27.1105), (-109.2940, -27.1045)]

W, E, S, N = -109.478, -109.202, -27.226, -27.034
m = Map(W, E, S, N, lakes=False)
for p in list(m.ax.patches):
    p.remove()
m.ax.add_patch(MplPoly(smooth(coast, n=6, closed=True), closed=True, fc=LAND, ec=SHORE, lw=1.6, zorder=1))
# the islets off Rano Kau
for lon, lat, r in ((-109.4525, -27.2015, 0.0016), (-109.4495, -27.1975, 0.0007)):
    m.ax.add_patch(Ellipse((lon, lat), 2 * r / COS, 2 * r, fc=LAND, ec=SHORE, lw=1.2, zorder=1))


def crater(lon, lat, r, lake=True):
    """A crater: a ring of rim with a lake inside."""
    m.ax.add_patch(Ellipse((lon, lat), 2 * r / COS, 2 * r, fc=SEA if lake else "none", ec=FILL["brown"], lw=4,
                           zorder=2.6))


def peak(lon, lat):
    m.ax.plot(lon, lat, "^", ms=20, mfc=FILL["brown"], mec=INK, mew=1.3, zorder=6)


crater(-109.4349, -27.1866, 0.0066)                    # Rano Kau, about 1.6 km across
crater(-109.2891, -27.1219, 0.0030)                    # Rano Raraku
peak(-109.3798, -27.0843)                              # Terevaka
peak(-109.2475, -27.0985)                              # Poike

road = dict(colour=INK, lw=3.0, arrow=False, style=(0, (2.4, 1.6)))
for r in (south_road, west_road, north_road):
    m.route(r, **road)

# the quarries
m.ax.plot(-109.2895, -27.1272, "s", ms=17, mfc=FILL["red"], mec=INK, mew=1.4, zorder=6.5)
m.ax.plot(-109.4005, -27.1478, "s", ms=15, mfc=FILL["red"], mec=INK, mew=1.4, zorder=6.5)

m.label(-109.2975, -27.1085, "Rano Raraku", size="small", colour=INK, fs=21, style="normal", ha="right")
m.label(-109.2975, -27.1145, "statue quarry", size="small", colour=INK, fs=17, ha="right")
m.label(-109.3990, -27.1360, "Puna Pau", size="small", colour=INK, fs=19)
m.label(-109.3990, -27.1415, "red-stone quarry", size="small", colour=INK, fs=16)
m.label(-109.3798, -27.0760, "Terevaka", size="small", colour=INK, fs=19)
m.label(-109.2475, -27.1090, "Poike", size="small", colour=INK, fs=19)
m.label(-109.4349, -27.1755, "Rano Kau", size="small", colour=INK, fs=19)

m.city(-109.2769, -27.1258, "Ahu Tongariki", dx=0.004, dy=-0.0075, ha="left")
m.city(-109.3236, -27.0737, "Anakena", dx=0.0, dy=0.0075)
m.city(-109.4269, -27.1395, "Tahai", dx=-0.0045, dy=0.0)
m.city(-109.4273, -27.1481, "Hanga Roa", dx=-0.0150, dy=-0.0010)

m.label(-109.343, -27.1300, "statue roads", size="small", colour=INK, fs=17, rot=-13)
m.label(-109.345, -27.103, "R A P A   N U I", size="land", fs=26, style="normal")
m.label(-109.455, -27.080, "Pacific\nOcean", size="sea", fs=22)
m.scale(5, lon=-109.470, lat=-27.218)

if os.environ.get("CHECK"):
    for el in json.load(open(os.environ["CHECK"]))["elements"]:
        xy = np.array([(g["lon"], g["lat"]) for g in el["geometry"]])
        m.ax.plot(xy[:, 0], xy[:, 1], color="red", lw=0.8, zorder=20)

# ---------------------------------------------------------------- the inset: the Polynesian triangle
IW, IE, IS, IN = 158.0, 297.0, -49.0, 26.0
FX0, FY0, FW = 0.555, 0.012, 0.433                # where the inset sits, in fractions of the main map
iw = 16.0 * FW
n = Map(IW, IE, IS, IN, width=iw, lakes=False)
tri = [(-155.5 + 360, 19.6), (174.8, -41.0), (-109.35 + 360, -27.12)]
t = np.array(tri + [tri[0]])
n.ax.plot(t[:, 0], t[:, 1], color=FILL["red"], lw=2.2, ls=(0, (5, 3)), zorder=3)
for lon, lat in tri:
    n.ax.plot(lon, lat, "o", ms=9, mfc=INK, mec=PAPER, mew=1.2, zorder=6)
n.label(-155.5 + 360 + 3, 19.6, "Hawaii", size="small", colour=INK, fs=17, ha="left", style="normal")
n.label(174.8 + 2.5, -43.8, "New Zealand", size="small", colour=INK, fs=17, ha="left", style="normal")
n.label(-109.35 + 360, -31.8, "Rapa Nui", size="small", colour=INK, fs=17, style="normal")
for lon, lat, name, dx, dy, ha in ((-149.43, -17.65, "Tahiti", 3.0, 0.0, "left"),
                                   (-175.2, -21.2, "Tonga", -2.5, -1.5, "right"),
                                   (-172.1, -13.8, "Samoa", -2.5, 1.0, "right")):
    n.city(lon + 360, lat, name, dx=dx, dy=dy, ha=ha, r=7, size=16)
n.label(291.8, -3.0, "SOUTH AMERICA", size="land", fs=15, style="normal", rot=90)
n.label(210.0, -3.0, "the Polynesian\ntriangle", size="small", colour=FILL["red"], fs=17)
n.ax.add_patch(MplPoly([(IW, IS), (IE, IS), (IE, IN), (IW, IN)], closed=True, fc="none", ec=INK, lw=3, zorder=10))
pi = os.path.join(SCRATCH, "ch34_inset.png")
n.save(pi)

img = mpimg.imread(pi)
ih = img.shape[0] / 100.0
fh = m.fig.get_size_inches()[1]
ax = m.fig.add_axes([FX0, FY0, FW, ih / fh])
ax.imshow(img)
ax.set_axis_off()

m.save("chapters/34-pacific/images/map_rapanui.png" if not os.environ.get("CHECK")
       else os.path.join(SCRATCH, "check34.png"))
