#!/usr/bin/env python3
"""Chapter 22: two maps.

1. The Xiongnu empire after the conquests of Modu, about 2,200 years ago. Its extent is drawn by
   eye after "Map of the Xiongnu, circa 150 BCE" (Wikimedia Commons, CC0), the map it replaces, and
   checked against the map of the Xiongnu empire under Modu in Di Cosmo, Ancient China and Its
   Enemies (2002): the steppe from Manchuria to the mountains of Central Asia, the oasis towns on
   its southern edge, the loop of the Yellow River and the corridor of oases. It is rough.

2. The Han empire about 2,080 years ago (60 BCE), with the corridor of oases and the oasis kingdoms
   of the Western Protectorate. Traced by eye from "Han dynasty (60 BC) with the Hexi Corridor
   highlighted" by Qiushufang (Wikimedia Commons, CC BY-SA 4.0), the map it replaces, turned into
   degrees by a quadratic fit to eleven lakes, coasts and cities (the source is a conic map), and
   checked against the map of the Western Regions in Hulsewé, China in Central Asia (1979). The
   wall is drawn along the north side of the corridor and on west of Dunhuang as a line of towers,
   after Stein's survey; it is schematic. City positions from English Wikipedia.
"""
from shapely.geometry import box
from lib import Map
from tracing import fit, states, hatched

# ---------------------------------------------------------------- 1. the Xiongnu under Modu
xiongnu = [(73.5, 41.5), (74.5, 44.5), (78.0, 47.5), (84.0, 49.8), (90.0, 51.8), (97.0, 53.0), (102.0, 54.6),
           (107.0, 56.0), (113.0, 55.8), (119.0, 54.0), (124.5, 51.0), (127.0, 47.5), (125.5, 43.8),
           (122.0, 41.8), (118.0, 41.0), (114.0, 40.8), (111.5, 39.6), (110.0, 37.8), (107.0, 37.2),
           (104.0, 36.6), (101.0, 37.4), (98.0, 38.8), (95.0, 39.3), (92.0, 38.6), (88.0, 37.6),
           (83.0, 36.6), (78.0, 36.8), (75.0, 38.6)]

m = Map(71.0, 130.5, 32.3, 57.0)
full = m.clip
m.clip = box(95, 30, 114.0, 45)          # the Yellow River above the plain only: its lower course has moved
m.river("Huang")
m.clip = full
m.river("Tarim")
m.region(xiongnu, "brown", alpha=0.42)
m.label(101.0, 46.3, "XIONGNU", fs=34)
m.label(116.6, 34.4, "HAN", fs=30)
m.label(124.0, 46.6, "Manchuria", size="land", fs=21)
m.label(107.0, 43.5, "Gobi", size="land", fs=22)
m.label(108.4, 51.0, "Mongolia", size="land", fs=21)
m.label(84.5, 39.0, "oasis towns", size="land", fs=21)
m.label(88.0, 34.2, "mountains of Tibet", size="land", fs=21)
m.label(108.8, 54.9, "Lake\nBaikal", size="sea", fs=19, ha="left")
m.label(99.6, 34.7, "Yellow River", size="sea", fs=20)
m.label(108.0, 39.9, "the loop", size="sea", fs=19)
m.city(108.94, 34.34, "Han capital", dx=0.0, dy=-1.0, size=20)
m.label(125.5, 36.5, "Yellow\nSea", size="sea", fs=20)
m.scale(500, lon=73.0, lat=33.1)
m.save("chapters/22-wall/images/map_xiongnu_modu.png")

# ---------------------------------------------------------------- 2. the Han and the corridor
deg = fit([((1155, 452), (122.7, 37.4)), ((1172, 820), (120.95, 23.7)), ((903, 955), (109.7, 19.2)),
           ((1262, 538), (126.55, 33.38)), ((1022, 428), (116.4, 39.9)), ((684, 493), (100.2, 36.9)),
           ((430, 325), (87.0, 42.0)), ((244, 259), (77.3, 42.4)), ((770, 108), (103.9, 51.6)),
           ((710, 120), (100.5, 51.0)), ((575, 128), (92.8, 50.3))], quad=True)

corridor = deg([(555, 368), (630, 375), (694, 414), (759, 436), (784, 464), (784, 525), (744, 514), (701, 486),
                (659, 454), (616, 429), (559, 414)])
han = deg([(616, 429), (659, 454), (701, 486), (744, 514), (784, 525), (790, 440), (820, 385), (870, 380),
           (950, 380), (1000, 370), (1050, 360), (1100, 340), (1150, 320), (1200, 315), (1230, 330),
           (1260, 420), (1250, 600), (1200, 800), (1000, 1000), (850, 1000), (720, 900), (670, 850),
           (680, 700), (668, 600), (666, 486), (630, 436)])
west = deg([(162, 329), (201, 307), (273, 286), (337, 243), (366, 218), (451, 214), (494, 257), (530, 307),
            (559, 364), (555, 414), (487, 407), (416, 421), (344, 436), (273, 436), (230, 414), (187, 393),
            (166, 364)])

m = Map(69.0, 121.0, 32.3, 48.6)
full = m.clip
m.clip = box(95, 30, 114.0, 45)
m.river("Huang")
m.clip = full
m.river("Tarim")
states(m, [(corridor, "blue"), (han, "purple")], alpha=0.45)
hatched(m, west, colour="pink", alpha=0.22)
wall = [(103.6, 37.2), (102.6, 38.2), (101.0, 39.1), (99.0, 39.95), (97.0, 40.35), (95.0, 40.45),
        (93.8, 40.4)]
towers = [(93.8, 40.4), (92.4, 40.3), (91.0, 40.25)]
m.line(wall, colour="#2f2a26", lw=3.2)
m.line(towers, colour="#2f2a26", lw=3.2, style=(0, (1, 1.6)))

m.label(114.2, 34.6, "HAN EMPIRE", fs=28)
m.label(105.0, 44.6, "XIONGNU", fs=28)
m.label(83.0, 41.5, "oasis kingdoms", size="region", fs=22, colour="#8a4a5c")
m.label(83.4, 38.5, "sea of dunes", size="land", fs=20)
m.label(100.6, 41.4, "corridor\nof oases", size="small", colour="#2f2a26", fs=20)
m.label(95.0, 35.6, "mountains of Tibet", size="land", fs=20)
m.label(104.5, 41.9, "Gobi", size="land", fs=22)
m.label(72.8, 41.7, "Ferghana", size="land", fs=20)
m.label(97.0, 46.6, "Mongolia", size="land", fs=20)
m.label(111.6, 41.0, "Yellow River", size="sea", fs=19)
m.label(93.0, 41.3, "wall", size="small", colour="#2f2a26", fs=19)
m.city(94.66, 40.14, "Dunhuang", dx=-0.4, dy=-0.8, size=20, bold=True)
m.city(108.94, 34.34, "Chang'an", dx=0.0, dy=-0.75, size=20)
m.city(116.4, 39.9, "Beijing", dx=-0.5, dy=0.0, size=18)
m.scale(500, lon=73.0, lat=33.3)
m.save("chapters/22-wall/images/map_han_corridor.png")
