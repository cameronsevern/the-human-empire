import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The air pump","Boyle and Hooke, Oxford, 1659")
GLASS="#e3eef0"; BRASS="#d4b25a"; IRONC="#8e959a"; FRAME="#c9a676"
CX=600
# the wooden frame: two posts, a top board, and a middle board (the "midriff")
for x in (430,770):
    s.path([(x-14,350),(x+14,350),(x+14,715),(x-14,715)],fill=FRAME,close=True,sw=2.5)
s.path([(400,340),(800,340),(800,362),(400,362)],fill=FRAME,close=True,sw=2.5)
s.path([(416,478),(784,478),(784,496),(416,496)],fill=FRAME,close=True,sw=2.5)
s.line(380,715,820,715,stroke=SOFT,sw=1.5)
# the receiver: a glass globe with a neck, a brass cover on the wide hole at the top
GY,GR=210,118
s.raw_path(f"M {CX-18},{GY+GR-6} C {CX-80},{GY+GR-20} {CX-GR},{GY+60} {CX-GR},{GY} C {CX-GR},{GY-70} {CX-60},{GY-GR+4} {CX-40},{GY-GR+10} "
           f"L {CX+40},{GY-GR+10} C {CX+60},{GY-GR+4} {CX+GR},{GY-70} {CX+GR},{GY} C {CX+GR},{GY+60} {CX+80},{GY+GR-20} {CX+18},{GY+GR-6} "
           f"L {CX+14},{332} L {CX-14},{332} Z",fill=GLASS,sw=3)
s.path([(CX-50,GY-GR+12),(CX+50,GY-GR+12),(CX+46,GY-GR-6),(CX-46,GY-GR-6)],fill=BRASS,close=True,sw=2.5)
s.path([(CX-9,GY-GR-6),(CX+9,GY-GR-6),(CX+6,GY-GR-26),(CX-6,GY-GR-26)],fill=BRASS,close=True,sw=2)
s.ellipse(CX,GY-GR-30,12,6,fill=BRASS,sw=2)
s.raw_path(f"M {CX-60},{GY-40} C {CX-70},{GY-10} {CX-66},{GY+20} {CX-50},{GY+40}",stroke="#ffffff",sw=5)  # glint
# the stopcock under the neck, with its key
s.path([(CX-16,330),(CX+16,330),(CX+16,376),(CX-16,376)],fill=BRASS,close=True,sw=2.5)
s.path([(CX+16,346),(CX+70,342),(CX+70,360),(CX+16,358)],fill=BRASS,close=True,sw=2.5)
s.ellipse(CX+74,351,8,14,fill=BRASS,sw=2)
# the brass cylinder, cut open to show the sucker inside
CT,CB,CW=378,620,40
s.path([(CX-CW-10,CT),(CX+CW+10,CT),(CX+CW+10,CB),(CX-CW-10,CB)],fill=BRASS,close=True,sw=3)
s.path([(CX-CW,CT+14),(CX+CW,CT+14),(CX+CW,CB),(CX-CW,CB)],fill="#f4ecd4",close=True,sw=2)
# the valve: a tapering brass peg in a hole at the top of the cylinder
s.path([(CX+CW+10,CT+4),(CX+CW+40,CT-2),(CX+CW+40,CT+12),(CX+CW+10,CT+12)],fill=BRASS,close=True,sw=2)
s.ellipse(CX+CW+44,CT+5,6,10,fill=BRASS,sw=2)
# the sucker, in terracotta, and its toothed iron rack
SY=520
s.path([(CX-CW,SY),(CX+CW,SY),(CX+CW,SY+34),(CX-CW,SY+34)],fill=ACC,close=True,sw=2.5)
s.path([(CX-10,SY+34),(CX+10,SY+34),(CX+10,700),(CX-10,700)],fill=IRONC,close=True,sw=2.5)
for y in range(SY+60,700,14):
    s.path([(CX+10,y),(CX+18,y+5),(CX+10,y+10)],fill=IRONC,close=True,sw=1.4)
# the pinion that drives it, and the handle
PX,PY=CX+44,650
s.circle(PX,PY,24,fill=IRONC,sw=2.5)
for a in range(0,360,30):
    x=PX+28*math.cos(math.radians(a)); y=PY+28*math.sin(math.radians(a))
    s.circle(round(x,1),round(y,1),4,fill=IRONC,sw=1.2)
s.line(PX,PY,PX+150,PY,stroke=INK,sw=9); s.line(PX,PY,PX+150,PY,stroke=WOOD,sw=5)
s.line(PX+150,PY,PX+150,PY-50,stroke=INK,sw=10); s.line(PX+150,PY,PX+150,PY-50,stroke=WOOD,sw=6)
s.circle(PX,PY,6,fill=INK,sw=0)

s.callout(1,CX-80,GY-40,300,190,"A glass globe of about|thirty quarts, with a|brass cover on top",anchor="end")
s.callout(2,CX+74,351,900,290,"A stopcock between|globe and pump")
s.callout(3,CX-CW-10,450,300,420,"A brass cylinder,|about 36 cm long",anchor="end")
s.callout(4,CX-CW+8,SY+18,300,560,"The sucker, a piston|drawn down by a|toothed rack and handle",anchor="end")
s.callout(5,CX+CW+44,CT+5,900,420,"The valve: a brass peg,|pulled out to let|the air go")
s.save(os.path.join(os.path.dirname(__file__),"..","51-air-pump","air-pump"))
