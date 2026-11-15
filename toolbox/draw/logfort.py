import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The log fort","Siberia, from the 1580s")
LOG="#c59a66"; LOGD="#a57c4c"; ROOFC="#8a6a48"; HUT="#d6b88c"; WATER="#b9cdd3"; GRASS="#d9d2b0"
OX,OY=280,520
def P(x,y,z=0): return (round(OX+x+0.55*y,1), round(OY-0.38*y-z,1))
# ground and river
s.path([P(-120,-40),P(560,-40),P(560,470),P(-120,470)],fill=GRASS,close=True,stroke=SOFT,sw=1.5)
s.raw_path("M 60,600 C 300,575 700,610 1140,580 L 1140,650 C 700,672 300,655 60,668 Z",fill=WATER,stroke=SOFT,sw=2)
# a flat-bottomed boat drawn up at the landing
s.path([(700,616),(840,612),(826,632),(716,636)],fill=WOOD,close=True,sw=2.5)
def wall(a,b,n,h=70,col=LOG,cut=None):
    (x0,y0),(x1,y1)=a,b
    for i in range(n):
        t0=i/n; t1=(i+1)/n
        if cut and cut[0]<=t0<cut[1]:
            hh=18      # a cut-away stump
        else: hh=h
        xa,ya=x0+(x1-x0)*t0,y0+(y1-y0)*t0; xb,yb=x0+(x1-x0)*t1,y0+(y1-y0)*t1
        xm,ym=(xa+xb)/2,(ya+yb)/2
        pts=[P(xa,ya,0),P(xa,ya,hh),P(xm,ym,hh+(14 if hh==h else 0)),P(xb,yb,hh),P(xb,yb,0)]
        s.path(pts,fill=col,close=True,sw=1.8)
def box(x,y,w,d,h,roofh,fill=HUT,roof=ROOFC):
    # front face, right face, gable roof running along x
    s.path([P(x,y),P(x+w,y),P(x+w,y,h),P(x,y,h)],fill=fill,close=True,sw=2.2)
    s.path([P(x+w,y),P(x+w,y+d),P(x+w,y+d,h),P(x+w,y,h)],fill="#c4a476",close=True,sw=2.2)
    s.path([P(x,y,h),P(x+w,y,h),P(x+w,y+d/2,h+roofh),P(x,y+d/2,h+roofh)],fill=roof,close=True,sw=2.2)
    s.path([P(x+w,y,h),P(x+w,y+d,h),P(x+w,y+d/2,h+roofh)],fill="#a5865e",close=True,sw=2.2)
# back and left walls
wall((0,380),(520,380),26,col="#9c4532")
wall((0,0),(0,380),19,col="#9c4532")
# inside, back to front: church, storehouse, hostages' hut
box(300,250,90,80,70,40,fill="#dcc29a")
cx,cy=P(345,290,110)
s.path([(cx-12,cy),(cx-12,cy-40),(cx+12,cy-40),(cx+12,cy)],fill="#dcc29a",close=True,sw=2)
s.raw_path(f"M {cx-14},{cy-40} C {cx-18},{cy-60} {cx},{cy-66} {cx},{cy-76} C {cx},{cy-66} {cx+18},{cy-60} {cx+14},{cy-40} Z",fill=METAL,sw=2)
s.line(cx,cy-76,cx,cy-92,sw=2); s.line(cx-6,cy-86,cx+6,cy-86,sw=2)
box(60,200,150,90,46,30)
for k in range(3):                                   # the storehouse's posts
    x0,y0=P(70+k*60,200); s.line(x0,y0,x0,y0+8,sw=3)
box(220,60,120,80,40,26)
dx,dy=P(270,60)
s.path([(dx,dy),(dx,dy-30),(dx+20,dy-30),(dx+20,dy)],fill="#6b5236",close=True,sw=2)      # the door
s.line(dx+2,dy-16,dx+18,dy-16,stroke=INK,sw=3)                                               # its bar
# right wall, then the front wall cut away in the middle
wall((520,0),(520,380),19,col="#a84a35")
wall((0,0),(520,0),26,col=ACC,cut=(0.2,0.8))
# the watchtower at the front left corner
T0,T1=-34,40
s.path([P(T0,T0),P(T1,T0),P(T1,T0,150),P(T0,T0,150)],fill=LOG,close=True,sw=2.5)
s.path([P(T1,T0),P(T1,T1),P(T1,T1,150),P(T1,T0,150)],fill=LOGD,close=True,sw=2.5)
for z in range(20,150,16):
    s.line(*P(T0,T0,z),*P(T1,T0,z),stroke="#8a6a48",sw=1.2)
s.path([P(T0-8,T0-8,150),P(T1+8,T0-8,150),P(T1+8,T1+8,150),P(3,3,215)],fill=ROOFC,close=True,sw=2.5)
s.path([P(T0-8,T0-8,150),P(T1+8,T0-8,150),P(3,3,215)],fill="#9c7b57",close=True,sw=2.5)
wx,wy=P(0,T0,118); s.path([(wx-10,wy),(wx+10,wy),(wx+10,wy+14),(wx-10,wy+14)],fill="#3a3430",close=True,sw=1.5)

s.callout(1,*P(480,0,40),1130,532,"Upright logs, sharpened,|four to six metres high",anchor="end")
s.callout(2,*P(3,3,190),130,190,"A watchtower|at the corner")
s.callout(3,*P(140,200,30),430,180,"The storehouse|for the furs")
s.callout(4,dx+10,dy-36,700,180,"The hostages' hut,|kept locked")
s.callout(5,760,624,560,700,"Boats on the river, the road east")
s.save(os.path.join(os.path.dirname(__file__),"..","50-log-fort","log-fort"))
