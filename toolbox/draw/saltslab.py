import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The salt slab","the Sahara, by the 1000s")
CAMEL="#dcc39a"; FAR="#cdb38a"; CLAYR="#c98f6a"; SAND="#e8d3a8"; POOR="#d8d2c4"; SALT="#f1eee6"; ROPE="#8a6a48"
G=712
s.line(60,G,1140,G,stroke=SOFT,sw=1.5)
# ---- the mine: a pit cut down through clay and poor salt to the good salt
TOP=360
s.path([(60,TOP-6),(520,TOP-6),(520,TOP+70),(60,TOP+70)],fill=CLAYR,close=True,sw=2.5)    # clay and sand
s.path([(60,TOP+70),(520,TOP+70),(520,TOP+150),(60,TOP+150)],fill=POOR,close=True,sw=2.5)  # poor salt
for y in (TOP+96,TOP+124):
    s.line(64,y,516,y,stroke=SOFT,sw=1.2)
s.path([(60,TOP+150),(520,TOP+150),(520,G),(60,G)],fill=SALT,close=True,sw=2.5)           # good salt
for y in (TOP+210,TOP+270):
    s.line(64,y,516,y,stroke=SOFT,sw=1.6)
s.line(60,TOP-6,520,TOP-6,stroke=SAND,sw=8)
# the pit itself: a square hole, its floor on the top layer of good salt
PX0,PX1=190,400
s.path([(PX0,TOP-10),(PX1,TOP-10),(PX1,TOP+150),(PX0,TOP+150)],fill="#f7f2e6",close=True,sw=3)
# a slab being split off the floor of the pit, one end lifted
s.path([(PX0+20,TOP+150),(PX0+30,TOP+132),(PX1-20,TOP+108),(PX1-14,TOP+126),(PX1-14,TOP+150)],fill=ACC,close=True,sw=3)
s.path([(PX0+30,TOP+132),(PX1-20,TOP+108),(PX1-14,TOP+126),(PX0+20,TOP+150)],fill="#c86a52",close=True,sw=2)
# the miner's axe, resting at the pit edge
s.line(PX1+20,TOP-12,PX1+100,TOP-110,stroke=INK,sw=9); s.line(PX1+20,TOP-12,PX1+100,TOP-110,stroke=WOOD,sw=5)
s.path([(PX1+80,TOP-128),(PX1+112,TOP-140),(PX1+124,TOP-108),(PX1+100,TOP-100)],fill=METAL,close=True,sw=2.5)
# ---- the camel, from the camel saddle drawing, smaller, loaded with salt
s.add('<g transform="translate(467,270.6) scale(0.62)">')
def leg(xt,yt,xk,yk,xf,w=15):
    s.raw_path(f"M {xt-w-6},{yt} C {xt-w},{yt+60} {xk-w},{yk-40} {xk-w+2},{yk} L {xf-8},{G-8} L {xf+8},{G-8} "
               f"L {xk+w-2},{yk} C {xk+w},{yk-40} {xt+w},{yt+60} {xt+w+8},{yt} Z",fill=CAMEL,sw=2.5)
    s.ellipse(xk,yk,w+1,13,fill=CAMEL,sw=2)
    s.ellipse(xf+4,G-5,20,7,fill=CAMEL,sw=2)
for (xt,xk,xf) in ((350,336,342),(668,680,672)):
    s.raw_path(f"M {xt-12},470 L {xk-10},590 L {xf-7},{G-8} L {xf+7},{G-8} L {xk+10},590 L {xt+12},470 Z",fill=FAR,sw=2)
    s.ellipse(xk,590,12,11,fill=FAR,sw=2)
    s.ellipse(xf+4,G-5,18,6,fill=FAR,sw=2)
s.raw_path("M 318,318 C 350,270 390,250 428,250 C 470,250 515,290 545,332 C 580,348 620,350 650,356 "
           "C 720,370 770,330 800,280 C 815,250 840,236 870,240 C 900,244 918,256 912,270 "
           "C 905,280 880,280 868,284 C 850,300 835,340 800,400 C 770,445 720,470 680,478 "
           "C 600,496 420,500 340,478 C 270,470 230,430 232,390 C 235,350 280,330 318,318 Z",fill=CAMEL,sw=3)
s.circle(884,254,3.5,fill=INK,sw=0)
s.raw_path("M 858,244 C 860,232 868,230 874,236",sw=2)
s.raw_path("M 236,382 C 214,400 208,440 214,490",sw=3)
leg(306,462,296,590,300)
leg(626,470,640,590,632)
# pack pad over the hump, the far slab showing above it, the near slab on the flank
s.raw_path("M 330,300 C 370,236 480,236 530,310 L 520,330 C 470,270 380,270 340,322 Z",fill="#b98a5e",sw=2.5)
s.path([(300,284),(560,284),(560,300),(300,300)],fill="#c86a52",close=True,sw=2.5)
s.path([(290,300),(560,300),(560,380),(290,380)],fill=ACC,close=True,sw=3)
for x in (330,520):
    s.line(x,262,x,384,stroke=ROPE,sw=5)
s.line(425,384,425,480,stroke=ROPE,sw=4,dash="10 7")
s.add('</g>')
def T(x,y): return (round(467+0.62*x,1),round(270.6+0.62*y,1))
s.callout(1,90,TOP+30,110,200,"Clay and sand,|dug away first")
s.callout(2,470,TOP+110,560,300,"Poor salt,|cut through")
s.callout(3,PX0+80,TOP+134,250,660,"Good salt, split off|in slabs with an axe")
x4,y4=T(500,340); s.callout(4,x4,y4,1155,560,"A slab about a metre|long, one on each side",anchor="end")
x5,y5=T(330,262); s.callout(5,x5,y5,780,190,"Roped to a pad|over the hump")
s.save(os.path.join(os.path.dirname(__file__),"..","35-salt-slab","salt-slab"))
