import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The sewn ship","the Indian Ocean, by the first century")
FIBRE="#c4a374"; FIBRE2="#a8875a"; HOLE="#5a4a3c"; PUTTY="#9a958c"
X0,X1=70,800
P=[(230,350),(350,470),(470,590)]          # three planks, seen from inside the hull
for (a,b) in P:
    s.path([(X0,a),(X1,a),(X1,b),(X0,b)],fill=WOOD,close=True,sw=3)
    for k in range(4):                          # wood grain
        y=a+18+k*27
        s.raw_path(f"M {X0+8},{y} C {X0+200},{y-6} {X0+420},{y+7} {X1-8},{y-2}",stroke="#cbb68f",sw=1.3)
SP=46                                            # hole spacing (about 5 cm)
def holes(seam,x0,x1):
    xs=list(range(x0,x1,SP)); return xs,[(x,seam-24) for x in xs],[(x,seam+24) for x in xs]
# upper seam: wadding roll laid along the joint and sewn over it
seam=350
s.path([(X0,seam-11),(X1,seam-11),(X1,seam+11),(X0,seam+11)],fill=FIBRE,close=True,sw=2)
for x in range(X0+6,X1-6,14):
    s.line(x,seam-9,x+9,seam+9,stroke=FIBRE2,sw=1.2)
xs,up,lo=holes(seam,X0+30,X1-10)
for (x,y) in up+lo: s.circle(x,y,5,fill=PUTTY,sw=1.5)
for i,x in enumerate(xs):
    s.line(x,seam-24,x,seam+24,stroke=ACC,sw=3.5)
    if i+1<len(xs):
        s.line(x,seam-24,xs[i+1],seam+24,stroke=ACC,sw=3.5)
        s.line(xs[i+1],seam-24,x,seam+24,stroke=ACC,sw=3.5)
# lower seam: on the left sewn, on the right the holes drilled and waiting
seam2=470; cut=430
s.path([(X0,seam2-11),(cut,seam2-11),(cut,seam2+11),(X0,seam2+11)],fill=FIBRE,close=True,sw=2)
for x in range(X0+6,cut-6,14):
    s.line(x,seam2-9,x+9,seam2+9,stroke=FIBRE2,sw=1.2)
xs2,up2,lo2=holes(seam2,X0+30,X1-10)
for (x,y) in up2+lo2:
    s.circle(x,y,5,fill=PUTTY if x<cut else HOLE,sw=1.5)
sewn=[x for x in xs2 if x<cut]
for i,x in enumerate(sewn):
    s.line(x,seam2-24,x,seam2+24,stroke=ACC,sw=3.5)
    if i+1<len(sewn):
        s.line(x,seam2-24,sewn[i+1],seam2+24,stroke=ACC,sw=3.5)
        s.line(sewn[i+1],seam2-24,x,seam2+24,stroke=ACC,sw=3.5)
# the loose end of the cord, with its stiffened tip
lx=sewn[-1]
s.raw_path(f"M {lx},{seam2+24} C {lx+30},{seam2+70} {lx+80},{seam2+80} {lx+120},{seam2+64}",stroke=ACC,sw=3.5)
# inset: the joint seen end on, inside of the hull at the left
CX,CY,R=1010,450,140
s.inset(CX,CY,R)
TH=44; xi,xo=CX-TH//2,CX+TH//2
s.path([(xi,CY-118),(xo,CY-118),(xo,CY-2),(xi,CY-2)],fill=WOOD,close=True,sw=2.5)
s.path([(xi,CY+2),(xo,CY+2),(xo,CY+118),(xi,CY+118)],fill=WOOD,close=True,sw=2.5)
s.circle(xi-12,CY,11,fill=FIBRE,sw=2); s.circle(xo+12,CY,11,fill=FIBRE,sw=2)
ya,yb=CY-36,CY+36
s.raw_path(f"M {xi},{ya} L {xo},{ya} C {xo+30},{ya+6} {xo+30},{yb-6} {xo},{yb} L {xi},{yb} "
           f"C {xi-30},{yb-6} {xi-30},{ya+6} {xi},{ya} Z",stroke=ACC,sw=3.5)
s.text(CX-62,CY+108,"inside",size=18,anchor="end",italic=True,fill=SOFT)
s.text(CX+62,CY+108,"outside",size=18,italic=True,fill=SOFT)
s.callout(1,600,290,640,170,"Planks set|edge to edge")
s.callout(2,xs2[-2],seam2+24,850,670,"Holes drilled in pairs,|about 5 cm apart")
s.callout(3,xs[0]+SP//2,seam,110,170,"Coconut-fibre cord, pulled|tight in X-shaped stitches")
s.callout(4,250,seam2,110,670,"A roll of fibre along|the seam, under the stitches")
s.callout(5,xo+22,CY+20,1150,170,"End on: the cord loops|through both planks|and over a roll each side",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","33-sewn-ship","sewn-ship"))
