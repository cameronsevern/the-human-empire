import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The standard measure","about 2,370 years ago")
BRONZE="#a9a37f"; BRD="#8f8a68"; GRAIN="#e3c98a"
# the scoop: a shallow rectangular box seen from the front and a little above
# front face
fx1,fx2,fy1,fy2=330,760,440,540
dx,dy=70,-60    # depth offset
# handle (short, at the left end)
s.path([(fx1+dx/2-150,fy1+dy/2+22),(fx1+dx/2,fy1+dy/2+22),(fx1+dx/2,fy1+dy/2+62),(fx1+dx/2-150,fy1+dy/2+62)],fill=BRONZE,sw=3,close=True)
s.ellipse(fx1+dx/2-150,fy1+dy/2+42,9,20,fill=BRD,sw=3)
# left end face
s.path([(fx1,fy1),(fx1+dx,fy1+dy),(fx1+dx,fy2+dy),(fx1,fy2)],fill=BRD,sw=3,close=True)
# back rim and grain surface
s.path([(fx1,fy1),(fx1+dx,fy1+dy),(fx2+dx,fy1+dy),(fx2,fy1)],fill=GRAIN,sw=3,close=True)
# front face
s.path([(fx1,fy1),(fx2,fy1),(fx2,fy2),(fx1,fy2)],fill=BRONZE,sw=3,close=True)
# right end face
s.path([(fx2,fy1),(fx2+dx,fy1+dy),(fx2+dx,fy2+dy),(fx2,fy2)],fill=BRD,sw=3,close=True)
# grain: levelled on the left, still heaped on the right
s.raw_path(f"M 590,{fy1-2} C 620,{fy1-70} 700,{fy1-120} 790,{fy1-70} L {fx2+dx-4},{fy1+dy+4} L {fx2},{fy1-2} Z",fill=GRAIN,sw=3)
import random; random.seed(4)
for i in range(60):
    x=random.uniform(fx1+30,fx2+40); y=random.uniform(fy1+dy+10,fy1-8)
    if x-(y-fy1)*dx/dy*-1 < fx1: continue
    s.ellipse(round(x,1),round(y,1),4,2,stroke=SOFT,sw=1.2,rot=random.choice((20,-30,70)))
for i in range(22):
    x=random.uniform(640,780); y=random.uniform(fy1-80,fy1-20)
    s.ellipse(round(x,1),round(y,1),4,2,stroke=SOFT,sw=1.2,rot=random.choice((20,-30,70)))
# the levelling stick, lying across the rim, with an arrow showing its sweep
s.path([(548,fy1+22),(566,fy1+22),(566+dx+34,fy1+dy-34),(548+dx+34,fy1+dy-34)],fill=WOOD,sw=3,close=True)
s.arrow(500,345,585,345)
# inscription on the front face: generic marks in columns
for c in range(9):
    x=400+c*36
    for r in range(3):
        y=fy1+22+r*26
        k=(c+r)%3
        if k==0: s.line(x,y,x+14,y,stroke=ACC,sw=3); s.line(x+7,y-7,x+7,y+9,stroke=ACC,sw=3)
        elif k==1: s.line(x,y-6,x+14,y-6,stroke=ACC,sw=3); s.line(x,y+6,x+14,y+6,stroke=ACC,sw=3); s.line(x+3,y-6,x+3,y+6,stroke=ACC,sw=3)
        else: s.line(x,y+8,x+7,y-7,stroke=ACC,sw=3); s.line(x+7,y-7,x+14,y+8,stroke=ACC,sw=3)
# the weight: a low bronze dome with a loop on top
wx,wy=985,540
s.raw_path(f"M {wx-62},{wy} C {wx-62},{wy-70} {wx-36},{wy-104} {wx},{wy-104} C {wx+36},{wy-104} {wx+62},{wy-70} {wx+62},{wy} Z",fill=BRONZE,sw=3)
s.raw_path(f"M {wx-14},{wy-102} C {wx-14},{wy-130} {wx+14},{wy-130} {wx+14},{wy-102}",sw=6,stroke=INK)
s.raw_path(f"M {wx-14},{wy-102} C {wx-14},{wy-130} {wx+14},{wy-130} {wx+14},{wy-102}",sw=2,stroke=BRONZE)
for c in range(4):
    for r in range(3):
        x=wx-40+c*24; y=wy-66+r*20
        s.line(x,y,x+10,y,stroke=SOFT,sw=2); s.line(x+5,y-5,x+5,y+6,stroke=SOFT,sw=2)
# table line and scale bar
s.line(120,fy2+2,1100,fy2+2,stroke=SOFT,sw=1.5)
s.line(fx1,600,fx2,600,sw=2); s.line(fx1,592,fx1,608,sw=2); s.line(fx2,592,fx2,608,sw=2)
s.text((fx1+fx2)/2,632,"about 12 cm",anchor="middle",italic=True,size=19)
s.callout(1,fx2+dx/2,fy1+dy/2+60,790,690,"A bronze box, open at the top. Filled|to the brim it holds one measure",anchor="end")
s.callout(2,235,455,90,560,"A short handle|at one end")
s.callout(3,418,fy1+48,300,250,"The ruler's order and|the size of the box,|cut into the metal",anchor="end")
s.callout(4,600,405,470,200,"A straight stick sweeps|the grain level with the rim")
s.callout(5,wx+30,wy-40,1130,640,"A bronze weight|carries the same order",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","21-standard-measure","standard-measure"))
