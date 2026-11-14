#!/usr/bin/env python3
"""Chapter 45: Japan and Korea, 1543-1640. Tanegashima, where the Portuguese landed in 1543; Nagasaki and
its island of Dejima; Kyoto; the battlefield of Nagashino; Edo; the invasion of Korea in 1592, from the
Japanese base in Kyushu by Tsushima to Busan, Seoul and Pyongyang; the sea battles of Hansan Island in 1592
and Myeongnyang in 1597; and the four doors of the closed country: Nagasaki, Tsushima (for Korea),
Satsuma (for the Ryukyu islands, off the map to the south-west) and the far north (for the Ainu of
Hokkaido).

Drawn for this chapter, which had no map. The invasion route is simplified, after the route usually
drawn for the main thrust of 1592 (English Wikipedia's article "Japanese invasions of Korea
(1592-1598)"): from Nagoya in Hizen by Tsushima to Busan, north to Seoul, and on to Pyongyang. Positions
from English Wikipedia: Hansan Island is Hansando, off Tongyeong; Myeongnyang is the Uldolmok strait off
Jindo.
"""
from lib import Map, INK, FILL, PAPER

m = Map(123.5, 145.5, 29.8, 42.8)

# Tsushima, too small for the Natural Earth coastline at this scale, drawn by hand
from matplotlib.patches import Polygon as MplPoly
from lib import LAND, SHORE, smooth
tsushima = [(129.47, 34.70), (129.35, 34.66), (129.28, 34.50), (129.27, 34.33), (129.22, 34.16), (129.29, 34.10),
            (129.37, 34.24), (129.42, 34.42), (129.50, 34.60)]
m.ax.add_patch(MplPoly(smooth(tsushima, n=6, closed=True), closed=True, fc=LAND, ec=SHORE, lw=0.8, zorder=1.05))

# the invasion of 1592
m.route([(129.88, 33.53), (129.45, 34.25), (129.10, 35.05)], colour="red", lw=3.4, arrow=False)
m.route([(129.04, 35.10), (128.60, 35.90), (127.93, 36.97), (127.10, 37.50), (126.60, 38.30), (125.80, 38.95)],
        colour="red", lw=3.4)
m.label(129.6, 37.1, "invasion\nof 1592", size="small", colour=FILL["red"], fs=19, ha="left")

# sea battles
for lon, lat in [(128.48, 34.77), (126.31, 34.57)]:
    m.ax.plot(lon, lat, "X", ms=17, mfc=INK, mec=PAPER, mew=1.3, zorder=6)
m.label(128.02, 34.15, "Hansan Island\n1592", size="small", colour=INK, fs=17)
m.label(125.55, 33.95, "Myeongnyang\n1597", size="small", colour=INK, fs=17)

m.city(126.98, 37.57, "Seoul", dx=-0.3, dy=0.0, bold=True)
m.city(125.75, 39.03, "Pyongyang", dx=0.3, dy=0.25, ha="left")
m.city(129.04, 35.10, "Busan", dx=0.3, dy=0.12, bold=True)
m.label(129.95, 34.55, "Tsushima", size="small", colour=INK, fs=17, ha="left")
m.city(129.87, 32.75, "Nagasaki (Dejima)", dx=-0.3, dy=0.0, bold=True)
m.label(130.75, 31.75, "SATSUMA", fs=17)
m.city(131.00, 30.62, "Tanegashima, 1543", dx=0.3, dy=-0.05)
m.city(135.77, 35.01, "Kyoto", dx=-0.25, dy=0.25, bold=True)
m.ax.plot(137.55, 34.92, "X", ms=17, mfc=INK, mec=PAPER, mew=1.3, zorder=6)
m.label(137.65, 34.35, "Nagashino 1575", size="small", colour=INK, fs=17)
m.city(139.69, 35.69, "Edo", dx=0.3, dy=0.0, bold=True)

# the Ryukyu islands lie off the map to the south-west
m.ax.annotate("", xy=(128.4, 29.95), xytext=(129.5, 30.75), zorder=5,
              arrowprops=dict(arrowstyle="-|>,head_width=0.4,head_length=0.8", color=INK, lw=2))
m.label(128.0, 30.95, "to the Ryukyu\nislands", size="small", colour=INK, fs=16, ha="center")

m.label(127.6, 40.4, "KOREA", fs=22)
m.label(138.6, 36.6, "JAPAN", fs=22)
m.label(142.5, 42.3, "HOKKAIDO", size="land", fs=17, style="normal")
m.label(125.5, 42.2, "CHINA", size="land", fs=18, style="normal")
m.label(124.4, 36.2, "Yellow\nSea", size="sea", fs=18)
m.label(141.8, 32.0, "PACIFIC OCEAN", size="sea", fs=20)
m.scale(200, lon=141.0, lat=30.4)
m.save("chapters/45-japan/images/map_japan_korea.png")
