import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The vanishing point","Florence, worked out by about 1415, written down in 1435")
TILE_A="#e6d6b8"; TILE_B="#b9a585"; WALL="#ffffff"

# ---- left: the scene from the side
GY=600; EX,EY=108,474; PX=230
s.line(60,GY,520,GY,stroke=SOFT,sw=1.5)
for k in range(5):                                       # tiles on the floor, equal steps
    x0=260+k*60
    s.path([(x0,GY),(x0+60,GY),(x0+60,GY+10),(x0,GY+10)],fill=TILE_A if k%2 else TILE_B,close=True,sw=1.5)
s.person(100,GY,lean=0.0,scale=0.78)
s.circle(EX,EY,4,fill=INK,sw=0)
# the picture, upright like a window between the eye and the floor
s.path([(PX-6,370),(PX+6,370),(PX+6,GY),(PX-6,GY)],fill=WALL,close=True,sw=2.5)
s.line(EX,EY,520,EY,stroke=SOFT,sw=1.5,dash="6 6")          # eye level
ticks=[]
for k in range(6):
    x=260+k*60; y=EY+(GY-EY)*(PX-EX)/(x-EX)
    s.line(EX,EY,x,GY,stroke=SOFT,sw=1.2)
    s.line(PX-10,round(y,1),PX+10,round(y,1),stroke=INK,sw=2.5); ticks.append(y)

# ---- right: the picture itself
L,R,T,B=590,1110,260,640; H=400; VX=850
s.path([(L,T),(R,T),(R,B),(L,B)],fill=WALL,close=True,sw=3)
D=2.6
rows=[H+(B-H)*D/(D+d) for d in range(0,9)]
STEP=(R-L-40)/8
xs=[L+20+k*STEP for k in range(-40,49)]
def px(x0,y): return VX+(x0-VX)*(y-H)/(B-H)
s.add(f'<clipPath id="pic"><rect x="{L}" y="{T}" width="{R-L}" height="{B-T}"/></clipPath>')
s.add('<g clip-path="url(#pic)">')
for j in range(len(rows)-1):
    for i in range(len(xs)-1):
        y0,y1=rows[j],rows[j+1]
        q=[(px(xs[i],y0),y0),(px(xs[i+1],y0),y0),(px(xs[i+1],y1),y1),(px(xs[i],y1),y1)]
        s.path(q,fill=TILE_A if (i+j)%2 else TILE_B,close=True,sw=1)
# a back wall standing on the last row of tiles, with a doorway
yb=rows[-1]
s.path([(L,T),(R,T),(R,yb),(L,yb)],fill="#efe7d6",close=True,sw=1.5)
s.path([(VX-30,yb),(VX-30,yb-70),(VX+30,yb-70),(VX+30,yb)],fill="#d9cdb6",close=True,sw=2)
# the horizon at eye height, and the lines running to the vanishing point
s.line(L,H,R,H,stroke=SOFT,sw=1.5,dash="6 6")
for k,x0 in enumerate(xs):
    s.line(round(x0,1),B,round(px(x0,yb),1),round(yb,1),stroke=ACC,sw=2.4)
    if 38<=k<=50: s.line(round(px(x0,yb),1),round(yb,1),VX,H,stroke=ACC,sw=1.6,dash="5 5")
s.add('</g>')
s.circle(VX,H,8,fill=ACC,sw=2)
s.path([(L,T),(R,T),(R,B),(L,B)],fill="none",close=True,sw=3)

s.callout(1,EX,EY,70,250,"The eye, held|still at one point")
s.callout(2,PX,410,330,250,"The picture is|a window",)
s.callout(3,L+40,H,620,180,"The horizon, at the|height of the eye")
s.callout(4,VX+6,H-6,900,180,"The vanishing point,|where the edges meet")
s.callout(5,PX,round(ticks[3]),300,690,"Equal steps on the floor|come closer in the picture")
s.save(os.path.join(os.path.dirname(__file__),"..","43-perspective","perspective"))
