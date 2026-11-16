import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("Barbed wire","Joseph Glidden, DeKalb, Illinois, 1874")
WIRE="#8f979b"; WIRE2="#b9c0c4"; DARK="#4b4f52"; GROUND=600

def strand(x0,x1,y,amp,per,sw,phase=0.0):
    """Two wires twisted together: two sine curves half a turn apart."""
    for k,(col,ph) in enumerate(((WIRE,phase),(WIRE2,phase+math.pi))):
        pts=[(x,y+amp*math.sin(2*math.pi*(x-x0)/per+ph)) for x in range(int(x0),int(x1)+1,3)]
        s.path(pts,stroke=col,sw=sw)

def small_barb(x,y,L=16,col=DARK,sw=2.5):
    s.ellipse(x,y,4,6,stroke=col,sw=sw)
    s.line(x-L*0.7,y-L*0.7,x+L*0.7,y+L*0.7,stroke=col,sw=sw)
    s.line(x-L*0.7,y+L*0.7,x+L*0.7,y-L*0.7,stroke=col,sw=sw)

# ================= a length of wire, life size-ish =================
strand(60,1140,190,5,26,4)
for x in (140,330,520,710,900,1090):
    small_barb(x,190)
s.text(600,235,"a length of fence wire",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= one barb, magnified =================
CX,CY,R=290,485,160
s.inset(CX,CY,R)
A,P,X0=14,70,CX-R+14
strand(X0,CX+R-14,CY,A,P,11)
# the barb: a short wire coiled round one strand, its two cut ends pointing out
bx=CX
for k in range(3):
    s.ellipse(bx-12+k*12,CY,6,20,fill="none",stroke=ACC,sw=6,rot=12)
s.line(bx-12,CY-8,bx-62,CY-78,stroke=ACC,sw=7)
s.line(bx+12,CY+8,bx+62,CY+78,stroke=ACC,sw=7)
s.text(CX,CY-R-18,"one barb, magnified",anchor="middle",italic=True,fill=SOFT,size=18)
XC=X0+P*2.5     # a crossing of the twist, right of the barb
XC=X0+P*3.5

# ================= wire in front of a trench =================
s.line(860,GROUND,1150,GROUND,stroke=SOFT,sw=1.5)
PICK=(900,1110)
for px in PICK:
    s.line(px,330,px,GROUND,stroke=DARK,sw=7)
    pts=[(px+12*math.sin(t/3.0),GROUND+t*1.0) for t in range(0,80,2)]
    s.path(pts,stroke=DARK,sw=4)
    for ey in (360,440,520):
        s.circle(px,ey,8,fill=PAPER,stroke=DARK,sw=3)
for ey in (360,440,520):
    strand(PICK[0]+8,PICK[1]-8,ey,3,20,3)
    for x in range(945,1090,45):
        small_barb(x,ey,L=11,sw=2)
s.text(1005,715,"strung on pickets in the war",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,190,CY+A*math.sin(2*math.pi*(190-X0)/P),90,690,"Two steel wires|twisted together")
s.callout(2,bx+12,CY+20,520,480,"A short barb coiled|round one wire")
s.callout(3,bx+58,CY+72,520,575,"Its two cut ends|stick out as points")
s.callout(4,XC,CY,520,350,"The twist locks|the barb in place")
s.callout(5,PICK[0],GROUND+45,800,690,"A corkscrew foot, screwed|in quietly at night",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","72-barbed-wire","barbed-wire"))
