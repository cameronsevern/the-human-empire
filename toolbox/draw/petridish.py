import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The Petri dish","Robert Koch's laboratory, Berlin, 1887")
GLASS="#e6eef0"; AGARP="#f1dcb6"; LAMP="#b9a27a"; FLAME="#e0a030"; WIRE="#8f979b"

# ================= the dish cut in half, seen from the side =================
X0,X1=120,520; BOT=330; WALL=270
s.raw_path(f"M {X0-26},{WALL-28} L {X1+26},{WALL-28} L {X1+26},{WALL+10} L {X1+18},{WALL+10} L {X1+18},{WALL-20} "
           f"L {X0-18},{WALL-20} L {X0-18},{WALL+10} L {X0-26},{WALL+10} Z",fill=GLASS,sw=2.5)          # lid
s.path([(X0+8,BOT-30),(X1-8,BOT-30),(X1-8,BOT-6),(X0+8,BOT-6)],fill=ACC,close=True,sw=2)              # agar
s.raw_path(f"M {X0},{WALL} L {X0},{BOT} L {X1},{BOT} L {X1},{WALL} L {X1-8},{WALL} L {X1-8},{BOT-6} "
           f"L {X0+8},{BOT-6} L {X0+8},{WALL} Z",fill=GLASS,sw=2.5)                                    # dish
for x in (200,260,300,380,430):                                         # colonies on the surface
    s.raw_path(f"M {x-9},{BOT-30} Q {x},{BOT-44} {x+9},{BOT-30} Z",fill=BONE,sw=1.5)
s.text(280,BOT+40,"cut through, from the side",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the wire loop, flamed before and after use =================
LX,LY=360,520
s.path([(LX-32,660),(LX+32,660),(LX+24,612),(LX-24,612)],fill=LAMP,close=True,sw=2.5)               # spirit lamp
s.line(LX,612,LX,600,stroke=INK,sw=3)
s.raw_path(f"M {LX},{600} C {LX-22},{575} {LX-6},{535} {LX},{505} C {LX+6},{535} {LX+22},{575} {LX},{600} Z",fill=FLAME,sw=1.5)
s.line(150,600,300,545,stroke="#a87e55",sw=9)                                                          # handle
s.line(300,545,LX-12,LY+4,stroke=WIRE,sw=2.5)
s.circle(LX,LY,12,stroke=WIRE,sw=2.5)

# ================= the dish from above, a day or two later =================
CX,CY,R=900,450,200
s.circle(CX,CY,R+12,fill=GLASS,sw=2.5)
s.circle(CX,CY,R,fill=AGARP,sw=2)
# first streak: thick; second and third: thinner; colonies apart at the end
for k in range(7):
    s.line(CX-150+k*6,CY-90+k*10,CX-40+k*6,CY-140+k*10,stroke="#d2bd92",sw=7)
for k in range(6):
    s.line(CX-20+k*14,CY-110,CX+30+k*14,CY+10,stroke="#d2bd92",sw=4)
import random; random.seed(4)
spots=[]
for k in range(5):
    y=CY+40+k*26
    for j in range(5+k):
        x=CX+120-k*40-j*26+random.uniform(-6,6)
        if (x-CX)**2+(y-CY)**2<(R-22)**2:
            spots.append((round(x,1),round(y+random.uniform(-5,5),1)))
for (x,y) in spots:
    s.circle(x,y,random.choice((5,6,7)),fill="#fbf4e2",stroke="#8a7a5c",sw=2)
s.text(CX,CY+R+48,"from above, a day or two later",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,X1+10,WALL-28,560,180,"A glass lid, a little|wider than the dish")
s.callout(2,180,BOT-18,90,165,"Agar jelly, firm even|at body heat")
s.callout(3,X1-50,BOT,450,425,"A shallow glass dish")
s.callout(4,LX+12,LY,450,560,"A wire loop, flamed,|spreads the sample thin")
s.callout(5,spots[0][0],spots[0][1],1150,235,"Each spot grew|from one germ",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","67-petri-dish","petri-dish"))
