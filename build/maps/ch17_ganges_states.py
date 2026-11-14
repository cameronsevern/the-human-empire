#!/usr/bin/env python3
"""Chapter 17: the states of the Ganges plain about 2,500 years ago, in the Buddha's time.

The states are traced by eye from "Mahajanapadas (c. 500 BCE)" by Avantiputra7 (Wikimedia
Commons, CC BY-SA 3.0), the map this one replaces, which shows each state as a soft patch of
colour around its capital; they are drawn here the same way, as rough areas, and only the
states of the plain are shown. Checked against the map of the sixteen great states in Thapar,
Early India (2002). The tracing is in the source map's pixels, turned into degrees by a fit to
fourteen towns. Town positions from English Wikipedia.
"""
from lib import Map
from tracing import fit, states

deg = fit([((531, 283), (78.00, 29.17)), ((505, 295), (77.25, 28.60)), ((521, 343), (77.67, 27.49)),
           ((659, 343), (82.04, 27.51)), ((662, 367), (82.20, 26.80)), ((684, 413), (83.00, 25.32)),
           ((640, 410), (81.39, 25.34)), ((753, 385), (85.13, 25.99)), ((758, 421), (85.42, 25.03)),
           ((811, 412), (86.95, 25.25)), ((701, 359), (83.89, 26.74)), ((464, 486), (75.78, 23.18)),
           ((528, 465), (77.81, 23.52)), ((560, 302), (79.14, 28.37))], quad=True)

shakya = deg([(662, 318), (702, 312), (708, 333), (668, 338)])
kosala = deg([(612, 322), (668, 336), (695, 338), (700, 365), (672, 388), (630, 382), (612, 355)])
malla = deg([(700, 343), (738, 343), (742, 372), (702, 380)])
vajji = deg([(740, 338), (792, 343), (792, 383), (745, 386)])
magadha = deg([(712, 398), (790, 393), (800, 430), (762, 455), (718, 440)])
anga = deg([(800, 392), (852, 396), (860, 432), (810, 440)])
kashi = deg([(650, 392), (705, 394), (708, 426), (672, 432), (650, 418)])
vatsa = deg([(585, 372), (645, 388), (650, 422), (618, 428), (585, 402)])
panchala = deg([(545, 282), (600, 296), (628, 326), (610, 355), (568, 346), (545, 315)])
kuru = deg([(468, 262), (540, 248), (552, 285), (530, 322), (490, 312), (465, 290)])
surasena = deg([(498, 328), (560, 342), (585, 378), (566, 396), (518, 372), (494, 348)])

m = Map(76.3, 88.4, 23.4, 30.4)
m.river("Ganges", "Yamuna", "Ghäghara", "Gandak", "Son")
states(m, [(shakya, "red"), (kosala, "gold"), (malla, "teal"), (vajji, "purple"), (magadha, "red"),
           (anga, "gold"), (kashi, "blue"), (vatsa, "green"), (panchala, "purple"), (kuru, "brown"),
           (surasena, "olive")], alpha=0.5, smooth_n=12)

m.label(83.0, 28.15, "ŚĀKYA", fs=20)
m.label(81.55, 27.0, "KOSALA", fs=20)
m.label(84.15, 27.15, "MALLA", fs=18)
m.label(85.5, 26.5, "VAJJI", fs=18)
m.label(85.75, 24.3, "MAGADHA", fs=20)
m.label(87.5, 25.2, "ANGA", fs=18)
m.label(82.75, 24.95, "KASHI", fs=18)
m.label(80.75, 25.55, "VATSA", fs=18)
m.label(79.9, 28.6, "PANCHALA", fs=18)
m.label(77.3, 29.4, "KURU", fs=18)
m.label(77.6, 26.4, "SURASENA", fs=18)
m.city(83.00, 25.32, "Varanasi", dx=-0.12, size=19)
m.city(84.99, 24.70, "Bodh Gaya", dx=-0.12, size=19)
m.label(82.4, 29.6, "H I M A L A Y A S", size="land", fs=20, rot=-20)
m.label(84.2, 25.75, "Ganges", size="sea", fs=19, rot=-5)
m.scale(200, lon=78.0, lat=23.75)
m.save("chapters/17-thinkers/images/map_ganges_states.png")
