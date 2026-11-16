import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The microchip","A chip in its package, lid cut away, and one transistor enlarged, 1970s")
PKG="#2f3033"; PKG2="#45474b"; LEG="#c4c9cc"; DIE="#9aa3ab"; GOLD="#d4a63a"; SI="#c7ccd1"; DOPE="#8fb2c9"; OXIDE="#eef2f0"; METALC="#b9c0c4"

# ================= the package, seen from above, with the middle cut away =================
X0,X1,Y0,Y1=90,560,330,500
CXd,CYd=(X0+X1)/2,(Y0+Y1)/2
# legs, seven along each long side
pins=[X0+50+k*62 for k in range(7)]
for x in pins:
    s.path([(x-9,Y0-46),(x+9,Y0-46),(x+9,Y0),(x-9,Y0)],fill=LEG,close=True,sw=2)
    s.path([(x-9,Y1),(x+9,Y1),(x+9,Y1+46),(x-9,Y1+46)],fill=LEG,close=True,sw=2)
s.path([(X0,Y0),(X1,Y0),(X1,Y1),(X0,Y1)],fill=PKG,close=True,sw=3)
s.raw_path(f"M {X0},{CYd-16} A 16 16 0 0 1 {X0},{CYd+16}",fill=PKG2,sw=2)        # notch at one end
# the cut-away window: lead fingers running in to the chip
WX0,WX1,WY0,WY1=CXd-150,CXd+150,Y0+14,Y1-14
s.path([(WX0,WY0),(WX1,WY0),(WX1,WY1),(WX0,WY1)],fill="#e9e3d3",close=True,sw=2)
D=34
for i,x in enumerate(pins):
    if WX0+10<x<WX1-10:
        tx=CXd+(x-CXd)*0.45
        s.path([(x-7,WY0),(x+7,WY0),(tx+5,CYd-D-14),(tx-5,CYd-D-14)],fill=LEG,close=True,sw=1.2)
        s.path([(x-7,WY1),(x+7,WY1),(tx+5,CYd+D+14),(tx-5,CYd+D+14)],fill=LEG,close=True,sw=1.2)
# the chip itself, with a faint grid of circuits
s.path([(CXd-D,CYd-D),(CXd+D,CYd-D),(CXd+D,CYd+D),(CXd-D,CYd+D)],fill=DIE,close=True,sw=2)
for k in range(1,6):
    s.line(CXd-D+k*D/3,CYd-D+4,CXd-D+k*D/3,CYd+D-4,stroke="#6f7a83",sw=0.8)
    s.line(CXd-D+4,CYd-D+k*D/3,CXd+D-4,CYd-D+k*D/3,stroke="#6f7a83",sw=0.8)
# gold bond wires from the chip's edge pads to the fingers
for i,x in enumerate(pins):
    if WX0+10<x<WX1-10:
        tx=CXd+(x-CXd)*0.45; px=CXd+(x-CXd)*0.28
        s.raw_path(f"M {px},{CYd-D+5} Q {(px+tx)/2},{CYd-D-22} {tx},{CYd-D-12}",stroke=GOLD,sw=2)
        s.raw_path(f"M {px},{CYd+D-5} Q {(px+tx)/2},{CYd+D+22} {tx},{CYd+D+12}",stroke=GOLD,sw=2)
# the spot that is enlarged
s.path([(CXd+6,CYd-6),(CXd+18,CYd-6),(CXd+18,CYd+6),(CXd+6,CYd+6)],fill="none",stroke=ACC,sw=2)
s.text((X0+X1)/2+95,Y0-80,"the package, about 2 cm long",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= inset: one transistor, cut across =================
IX,IY,IR=930,410,200
s.line(CXd+18,CYd-6,IX-IR*0.92,IY-IR*0.4,stroke=SOFT,sw=1.2,dash="5 5")
s.line(CXd+18,CYd+6,IX-IR*0.92,IY+IR*0.4,stroke=SOFT,sw=1.2,dash="5 5")
s.inset(IX,IY,IR)
s.text(IX,IY+IR+40,"one transistor, cut across",anchor="middle",italic=True)
TOP=IY+10
# the silicon underneath
s.path([(IX-180,TOP),(IX+180,TOP),(IX+150,IY+150),(IX-150,IY+150)],fill=SI,close=True,sw=0)
s.line(IX-180,TOP,IX+180,TOP,stroke=INK,sw=2)
# source and drain: treated silicon on each side
for sx in (-1,1):
    x0=IX+sx*55; x1=IX+sx*150
    a,b=min(x0,x1),max(x0,x1)
    s.raw_path(f"M {a},{TOP} L {b},{TOP} L {b},{TOP+40} Q {(a+b)/2},{TOP+70} {a},{TOP+40} Z",fill=DOPE,sw=2)
# the channel between them, where the current flows when the switch is on
s.line(IX-52,TOP+10,IX+52,TOP+10,stroke=INK,sw=2,dash="6 5")
s.arrow(IX-40,TOP+26,IX+40,TOP+26)
# thin glassy oxide, then the gate on top of it
s.path([(IX-60,TOP-10),(IX+60,TOP-10),(IX+60,TOP),(IX-60,TOP)],fill=OXIDE,close=True,sw=1.5)
s.path([(IX-55,TOP-62),(IX+55,TOP-62),(IX+55,TOP-10),(IX-55,TOP-10)],fill=ACC,close=True,sw=2.5)
# metal contacts on source and drain
for sx in (-1,1):
    cx=IX+sx*105
    s.path([(cx-18,TOP-62),(cx+18,TOP-62),(cx+18,TOP),(cx-18,TOP)],fill=METALC,close=True,sw=2)
    s.line(cx,TOP-62,cx,TOP-100,stroke=INK,sw=3)
s.line(IX,TOP-62,IX,TOP-100,stroke=INK,sw=3)
s.text(IX-105,TOP+108,"source",anchor="middle",size=17,italic=True,fill=SOFT,halo=SI)
s.text(IX+105,TOP+108,"drain",anchor="middle",size=17,italic=True,fill=SOFT,halo=SI)

s.callout(1,IX,TOP-40,1150,170,"The gate: a small voltage|here turns the switch on",anchor="end")
s.callout(2,IX+30,TOP+26,1150,690,"Current then flows from|source to drain beneath it",anchor="end")
s.callout(3,CXd,CYd+D-8,430,690,"The chip: a square of silicon|a few millimetres across")
s.callout(4,CXd-60,CYd-D-14,180,170,"Gold wires finer than a hair|join the chip to the legs")
s.callout(5,pins[0],Y1+40,pins[0],640,"Legs carry signals|to the circuit board")
s.save(os.path.join(os.path.dirname(__file__),"..","107-microchip","microchip"))
