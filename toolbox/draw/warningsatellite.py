import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The early-warning satellite","A Soviet satellite of the 1980s, watching from high over the north (not to scale)")
SEA="#bcd3df"; LAND="#d8cfae"; SPACE="#2c3440"; BODY="#b9c0c4"; PANEL="#3b5272"; FLAME="#e8a23a"

EX,EY,ER=330,530,150
# ================= the satellite's orbit and position =================
SX,SY=840,215
dx,dy=SX-EX,SY-EY; dist=math.hypot(dx,dy); ux,uy=dx/dist,dy/dist
rp=ER+22; a=(dist+rp)/2; b=125
OX,OY=EX+(dist-a)*ux,EY+(dist-a)*uy
ang=math.degrees(math.atan2(dy,dx))
s.ellipse(round(OX,1),round(OY,1),round(a,1),b,stroke=SOFT,sw=2,rot=round(ang,1))
# ================= the Earth =================
EX,EY,ER=330,530,150
s.circle(EX,EY,ER,fill=SEA,sw=3)
for k in (-2,-1,0,1,2):                       # a few lines of latitude, for roundness
    y=EY+k*50; w=math.sqrt(ER*ER-(k*50)**2)
    s.ellipse(EX,y,round(w,1),round(w*0.18,1),stroke=SOFT,sw=1)

# the missile fields, just short of the edge of the Earth as the satellite sees it
th=math.atan2(dy,dx)-math.acos(ER/dist)
LX,LY=EX+ER*math.cos(th),EY+ER*math.sin(th)
FX,FY=EX+(ER-8)*math.cos(th+0.12),EY+(ER-8)*math.sin(th+0.12)
s.text(FX+60,FY+36,"missile fields",anchor="middle",italic=True,fill="#2f3f4c",size=16,halo=SEA)
for k in range(3):
    s.circle(round(FX+12+k*14,1),round(FY+8+k*3,1),3,fill=INK,sw=0)
# beyond the edge, the black of space behind the rocket
bx,by=LX+(LX-SX)*0.28,LY+(LY-SY)*0.28
s.ellipse(round(bx,1),round(by,1),70,34,fill=SPACE,sw=1.5,rot=round(ang,1))
# the rocket's flame rising
s.path([(FX,FY),(FX-6,FY-30),(FX-2,FY-56),(FX+4,FY-30)],fill=FLAME,close=True,sw=1.5)
s.path([(FX-2,FY-56),(FX+2,FY-56),(FX+2,FY-70),(FX-2,FY-70)],fill=INK,close=True,sw=1)
# the line of sight, grazing the edge
s.line(SX,SY,round(bx,1),round(by,1),stroke=INK,sw=1.6,dash="9 6")
# Moscow and the radio link
MX,MY=EX+ER*math.cos(math.radians(-10)),EY+ER*math.sin(math.radians(-10))
MX,MY=MX-6,MY
s.circle(round(MX,1),round(MY,1),6,fill=INK,sw=0)
s.text(MX-14,MY+6,"Moscow",anchor="end",italic=True,fill="#2f3f4c",size=16,halo=SEA)
for k in range(1,10):
    t0=(k-0.75)/9; t1=k/9
    s.line(round(SX+(MX-SX)*t0,1),round(SY+(MY-SY)*t0,1),round(SX+(MX-SX)*t1,1),round(SY+(MY-SY)*t1,1),stroke=ACC,sw=2.5)
# the satellite, small
s.path([(SX-14,SY-9),(SX+14,SY-9),(SX+14,SY+9),(SX-14,SY+9)],fill=BODY,close=True,sw=2)
for sx in (-1,1):
    s.path([(SX+sx*16,SY-5),(SX+sx*40,SY-5),(SX+sx*40,SY+5),(SX+sx*16,SY+5)],fill=PANEL,close=True,sw=1.5)

# ================= inset: the satellite =================
IX,IY,IR=1000,545,140
s.inset(IX,IY,IR)
s.text(IX,IY+IR+34,"the satellite, enlarged",anchor="middle",italic=True)
# body: a cylinder seen from the side
s.path([(IX-60,IY-40),(IX+70,IY-40),(IX+70,IY+40),(IX-60,IY+40)],fill=BODY,close=True,sw=2.5)
s.ellipse(IX+70,IY,12,40,fill="#a1a8ac",sw=2)
for k in range(1,4): s.line(IX-60+k*32,IY-40,IX-60+k*32,IY+40,stroke=INK,sw=1)
# solar panels above and below
for sy in (-1,1):
    y0=IY+sy*48; y1=IY+sy*118
    s.path([(IX-30,y0),(IX+40,y0),(IX+40,y1),(IX-30,y1)],fill=PANEL,close=True,sw=2)
    for k in range(1,4):
        yy=y0+(y1-y0)*k/4; s.line(IX-30,yy,IX+40,yy,stroke="#8fa3bf",sw=1)
    s.line(IX+5,IY+sy*40,IX+5,y0,stroke=INK,sw=2)
# the telescope, pointing back towards the Earth
s.path([(IX-130,IY-30),(IX-60,IY-24),(IX-60,IY+24),(IX-130,IY+30)],fill=ACC,close=True,sw=2.5)
s.ellipse(IX-130,IY,8,30,fill="#7a3324",sw=2)
# radio aerial
s.line(IX+82,IY,IX+112,IY-30,stroke=INK,sw=2.5)
s.raw_path(f"M {IX+100},{IY-48} Q {IX+124},{IY-42} {IX+124},{IY-18}",stroke=INK,sw=2.5)

vx,vy=-uy,ux
def orb(tt): return (round(OX+a*math.cos(tt)*ux+b*math.sin(tt)*vx,1),round(OY+a*math.cos(tt)*uy+b*math.sin(tt)*vy,1))
P1=min((orb(k/50*2*math.pi) for k in range(50)),key=lambda p:(p[0]-170)**2+(p[1]-610)**2)
s.callout(1,P1[0],P1[1],60,680,"A looping orbit,|twice a day")
s.callout(2,IX-122,IY+10,890,360,"A half-metre telescope|that sees in infrared")
s.callout(3,round(bx+(SX-bx)*0.04,1),round(by+(SY-by)*0.04,1),80,200,"It looks at the fields|edge-on, against space")
s.callout(4,FX-2,FY-50,395,200,"A rocket's hot flame")
s.callout(5,round(SX+(MX-SX)*0.5,1),round(SY+(MY-SY)*0.5,1),760,440,"Pictures sent|by radio",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","113-warning-satellite","warning-satellite"))
