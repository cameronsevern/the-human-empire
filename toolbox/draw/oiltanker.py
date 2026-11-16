import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The oil tanker","A supertanker of the 1970s, cut away along its length")
HULL="#4b4f52"; RED2="#8f3a2a"; WHITE="#ece8dc"; SEA="#a9c3cc"; STEEL="#9aa1a5"; OIL=ACC

DECK,KEEL,WL=420,520,490          # deck, keel, and the waterline when loaded
XS,XB=110,1110                    # stern and bow
# ================= the sea =================
s.path([(60,WL),(1150,WL),(1150,KEEL+28),(60,KEEL+28)],fill=SEA,close=True,sw=0,extra='opacity="0.55"')
# ================= the hull =================
hull=[(XS,DECK-6),(XB-30,DECK),(XB,DECK-14),(XB+6,DECK-14),(XB-8,WL-6),(XB-30,KEEL-4),(XS+112,KEEL),(XS+96,KEEL-58),(XS+22,KEEL-58),(XS,DECK+30)]
s.path(hull,fill=HULL,close=True,sw=3)
# the bulb under the bow
s.path([(XB-40,KEEL-20),(XB-6,KEEL-34),(XB+20,KEEL-24),(XB+10,KEEL-8),(XB-34,KEEL-6)],fill=HULL,close=True,sw=2.5)
# the cut-away: cargo tanks, a pump room and the engine room
TX0,TX1=330,1020
nt=6; tw=(TX1-TX0)/nt
for k in range(nt):
    x0=TX0+k*tw+5; x1=TX0+(k+1)*tw-5
    s.path([(x0,DECK+8),(x1,DECK+8),(x1,KEEL-10),(x0,KEEL-10)],fill="#2f2e2c",close=True,sw=1.5)
    s.path([(x0+3,DECK+22),(x1-3,DECK+22),(x1-3,KEEL-13),(x0+3,KEEL-13)],fill=OIL,close=True,sw=1)   # oil, with a gap of air above
s.path([(276,DECK+8),(322,DECK+8),(322,KEEL-10),(276,KEEL-10)],fill=STEEL,close=True,sw=1.5)          # pump room
s.circle(299,KEEL-34,10,fill=HULL,sw=1.5)
s.path([(146,DECK+8),(268,DECK+8),(268,KEEL-66),(146,KEEL-66)],fill="#d8d4c8",close=True,sw=1.5)  # engine room
s.path([(166,DECK+20),(250,DECK+20),(250,KEEL-72),(166,KEEL-72)],fill=STEEL,close=True,sw=1.5)
s.line(146,KEEL-72,120,KEEL-30,stroke=STEEL,sw=0)
# ================= the propeller and rudder =================
s.path([(XS+26,KEEL-58),(XS+42,KEEL-58),(XS+42,KEEL-2),(XS+26,KEEL-2)],fill=HULL,close=True,sw=2)          # rudder
s.ellipse(XS+72,KEEL-28,8,26,fill="#b8963e",sw=2)            # propeller seen edge on
# ================= the deck: a long pipe, the loading point midships =================
s.line(XS+130,DECK-8,XB-60,DECK-8,stroke=STEEL,sw=5)
s.line(XS+130,DECK-16,XB-60,DECK-16,stroke=STEEL,sw=3)
for x in range(420,1020,115): s.line(x,DECK-16,x,DECK,stroke=STEEL,sw=3)
s.path([(600,DECK-36),(640,DECK-36),(640,DECK-8),(600,DECK-8)],fill=STEEL,close=True,sw=2)
for x in (606,620,634): s.line(x,DECK-36,x,DECK-48,stroke=INK,sw=3)
s.line(XB-80,DECK-4,XB-80,DECK-40,stroke=INK,sw=2)            # foremast
# ================= the stern block: cabins, bridge and funnel =================
s.path([(140,DECK-6),(240,DECK-6),(240,DECK-110),(140,DECK-110)],fill=WHITE,close=True,sw=2.5)
s.path([(130,DECK-110),(252,DECK-110),(252,DECK-124),(130,DECK-124)],fill=WHITE,close=True,sw=2.5)   # bridge
for y in range(DECK-96,DECK-10,20):
    for x in range(152,236,18): s.path([(x,y),(x+10,y),(x+10,y+8),(x,y+8)],fill="#5b6870",close=True,sw=1)
s.path([(108,DECK-6),(136,DECK-6),(136,DECK-140),(114,DECK-140)],fill=WHITE,close=True,sw=2.5)        # funnel
s.path([(112,DECK-140),(136,DECK-140),(136,DECK-122),(113,DECK-122)],fill=HULL,close=True,sw=2)
# length line
s.line(XS,KEEL+60,XB+6,KEEL+60,stroke=SOFT,sw=1.5)
for x in (XS,XB+6): s.line(x,KEEL+50,x,KEEL+70,stroke=SOFT,sw=1.5)
s.text(640,KEEL+94,"about 330 metres",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,880,470,880,250,"Walls divide the oil|into many separate tanks")
s.callout(2,620,DECK-40,500,300,"Hoses join the deck pipes|here, midway along")
s.callout(3,190,DECK-120,110,190,"Bridge, cabins and|engine at the stern")
s.callout(4,XB+8,KEEL-24,1140,690,"A bulb under the bow|eases it through the water",anchor="end")
s.callout(5,XS+72,KEEL-28,110,690,"One great propeller")
s.save(os.path.join(os.path.dirname(__file__),"..","97-oil-tanker","oil-tanker"))
