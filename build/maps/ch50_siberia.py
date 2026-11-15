#!/usr/bin/env python3
"""Chapter 50: northern Asia, 1582-1771. The Russian advance from Moscow and Kazan over the Urals to Sibir,
and by the Ob, the Yenisei and the Lena to the Sea of Okhotsk: the forts on the Yenisei (Yeniseisk,
1619) and the Lena (Yakutsk, 1632), and the sea reached in 1639. The fort of Albazin on the Amur, and
Nerchinsk, where the treaty of 1689 was made. On the Chinese side, Beijing, the gate where the Great Wall
meets the sea (Shanhai Pass), the Manchu homeland, Mongolia and the Gobi, the lands of the Zunghars,
and Tibet with Lhasa. And the journey of the Torghuts from the Volga in 1771.

Drawn for this chapter, which had no map. The Russian advance is drawn as one simplified line, after
the routes usually drawn for the conquest of Siberia (English Wikipedia's article "Russian conquest
of Siberia"): Tobolsk, down the Irtysh to the Ob, up the Ket and over the portage to Yeniseisk, by the
Angara and the Ilim to the Lena, down the Lena to Yakutsk, and over the mountains to the Sea of Okhotsk.
The Zunghar lands and the Manchu homeland are soft and approximate, after the maps in English
Wikipedia's articles "Dzungar Khanate" and "Manchuria" (the Manchu homeland is drawn round the old
Jianzhou lands in the south-east, where Nurhaci rose). The Torghut route is simplified: from the lower
Volga across the Kazakh steppe to the Ili valley. Positions from English Wikipedia.
"""
import lib
from lib import Map, INK, FILL, PAPER

m = Map(34.0, 150.0, 27.0, 73.0)
m.river("Volga", "Ob", "Irtysh", "Yenisey", "Lena", "Amur", "Angara", "Shilka", "Argun", "Kama", "Tobol",
        "Selenga", en=True, lw=1.5)

zunghar = [(75.0, 44.0), (78.5, 42.6), (82.0, 42.2), (86.0, 42.6), (90.0, 43.4), (94.0, 44.2), (96.2, 46.2),
           (94.6, 48.4), (90.5, 49.6), (86.5, 49.8), (83.0, 48.6), (79.5, 47.0), (76.5, 46.0)]
manchu = [(121.8, 41.6), (124.4, 40.2), (127.6, 41.2), (130.6, 42.6), (131.4, 45.0), (129.4, 46.8), (126.0, 46.6),
          (123.0, 45.0)]
m.region(zunghar, "purple", alpha=0.38)
m.region(manchu, "gold", alpha=0.45)

# the Russian advance
m.route([(37.62, 55.75), (43.5, 56.2), (49.12, 55.79), (56.0, 57.6), (61.5, 58.4), (65.5, 58.1), (68.25, 58.2)],
        colour="red", lw=3.4, arrow=False)
m.route([(68.25, 58.2), (70.5, 59.4), (75.0, 60.6), (80.0, 60.0), (84.5, 58.8), (89.0, 58.4), (92.17, 58.45),
         (98.0, 57.6), (102.5, 56.9), (106.0, 57.4), (108.0, 57.0), (112.0, 58.6), (118.0, 60.4), (124.0, 61.4),
         (129.73, 62.03), (134.0, 61.6), (138.0, 60.4), (141.6, 59.4)], colour="red", lw=3.4)
m.route([(112.0, 58.6), (113.6, 55.6), (116.52, 51.98), (120.5, 52.9), (124.13, 53.4)], colour="red", lw=2.6,
        arrow=False, style=(0, (5, 2.5)))

# the Torghuts, 1771
m.route([(46.5, 47.8), (52.0, 48.6), (58.0, 48.2), (64.0, 47.0), (70.0, 45.8), (75.0, 44.6), (79.6, 44.0)],
        colour=INK, lw=2.6, style=(0, (4, 2.5)))
m.label(58.5, 50.4, "the Torghuts, 1771", size="small", colour=INK, fs=18)

# Russia
m.city(37.62, 55.75, "Moscow", dx=0.0, dy=1.4, bold=True)
m.city(49.12, 55.79, "Kazan", dx=0.0, dy=-1.3)
m.label(59.2, 63.5, "URALS", size="land", fs=17, style="normal", rot=90, spaced=False)
m.city(68.25, 58.20, "Sibir (Tobolsk), 1582", dx=-0.5, dy=-1.5, ha="center")
m.city(92.17, 58.45, "Yeniseisk, 1619", dx=0.0, dy=-1.4)
m.city(129.73, 62.03, "Yakutsk, 1632", dx=0.0, dy=1.5)
m.city(141.6, 59.4, None)
m.label(141.0, 57.2, "Pacific reached,\n1639", size="small", colour=INK, fs=17, ha="center")
m.city(124.13, 53.40, "Albazin", dx=1.0, dy=0.3)
m.city(116.52, 51.98, "Nerchinsk, 1689", dx=0.0, dy=-1.3)

# China and the steppe
m.city(116.40, 39.90, "Beijing", dx=-1.0, dy=0.0, bold=True)
m.city(119.75, 40.00, "Shanhai Pass", dx=0.3, dy=-1.3, ha="left")
m.label(127.0, 43.9, "MANCHU\nHOMELAND", fs=17)
m.label(86.5, 46.0, "ZUNGHARS", fs=18)
m.label(103.5, 47.2, "MONGOLIA", fs=19)
m.label(106.0, 42.6, "GOBI", size="land", fs=17, style="normal", spaced=True)
m.label(88.0, 33.0, "TIBET", fs=19)
m.city(91.13, 29.65, "Lhasa", dx=1.0, dy=0.0)
m.label(110.0, 33.0, "CHINA", size="land", fs=19, style="normal")
m.label(100.0, 65.5, "S I B E R I A", size="land", fs=19, style="normal")

# rivers named
for lon, lat, name, rot in [(72.2, 64.5, "Ob", 0), (85.0, 66.5, "Yenisei", 0), (125.0, 67.0, "Lena", 0),
                            (131.0, 50.4, "Amur", 0), (45.5, 51.5, "Volga", 0)]:
    m.label(lon, lat, name, size="sea", fs=17, rot=rot)

m.label(51.0, 42.0, "Caspian\nSea", size="sea", fs=16)
m.label(146.0, 55.0, "Sea of\nOkhotsk", size="sea", fs=16)
m.label(92.0, 71.6, "ARCTIC OCEAN", size="sea", fs=19)
m.scale(1000, lon=60.0, lat=29.0)
m.save("chapters/50-russia/images/map_siberia.png")
