#!/usr/bin/env python3
"""Chapter 43: Italy about 1494, on the eve of the French invasion. The five main states (the Republic of
Venice, the Duchy of Milan, the Republic of Florence, the States of the Church and the Kingdom of Naples)
as soft areas, with the small Republic of Siena between Florence and the pope's lands, and the cities
the text names: Florence, Venice, Milan, Genoa, Rome, Verona and Bologna, with Naples.

Drawn for this chapter, which had no map. The extents are rough, after the maps of Italy in 1494 in
Shepherd's Historical Atlas and in English Wikipedia's article "Italian Wars", checked against the
towns each state held: Venice from Bergamo and Crema to Friuli and western Istria, with the Polesine and
Ravenna, and its Dalmatian towns and islands; Milan with Como, Novara, Pavia, Alessandria, Cremona,
Piacenza and Parma; Florence with Pisa, Livorno, Arezzo, Cortona and Sansepolcro; the pope from Bologna
and the Romagna to Terracina; Naples the whole south of the mainland. Small states (Savoy, Montferrat,
Mantua, Ferrara, Lucca, Genoa, which was then under Milan's lordship) are left unshaded. Positions from
English Wikipedia.
"""
import lib
from lib import Map, INK, FILL
from tracing import states

W, E, S, N = 5.0, 18.9, 37.75, 47.0
m = Map(W, E, S, N)
m.river("Po", "Tiber", "Adige")

venice = [(9.45, 46.15), (10.3, 46.35), (10.6, 46.05), (11.05, 45.95), (11.6, 46.1), (12.2, 46.6), (12.9, 46.65),
          (13.55, 46.3), (13.5, 45.85), (13.75, 45.45), (14.0, 44.9), (13.4, 44.8), (12.6, 44.7), (12.4, 44.3),
          (12.1, 44.3), (12.0, 44.6), (11.9, 44.85), (11.4, 45.05), (11.0, 45.15), (10.6, 45.35), (10.1, 45.28),
          (9.6, 45.25), (9.48, 45.6)]
dalmatia = [(14.6, 45.1), (15.3, 44.4), (16.1, 43.75), (16.9, 43.35), (17.0, 43.05), (16.4, 42.9), (15.8, 43.4),
            (14.9, 44.0), (14.2, 44.6)]
milan = [(8.2, 46.3), (8.9, 46.5), (9.4, 46.45), (10.3, 46.55), (10.35, 46.4), (9.45, 46.15), (9.48, 45.6),
         (9.6, 45.25), (10.1, 45.28), (10.55, 45.05), (10.45, 44.6), (10.1, 44.4), (9.5, 44.55), (8.9, 44.62),
         (8.5, 44.7), (8.5, 45.25), (8.45, 45.65), (8.15, 45.95)]
florence = [(10.22, 43.5), (10.28, 43.8), (10.6, 43.78), (10.75, 43.98), (10.95, 44.12), (11.4, 44.22),
            (11.8, 44.08), (12.12, 43.75), (12.15, 43.5), (11.97, 43.22), (11.7, 43.3), (11.3, 43.45),
            (10.95, 43.32), (10.7, 43.2), (10.5, 43.25)]
siena = [(10.5, 43.25), (10.7, 43.2), (10.95, 43.32), (11.3, 43.45), (11.7, 43.3), (11.97, 43.22), (11.9, 42.85),
         (11.75, 42.65), (11.45, 42.35), (11.05, 42.35), (10.7, 42.75), (10.45, 43.0)]
papal = [(12.4, 44.3), (12.6, 44.05), (13.0, 43.8), (13.6, 43.55), (13.9, 42.9), (13.45, 42.7), (13.15, 42.4),
         (13.4, 42.1), (13.8, 41.8), (13.5, 41.55), (13.1, 41.2), (12.4, 41.6), (11.8, 42.05), (11.45, 42.35),
         (11.75, 42.65), (11.9, 42.85), (11.97, 43.22), (12.15, 43.5), (12.12, 43.75), (11.8, 44.08),
         (11.4, 44.22), (11.05, 44.4), (11.0, 44.62), (11.5, 44.66), (11.8, 44.5), (12.1, 44.3)]
naples = [(13.9, 42.9), (14.9, 42.2), (16.2, 41.9), (18.6, 40.3), (18.6, 39.8), (16.8, 37.8), (15.6, 37.8),
          (15.4, 38.5), (15.4, 40.1), (14.0, 40.8), (13.1, 41.2), (13.5, 41.55), (13.8, 41.8), (13.4, 42.1),
          (13.15, 42.4), (13.45, 42.7)]
states(m, [(venice, "blue"), (dalmatia, "blue"), (milan, "green"), (florence, "red"), (siena, "brown"),
           (papal, "gold"), (naples, "purple")])

m.label(11.55, 46.25, "REPUBLIC\nOF VENICE", fs=19)
m.label(9.55, 44.93, "DUCHY\nOF MILAN", fs=18)
m.label(10.05, 43.62, "REPUBLIC OF\nFLORENCE", fs=17, ha="right")
m.label(11.2, 42.85, "SIENA", fs=16)
m.label(13.0, 42.95, "STATES OF\nTHE CHURCH", fs=18)
m.label(16.2, 40.15, "KINGDOM\nOF NAPLES", fs=20)
m.label(7.35, 45.05, "Savoy", size="land", fs=17)
m.label(5.75, 44.3, "FRANCE", size="land", fs=19)
m.label(14.0, 38.2, "Sicily", size="land", fs=17)
m.label(9.0, 40.2, "Sardinia", size="land", fs=17)
m.label(15.5, 42.75, "Adriatic\nSea", size="sea", fs=20)
m.label(11.7, 39.9, "Tyrrhenian\nSea", size="sea", fs=20)
m.label(8.2, 43.25, "Ligurian Sea", size="sea", fs=17)
m.ax.text(7.4, 46.25, "A  L  P  S", fontsize=17, color=lib.SOFT, ha="center", va="center", rotation=0, zorder=7,
          path_effects=lib.HALO, style="italic")

m.city(11.255, 43.770, "Florence", dx=0.18, dy=0.12, bold=True)
m.city(12.336, 45.437, "Venice", dx=0.18, dy=-0.12, bold=True)
m.city(9.190, 45.464, "Milan", dx=-0.18, dy=0.0, bold=True)
m.city(8.934, 44.407, "Genoa", dx=-0.15, dy=0.14)
m.city(12.496, 41.903, "Rome", dx=0.17, dy=-0.06, bold=True)
m.city(10.992, 45.438, "Verona", dx=0.0, dy=0.24)
m.city(11.343, 44.494, "Bologna", dx=0.18, dy=0.08)
m.city(14.268, 40.852, "Naples", dx=0.2, dy=-0.2)
m.scale(200, lon=5.6, lat=38.2)
m.save("chapters/43-renaissance/images/map_italy.png")
