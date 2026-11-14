#!/usr/bin/env python3
"""Chapter 17: the seven warring states of China about 2,300 years ago (about 260 BCE).

The states are traced by eye from "EN-WarringStatesAll260BCE" by Philg88 (Wikimedia Commons,
CC BY-SA 3.0), the map this one replaces, and checked against the map of the Warring States in
The Cambridge History of Ancient China (1999). The source is drawn freely, so the tracing is
turned into degrees by a quadratic fit to fourteen of its cities; the borders are rough. The
Yellow River is drawn only above the plain, because its lower course then ran far to the north
of where it runs now. Lu, Confucius's state, was still a small state between Qi and Chu.
City positions from English Wikipedia.
"""
from shapely.geometry import box
from lib import Map
from tracing import fit, states

deg = fit([((558, 866), (108.71, 34.33)), ((818, 832), (112.45, 34.62)), ((1224, 617), (118.31, 36.86)),
           ((955, 630), (114.49, 36.61)), ((1068, 375), (116.39, 39.90)), ((800, 1210), (112.19, 30.42)),
           ((1126, 1024), (116.78, 32.56)), ((1447, 1086), (120.62, 31.30)), ((178, 1187), (104.07, 30.66)),
           ((943, 822), (114.34, 34.80)), ((997, 897), (114.88, 33.73)), ((430, 968), (107.03, 33.07)),
           ((357, 1220), (106.55, 29.56)), ((934, 373), (114.56, 39.84))], quad=True)

qin = deg([(205, 800), (260, 780), (400, 730), (500, 680), (560, 620), (620, 520), (690, 440), (670, 625),
           (660, 700), (650, 835), (620, 880), (700, 930), (740, 960), (770, 1020), (800, 1100), (840, 1180),
           (840, 1230), (760, 1250), (680, 1240), (560, 1290), (450, 1320), (350, 1350), (250, 1340),
           (150, 1310), (80, 1240), (100, 1050), (130, 960), (100, 880)])
zhao = deg([(420, 345), (440, 290), (480, 255), (560, 285), (680, 300), (760, 320), (860, 370), (935, 345),
            (985, 375), (990, 410), (1040, 470), (1085, 520), (1060, 580), (1055, 625), (1000, 618), (950, 640),
            (890, 615), (890, 550), (840, 600), (760, 605), (670, 625), (690, 440), (715, 425), (720, 360),
            (680, 330), (560, 315), (470, 310), (440, 355)])
yan = deg([(985, 375), (1060, 330), (1110, 280), (1140, 300), (1250, 250), (1330, 200), (1400, 140),
           (1460, 100), (1550, 110), (1450, 230), (1430, 270), (1310, 330), (1250, 400), (1170, 430),
           (1160, 480), (1100, 520), (1085, 520), (1040, 470), (990, 410)])
qi = deg([(1100, 520), (1160, 480), (1230, 550), (1350, 520), (1430, 540), (1510, 545), (1490, 590),
          (1430, 640), (1350, 700), (1250, 700), (1150, 700), (1100, 710), (1060, 690), (1030, 660),
          (1060, 580), (1085, 520)])
wei = deg([(670, 625), (760, 605), (840, 600), (890, 550), (890, 615), (950, 640), (1000, 618), (1055, 625),
           (1030, 660), (1065, 700), (990, 760), (990, 830), (1005, 880), (985, 880), (930, 815), (800, 815),
           (650, 835), (660, 700)])
han = deg([(620, 880), (650, 835), (800, 815), (930, 815), (985, 880), (950, 925), (850, 920), (720, 925),
           (640, 900)])
chu = deg([(985, 880), (1005, 880), (990, 760), (1065, 700), (1100, 710), (1250, 700), (1330, 700),
           (1310, 760), (1340, 820), (1420, 900), (1490, 1010), (1480, 1040), (1470, 1140), (1400, 1180),
           (1250, 1250), (1100, 1270), (950, 1280), (920, 1340), (870, 1380), (780, 1350), (700, 1300),
           (680, 1240), (760, 1250), (840, 1230), (840, 1180), (800, 1100), (770, 1020), (740, 960),
           (720, 925), (850, 920), (950, 925)])

m = Map(102.8, 122.6, 27.6, 42.0)
full = m.clip
m.clip = box(95, 30, 114.0, 45)          # the Yellow River above the plain only
m.river("Huang")
m.clip = full
m.river("Yangtze", "Chang Jiang", "Han")
states(m, [(han, "purple"), (wei, "olive"), (qi, "gold"), (yan, "pink"), (zhao, "brown"), (qin, "red"),
           (chu, "green")])

m.label(106.3, 32.2, "QIN", fs=30)
m.label(112.4, 38.4, "ZHAO", fs=30)
m.label(117.0, 40.9, "YAN", fs=30)
m.label(119.6, 36.6, "QI", fs=30)
m.label(112.2, 35.7, "WEI", fs=26)
m.label(113.2, 34.0, "HAN", fs=22)
m.label(115.6, 31.0, "CHU", fs=30)
m.city(112.45, 34.62, "Zhou king", dx=0.0, dy=0.42, size=19, bold=True)
m.city(116.99, 35.58, "Lu", dx=0.3, size=19, bold=True)
m.label(108.6, 39.6, "Yellow River", size="sea", fs=19, rot=0)
m.label(109.0, 29.6, "Yangtze", size="sea", fs=19, rot=-5)
m.label(121.5, 33.6, "Yellow\nSea", size="sea", fs=19)
m.scale(300, lon=118.0, lat=28.2)
m.save("chapters/17-thinkers/images/map_warring_states.png")
