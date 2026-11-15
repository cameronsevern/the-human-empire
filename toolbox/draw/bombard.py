import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The great bombard","Ottoman, cast in bronze, 1450s and 1460s")
BRONZE="#a8a074"; BAND="#958c60"; HOLE="#f4eee2"; DARK="#3b3631"
C=430                                   # the gun's centre line; 1 metre is about 185 px
XB,XJ,XS,XM=130,470,570,1090            # breech end, joint, end of the screw, muzzle
RO,RC,RS,RB,RP=96,92,74,58,24           # outer radius of barrel and chamber piece, screw, bore, powder chamber
# ---- the wooden bed it lies on
s.path([(110,C+RO+4),(1110,C+RO+4),(1100,C+RO+40),(120,C+RO+40)],fill=WOOD,close=True,sw=2.5)
for x in (240,520,820,1040):
    s.path([(x-40,C+RO+40),(x+40,C+RO+40),(x+34,C+RO+90),(x-34,C+RO+90)],fill=WOOD,close=True,sw=2.5)
s.line(80,C+RO+90,1140,C+RO+90,stroke=SOFT,sw=1.5)
# ---- the chamber piece, cut lengthwise
s.path([(XB,C-RC),(XJ,C-RC),(XJ,C-RS),(XS,C-RS),(XS,C+RS),(XJ,C+RS),(XJ,C+RC),(XB,C+RC)],fill=BRONZE,close=True,sw=3)
# ---- the barrel piece, cut lengthwise, its back end threaded round the chamber piece's screw
s.path([(XJ+4,C-RO),(XM,C-RO),(XM,C-RB),(XS,C-RB),(XS,C-RS),(XJ+4,C-RS)],fill=BRONZE,close=True,sw=3)
s.path([(XJ+4,C+RO),(XM,C+RO),(XM,C+RB),(XS,C+RB),(XS,C+RS),(XJ+4,C+RS)],fill=BRONZE,close=True,sw=3)
# the screw thread, a zigzag along the join above and below
for sg in (-1,1):
    pts=[(XJ+4,C+sg*RS)]
    x=XJ+4
    while x<XS-10:
        pts+= [(x+8,C+sg*(RS-9)),(x+16,C+sg*RS)]; x+=16
    pts.append((XS,C+sg*RS))
    s.path(pts,stroke=INK,sw=2.5)
# raised bands with sockets for levers at each end of each piece
def band(x0,x1,r):
    s.path([(x0,C-r-8),(x1,C-r-8),(x1,C-r),(x0,C-r)],fill=BAND,close=True,sw=2.5)
    s.path([(x0,C+r),(x1,C+r),(x1,C+r+8),(x0,C+r+8)],fill=BAND,close=True,sw=2.5)
    for xx in range(x0+8,x1-8,18):
        s.path([(xx,C-r-6),(xx+9,C-r-6),(xx+9,C-r+2),(xx,C-r+2)],fill=DARK,close=True,sw=1)
        s.path([(xx,C+r-2),(xx+9,C+r-2),(xx+9,C+r+6),(xx,C+r+6)],fill=DARK,close=True,sw=1)
band(XB,XB+56,RC); band(XJ-56,XJ,RC); band(XJ+4,XJ+60,RO); band(XM-60,XM,RO)
# mouldings along the barrel
for x in (700,830,960):
    s.line(x,C-RO,x,C-RB,stroke=SOFT,sw=2); s.line(x,C+RB,x,C+RO,stroke=SOFT,sw=2)
# ---- the bore and the powder chamber
s.path([(XS,C-RB),(XM,C-RB),(XM,C+RB),(XS,C+RB)],fill=HOLE,close=True,sw=2.5)
s.path([(XB+100,C-RP),(XS,C-RP),(XS,C+RP),(XB+100,C+RP)],fill=ACC,close=True,sw=2.5)
for x in range(XB+112,XS-6,22):                          # grains of powder
    s.circle(x,C-8,2.5,fill=DARK,sw=0); s.circle(x+11,C+9,2.5,fill=DARK,sw=0)
# the touch hole, from the top of the gun down into the powder
TX=XB+130
s.line(TX,C-RC,TX,C-RP,stroke=INK,sw=7); s.line(TX,C-RC,TX,C-RP,stroke=HOLE,sw=3)
# the wooden plug, then the stone ball
s.path([(XS+2,C-RB+2),(XS+26,C-RB+2),(XS+26,C+RB-2),(XS+2,C+RB-2)],fill=WOOD,close=True,sw=2.5)
s.circle(XS+26+RB,C,RB-2,fill=STONE,sw=3)
s.raw_path(f"M {XS+60},{C-30} C {XS+78},{C-38} {XS+96},{C-30} {XS+104},{C-14}",stroke=SOFT,sw=2)
# ---- labels
s.callout(1,900,C+28,720,660,"The barrel, wide enough|for a stone ball")
s.callout(2,380,C+12,230,660,"The chamber: narrow, with|thick walls, for the powder")
s.callout(3,XJ+40,C-RS+4,560,200,"A screw joins|the two halves")
s.callout(4,XM-30,C-RO-6,1120,200,"Sockets for the levers|that turned the screw",anchor="end")
s.callout(5,TX,C-RC-4,230,200,"The touch hole")
s.save(os.path.join(os.path.dirname(__file__),"..","42-great-bombard","great-bombard"))
