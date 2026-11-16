import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The company share","Amsterdam, 1602")
GOLD="#d9b65a"; CHEST="#b98a5a"; SAIL="#f1ece0"; HULL="#9c7048"; SEA="#c9d6d8"

def coin(x,y,r=9): s.ellipse(x,y,r,r*0.45,fill=GOLD,sw=1.6)
def stack(x,yb,n):
    for i in range(n): coin(x,yb-i*7,14)

# ---- many investors, large and small, each putting money in
INV=[(110,290,0.62),(185,370,0.72),(100,450,0.58),(185,535,0.8),(110,625,0.66)]
CHX,CHY=500,390
for (x,y,sc) in INV:
    s.person(x,y,lean=0.2,scale=sc,arm_to=(x+52*sc,y-60*sc))
    cx,cy=x+62*sc,y-58*sc
    coin(cx,cy,8)
    s.line(round(cx+14,1),round(cy,1),CHX-110,round(CHY+(cy-CHY)*0.25,1),stroke=SOFT,sw=1.8,dash="6 6")
s.arrow(CHX-130,CHY,CHX-96,CHY)

# ---- the company: one great chest, its money kept for good
s.path([(CHX-90,CHY-40),(CHX+90,CHY-40),(CHX+90,CHY+60),(CHX-90,CHY+60)],fill=CHEST,close=True,sw=3)
s.raw_path(f"M {CHX-90},{CHY-40} C {CHX-90},{CHY-100} {CHX+90},{CHY-100} {CHX+90},{CHY-40} Z",fill=CHEST,sw=3)
for dx in (-60,60): s.line(CHX+dx,CHY-82,CHX+dx,CHY+60,stroke=INK,sw=4)
s.path([(CHX-14,CHY-30),(CHX+14,CHY-30),(CHX+14,CHY+2),(CHX-14,CHY+2)],fill=METAL,close=True,sw=2)
s.circle(CHX,CHY-18,4,fill=INK,sw=0)

# ---- ships out to Asia and home again
def ship(x,y,d=1,cargo=False):
    s.path([(x-60*d,y),(x+70*d,y),(x+48*d,y+26),(x-46*d,y+26)],fill=HULL,close=True,sw=2.5)
    s.line(x,y,x,y-90,sw=3)
    s.path([(x-34,y-80),(x+34,y-80),(x+38,y-30),(x-38,y-30)],fill=SAIL,close=True,sw=2)
    s.path([(x+6*d,y-92),(x+30*d,y-86),(x+6*d,y-80)],fill=ACC if False else SOFT,close=True,sw=1.5)
    if cargo:
        for k in (-34,-12,10,32): s.ellipse(x+k,y-6,10,8,fill="#c9a46a",sw=1.5)
s.path([(640,282),(1150,282),(1150,300),(640,300)],fill=SEA,stroke="none",close=True,sw=0)
ship(820,270,1)
ship(1080,270,-1,cargo=True)
s.raw_path("M 880,200 C 930,160 990,160 1030,190",stroke=INK,sw=2,extra='stroke-dasharray="7 6"')
s.arrow(1012,178,1034,194)
s.raw_path("M 1040,330 C 990,365 920,365 870,330",stroke=INK,sw=2,extra='stroke-dasharray="7 6"')
s.arrow(890,346,868,330)
s.text(1130,180,"Asia",italic=True,fill=SOFT,anchor="middle")
s.arrow(CHX+100,CHY-50,730,300)          # money out to the ships
s.arrow(760,330,CHX+100,CHY+20)          # cargo sold, money back

# ---- profits, shared out in proportion to what each put in
PY=610
for (x,n) in ((420,8),(490,4),(560,2),(620,1)):
    stack(x,PY,n)
s.arrow(CHX,CHY+70,CHX,PY-80)
s.arrow(390,PY-30,250,PY-30)

# ---- a share sold: the seller hands over his share, the buyer pays him
SX,BX,FY=770,1030,690
s.person(SX,FY,lean=0.15,scale=0.95,arm_to=(SX+70,FY-110))
s.add(f'<g transform="translate({2*BX},0) scale(-1,1)">')
s.person(BX,FY,lean=0.15,scale=0.95,arm_to=(BX+70,FY-110))
s.add('</g>')
PX,PYc=900,585
s.add(f'<g transform="rotate(-8 {PX} {PYc})">')
s.path([(PX-44,PYc-56),(PX+44,PYc-56),(PX+44,PYc+56),(PX-44,PYc+56)],fill=ACC,close=True,sw=3)
for k in range(5): s.line(PX-30,PYc-34+k*15,PX+30,PYc-34+k*15,stroke="#f3d6c8",sw=2)
s.circle(PX+22,PYc+40,9,fill="#7a2f20",sw=1.5)
s.add('</g>')
s.arrow(PX+56,PYc-60,PX+116,PYc-64)
for k,(x,y) in enumerate(((890,672),(908,676),(926,672))): coin(x,y,9)
s.arrow(875,682,835,682)

x1,y1=110+62*0.62,290-58*0.62
s.callout(1,x1,y1,250,170,"Many investors, large|and small, pay in")
s.callout(2,CHX-30,CHY-70,470,225,"One company keeps|the money for good")
s.callout(3,1080,215,1150,375,"Ships sail out|to Asia and home",anchor="end")
s.callout(4,420,PY-50,300,690,"Profits shared out by|the size of each stake")
s.callout(5,PX-6,PYc-44,900,465,"A share sold on; the|company carries on")
s.save(os.path.join(os.path.dirname(__file__),"..","54-share","share"))
