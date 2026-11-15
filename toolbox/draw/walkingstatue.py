import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The walking statue","Rapa Nui, in the centuries after about 1200")
TUFF="#b9ab98"; ROPE="#9b7653"; G=650
s.line(50,G,1150,G,stroke=SOFT,sw=1.5)
s.add(f'<path d="M 50,{G} L 1150,{G} L 1150,{G+60} L 50,{G+60} Z" fill="#efe3c8" stroke="none"/>')

K=0.82
def rot(pts,px,py,deg):
    a=math.radians(deg)
    return [(px+K*(x*math.cos(a)-y*math.sin(a)), py+K*(x*math.sin(a)+y*math.cos(a))) for x,y in pts]

# ---- side view: the statue faces right and leans forward, pivoting on the front of its base
SIDE=[(-78,0),(-70,-150),(-58,-270),(-52,-330),(-44,-400),(-30,-420),(36,-420),(52,-402),
      (60,-372),(78,-360),(70,-350),(92,-300),(88,-290),(70,-288),(76,-276),(66,-266),(74,-256),
      (84,-240),(62,-226),(58,-210),(66,-170),(80,-100),(86,-50),(84,-22),(70,-4),(52,0)]
PX,PY=420,G                                       # pivot: front of the base
LEAN=13
def side(pts): return rot([(x-60,y) for x,y in pts],PX,PY,LEAN)
s.path(side(SIDE),fill=TUFF,close=True,sw=3)
# the arm carved along the side, and the ear
s.path(side([(-20,-215),(10,-150),(20,-80),(56,-60)]),stroke=INK,sw=2)
s.path(side([(-6,-330),(8,-325),(10,-280),(-4,-270)]),stroke=INK,sw=2)
s.path(side([(76,-362),(60,-352)]),stroke=INK,sw=2)
# the rounded front edge of the base, in terracotta
s.path(side([(86,-50),(84,-22),(70,-4),(52,0)]),stroke=ACC,sw=9)
# rope from the head back to the team behind
hx,hy=side([(-50,-345)])[0]
fx,fy=side([(30,-345)])[0]
s.line(hx,hy,fx,fy,stroke=ROPE,sw=4)
hands=[]
for f in (110,170,230):
    h=(f+26,G-104); s.person(f,G,lean=-0.45,arm_to=h); hands.append(h)
s.path([(hx,hy)]+hands[::-1]+[(hands[0][0]-30,hands[0][1]+20)],stroke=ROPE,sw=3)

# ---- front view: the statue tipped onto its right corner
FRONT=[(-100,0),(-104,-40),(-96,-160),(-90,-230),(-78,-250),(-66,-262),(-68,-330),(-70,-395),
       (-56,-420),(56,-420),(70,-395),(68,-330),(66,-262),(78,-250),(90,-230),(96,-160),(104,-40),(100,0)]
CX=900; TILT=7
cpx,cpy=CX+100,G                                  # pivot: the right corner of the base
def front(pts): return rot([(x-100,y) for x,y in pts],cpx,cpy,TILT)
s.path(front(FRONT),fill=TUFF,close=True,sw=3)
for pts in ([(-40,-330),(-10,-338)],[(10,-338),(40,-330)],[(0,-338),(0,-292)],[(-14,-290),(14,-290)],
            [(-22,-272),(22,-272)],[(-60,-336),(-64,-290),(-56,-272)],[(60,-336),(64,-290),(56,-272)],
            [(-84,-210),(-60,-110),(-30,-80)],[(84,-210),(60,-110),(30,-80)]):
    s.path(front(pts),stroke=INK,sw=2)
# the right-hand corner it stands on, in terracotta; the left corner lifted clear of the road
s.path(front([(60,0),(96,-4),(104,-40)]),stroke=ACC,sw=9)
# side ropes from the head: right one taut, left one slack
lx,ly=front([(-69,-350)])[0]; rx,ry=front([(69,-350)])[0]
rh=[]
for f in (1040,1095):
    h=(f+30,G-104); s.person(f,G,lean=0.4,arm_to=h); rh.append(h)
s.path([(rx,ry)]+rh+[(rh[-1][0]+26,rh[-1][1]+22)],stroke=ROPE,sw=3)
s.path(front([(-69,-350),(0,-356),(69,-350)]),stroke=ROPE,sw=4)
for f in (600,645):
    s.person(f,G,lean=-0.05,arm_to=(f-4,G-100))
s.raw_path(f"M {lx:.0f},{ly:.0f} C {lx-40:.0f},{ly+140:.0f} 690,{G-120} 641,{G-100} L 596,{G-100} L 580,{G-70}",stroke=ROPE,sw=3)
# the lifted side swings forward
bl=front([(-100,0)])[0]
s.raw_path(f"M {bl[0]-6:.0f},{bl[1]+8:.0f} C {bl[0]-40:.0f},{bl[1]+30:.0f} {bl[0]-40:.0f},{bl[1]-40:.0f} {bl[0]-20:.0f},{bl[1]-56:.0f}",stroke=INK,sw=2.5)
s.arrow(bl[0]-28,bl[1]-46,bl[0]-14,bl[1]-62)

# ---- callouts
c1=side([(30,-418)])[0]; s.callout(1,round(c1[0]),round(c1[1]),530,190,"Leans forward by up|to about 15 degrees",anchor="end")
ry2=420; rx2=hx+(hands[-1][0]-hx)*(ry2-hy)/(hands[-1][1]-hy)
s.callout(2,round(rx2),ry2,330,300,"The team behind|keeps it from|falling on its face",anchor="end")
c3=((rx+rh[0][0])/2,(ry+rh[0][1])/2); s.callout(3,round(c3[0]),round(c3[1]),1130,190,"The teams at the|sides pull in turn",anchor="end")
c4=side([(80,-30)])[0]; s.callout(4,round(c4[0]),round(c4[1]),470,700,"A rounded front edge to rock on",halo="#efe3c8")
s.callout(5,round(bl[0]-30),round(bl[1]-24),820,330,"Each pull tips it onto|one corner, and the|other swings forward",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","34-walking-statue","walking-statue"))
