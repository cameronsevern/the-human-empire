import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The tractor","The Fordson, 1917, and its Soviet copies")
GREY="#7d8285"; DARK="#4b4f52"; IRON="#5e6366"; WATER="#b9c0c4"; GROUND=600

s.line(60,GROUND,1150,GROUND,stroke=SOFT,sw=1.5)

# ================= the body: engine, gearbox and back axle bolted into one =================
s.path([(300,372),(560,372),(560,470),(300,470)],fill=ACC,close=True,sw=3)            # engine block
s.path([(560,400),(700,410),(720,470),(700,500),(560,486)],fill=ACC,close=True,sw=3)  # gearbox housing
for x in (560,):
    s.line(x,372,x,486,stroke=INK,sw=2)
for y in (390,430,460):
    s.circle(560,y,3,fill=INK,sw=0)                                                   # bolts at the joint
s.path([(300,470),(560,470),(560,486),(320,490)],fill="#8e3b28",close=True,sw=2)       # sump
# radiator at the front
s.path([(250,330),(300,330),(300,485),(250,485)],fill=WATER,close=True,sw=3)
for y in range(345,480,12): s.line(256,y,294,y,stroke="#8f979b",sw=1.5)
# fuel tank on top
s.raw_path("M 300,330 L 560,330 Q 572,350 560,372 L 300,372 Z",fill=GREY,sw=3)
s.circle(470,322,7,fill=DARK,sw=1.5)
# steering column and wheel, seat
s.line(330,372,700,282,stroke=DARK,sw=6)
s.ellipse(705,278,34,9,fill="none",stroke=DARK,sw=5,rot=-20)
s.path([(640,440),(770,330)],stroke=DARK,sw=6)                                       # seat spring
s.raw_path("M 750,312 Q 790,300 812,326 L 760,334 Z",fill=DARK,sw=2)

# ================= the wheels =================
def wheel(cx,cy,r,lugs):
    s.circle(cx,cy,r,fill="none",stroke=IRON,sw=10)
    for k in range(10 if lugs else 8):
        a=2*math.pi*k/(10 if lugs else 8)
        s.line(cx,cy,round(cx+(r-6)*math.cos(a),1),round(cy+(r-6)*math.sin(a),1),stroke=IRON,sw=4)
    s.circle(cx,cy,r*0.22,fill=DARK,sw=2)
    if lugs:
        n=22
        for k in range(n):
            a=2*math.pi*k/n
            x1,y1=cx+(r+2)*math.cos(a),cy+(r+2)*math.sin(a)
            x2,y2=cx+(r+16)*math.cos(a+0.06),cy+(r+16)*math.sin(a+0.06)
            s.line(round(x1,1),round(y1,1),round(x2,1),round(y2,1),stroke=IRON,sw=6)
wheel(330,513,87,False)
wheel(720,470-0+0,114,True)
# drawbar and hook at the back
s.path([(760,520),(870,526)],stroke=DARK,sw=9)
s.circle(878,527,10,stroke=DARK,sw=5)

s.callout(1,520,354,560,180,"A 20-horsepower engine|that burns cheap paraffin")
s.callout(2,470,440,520,680,"No frame: engine, gearbox and|axle bolted into one body",anchor="end")
s.callout(3,813,548,1010,680,"Steel wheels with lugs|that grip the soil",anchor="end")
s.callout(4,885,527,960,430,"A hook that|pulls the plough")
s.callout(5,262,380,130,250,"Water in the radiator|cools the engine")
s.save(os.path.join(os.path.dirname(__file__),"..","78-tractor","tractor"))
