import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The book with pages","about the year 200")
PAGE="#f3e8cf"; LEATHER="#9c6b45"
# --- the open book, at the left ---
SX=380   # spine
# leather cover behind the pages
s.raw_path(f"M {SX},{632} C {SX-90},{620} {SX-200},{640} {SX-290},{628} L {SX-290},{232} C {SX-200},{246} {SX-90},{226} {SX},{240} "
           f"C {SX+90},{226} {SX+200},{246} {SX+290},{232} L {SX+290},{628} C {SX+200},{640} {SX+90},{620} {SX},{632} Z",fill=LEATHER,sw=3)
# page edges (a few leaves showing)
for k in (3,2,1):
    d=k*5
    s.raw_path(f"M {SX},{612+d} C {SX-90},{598+d} {SX-190},{618+d} {SX-270+d},{606+d} L {SX-270+d},{250+d} C {SX-190},{262+d} {SX-90},{244+d} {SX},{256+d} Z",fill=PAGE,sw=1.5)
    s.raw_path(f"M {SX},{612+d} C {SX+90},{598+d} {SX+190},{618+d} {SX+270-d},{606+d} L {SX+270-d},{250+d} C {SX+190},{262+d} {SX+90},{244+d} {SX},{256+d} Z",fill=PAGE,sw=1.5)
s.raw_path(f"M {SX},{612} C {SX-90},{598} {SX-190},{618} {SX-270},{606} L {SX-270},{250} C {SX-190},{262} {SX-90},{244} {SX},{256} Z",fill=PAGE,sw=2.5)
s.raw_path(f"M {SX},{612} C {SX+90},{598} {SX+190},{618} {SX+270},{606} L {SX+270},{250} C {SX+190},{262} {SX+90},{244} {SX},{256} Z",fill=PAGE,sw=2.5)
# two columns of writing on each page
for side in (-1,1):
    for col in range(2):
        x0=SX+side*(32+col*118); x1=x0+side*100
        for i in range(16):
            y=290+i*19
            s.line(min(x0,x1),y,max(x0,x1)-(i*17%30),y,stroke=SOFT,sw=2.2)
# the thread, seen in the middle of the gathering
for i in range(5):
    y=290+i*78
    s.line(SX,y,SX,y+40,stroke=ACC,sw=4.5)
    s.circle(SX,y,3.5,fill=INK,sw=0); s.circle(SX,y+40,3.5,fill=INK,sw=0)
# --- a gathering seen from the end, at the right ---
GX,GY=980,470
for k in range(5):
    spread=140-k*16
    s.path([(GX-spread,GY-170+k*6),(GX,GY-k*12),(GX+spread,GY-170+k*6)],stroke=INK,sw=3)
# thread through the fold, round the spine
s.raw_path(f"M {GX},{GY-56} L {GX},{GY+6} C {GX},{GY+30} {GX-20},{GY+36} {GX-30},{GY+22}",stroke=ACC,sw=4.5)
s.raw_path(f"M {GX},{GY+6} C {GX},{GY+30} {GX+20},{GY+36} {GX+30},{GY+22}",stroke=ACC,sw=4.5)
s.text(GX,715,"A gathering, seen from the end",anchor="middle",italic=True)
s.callout(1,GX+105,GY-128,1150,150,"A sheet of papyrus or|parchment, folded in half",anchor="end")
s.callout(2,GX-110,GY-133,720,230,"Several sheets,|one inside another")
s.callout(3,GX,GY+30,GX,610,"Thread through|the fold holds|them together")
s.callout(4,SX-190,330,160,170,"Writing on both|sides of every leaf")
s.callout(5,SX-283,560,150,690,"A cover of wood or leather")
s.save(os.path.join(os.path.dirname(__file__),"..","25-codex","codex"))
