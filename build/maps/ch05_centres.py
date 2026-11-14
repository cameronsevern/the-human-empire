#!/usr/bin/env python3
"""Chapter 5: the places where farming began on its own.

The eight places the chapter names, with the crops it names. Areas are rough, drawn after
the Commons map by Ian Alexander (CC BY-SA 4.0, after Diamond and Bellwood 2003) and
checked against the map of centres of domestication in Larson et al. 2014 (PNAS).
Only the first and last dates are shown, as the chapter gives them.
"""
from lib import Map

m = Map(-128, 158, -38, 56)
G = "green"
m.region([(34.6, 31.2), (35.6, 35.4), (37.5, 37.4), (40.5, 37.9), (43.5, 37.2), (46.5, 35.6), (47.6, 33.6),
          (45.6, 33.4), (42.5, 35.0), (39.0, 35.6), (36.8, 33.6), (35.8, 31.2)], G, alpha=0.6)     # Middle East
m.region([(106.5, 34.0), (110.0, 37.8), (115.0, 38.2), (118.6, 36.2), (116.0, 33.6), (110.5, 33.4)], G, alpha=0.6)  # Yellow River
m.region([(110.5, 29.0), (113.0, 31.6), (118.0, 32.2), (121.6, 31.0), (119.0, 28.8), (114.0, 28.0)], G, alpha=0.6)  # Yangtze
m.region([(142.0, -5.2), (144.0, -5.0), (146.2, -6.0), (145.4, -6.9), (143.0, -6.5)], G, alpha=0.6, land_only=False)  # New Guinea highlands
m.region([(-103.5, 19.6), (-100.5, 20.4), (-97.0, 19.0), (-96.0, 17.0), (-99.5, 16.8), (-102.8, 18.0)], G, alpha=0.6)  # southern Mexico
m.region([(-80.0, -6.5), (-77.5, -6.0), (-73.0, -11.5), (-68.5, -15.0), (-67.5, -19.0), (-70.0, -18.5),
          (-74.5, -14.5), (-79.0, -9.0)], G, alpha=0.6)     # Andes
m.region([(-15.0, 11.5), (-5.0, 15.5), (10.0, 14.5), (25.0, 14.0), (36.0, 13.0), (35.0, 9.5), (20.0, 9.5),
          (5.0, 9.5), (-8.0, 9.0), (-14.5, 9.5)], G, alpha=0.6)   # Sahel and savanna
m.region([(-93.0, 36.0), (-90.0, 41.0), (-85.0, 41.2), (-81.5, 38.8), (-84.0, 35.0), (-89.5, 34.4)], G, alpha=0.6)  # eastern N. America

R = dict(size="region", fs=19)
T = dict(size="small", colour="#2f2a26", fs=16.5)
m.label(-88.0, 52.0, "eastern North America", **R)
m.label(-88.0, 47.2, "about 4,000 years ago", **T)
m.label(-107.0, 19.5, "southern\nMexico", ha="right", **R)
m.label(-107.0, 13.0, "maize", ha="right", **T)
m.label(-83.0, -9.5, "Andes", ha="right", **R)
m.label(-83.0, -14.0, "potatoes", ha="right", **T)
m.label(14.0, 2.5, "Africa south\nof the Sahara", **R)
m.label(40.0, 45.5, "Middle East", **R)
m.label(44.0, 25.5, "wheat, barley\n11,000 years ago", **T)
m.label(110.0, 49.0, "northern China", **R)
m.label(110.0, 44.0, "millet", **T)
m.label(124.5, 28.5, "Yangtze", ha="left", **R)
m.label(124.5, 24.0, "rice", ha="left", **T)
m.label(141.0, 3.5, "New Guinea", **R)
m.label(143.0, -13.5, "taro, bananas", **T)

m.label(-42.0, 22.0, "Atlantic\nOcean", size="sea")
m.label(-118.0, -22.0, "Pacific\nOcean", size="sea")
m.label(75.0, -15.0, "Indian Ocean", size="sea")
m.save("chapters/05-farming/images/map_farming_centres.png")
