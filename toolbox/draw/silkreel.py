import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The silk reel","about 2,000 years ago")
WATER="#c9d6dc"; LEAF="#b9c49a"
s.line(60,640,1140,640,stroke=SOFT,sw=1.5)
# stove: a small clay firebox with a fire inside
s.path([(190,640),(205,520),(455,520),(470,640)],fill=CLAY,sw=3,close=True)
s.raw_path("M 285,640 L 285,585 C 285,560 375,560 375,585 L 375,640 Z",fill=INK,sw=3)
for fx in (305,330,355):
    s.raw_path(f"M {fx-10},638 C {fx-14},615 {fx},610 {fx},592 C {fx+4},610 {fx+14},615 {fx+10},638 Z",fill="#e9a35c",sw=1.5)
# pan of hot water
s.path([(170,470),(490,470),(455,520),(205,520)],fill=METAL,sw=3,close=True)
s.ellipse(330,470,160,26,fill=WATER,sw=3)
# steam
for x in (215,440):
    s.raw_path(f"M {x},435 C {x-12},415 {x+12},400 {x},380",sw=1.5,stroke=SOFT)
# cocoons and filaments rising to the guide ring
ring=(330,250)
cocoons=[(240,468),(285,478),(330,464),(375,478),(420,468)]
for (x,y) in cocoons:
    s.line(x,y-8,ring[0],ring[1]+8,stroke=SOFT,sw=1.3)
for (x,y) in cocoons:
    s.ellipse(x,y,17,10,fill=BONE,sw=2.5,rot=-10)
# guide: a ring on an arm from a post beside the pan
s.line(120,640,120,235,sw=7,stroke=INK); s.line(120,640,120,235,sw=3,stroke=WOOD)
s.line(120,250,318,250,sw=7,stroke=INK); s.line(120,250,318,250,sw=3,stroke=WOOD)
s.circle(ring[0],ring[1],11,sw=4)
# the reel: a four-armed frame turning on an axle, held by two posts, with a crank
rx,ry,R=790,400,140
s.line(rx-40,640,rx,ry,sw=9,stroke=INK); s.line(rx-40,640,rx,ry,sw=5,stroke=WOOD)
s.line(rx+40,640,rx,ry,sw=9,stroke=INK); s.line(rx+40,640,rx,ry,sw=5,stroke=WOOD)
ends=[]
for i in range(4):
    a=math.pi/4+i*math.pi/2
    ex,ey=rx+R*math.cos(a),ry+R*math.sin(a); ends.append((ex,ey))
    s.line(rx,ry,ex,ey,stroke=ACC,sw=9)
# wound thread: a pale band round the four arm ends
for k in (0,7,14):
    pts=[(rx+(R-k)*math.cos(math.pi/4+i*math.pi/2),ry+(R-k)*math.sin(math.pi/4+i*math.pi/2)) for i in range(4)]
    s.path(pts,stroke=BONE,sw=6,close=True); s.path(pts,stroke=SOFT,sw=1.2,close=True)
for (ex,ey) in ends: s.circle(round(ex,1),round(ey,1),7,fill=ACC,sw=2)
s.circle(rx,ry,13,fill=WOOD,sw=3)
# crank handle
s.line(rx,ry,rx+62,ry,sw=5); s.line(rx+62,ry,rx+62,ry+34,sw=5)
# turning arrow
s.raw_path(f"M {rx+R+10},{ry-70} A 190 190 0 0 1 {rx+R+10},{ry+70}",sw=2.5)
s.line(rx+R+10,ry+70,rx+R+24,ry+52,sw=2.5); s.line(rx+R+10,ry+70,rx+R-8,ry+58,sw=2.5)
# the single thread from ring to the top of the reel
top=ends[3]  # upper left arm end is index 2? choose the upper-left one below
ul=min(ends,key=lambda p:p[0]+p[1])
s.line(ring[0]+10,ring[1]-3,ul[0],ul[1],sw=2.5,stroke=INK)
# corner: mulberry leaf with a silkworm
lx,ly=1010,150
s.raw_path(f"M {lx-70},{ly+20} C {lx-50},{ly-50} {lx+40},{ly-60} {lx+85},{ly-15} C {lx+50},{ly+45} {lx-30},{ly+55} {lx-70},{ly+20} Z",fill=LEAF,sw=2.5)
s.line(lx-70,ly+20,lx+80,ly-14,sw=1.5,stroke=SOFT)
for i in range(6):
    s.circle(lx-28+i*13,ly-2-i*2,8,fill=BONE,sw=2)
s.callout(1,455,485,540,686,"Hot water softens the gum|that holds a cocoon together")
s.callout(2,385,400,470,360,"A strand from|each cocoon,|too fine to|use alone")
s.callout(3,ring[0],ring[1]-11,300,160,"A ring gathers|the strands into|one thread",anchor="end")
s.callout(4,rx+R*math.cos(math.pi/4)-30,ry+R*math.sin(math.pi/4)-30,1130,560,"The turning frame|pulls the thread|and winds it up",anchor="end")
s.callout(5,lx+40,ly+10,1130,250,"A silkworm on|a mulberry leaf",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","22-silk-reel","silk-reel"))
