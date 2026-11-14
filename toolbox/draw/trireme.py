import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The trireme","about 2,500 years ago")
WATER="#9fb8c8"
# oars first, so the hull sits over their inboard ends
for row,(y0,dx,dy,col) in enumerate(((396,-40,112,INK),(414,-34,96,INK),(432,-28,80,INK))):
    for i in range(22):
        x=300+i*29+row*9
        s.line(x,y0,x+dx,y0+dy,stroke=col,sw=1.6)
# hull, stern post at the left, beak at the right
s.raw_path("M 150,285 C 150,380 200,446 300,452 L 985,452 L 990,388 L 232,388 C 204,380 188,340 182,285 Z",fill=WOOD)
s.raw_path("M 985,452 L 1072,447 L 990,424 Z",fill=ACC,stroke=ACC,sw=2)
s.line(232,402,990,402,sw=1.5); s.circle(955,412,8,fill=PAPER,sw=2); s.circle(955,412,3,fill=INK,sw=0)
# mast, yard and furled sail
s.line(560,388,560,232,sw=4); s.line(470,246,650,246,sw=3)
s.raw_path("M 474,250 Q 560,268 646,250",fill=BONE,sw=2)
# water
s.raw_path("M 80,455 Q 110,447 140,455 T 200,455",stroke=WATER,sw=2.5)
s.line(1075,455,1130,455,stroke=WATER,sw=2.5)
# scale
s.line(150,575,1072,575,sw=2); s.line(150,566,150,584,sw=2); s.line(1072,566,1072,584,sw=2); s.text(611,606,"about 37 metres",anchor="middle",italic=True,size=19)
# cut across the hull
ix,iy,r=985,215,100
s.inset(ix,iy,r,caption="Cut across the hull")
s.raw_path(f"M {ix-62},{iy-40} C {ix-62},{iy+82} {ix+62},{iy+82} {ix+62},{iy-40}",fill=WOOD,sw=2.5)
s.line(ix-62,iy-40,ix-86,iy-40,sw=2.5); s.line(ix+62,iy-40,ix+86,iy-40,sw=2.5)
for (hx,hy,ox,oy) in ((ix-40,iy-48,ix-98,iy+8),(ix-30,iy-14,ix-90,iy+34),(ix-20,iy+18,ix-80,iy+58)):
    s.circle(hx,hy,7,fill=SOFT,stroke=SOFT,sw=1); s.line(hx-4,hy+8,ox,oy,stroke=ACC,sw=2.5)
s.callout(1,1046,446,1150,520,"A wooden beak|sheathed in bronze",anchor="end")
s.callout(2,480,500,330,660,"170 rowers, in three rows|on each side, one man|to an oar")
s.callout(3,ix-70,iy-34,760,130,"The top row's oars rest|on a frame built out|from the side",anchor="end")
s.callout(4,560,300,330,170,"A sail for travelling.|In battle it moves|by muscle alone",anchor="end")
s.callout(5,760,420,800,680,"A long, narrow hull|of light timber")
s.save(os.path.join(os.path.dirname(__file__),"..","18-trireme","trireme"))
