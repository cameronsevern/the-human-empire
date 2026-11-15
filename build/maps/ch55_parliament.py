#!/usr/bin/env python3
"""Chapter 55: the three kingdoms of England, Scotland and Ireland in the 1640s, with the places of the
story: London, Oxford (the king's base during the war), Naseby (June 1645), Edinburgh, Dublin and Drogheda
(1649), and Torbay, where William of Orange landed in 1688, with his crossing from Holland. The areas
held for the king and for Parliament at the end of 1642 are shaded roughly.

Drawn for this chapter, which had no map. The areas are rough and show only the parts that were firmly
held at the end of 1642, after the maps of the First English Civil War in English Wikipedia ("First
English Civil War") and in the Atlas of the English Civil War (P. R. Newman): Parliament's London, the
south-east and East Anglia; the king's Wales and the Marches, Cornwall, and the far north with York. The
Midlands, the West Country and much of Yorkshire were contested and are left unshaded; Scotland and
Ireland are not shaded. William's crossing is simplified, from Hellevoetsluis down the Channel to Torbay.
Positions from English Wikipedia.
"""
from lib import Map, INK, FILL

m = Map(-10.8, 5.2, 49.7, 58.9)
m.river("Thames", "Severn", "Shannon")

# end of 1642, roughly
m.region([(-1.9, 50.6), (0.5, 50.6), (1.6, 51.1), (1.9, 51.4), (1.9, 52.5), (1.8, 53.0), (0.3, 53.1), (-0.6, 52.6),
          (-0.9, 52.2), (-1.0, 51.9), (-0.8, 51.6), (-1.4, 51.4), (-1.9, 51.2)], "blue", alpha=0.45)
m.region([(-5.6, 51.6), (-3.2, 51.4), (-2.6, 51.6), (-2.3, 52.1), (-2.4, 52.9), (-2.9, 53.3), (-4.7, 53.5),
          (-4.9, 52.6)], "red", alpha=0.45)
m.region([(-5.9, 49.9), (-4.2, 50.25), (-4.25, 50.9), (-4.6, 51.0), (-5.9, 50.5)], "red", alpha=0.45)
m.region([(-3.6, 54.4), (-3.05, 54.98), (-2.6, 55.1), (-2.25, 55.33), (-2.1, 55.6), (-1.9, 55.75), (-1.5, 55.7), (-1.0, 54.8), (-0.4, 54.3), (-0.9, 53.85),
          (-2.0, 53.9), (-3.3, 54.0)], "red", alpha=0.45)

m.label(0.3, 52.2, "for\nParliament", size="small", colour=INK, fs=18, style="italic")
m.label(-3.75, 52.35, "for the\nking", size="small", colour=INK, fs=18, style="italic")
m.label(-2.05, 54.75, "for the\nking", size="small", colour=INK, fs=18, style="italic")
m.label(-5.6, 50.85, "for the king", size="small", colour=INK, fs=17, style="italic")

# William's crossing, 1688
m.route([(4.13, 51.82), (2.6, 51.3), (1.4, 50.9), (-0.5, 50.35), (-2.0, 50.2), (-3.35, 50.42)], colour=INK, lw=2.6,
        style=(0, (4, 2.5)))
m.label(1.5, 50.15, "William of Orange, 1688", size="small", colour=INK, fs=18)
m.label(3.5, 52.45, "HOLLAND", size="land", fs=17, style="normal")

m.city(-0.13, 51.51, "London", dx=0.22, dy=-0.2, bold=True)
m.city(-1.26, 51.75, "Oxford", dx=-0.25, dy=0.0)
m.city(-0.97, 52.42, "Naseby, 1645", dx=-0.25, dy=0.0, star=True, r=7)
m.city(-3.19, 55.95, "Edinburgh", dx=-0.3, dy=0.0, bold=True)
m.city(-6.26, 53.35, "Dublin", dx=-0.3, dy=0.0, bold=True)
m.city(-6.35, 53.72, "Drogheda, 1649", dx=-0.3, dy=0.0)
m.city(-3.53, 50.46, "Torbay", dx=0.22, dy=0.2)

m.label(-3.6, 57.3, "SCOTLAND", fs=23)
m.label(-1.1, 53.4, "ENGLAND", fs=23, ha="left")
m.label(-8.1, 52.9, "IRELAND", fs=23)
m.label(-4.6, 53.9, "Irish\nSea", size="sea", fs=19)
m.label(2.6, 55.0, "North Sea", size="sea", fs=22)
m.label(-9.4, 55.9, "Atlantic\nOcean", size="sea", fs=20)
m.scale(100, lon=3.3, lat=56.4)
m.save("chapters/55-parliament/images/map_three_kingdoms.png")
