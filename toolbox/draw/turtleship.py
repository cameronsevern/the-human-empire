import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The turtle ship","Korea, Yi Sun-sin's version of 1592")
HULL="#c9a676"; DECK="#b8925e"; ROOF="#9c7b57"; WATER="#b9cdd3"
WL=520; X0,X1=200,1030
RT,WT,WB=300,370,440          # roof top, wall top (roof eaves), wall bottom (gunwale)
# water
s.raw_path(f"M 40,{WL} "+" ".join(f"Q {x+20},{WL-8} {x+40},{WL} Q {x+60},{WL+8} {x+80},{WL}" for x in range(40,1160,80))+f" L 1160,610 L 40,610 Z",fill=WATER,stroke=SOFT,sw=2)
# the hull: heavy and flat-bottomed, with a raised stern
s.raw_path(f"M {X0},{WB} L {X1},{WB} C {X1+30},{WB-8} {X1+50},{WB-40} {X1+60},{WB-80} L {X1+78},{WB-74} "
           f"C {X1+74},{WB-20} {X1+50},{WL-10} {X1-20},{WL+30} L {X0+60},{WL+30} C {X0+20},{WL+20} {X0},{WL-20} {X0},{WB} Z",fill=HULL,sw=3)
for y in (WB+30,WB+60):
    s.line(X0+6,y,X1+20,y,stroke="#9b7c55",sw=1.6)
# oars, from ports along the hull down into the water
for k in range(10):
    x=300+k*76
    s.path([(x-5,WB+14),(x+5,WB+14),(x+5,WB+24),(x-5,WB+24)],fill=INK,close=True,sw=1)
    s.line(x,WB+19,x-50,WL+50,stroke=INK,sw=6); s.line(x,WB+19,x-50,WL+50,stroke=WOOD,sw=3)
    s.path([(x-50,WL+50),(x-62,WL+82),(x-46,WL+86),(x-40,WL+52)],fill=WOOD,close=True,sw=2)
# the gun deck wall, with ports
s.path([(X0,WT),(X1,WT),(X1,WB),(X0,WB)],fill=DECK,close=True,sw=3)
for k in range(11):
    s.circle(250+k*74,WT+36,12,fill="#3a3430",sw=2)
# the roof: an arch of planks, studded with iron spikes
s.raw_path(f"M {X0+4},{WT} C {X0+60},{RT-50} {X0+220},{RT-66} 615,{RT-68} C 810,{RT-66} {X1-60},{RT-50} {X1-4},{WT} Z",fill=ROOF,sw=3)
for y,x0,x1 in ((RT-24,330,900),(RT+10,250,980),(RT+44,215,1015)):
    s.line(x0,y,x1,y,stroke="#7a5a3c",sw=1.4)
for y,x0,x1 in ((RT-42,420,820),(RT-10,300,935),(RT+24,240,990),(RT+56,215,1012)):
    x=x0
    while x<x1:
        s.path([(x-5,y+3),(x,y-11),(x+5,y+3)],fill=ACC,close=True,sw=1.6)
        x+=30
# the dragon's head at the bow, a gun muzzle in its mouth
s.raw_path(f"M {X0+4},{WT+40} C {X0-10},{WT} {X0-20},{WT-40} {X0-40},{WT-62} C {X0-60},{WT-80} {X0-90},{WT-80} {X0-102},{WT-68} "
           f"L {X0-108},{WT-40} L {X0-80},{WT-30} L {X0-100},{WT-18} C {X0-80},{WT} {X0-50},{WT} {X0-32},{WT-12} C {X0-20},{WT+14} {X0-14},{WT+40} {X0-10},{WT+60} Z",fill=HULL,sw=3)
s.circle(X0-68,WT-62,5,fill=INK,sw=0)
s.path([(X0-116,WT-40),(X0-90,WT-42),(X0-90,WT-28),(X0-116,WT-26)],fill=METAL,close=True,sw=2.5)
s.ellipse(X0-116,WT-33,4,7,fill="#3a3430",sw=1.5)

s.callout(1,615,RT-10,700,170,"A roof of planks studded|with iron spikes")
s.callout(2,X0-112,WT-33,120,200,"A dragon's head, with|a gun in its mouth")
s.callout(3,766,WT+36,720,660,"Gun ports along|both sides",anchor="end")
s.callout(4,300-62,WL+84,170,660,"Oars, worked from|under the roof")
s.callout(5,1060,WB+30,1120,660,"A heavy hull with|a flat bottom",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","45-turtle-ship","turtle-ship"))
