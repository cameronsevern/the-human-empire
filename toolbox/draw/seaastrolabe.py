import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The sea astrolabe","Portugal, 1480s to the 1600s")
BRASS="#c9ad6a"; DARKB="#a88c4c"; SUN="#e9c25a"
cx,cy,RO,RI,SP=430,470,200,158,17
# ---- suspension: ring, swivel and lug
s.path([(cx-22,cy-RO+4),(cx-14,cy-RO-24),(cx+14,cy-RO-24),(cx+22,cy-RO+4)],fill=BRASS,close=True,sw=2.5)
s.path([(cx-9,cy-RO-24),(cx-9,cy-RO-56),(cx+9,cy-RO-56),(cx+9,cy-RO-24)],fill=DARKB,close=True,sw=2.5)
s.circle(cx,cy-RO-82,26,stroke=INK,sw=11); s.circle(cx,cy-RO-82,26,stroke=BRASS,sw=6)
# ---- the wheel: a heavy brass ring with a cross, cut open to let the wind through
s.circle(cx,cy,RO,fill=BRASS,sw=3)
def cut(sx,sy,y_lim=None):
    """open one quarter of the wheel between the spokes; lower quarters stop short to leave a weight."""
    xi=SP; yi=SP
    ye=math.sqrt(RI**2-xi**2); xe=math.sqrt(RI**2-yi**2)
    if y_lim is None:
        d=(f"M {cx+sx*xi},{cy+sy*yi} L {cx+sx*xi},{cy+sy*ye:.1f} "
           f"A {RI},{RI} 0 0 {1 if sx*sy<0 else 0} {cx+sx*xe:.1f},{cy+sy*yi} Z")
    else:
        xl=math.sqrt(RI**2-y_lim**2)
        d=(f"M {cx+sx*xi},{cy+yi} L {cx+sx*xi},{cy+y_lim} Q {cx+sx*(xi+xl)/2},{cy+y_lim+26} {cx+sx*xl:.1f},{cy+y_lim} "
           f"A {RI},{RI} 0 0 {0 if sx>0 else 1} {cx+sx*xe:.1f},{cy+yi} Z")
    s.raw_path(d,fill=PAPER,sw=2.5)
cut(-1,-1); cut(1,-1); cut(-1,1,98); cut(1,1,98)
# the scale: degrees round the upper half of the rim
for k in range(0,181,5):
    a=math.radians(180+k); L=16 if k%10==0 else 9
    x1,y1=cx+(RO-4)*math.cos(a),cy+(RO-4)*math.sin(a); x2,y2=cx+(RO-4-L)*math.cos(a),cy+(RO-4-L)*math.sin(a)
    s.line(round(x1,1),round(y1,1),round(x2,1),round(y2,1),stroke=INK,sw=1.6)
# ---- the pointer (alidade), turned towards the sun, with a vane and a hole at each end
A=math.radians(-58)                                  # direction up and to the right
ux,uy=math.cos(A),math.sin(A); px,py=-uy,ux
def P(t,n): return (round(cx+ux*t+px*n,1),round(cy+uy*t+py*n,1))
s.path([P(-185,-11),P(185,-11),P(185,11),P(-185,11)],fill=ACC,close=True,sw=2.5)
for t in (-120,120):
    s.path([P(t-5,-30),P(t+5,-30),P(t+5,30),P(t-5,30)],fill=ACC,close=True,sw=2.5)
    s.circle(*P(t,-18),3.5,fill=INK,sw=0)
s.circle(cx,cy,14,fill=DARKB,sw=2.5)
# ---- inset: sunlight through both holes
ix,iy,ir=930,440,170
s.inset(ix,iy,ir)
B=math.radians(-42); vx,vy=math.cos(B),math.sin(B); nx,ny=-vy,vx
def Q(t,n): return (round(ix+vx*t+nx*n,1),round(iy+vy*t+ny*n,1))
s.path([Q(-120,-12),Q(70,-12),Q(70,12),Q(-120,12)],fill=ACC,close=True,sw=2.5)
for t in (-100,50):
    s.path([Q(t-7,-48),Q(t+7,-48),Q(t+7,22),Q(t-7,22)],fill=ACC,close=True,sw=2.5)
    s.circle(*Q(t,-30),5,fill=PAPER,sw=1.5)
sx_,sy_=Q(130,-30)
s.circle(sx_,sy_,20,fill=SUN,sw=2.5)
for k in range(8):
    a=k*math.pi/4; s.line(round(sx_+27*math.cos(a),1),round(sy_+27*math.sin(a),1),round(sx_+36*math.cos(a),1),round(sy_+36*math.sin(a),1),stroke=INK,sw=2)
x0,y0=Q(108,-30); x1,y1=Q(-92,-30)
s.line(x0,y0,x1,y1,stroke=SUN,sw=4,dash="10 7")
s.circle(*Q(-93,-30),8,fill=SUN,sw=1.5)
# ---- labels
s.callout(1,cx-24,cy-RO-82,205,200,"A ring to|hang it from|the thumb",anchor="end")
s.callout(4,cx-140,cy-140,205,350,"The scale,|in degrees",anchor="end")
s.callout(3,*P(-150,0),205,600,"The pointer,|turned to|the sun",anchor="end")
s.callout(2,cx+70,cy+150,700,680,"Heavy at the bottom, and open|so the wind blows through")
x5,y5=Q(50,-30); s.callout(5,x5,y5,740,170,"Turned until the sun shines|through both holes")
s.save(os.path.join(os.path.dirname(__file__),"..","40-sea-astrolabe","sea-astrolabe"))
