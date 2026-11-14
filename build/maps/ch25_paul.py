#!/usr/bin/env python3
"""Chapter 25: Paul's journeys around the eastern Mediterranean, and his voyage to Rome as a prisoner.

The routes follow the account in Acts, as drawn in "Paul's missionary journeys" (Biblica Open Bible
map 16-17, Wikimedia Commons, CC BY-SA 4.0), the map this one replaces, and the maps in the Barrington
Atlas. The three journeys are drawn as one network of routes, each stretch once, without telling
the journeys apart; where two journeys took different ways between the same places, only one way is
drawn (the sea passages from Ephesus to Caesarea at the end of the second journey and from
Attalia to Antioch at the end of the first are left out). The
voyage is drawn on its own. Courses at sea are schematic. Positions from English Wikipedia.
"""
from lib import Map, INK

antioch, seleucia, tarsus = (36.16, 36.20), (35.93, 36.12), (34.90, 36.92)
pisidia, iconium, lystra, derbe = (31.19, 38.31), (32.48, 37.87), (32.33, 37.58), (33.36, 37.35)
perga, attalia = (30.85, 36.96), (30.70, 36.89)
troas, neapolis, philippi = (26.16, 39.75), (24.41, 40.94), (24.29, 41.01)
amphipolis, thessalonica, beroea = (23.85, 40.82), (22.94, 40.64), (22.20, 40.52)
athens, corinth, ephesus, miletus = (23.73, 37.98), (22.88, 37.91), (27.34, 37.94), (27.28, 37.53)
caesarea, jerusalem, tyre, sidon = (34.89, 32.50), (35.23, 31.78), (35.20, 33.27), (35.37, 33.56)

journeys = [
    [antioch, seleucia, (34.9, 35.6), (33.90, 35.18), (32.41, 34.76), (31.4, 35.8), perga, (31.0, 37.7), pisidia,
     iconium, lystra, derbe],
    [antioch, (36.17, 36.85), tarsus, (34.8, 37.3), derbe],
    [pisidia, (29.6, 39.2), (27.6, 39.8), troas],
    [troas, (25.53, 40.48), neapolis, philippi, amphipolis, thessalonica, beroea],
    [beroea, (22.8, 40.2), (23.6, 39.2), (24.2, 38.3), athens, corinth],
    [corinth, (23.8, 37.6), (25.6, 37.6), ephesus],
    [pisidia, (29.1, 37.8), ephesus],
    [troas, (26.34, 39.49), (26.55, 39.10), (26.1, 38.4), (26.9, 37.7), miletus, ephesus],
    [miletus, (27.29, 36.89), (28.22, 36.43), (29.32, 36.26), (31.5, 34.6), (34.0, 33.5), tyre,
     (35.07, 32.93), caesarea, jerusalem],
    [tyre, sidon, (35.8, 34.8), (35.9, 35.6), antioch],
]
voyage = [caesarea, sidon, (34.6, 35.8), (32.5, 36.1), (29.98, 36.26), (28.5, 36.35), (27.37, 36.69), (26.3, 35.3),
          (24.8, 34.9), (23.2, 34.6), (19.0, 35.0), (14.40, 35.95), (15.29, 37.07), (15.65, 38.11), (14.12, 40.82),
          (13.4, 41.4), (12.48, 41.89)]

m = Map(11.3, 38.6, 30.9, 42.9)
for leg in journeys:
    m.route(leg, colour="red", lw=3.0, arrow=False)
m.route(voyage, colour="blue", lw=3.4, style=(0, (2.2, 1.4)))

m.city(*jerusalem, "Jerusalem", dx=-0.3, dy=-0.25, bold=True, size=20)
m.city(36.29, 33.51, "Damascus", dx=0.25, dy=-0.35, ha="left", size=19)
m.city(*antioch, "Antioch", dx=0.25, dy=0.35, ha="left", size=19)
m.city(*tarsus, "Tarsus", dx=-0.3, dy=-0.35, size=19)
m.city(*ephesus, "Ephesus", dx=0.35, dy=0.15, size=19)
m.city(*philippi, "Philippi", dx=0.0, dy=0.45, size=19)
m.city(*thessalonica, "Thessalonica", dx=-0.25, dy=0.45, size=19)
m.city(*athens, "Athens", dx=0.35, dy=0.3, size=19)
m.city(*corinth, "Corinth", dx=-0.35, dy=-0.25, size=19)
m.city(12.48, 41.89, "Rome", dx=0.0, dy=0.45, bold=True, size=20)
m.label(14.40, 35.45, "Malta", size="land", fs=19)
m.label(24.9, 35.65, "Crete", size="land", fs=19)
m.label(33.0, 34.35, "Cyprus", size="land", fs=19)
m.label(35.9, 31.5, "JUDEA", fs=19, ha="left")
m.label(33.5, 40.4, "the Turkey of today", size="land", fs=19)
m.label(19.5, 34.4, "the voyage to Rome,\nas a prisoner", size="small", colour="blue", fs=19)
m.label(33.6, 38.75, "the journeys", size="small", colour="red", fs=19, rot=0)
m.label(19.2, 37.4, "Mediterranean Sea", size="sea", fs=21)
m.label(25.0, 39.0, "Aegean\nSea", size="sea", fs=19)
m.scale(300, lon=29.0, lat=31.3)
m.save("chapters/25-christianity/images/map_paul.png")
