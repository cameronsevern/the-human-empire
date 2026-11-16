"""Shared shapes for the maps of Japan's war, chapters 80 and 81: Japan's empire and the parts of China
its army held, built roughly from the modern countries (Natural Earth admin-0, as shipped with geopandas)
and hand-drawn soft areas.

Manchuria (Manchukuo, with Jehol) is drawn roughly as in ch75_china.py. Occupied China follows the maps of
the Second Sino-Japanese War in English Wikipedia ("Second Sino-Japanese War", the map of Japanese
occupation in 1940): the north-east from Inner Mongolia (Baotou, Kalgan) through Shanxi and Hebei and
Shandong to the Yellow River, the lower Yangzi to Yichang and Yueyang, Nanchang, Hangzhou and Shanghai,
and a pocket round Canton, with Hainan. The Japanese held the cities and the railways rather than all the
land, so this is a rough extent. Karafuto is Sakhalin south of 50 degrees north.
"""
import geopandas as gpd
from shapely.geometry import Point, Polygon, box
from shapely.ops import unary_union
from lib import smooth

C = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
G = {r["name"]: r.geometry for _, r in C.iterrows()}
soft = lambda pts: Polygon(smooth(pts, n=10, closed=True)).buffer(0)

manchuria = soft([(117.3, 40.3), (119.3, 39.9), (121.2, 38.7), (124.3, 39.9), (126.5, 41.4), (129.0, 42.3),
                  (130.6, 42.4), (131.2, 43.5), (131.0, 44.9), (133.5, 45.5), (135.0, 48.3), (132.5, 47.8),
                  (130.8, 48.9), (127.6, 49.8), (125.5, 53.0), (121.5, 53.3), (119.8, 50.5), (117.8, 49.6),
                  (116.0, 47.2), (117.4, 45.4), (118.0, 42.8), (116.6, 41.6)])
occupied_china = unary_union([
    soft([(109.6, 40.8), (113.0, 41.9), (116.0, 41.8), (117.3, 40.3), (119.3, 39.9), (119.8, 38.9), (118.6, 38.0),
          (119.5, 37.2), (122.5, 37.3), (120.5, 35.5), (119.2, 34.6), (120.3, 33.2), (121.8, 31.8), (121.9, 30.8),
          (120.8, 29.9), (119.8, 29.6), (118.3, 29.9), (117.0, 29.3), (116.1, 28.4), (115.3, 28.8),
          (114.0, 29.4), (113.0, 29.1), (112.3, 29.9), (111.2, 30.6), (111.8, 31.4), (113.2, 31.7), (114.5, 32.8),
          (114.6, 34.4), (113.6, 34.9), (112.3, 35.1), (110.6, 35.6), (110.6, 37.4), (110.2, 39.2)]),
    soft([(112.6, 23.6), (114.2, 23.6), (114.8, 22.8), (114.3, 22.3), (113.4, 22.1), (112.5, 22.6)]),
    G["China"].intersection(box(108.4, 18.0, 111.2, 20.2)),
]).difference(Point(114.17, 22.33).buffer(0.22))         # Hong Kong, British until 25 December 1941
korea = unary_union([G["North Korea"], G["South Korea"]])
karafuto = box(141.7, 45.8, 144.8, 50.0)                 # boxes: intersect with the land of the map
kurils = box(145.3, 43.3, 157.0, 50.8)
japan = unary_union([G["Japan"].buffer(0.3), karafuto, kurils])
indochina = unary_union([G["Vietnam"], G["Laos"], G["Cambodia"]])
