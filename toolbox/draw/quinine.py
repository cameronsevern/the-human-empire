import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("Quinine","From the bark of the cinchona tree; drawn out in Paris, 1820")
BARK="#9a6b48"; INNER="#c98a5a"; LEAF="#8fa070"; GLASS="#e6eef0"; MORTAR="#cdc6ba"; CELL="#efc6bc"; CELLRIM="#c98f84"; PARA="#6b4a7a"

# ================= the tree: a trunk with a strip of bark peeled away =================
s.path([(105,560),(175,560),(170,250),(110,250)],fill=BARK,close=True,sw=3)
s.path([(140,330),(168,330),(168,440),(140,440)],fill=INNER,close=True,sw=2)            # bare wood where the strip came off
s.raw_path("M 168,330 C 200,330 222,350 222,380 C 222,410 205,430 190,440 L 176,436 C 192,422 204,404 204,382 C 204,356 188,344 168,344 Z",fill=BARK,sw=2)   # the strip
for (x1,y1,x2,y2) in ((140,250,90,190),(140,250,150,170),(160,250,220,195)):
    s.line(x1,y1,x2,y2,stroke=BARK,sw=8)
for (x,y,r) in ((80,180,-30),(95,205,20),(150,160,0),(130,185,-50),(225,185,30),(210,210,-20),(240,205,60)):
    s.ellipse(x,y,22,10,fill=LEAF,sw=2,rot=r)
s.line(60,560,260,560,stroke=SOFT,sw=1.5)
s.text(140,600,"the tree",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= ground bark in a mortar =================
MX,MY=400,470
s.raw_path(f"M {MX-70},{MY-30} L {MX+70},{MY-30} C {MX+70},{MY+40} {MX+40},{MY+60} {MX},{MY+60} C {MX-40},{MY+60} {MX-70},{MY+40} {MX-70},{MY-30} Z",fill=MORTAR,sw=3)
s.raw_path(f"M {MX-58},{MY-30} Q {MX},{MY-52} {MX+58},{MY-30} Z",fill=INNER,sw=1.5)     # the powder
s.line(MX+20,MY-40,MX+75,MY-130,stroke="#a87e55",sw=12)                                  # pestle
s.path([(MX-30,MY+60),(MX+30,MY+60),(MX+36,MY+74),(MX-36,MY+74)],fill=MORTAR,close=True,sw=2.5)
s.text(MX,600,"ground bark",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= quinine: white crystals in a jar, then a daily dose =================
JX,JY=590,470
s.path([(JX-45,JY-70),(JX+45,JY-70),(JX+45,JY+70),(JX-45,JY+70)],fill=GLASS,close=True,sw=2.5)
s.path([(JX-35,JY-90),(JX+35,JY-90),(JX+35,JY-70),(JX-35,JY-70)],fill="#a87e55",close=True,sw=2.5)
s.raw_path(f"M {JX-43},{JY+68} L {JX-43},{JY+20} L {JX-28},{JY+6} L {JX-12},{JY+18} L {JX+4},{JY} L {JX+20},{JY+14} L {JX+43},{JY+4} L {JX+43},{JY+68} Z",fill=ACC,sw=2)
s.text(JX,600,"quinine",anchor="middle",italic=True,fill=SOFT,size=18)
PX,PY=760,490
s.path([(PX-24,PY-50),(PX+24,PY-50),(PX+20,PY+50),(PX-20,PY+50)],fill=GLASS,close=True,sw=2.5)   # a glass of water
s.path([(PX-22,PY-20),(PX+22,PY-20),(PX+20,PY+48),(PX-20,PY+48)],fill="#d8e6ea",close=True,sw=0,stroke="none")
s.ellipse(PX-62,PY+38,16,10,fill=ACC,sw=2)                                              # the pill
s.text(PX+5,600,"every day",anchor="middle",italic=True,fill=SOFT,size=18)
for (x1,x2) in ((240,315),(485,532),(648,688)):
    s.arrow(x1,400,x2,400)

# ================= in the blood, much magnified =================
CX,CY,R=990,450,150
s.circle(CX,CY,R,fill="#fbeeea",sw=2.5)
cells=((930,390),(1050,380),(1000,480),(910,500),(1070,500),(990,560))
for (x,y) in cells:
    s.circle(x,y,38,fill=CELL,stroke=CELLRIM,sw=2.5)
    s.circle(x,y,16,fill="#f6dcd6",stroke="none",sw=0)
for (x,y) in ((1000,480),(1050,380)):                                                    # parasites inside cells
    s.circle(x+10,y-8,10,stroke=PARA,sw=3); s.circle(x+16,y-14,3,fill=PARA,sw=0)
for (x,y) in ((985,468),(1020,500),(1036,370),(1068,392),(1012,458),(1060,366)):
    s.circle(x,y,3.5,fill=ACC,sw=0)                                                     # quinine reaching them
s.text(CX,CY+R+38,"blood, magnified",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,212,385,330,190,"Bark of the cinchona,|a tree of the Andes")
s.callout(2,MX-30,MY-36,300,680,"Ground, it was sold as|Jesuits' bark from the 1600s")
s.callout(3,JX,JY+30,520,265,"Quinine, drawn out|of the bark in 1820")
s.callout(4,PX-62,PY+38,700,680,"A small dose every|day, before any fever")
s.callout(5,1010,474,1150,215,"In the blood, it kills the|parasite inside red cells",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","69-quinine","quinine"))
