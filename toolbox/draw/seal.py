"""The cylinder seal, drawn in an oblique view so the geometry is honest.

The clay strip runs left to right. The seal lies ACROSS it, with its axis pointing
away from the viewer, and rolls to the right. One point of the stone touches one point
of the clay, so the carving on the stone is computed from the print on the clay:
a mark at distance s behind the line of contact sits at angle s/R round the stone.
"""
import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The cylinder seal","about 5,500 years ago")

R=60; C=2*math.pi*R            # radius of the seal; one full turn prints C of clay
LEN=170                        # length of the seal = width of the printed band
DX,DY=0.24,-0.74               # one unit of depth, as drawn on the page
XC,Y0=820,560                  # line of contact, and the near edge of the clay
X_L,X_R=60,985                 # ends of the clay strip

def clay(x,v): return (x+v*DX, Y0+v*DY)
def stone(x,v):
    """Where the mark that prints at (x,v) sits on the stone right now; None if out of sight."""
    a=((XC-x)/R)%(2*math.pi)
    nx,ny=-math.sin(a),math.cos(a)
    if nx*DX+ny*DY<=0.06: return None
    return (XC+R*nx+v*DX, Y0-R+R*ny+v*DY)

# --- the picture, as polylines in (u across, v up) with the tree at u=0 ---
K=1.5
def P(xo,yo): return (xo*K, 22+(34-yo)*K)
def quad(p0,p1,p2,n=10):
    return [((1-t)**2*p0[0]+2*t*(1-t)*p1[0]+t*t*p2[0], (1-t)**2*p0[1]+2*t*(1-t)*p1[1]+t*t*p2[1]) for t in [i/n for i in range(n+1)]]
def goat(x,f):
    g=lambda a,b: P(x+a*f,b)
    return [quad(g(-18,6),g(0,-10),g(16,-22)), [g(16,-22),g(24,-34),g(34,-30)],
            quad(g(24,-34),g(14,-50),g(4,-44)),
            [g(-16,6),g(-20,34)], [g(-8,2),g(-8,34)], [g(12,-16),g(26,-6)], [g(8,-12),g(22,2)]]
def tree():
    t=[[P(0,34),P(0,-44)]]
    for j in (-28,-10,8): t+= [[P(0,j),P(-14,j-14)], [P(0,j),P(14,j-14)]]
    return t
SCENE=goat(-63,1)+tree()+goat(63,-1)

def dense(pl,step=3.0):
    out=[pl[0]]
    for a,b in zip(pl,pl[1:]):
        n=max(1,int(math.hypot(b[0]-a[0],b[1]-a[1])/step))
        out+=[(a[0]+(b[0]-a[0])*i/n, a[1]+(b[1]-a[1])*i/n) for i in range(1,n+1)]
    return out
def draw(fn,x0,col,sw):
    for pl in SCENE:
        run=[]
        for u,v in dense(pl):
            p=fn(x0+u,v)
            if p is None:
                if len(run)>1: s.path(run,stroke=col,sw=sw)
                run=[]
            else: run.append(p)
        if len(run)>1: s.path(run,stroke=col,sw=sw)

# --- the clay strip, lying flat ---
T=16
s.path([clay(X_L,0),clay(X_R,0),clay(X_R,LEN),clay(X_L,LEN)],fill=CLAY,close=True)
s.path([clay(X_L,0),clay(X_R,0),(X_R,Y0+T),(X_L,Y0+T)],fill="#c39a76",close=True)
# faint borders of the printed band, which stop at the seal
for v in (10,LEN-10):
    a,b=clay(X_L+6,v),clay(XC,v); s.line(a[0],a[1],b[0],b[1],stroke=SOFT,sw=1.5)
TREE=XC-0.57*C                  # the tree last printed this far behind the seal
for k in (0,1): draw(clay,TREE-k*C,INK,3)

# --- the seal, lying across the strip ---
cx,cy=XC,Y0-R; fx,fy=cx+LEN*DX,cy+LEN*DY
dl=math.hypot(DX,DY); px,py=-DY/dl,DX/dl
s.ellipse(XC+LEN*DX/2+4,Y0+LEN*DY/2+3,34,9,fill="#b98f6c",stroke="none",sw=0,rot=math.degrees(math.atan2(DY,DX)))
s.circle(fx,fy,R,fill=STONE)
s.path([(cx+R*px,cy+R*py),(fx+R*px,fy+R*py),(fx-R*px,fy-R*py),(cx-R*px,cy-R*py)],fill=STONE,stroke="none",sw=0,close=True)
for sg in (1,-1): s.line(cx+sg*R*px,cy+sg*R*py,fx+sg*R*px,fy+sg*R*py)
draw(stone,TREE,ACC,3.2)
s.circle(cx,cy,R,fill="#ddd7cc")
s.circle(cx,cy,8,fill=PAPER,sw=2.5)
# turning arrow on the near end: clockwise, so the top moves the way the seal travels
r=36; a0,a1=math.radians(215),math.radians(-35)
s.raw_path(f"M {cx+r*math.cos(a0):.1f},{cy-r*math.sin(a0):.1f} A {r},{r} 0 1 1 {cx+r*math.cos(a1):.1f},{cy-r*math.sin(a1):.1f}",sw=2.5)
ex,ey=cx+r*math.cos(a1),cy-r*math.sin(a1)
for da in (0.55,-0.45):
    t=a1+math.pi/2+da; s.line(ex,ey,ex+15*math.cos(t),ey-15*math.sin(t),sw=2.5)
# direction of travel
s.arrow(730,612,900,612); s.text(815,646,"it rolls this way",anchor="middle",italic=True)

s.callout(1,fx+10,fy-R+6,925,165,"A cylinder of stone,|the size of a|thumb joint")
p=stone(TREE,105); s.callout(2,p[0],p[1],610,235,"The picture is cut|into the stone,|back to front",anchor="end")
p=clay(TREE-C-63*K,120); s.callout(3,p[0],p[1],110,300,"Rolled across damp|clay, it leaves the|picture standing up")
p=clay(TREE-C/2,14); s.callout(4,p[0],p[1],250,690,"One full turn prints the picture|once, and then it begins again")
s.callout(5,cx,cy+2,1150,660,"A hole for a cord,|worn at the neck|or wrist",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","08-cylinder-seal","cylinder-seal"))
