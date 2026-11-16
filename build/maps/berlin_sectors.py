#!/usr/bin/env python3
"""Build data/berlin_sectors_1945.geojson, the four sectors of Berlin, for ch88_europe.py.

The sectors of 1945 followed the twenty boroughs (Bezirke) of Greater Berlin of 1920. Those boroughs survive
as groups of today's localities (Ortsteile), whose boundaries are taken from OpenStreetMap (data (c)
OpenStreetMap contributors, ODbL), fetched once from the Overpass API with

    [out:json];area["name"="Berlin"]["admin_level"="4"]->.b;
    rel(area.b)["boundary"="administrative"]["admin_level"="10"];out geom;

and saved as ortsteile_osm.json. Then:  python berlin_sectors.py ortsteile_osm.json data/berlin_sectors_1945.geojson
French: Reinickendorf and Wedding. British: Tiergarten, Charlottenburg, Wilmersdorf, Spandau. American:
Kreuzberg, Neukoelln, Tempelhof, Schoeneberg, Steglitz, Zehlendorf. Soviet: the rest. The small exchanges of
land at the city's edge after 1945 (West Staaken, Gross Glienicke) are ignored.
"""
import json, sys
from shapely.geometry import LineString, mapping
from shapely.ops import polygonize, unary_union, linemerge
d = json.load(open(sys.argv[1]))
FR = "Reinickendorf Tegel Konradshöhe Heiligensee Frohnau Hermsdorf Waidmannslust Lübars Wittenau|Märkisches Viertel|Borsigwalde Wedding Gesundbrunnen"
BR = "Tiergarten Moabit Hansaviertel Charlottenburg Charlottenburg-Nord Westend Wilmersdorf Schmargendorf Grunewald Halensee Spandau Haselhorst Siemensstadt Staaken Gatow Kladow Hakenfelde|Falkenhagener Feld|Wilhelmstadt"
US = "Kreuzberg Neukölln Britz Buckow Rudow Gropiusstadt Tempelhof Mariendorf Marienfelde Lichtenrade Schöneberg Friedenau Steglitz Lichterfelde Lankwitz Zehlendorf Dahlem Nikolassee Wannsee Schlachtensee"
def names(s):
    out = []
    for part in s.split("|"):
        out += [part] if " " in part and part in ("Märkisches Viertel","Falkenhagener Feld") else part.split()
    return set(out)
sec = {"French": names(FR), "British": names(BR), "American": names(US)}
polys = {}
for e in d["elements"]:
    lines = [LineString([(p["lon"], p["lat"]) for p in mb["geometry"]]) for mb in e["members"]
             if mb["type"] == "way" and mb.get("role") in ("outer", "") and "geometry" in mb]
    pg = unary_union(list(polygonize(unary_union(lines))))
    polys[e["tags"]["name"]] = pg
allset = set().union(*sec.values())
missing = allset - set(polys)
print("missing", missing)
out = {"type": "FeatureCollection", "features": []}
for s, ns in list(sec.items()) + [("Soviet", set(polys) - allset)]:
    g = unary_union([polys[n].buffer(0.0003) for n in ns if n in polys]).buffer(-0.0003).simplify(0.0008)
    print(s, len(ns), g.geom_type, round(g.area, 4))
    out["features"].append({"type": "Feature", "properties": {"sector": s}, "geometry": mapping(g)})
json.dump(out, open(sys.argv[2], "w"))
