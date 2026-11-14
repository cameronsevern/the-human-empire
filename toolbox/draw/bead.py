import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The bead","more than 140,000 years ago")
def shell(x,y,k=1.0,hole=False,fill=BONE,rot=0):
    s.add(f'<g transform="rotate({rot} {x} {y})">')
    s.raw_path(f"M {x},{y-52*k} C {x+44*k},{y-40*k} {x+48*k},{y+30*k} {x},{y+56*k} C {x-48*k},{y+30*k} {x-44*k},{y-40*k} {x},{y-52*k} Z",fill=fill,sw=2.5)
    s.raw_path(f"M {x-4*k},{y-40*k} C {x+14*k},{y-20*k} {x+14*k},{y+20*k} {x-2*k},{y+44*k}",sw=1.5)
    if hole: s.circle(x-16*k,y-8*k,8*k,fill=PAPER,sw=2)
    s.add('</g>')
shell(200,400)                                        # 1 a small sea shell
shell(470,400)                                        # 2 being pierced
s.line(560,300,462,388,sw=6); s.path([(468,380),(450,398),(460,402)],fill=STONE,close=True)
shell(740,400,hole=True)                              # 3 pierced
s.arrow(280,400,380,400); s.arrow(560,400,650,400)
# 4 a string of them
s.raw_path("M 150,640 Q 560,560 1010,640",sw=3,stroke=ACC)
for i in range(11):
    t=i/10; x=190+t*790; y=640-4*80*t*(1-t)
    shell(x,y+20,0.42,hole=True,rot=(i%3)*12-12)
s.callout(1,200,350,150,200,"A small sea shell,|picked for its size")
s.callout(2,520,336,560,200,"A hole is made with|a point of bone or stone")
s.callout(3,724,392,1100,250,"The hole is made in the|same way, shell after shell",anchor="end")
s.callout(4,390,612,330,520,"Strung on a cord and worn",anchor="end")
s.callout(5,826,634,1050,520,"The cord rubs the edge of the|hole smooth: proof it was worn",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","03-bead","bead"))
