import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The hearth","about 400,000 years ago")
cx,cy=560,470
s.ellipse(cx,cy,300,95,fill="#efe3c8",stroke=SOFT,sw=1.5)                      # the circle of light
s.ellipse(cx,cy+8,120,40,fill="#5a4a40",sw=2.5)                                 # ash and embers
for i in range(10):                                                              # ring of stones
    a=i*math.pi/5; s.ellipse(cx+138*math.cos(a),cy+8+46*math.sin(a),30,20,fill=STONE,sw=2.5,rot=(i*37)%40-20)
for (x1,y1,x2,y2) in ((cx-95,cy+15,cx+60,cy-30),(cx+95,cy+18,cx-55,cy-28),(cx-20,cy+30,cx+10,cy-40)):
    s.line(x1,y1,x2,y2,stroke=INK,sw=17); s.line(x1,y1,x2,y2,stroke="#8a6a48",sw=12)
s.raw_path(f"M {cx-50},{cy-20} C {cx-70},{cy-110} {cx-10},{cy-120} {cx-20},{cy-200} C {cx+40},{cy-150} {cx+20},{cy-110} {cx+60},{cy-150} C {cx+80},{cy-90} {cx+70},{cy-50} {cx+50},{cy-20} Z",fill=ACC,sw=2.5)
s.raw_path(f"M {cx-22},{cy-22} C {cx-30},{cy-70} {cx+5},{cy-80} {cx},{cy-125} C {cx+30},{cy-90} {cx+25},{cy-50} {cx+24},{cy-22} Z",fill="#e9b24a",sw=1.5)
for (ex,ey) in ((cx-40,cy+22),(cx+10,cy+30),(cx+50,cy+20)): s.circle(ex,ey,6,fill=ACC,sw=0)
# meat on a stick, leaning over the stones
s.line(cx+250,cy+40,cx+95,cy-95,sw=4); s.ellipse(cx+112,cy-80,26,14,fill="#b98a6a",sw=2.5,rot=-40)
s.callout(1,cx-10,cy-110,330,200,"Fire, carried home|and kept alive",anchor="end")
s.callout(2,cx+138,cy+8,930,330,"A ring of stones|keeps it in one place")
s.callout(3,cx-70,cy+5,250,400,"Dry wood, fed in|a little at a time",anchor="end")
s.callout(4,cx+112,cy-80,880,180,"Cooked food gives more|from every mouthful")
s.callout(5,cx+240,cy+70,720,660,"A circle of warmth and light,|where people sit after dark")
s.save(os.path.join(os.path.dirname(__file__),"..","01-hearth","hearth"))
