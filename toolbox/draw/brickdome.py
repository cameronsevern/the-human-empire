import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The brick dome","Florence, 1420 to 1436")
BRICK="#d7a17e"; TILE="#c4704f"; MARBLE="#ece6da"
CXD=430; YS=620; HALF=200; R=320; OFF=R-HALF            # a pointed dome: two arcs of radius R
def arc(Rr,side,n=40):
    """Points on one side of the pointed profile with radius Rr, springing to apex."""
    cx=CXD-side*OFF                                       # centre of the left side's arc lies right of the axis
    top=math.sqrt(Rr*Rr-OFF*OFF)
    out=[]
    for i in range(n+1):
        y=YS-top*i/n
        x=cx+side*math.sqrt(max(Rr*Rr-(YS-y)**2,0))
        out.append((x,y))
    return out
def xat(Rr,side,y): return CXD-side*OFF+side*math.sqrt(Rr*Rr-(YS-y)**2)
R0,R1,R2,R3=R,R+26,R+56,R+68                          # inner shell R0-R1, gap R1-R2, outer shell R2-R3
# the drum below
for side in (-1,1):
    x0=xat(R0,side,YS); x3=xat(R3,side,YS)
    s.path([(x3,YS),(x0,YS),(x0,700),(x3,700)],fill=STONE,close=True,sw=3)
    s.circle(round((x0+x3)/2,1),660,10,fill="#ffffff",sw=2)
s.line(80,700,780,700,stroke=SOFT,sw=1.5)
for side in (-1,1):
    # outer shell, tiled
    s.path(arc(R3,side)+arc(R2,side)[::-1],fill=TILE,close=True,sw=3)
    # inner shell, brick
    s.path(arc(R1,side)+arc(R0,side)[::-1],fill=BRICK,close=True,sw=3)
    # courses of brick in the inner shell, laid at right angles to the curve
    for i in range(2,40,3):
        a=arc(R0,side)[i]; b=arc(R1,side)[i]
        s.line(round(a[0],1),round(a[1],1),round(b[0],1),round(b[1],1),stroke="#a8765a",sw=1.2)
# a stair climbing between the shells, on the left
st=[]
for i in range(3,34,2):
    p=arc((R1+R2)/2,-1)[i]; q=arc((R1+R2)/2,-1)[i+2]
    st+= [(p[0]-3,p[1]+5),(q[0]-3,p[1]+5)]
s.path(st,stroke=INK,sw=2)
# the lantern on top
ay=YS-math.sqrt(R3*R3-OFF*OFF)
s.path([(CXD-26,ay+8),(CXD-26,ay-50),(CXD+26,ay-50),(CXD+26,ay+8)],fill=MARBLE,close=True,sw=2.5)
for dx in (-12,0,12): s.line(CXD+dx,ay-42,CXD+dx,ay-4,stroke=INK,sw=1.5)
s.path([(CXD-30,ay-50),(CXD,ay-96),(CXD+30,ay-50)],fill=MARBLE,close=True,sw=2.5)
s.circle(CXD,ay-104,8,fill="#d4b25a",sw=2)
# a chain of stone beams and iron clamps, running right round inside the inner shell like a hoop
YC=560
xl=xat((R0+R1)/2,-1,YC); xr=xat((R0+R1)/2,1,YC); rx=(xr-xl)/2; ry=24
s.raw_path(f"M {xl:.1f},{YC} A {rx:.1f},{ry} 0 0 1 {xr:.1f},{YC}",stroke=SOFT,sw=2,extra='stroke-dasharray="6 6"')
pts=[(CXD+rx*math.cos(math.radians(a)),YC+ry*math.sin(math.radians(a))) for a in range(0,181,6)]
s.path(pts,stroke=INK,sw=9); s.path(pts,stroke=STONE,sw=6)
for k in range(3,30,5):
    x,y=pts[k]; s.circle(round(x,1),round(y,1),4,fill=INK,sw=0)

# inset: the bricks of the inner shell, seen close up
CX,CY,RR=1005,445,135
s.inset(CX,CY,RR)
RH=16; BW=46
s.add(f'<clipPath id="ic"><circle cx="{CX}" cy="{CY}" r="{RR-3}"/></clipPath>')
s.add('<g clip-path="url(#ic)">')
up=set()
for line in range(-6,7):                               # diagonal lines of upright bricks, rising to the right
    for r in range(-10,11):
        up.add((r, line*5 - r))                            # (row, column index of the upright brick)
for r in range(-9,10):
    y=CY+r*RH
    off=(r%2)*BW/2
    x=CX-RR-BW
    c=0
    while x<CX+RR+BW:
        s.add(f'<rect x="{x+off:.1f}" y="{y:.1f}" width="{BW}" height="{RH}" fill="{BRICK}" stroke="{INK}" stroke-width="1.5"/>')
        x+=BW
for line in range(-4,5):
    for k in range(-10,11):
        x=CX+line*120+k*24; y=CY+RH*(-2*k)
        s.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="15" height="{RH*3}" fill="{ACC}" stroke="{INK}" stroke-width="2"/>')
s.add('</g>')
s.circle(CX,CY,RR,fill="none",sw=2.5)
s.text(CX,CY-RR-16,"The bricks, close up",anchor="middle",italic=True)

s.callout(1,round(xat(R0+13,-1,500)),500,335,490,"A thick inner|shell of brick")
s.callout(2,xat(R3-6,-1,330),330,300,190,"A thin outer shell|under the tiles",anchor="end")
p=arc((R1+R2)/2,-1)[16]
s.callout(3,round(p[0]),round(p[1]),345,395,"A stair between|the shells")
s.callout(4,CX-41,CY+88,1150,680,"Upright bricks lock|each new ring",anchor="end")
x5,y5=pts[8]; s.callout(5,round(x5),round(y5),720,190,"A chain of stone and|iron, like a hoop")
s.save(os.path.join(os.path.dirname(__file__),"..","43-brick-dome","brick-dome"))
