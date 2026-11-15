import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The three sisters","Mexico to the north-east woodlands")
SOIL="#b98f6a"; SOIL2="#a47b58"; MAIZE="#a9b56f"; LEAF="#8fa65e"; LEAF2="#7b9450"; SQ="#e3a64a"; COB="#efd37a"; TAS="#d9c28a"
GL=560                                              # ground level
# a cut through the ground under the mound
s.path([(300,GL),(760,GL),(760,712),(300,712)],fill=SOIL2,close=True,sw=2.5)
# the mound
s.raw_path(f"M 330,{GL} C 380,{GL-20} 420,{GL-88} 530,{GL-90} C 640,{GL-88} 680,{GL-20} 730,{GL} Z",fill=SOIL,sw=3)
s.line(60,GL,1140,GL,stroke=SOFT,sw=1.5)
# maize roots, fine and spreading
for a in (-60,-35,-12,12,35,60):
    r=math.radians(a); x2=530+150*math.sin(r); y2=GL-70+150*math.cos(r)
    s.raw_path(f"M 530,{GL-70} C {530+40*math.sin(r)},{GL-20} {x2-10*math.sin(r)},{y2-30} {x2:.0f},{min(y2,700):.0f}",stroke=INK,sw=1.5)
# bean roots, with the nodules on them
for (x0,dx) in ((560,1),(500,-1)):
    s.raw_path(f"M {x0},{GL-74} C {x0+dx*20},{GL-20} {x0+dx*40},{GL+40} {x0+dx*70},{GL+110}",stroke=INK,sw=2)
    for t in (0.35,0.55,0.75,0.92):
        x=x0+dx*70*t**1.2; y=GL-74+184*t
        s.circle(round(x+dx*6,1),round(y,1),5.5,fill=ACC,sw=1.5)
# maize: three stalks, leaves, a cob, tassels
for x,top in ((506,180),(530,160),(556,190)):
    s.line(x,GL-88,x+(x-530)*0.3,top,stroke=INK,sw=10); s.line(x,GL-88,x+(x-530)*0.3,top,stroke=MAIZE,sw=6)
    for k,y in enumerate(range(GL-130,top+40,-62)):
        d=1 if (k+x)%2 else -1
        s.raw_path(f"M {x},{y} C {x+d*40},{y-40} {x+d*90},{y-30} {x+d*120},{y+10} C {x+d*80},{y-14} {x+d*40},{y-12} {x},{y+8} Z",fill=MAIZE,sw=2)
    tx=x+(x-530)*0.3
    for d in (-14,0,14):
        s.line(tx,top,tx+d,top-34,stroke=TAS,sw=4)
s.raw_path("M 534,330 C 556,300 568,280 566,250 C 552,270 538,300 534,330 Z",fill=COB,sw=2)
s.raw_path("M 534,334 C 560,316 576,290 574,240 C 590,290 572,320 540,338 Z",fill=MAIZE,sw=2)
s.raw_path("M 566,250 C 570,236 580,228 590,226",stroke="#b0824a",sw=2)
# beans: a vine winding up the middle stalk, with leaves and pods
pts=[]
for i in range(0,61):
    y=GL-90-i*5.2; x=530+14*math.sin(i*0.55)
    pts.append((x,y))
s.path(pts,stroke=ACC,sw=3.5)
for i in (10,22,34,46,56):
    x,y=pts[i]; d=1 if i%4 else -1
    s.raw_path(f"M {x:.0f},{y:.0f} C {x+d*14:.0f},{y-18:.0f} {x+d*34:.0f},{y-12:.0f} {x+d*32:.0f},{y+6:.0f} C {x+d*22:.0f},{y+10:.0f} {x+d*10:.0f},{y+6:.0f} {x:.0f},{y:.0f} Z",fill=LEAF,sw=1.8)
for i in (16,40):
    x,y=pts[i]
    s.raw_path(f"M {x:.0f},{y:.0f} C {x-8:.0f},{y+20:.0f} {x-10:.0f},{y+40:.0f} {x-4:.0f},{y+52:.0f} C {x+2:.0f},{y+40:.0f} {x+4:.0f},{y+20:.0f} {x:.0f},{y:.0f} Z",fill=ACC,sw=1.8)
# squash: vines running off the mound across the ground, big leaves, a fruit
for d in (-1,1):
    s.raw_path(f"M {530+d*90},{GL-60} C {530+d*200},{GL-20} {530+d*320},{GL-6} {530+d*470},{GL-4}",stroke=LEAF2,sw=4)
    for xo in (190,300,410):
        x=530+d*xo; y=GL-26+ (6 if xo>250 else -6)
        s.raw_path(f"M {x-34},{y+10} C {x-40},{y-30} {x-10},{y-46} {x},{y-34} C {x+10},{y-46} {x+40},{y-30} {x+34},{y+10} C {x+10},{y+18} {x-10},{y+18} {x-34},{y+10} Z",fill=LEAF,sw=2)
        s.line(x,y+12,x,y-30,stroke=LEAF2,sw=1.5)
s.ellipse(800,GL-18,36,20,fill=SQ,sw=2.5)
s.callout(1,560,300,760,175,"Maize, the stalk|the beans climb")
s.callout(2,522,360,300,250,"Beans, twining up|the maize",anchor="end")
s.callout(3,601,587,820,620,"Swellings on the bean|roots hold bacteria that|take nitrogen from the air")
s.callout(4,940,GL-40,915,390,"Squash leaves|shade the soil|and smother weeds")
s.callout(5,390,GL-30,240,650,"A mound of earth|a foot high",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","39-three-sisters","three-sisters"))
