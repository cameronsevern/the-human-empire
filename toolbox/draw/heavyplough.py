import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The heavy plough","northern Europe, in wide use after about 800")
SOIL="#cdb48e"; DARK="#a8865c"; GRASS="#7d8f5a"; G=560
# soil in section: unbroken ground ahead, turned ridges behind
s.add(f'<path d="M 60,{G} L 1140,{G} L 1140,660 L 60,660 Z" fill="{SOIL}" stroke="none"/>')
s.line(640,G,1140,G,stroke=INK,sw=2.5)
for x in range(650,1140,22): s.line(x,G,x+4,G-9,stroke=GRASS,sw=2)
d=f"M 60,{G} "
for k in range(8):
    x=60+k*48; d+=f"C {x+4},{G-26} {x+40},{G-30} {x+48},{G-2} "
s.raw_path(d+f"L 440,{G} Z",fill=DARK,sw=2.5)
# the furrow bottom left behind the plough
s.line(60,616,440,616,stroke=INK,sw=1.5,dash="6 6")
# the slab rising over the board and curling back
s.raw_path("M 600,606 C 560,580 520,548 470,532 C 440,524 420,530 430,548 L 470,560 C 510,572 560,590 590,612 Z",fill=DARK,sw=2)
# the standard (upright) joining beam to sole, behind the board
s.line(560,450,560,612,stroke=INK,sw=11); s.line(560,450,560,612,stroke=WOOD,sw=7)
# sole and handles
s.line(430,616,600,616,stroke=INK,sw=11); s.line(430,616,600,616,stroke=WOOD,sw=7)
s.line(212,402,440,612,stroke=INK,sw=11); s.line(212,402,440,612,stroke=WOOD,sw=7)
# the curved board
s.raw_path("M 604,602 C 580,575 540,548 488,536 C 462,532 446,536 448,552 C 500,560 552,584 586,616 Z",fill=ACC,sw=2.5)
# the share: an iron point at the front of the sole
s.path([(590,604),(686,620),(590,628)],fill=METAL,close=True,sw=2.5)
# the beam, from the handles to the wheels
s.line(330,446,860,470,stroke=INK,sw=15); s.line(330,446,860,470,stroke=WOOD,sw=10)
s.line(330,446,300,430,stroke=INK,sw=6)
# the knife (coulter) through the beam, raking forward
s.path([(672,402),(686,402),(706,600),(696,604)],fill=METAL,close=True,sw=2.5)
s.line(668,446,692,446,stroke=INK,sw=3)
# fore-carriage: two wheels on an axle (the far wheel just showing)
s.circle(856,500,56,fill="none",stroke=SOFT,sw=4)
s.circle(840,505,55,fill="none",stroke=INK,sw=5)
for a in range(0,360,45):
    r=math.radians(a); s.line(840,505,round(840+52*math.cos(r),1),round(505+52*math.sin(r),1),stroke=INK,sw=3)
s.circle(840,505,9,fill=WOOD,sw=2.5)
s.line(840,468,840,500,stroke=INK,sw=5)
# draught chain to the oxen, off to the right
s.path([(850,505),(900,512),(1000,524),(1140,536)],stroke=SOFT,sw=3,extra='stroke-dasharray="10 5"')
s.text(1130,580,"to the oxen",anchor="end",italic=True,fill=SOFT,halo=SOIL)
# the ploughman
s.person(170,G,lean=0.35,arm_to=(212,404))

# inset: the cut seen from behind
CX,CY,RR=1030,330,112
s.inset(CX,CY,RR)
S=CY+10
s.add(f'<path d="M {CX-110},{S} L {CX-20},{S} L {CX-20},{S+40} L {CX+40},{S+40} L {CX+40},{S+38} L {CX+110},{S+38} L {CX+90},{CY+80} L {CX-90},{CY+80} Z" fill="{SOIL}" stroke="none"/>')
s.path([(CX-110,S),(CX-20,S),(CX-20,S+40),(CX+110,S+40)],stroke=INK,sw=2.5)
for x in range(CX-104,CX-24,14): s.line(x,S,x+3,S-8,stroke=GRASS,sw=2)
def slab(cx,cy,ang,w=50,h=36):
    a=math.radians(ang)
    loc=[(-w/2,h/2),(w/2,h/2),(w/2,-h/2),(-w/2,-h/2)]          # grass on the top face
    P=[(cx+x*math.cos(a)-y*math.sin(a), cy+x*math.sin(a)+y*math.cos(a)) for x,y in loc]
    s.path(P,fill=DARK,close=True,sw=2.5)
    (x0,y0),(x1,y1)=P[3],P[2]; nx,ny=(P[3][0]-P[0][0])/h,(P[3][1]-P[0][1])/h
    for t in (0.2,0.5,0.8):
        x=x0+(x1-x0)*t; y=y0+(y1-y0)*t
        s.line(round(x,1),round(y,1),round(x+nx*7,1),round(y+ny*7,1),stroke=GRASS,sw=2)
    return P
slab(CX+104,S+22,176); slab(CX+66,S+20,170)
mid=slab(CX+18,S+4,68)
s.raw_path(f"M {CX-22},{S+40} C {CX-18},{S+22} {CX-14},{S+8} {CX-6},{S-8}",stroke=ACC,sw=7)   # the board
s.raw_path(f"M {CX+6},{S-46} C {CX+26},{S-62} {CX+48},{S-58} {CX+62},{S-40}",stroke=INK,sw=2.5)
s.arrow(CX+52,S-52,CX+64,S-36)
s.text(CX,CY-RR-18,"From behind",anchor="middle",italic=True)

s.callout(1,880,540,1150,700,"Wheels carry the front|and set the depth",anchor="end")
s.callout(2,690,520,600,190,"An iron knife slices|the turf upright")
s.callout(3,650,618,620,700,"An iron share cuts|underneath")
s.callout(4,520,548,300,190,"A curved board turns|the slab over")
s.callout(5,CX+100,S+24,1150,468,"Upside down,|weeds buried",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","36-heavy-plough","heavy-plough"))
