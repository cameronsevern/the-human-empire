#!/usr/bin/env python3
"""Chapter 24: the Roman provinces in the year Augustus died, about 2,010 years ago (14 CE).

Traced by eye from "Roman empire 14 AD (provinces) en" by Homoatrox (Wikimedia Commons, CC BY-SA 4.0),
the map this one replaces, and checked against the map of the provinces under Augustus in The
Cambridge Ancient History, vol. X (1996). The tracing is in the source map's pixels, turned into
degrees by a quadratic fit to twenty-five capes, river mouths and coasts (error under one degree,
so the borders are rough). One change from the source: Sardinia and Corsica are shown as the emperor's, because Augustus
took the island from the Senate in 6 CE (Cassius Dio 55.28) and it went back only under Nero. Client
kingdoms (Thrace, Mauretania, Cappadocia) and the land beyond the Rhine lost in 9 CE are left out.
"""
from lib import Map, INK
from tracing import fit, states, hatched

deg = fit([((125, 640), (-5.35, 36.11)), ((40, 595), (-8.99, 37.02)), ((585, 450), (9.4, 43.0)),
           ((565, 590), (8.64, 38.87)), ((668, 645), (12.43, 37.8)), ((738, 682), (15.1, 36.69)),
           ((610, 665), (11.05, 37.08)), ((1355, 610), (34.59, 35.69)), ((1300, 655), (32.27, 35.06)),
           ((1030, 692), (23.55, 35.45)), ((1110, 685), (26.3, 35.25)), ((1155, 440), (29.0, 41.1)),
           ((1390, 540), (36.2, 36.6)), ((965, 635), (22.48, 36.39)), ((240, 190), (-4.75, 48.4)),
           ((320, 155), (-1.94, 49.72)), ((1130, 298), (29.7, 45.2)), ((1315, 240), (36.5, 45.3)),
           ((1485, 320), (41.6, 41.6)), ((1255, 810), (29.9, 31.2)), ((1315, 792), (31.8, 31.5)),
           ((1355, 837), (32.55, 29.97)), ((1440, 837), (35.0, 29.53)), ((930, 827), (20.07, 32.1)),
           ((1395, 782), (34.46, 31.5))], quad=True)

italy = deg([(520, 335), (560, 322), (640, 318), (712, 318), (722, 350), (730, 360), (800, 450), (870, 540),
             (820, 600), (790, 615), (770, 580), (690, 500), (640, 470), (590, 425), (525, 405)])
# the Senate's provinces
baetica = deg([(75, 565), (95, 540), (150, 540), (185, 560), (210, 565), (245, 620), (210, 640), (160, 645),
               (125, 642), (90, 630), (40, 620)])
narbonensis = deg([(355, 395), (365, 370), (420, 360), (470, 340), (490, 330), (500, 390), (525, 405),
                   (500, 450), (400, 450), (350, 430)])
sicily = deg([(655, 635), (700, 620), (775, 628), (782, 650), (745, 700), (660, 670)])
africa = deg([(420, 765), (440, 655), (560, 600), (640, 640), (700, 720), (820, 770), (900, 790), (905, 905),
              (890, 930), (420, 770)])
cyrenaica = deg([(905, 925), (905, 780), (1030, 760), (1110, 800), (1110, 880), (1000, 935)])
crete = deg([(1015, 682), (1120, 668), (1125, 708), (1015, 708)])
macedonia = deg([(875, 445), (990, 442), (1003, 470), (1020, 500), (1000, 540), (990, 562), (925, 565),
                 (910, 560), (885, 520), (850, 470)])
achaea = deg([(910, 560), (990, 562), (1010, 620), (1000, 665), (930, 665), (880, 600)])
asia = deg([(1075, 470), (1150, 480), (1210, 495), (1212, 560), (1210, 600), (1190, 625), (1100, 625),
            (1050, 560), (1060, 480)])
bithynia = deg([(1145, 430), (1180, 410), (1230, 395), (1300, 380), (1330, 375), (1325, 400), (1290, 415),
                (1255, 450), (1210, 495), (1150, 480), (1140, 450)])
cyprus = deg([(1290, 640), (1370, 595), (1375, 625), (1310, 670)])
senate = [baetica, narbonensis, sicily, africa, cyrenaica, crete, macedonia, achaea, asia, bithynia, cyprus]
# the emperor's provinces
west = deg([(10, 600), (10, 330), (70, 330), (150, 260), (230, 180), (300, 140), (400, 90), (470, 40),
            (495, 45), (510, 70), (530, 120), (545, 180), (555, 240), (520, 300), (520, 335), (525, 405),
            (520, 420), (420, 460), (330, 560), (250, 632), (140, 640), (10, 630)])
danube = deg([(555, 240), (600, 215), (650, 225), (720, 210), (800, 240), (880, 265), (890, 330), (960, 345),
              (1040, 325), (1100, 300), (1135, 300), (1120, 330), (1060, 350), (1010, 380), (1000, 440),
              (960, 442), (875, 445), (845, 460), (745, 375), (725, 358), (712, 318), (640, 318), (560, 322),
              (520, 335), (520, 300)])
east = deg([(1210, 495), (1255, 450), (1290, 415), (1325, 400), (1345, 420), (1345, 540), (1400, 525),
            (1420, 520), (1530, 565), (1480, 650), (1460, 690), (1420, 780), (1400, 800), (1390, 790),
            (1350, 700), (1380, 600), (1250, 600), (1210, 600)])
egypt = deg([(1110, 830), (1110, 960), (1470, 960), (1460, 870), (1400, 800), (1390, 790), (1250, 800),
             (1110, 800)])
sardinia = deg([(555, 435), (605, 435), (605, 605), (545, 605)])

m = Map(-10.0, 40.5, 27.5, 52.3)
m.river("Rhine", "Danube", "Nile", en=True)
states(m, [(italy, "gold")] + [(p, "blue") for p in senate] +
       [(p, "red") for p in (west, danube, east, egypt, sardinia)], alpha=0.45)
for p in senate:
    hatched(m, p, colour="#3d6487", alpha=0.0, edge=False)

m.label(13.6, 42.6, "ITALY", fs=24, rot=-38)
m.city(12.48, 41.89, "Rome", dx=-0.4, dy=-0.4, star=True, bold=True, size=20)
m.label(30.5, 28.6, "EGYPT", fs=26)
m.label(37.6, 34.5, "SYRIA", fs=24)
m.label(29.0, 38.6, "ASIA", fs=24)
m.label(10.0, 34.3, "AFRICA", fs=24)
m.label(2.5, 47.6, "GAUL", fs=26)
m.label(-4.0, 40.3, "SPAIN", fs=26)
m.label(22.0, 41.2, "MACEDONIA", fs=19)
m.label(22.0, 37.6, "GREECE", fs=19)
m.label(20.5, 45.7, "the Danube\nprovinces", size="small", colour=INK, fs=19)
m.label(35.4, 31.0, "Judea", size="small", colour=INK, fs=19, ha="left")
m.label(5.5, 38.3, "Mediterranean Sea", size="sea", fs=22)
m.label(34.0, 43.5, "Black Sea", size="sea", fs=22)
m.label(10.0, 51.0, "Germany", size="land", fs=21)
m.key([("red", "the emperor's provinces, with the legions"), (("hatch", "blue", "//"), "the Senate's provinces")],
      loc="lower left", size=19)
m.scale(500, lon=15.5, lat=34.0)
m.save("chapters/24-republic/images/map_provinces.png")
