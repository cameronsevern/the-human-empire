import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The spoked wheel","about 4,000 years ago")
cx,cy,R=560,440,215
s.circle(cx,cy,R,fill=WOOD,sw=3); s.circle(cx,cy,R-30,fill=PAPER,sw=3)
for i in range(10):
    a=i*math.pi/5+0.15
    s.line(cx+34*math.cos(a),cy+34*math.sin(a),cx+(R-30)*math.cos(a),cy+(R-30)*math.sin(a),stroke=ACC,sw=9)
s.circle(cx,cy,40,fill=WOOD,sw=3); s.circle(cx,cy,14,fill=PAPER,sw=3)
# rim join
s.line(cx+ (R-30)*math.cos(-1.2),cy+(R-30)*math.sin(-1.2),cx+R*math.cos(-1.15),cy+R*math.sin(-1.15),sw=3)
# inset: solid plank wheel for comparison
ix,iy=990,560
s.circle(ix,iy,95,fill=WOOD,sw=3); s.line(ix-30,iy-90,ix-30,iy+90,sw=2.5); s.line(ix+30,iy-90,ix+30,iy+90,sw=2.5)
s.line(ix-88,iy-35,ix+88,iy-35,sw=5); s.line(ix-88,iy+35,ix+88,iy+35,sw=5); s.circle(ix,iy,13,fill=PAPER,sw=3)
s.callout(1,cx+30,cy-25,830,150,"The hub: a block of wood|with a hole for the axle")
s.callout(2,cx-120,cy+40,60,560,"Ten or twelve thin spokes,|all the same length")
s.callout(3,cx-200,cy-70,60,200,"The rim: wood soaked or|steamed and bent|into a circle")
s.callout(4,cx+175,cy+60,830,250,"Each spoke sits in a socket|in the hub and another|in the rim")
s.callout(5,ix,iy-95,1130,400,"The solid wheel it replaced|weighs several times as much",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","10-spoked-wheel","spoked-wheel"))
