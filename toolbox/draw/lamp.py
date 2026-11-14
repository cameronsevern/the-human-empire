import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The lamp","more than 20,000 years ago")
cx,cy=520,470
# stone slab with handle, seen at an angle
s.raw_path(f"M {cx-260},{cy} C {cx-260},{cy-70} {cx-120},{cy-110} {cx},{cy-110} C {cx+140},{cy-110} {cx+230},{cy-80} {cx+250},{cy-30} L {cx+420},{cy-20} L {cx+420},{cy+40} L {cx+250},{cy+50} C {cx+200},{cy+120} {cx+80},{cy+140} {cx},{cy+140} C {cx-140},{cy+140} {cx-260},{cy+80} {cx-260},{cy} Z",fill=STONE)
s.ellipse(cx-10,cy,170,70,fill="#f3e3a8")
s.raw_path(f"M {cx-60},{cy+10} C {cx-40},{cy-10} {cx-20},{cy-5} {cx},{cy-20}",stroke=ACC,sw=9)
s.raw_path(f"M {cx},{cy-22} C {cx-28},{cy-70} {cx+6},{cy-110} {cx+4},{cy-150} C {cx+34},{cy-110} {cx+30},{cy-60} {cx},{cy-22} Z",fill="#f1b24a",sw=2.5)
s.callout(1,cx-230,cy+40,120,640,"A hollow ground into|a slab of stone")
s.callout(2,cx+90,cy+20,560,660,"Animal fat. It melts|as the stone warms")
s.callout(3,cx-40,cy+2,330,250,"A wick of moss or|a juniper twig",anchor="end")
s.callout(4,cx+10,cy-110,640,200,"A steady flame, about|as bright as a candle")
s.callout(5,cx+380,cy+10,1080,560,"A handle that|stays cool",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","03-lamp","lamp"))
