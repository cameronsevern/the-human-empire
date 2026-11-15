import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The longship","Scandinavia, with keel and sail by the 700s")
WATER="#c9d6d8"; SAIL="#e9dcc0"; STRIPE="#b98f6a"; OAK="#c9a77a"
WL=540                                            # waterline
def bez(p0,p1,p2,p3,t):
    u=1-t; return (u**3*p0[0]+3*u*u*t*p1[0]+3*u*t*t*p2[0]+t**3*p3[0], u**3*p0[1]+3*u*u*t*p1[1]+3*u*t*t*p2[1]+t**3*p3[1])
# sheer (top edge) and keel (bottom edge), stern at left, bow at right
TOP=((110,420),(250,486),(600,486),(740,420))
BOT=((130,520),(260,572),(590,572),(720,520))
N=60
top=[bez(*TOP,i/N) for i in range(N+1)]; bot=[bez(*BOT,i/N) for i in range(N+1)]
# water behind the hull
s.add(f'<path d="M 50,{WL} L 830,{WL} L 830,{WL+80} L 50,{WL+80} Z" fill="{WATER}" stroke="none"/>')
# mast and sail behind the hull
MX=425
s.line(MX,486,MX,170,stroke=INK,sw=9); s.line(MX,486,MX,170,stroke=WOOD,sw=5)
s.line(MX-170,200,MX+170,200,stroke=INK,sw=6)                         # yard
s.raw_path(f"M {MX-165},204 L {MX+165},204 C {MX+175},300 {MX+185},380 {MX+180},430 L {MX-180},430 C {MX-185},380 {MX-175},300 {MX-165},204 Z",fill=SAIL,sw=3)
for k in range(-2,3):
    x=MX+k*66
    s.raw_path(f"M {x-14},206 L {x+14},206 L {x+18+k*3},428 L {x-18+k*3},428 Z",fill=STRIPE,stroke="none",sw=0)
s.raw_path(f"M {MX-165},204 L {MX+165},204 C {MX+175},300 {MX+185},380 {MX+180},430 L {MX-180},430 C {MX-185},380 {MX-175},300 {MX-165},204 Z",fill="none",sw=3)
s.line(MX,172,180,445,stroke=SOFT,sw=1.5); s.line(MX,172,690,445,stroke=SOFT,sw=1.5)   # stays
# hull
hull=top+bot[::-1]
s.path(hull,fill=OAK,close=True,sw=3)
# stern and stem posts curling up
s.raw_path("M 110,420 C 92,400 78,350 92,312 C 100,292 122,296 118,316",stroke=INK,sw=11)
s.raw_path("M 110,420 C 92,400 78,350 92,312 C 100,292 122,296 118,316",stroke=OAK,sw=6)
s.raw_path("M 740,420 C 760,398 774,348 760,310 C 752,290 730,294 734,314",stroke=INK,sw=11)
s.raw_path("M 740,420 C 760,398 774,348 760,310 C 752,290 730,294 734,314",stroke=OAK,sw=6)
s.raw_path("M 130,520 C 118,500 110,460 110,420",sw=3); s.raw_path("M 720,520 C 732,500 740,460 740,420",sw=3)
# overlapping planks: each strake edge drawn with a lip, and rows of rivets
for k in range(1,6):
    f=k/6; line=[(t[0]+(b[0]-t[0])*f, t[1]+(b[1]-t[1])*f) for t,b in zip(top,bot)]
    s.path(line,stroke=INK,sw=2.2)
    s.path([(x,y+3) for x,y in line[2:-2]],stroke="#a88456",sw=2)
    for i in range(3,N-2,3):
        x,y=line[i]; s.circle(round(x,1),round(y-4,1),1.8,fill=INK,sw=0)
# oar holes in the top plank, shutters open
ports=[]
for i in range(9,N-8,5):
    t0,b0=top[i],bot[i]; x=t0[0]; y=t0[1]+(b0[1]-t0[1])*0.09
    s.circle(round(x,1),round(y,1),5,fill=INK,sw=0); ports.append((x,y))
# the keel strip along the bottom
s.path(bot[4:-4],stroke=INK,sw=8)
s.add(f'<path d="M 50,{WL} L 830,{WL} L 830,{WL+80} L 50,{WL+80} Z" fill="{WATER}" fill-opacity="0.6" stroke="none"/>')
# steering oar on the right-hand side, near the stern
s.line(150,384,212,600,stroke=INK,sw=9); s.line(150,384,212,600,stroke=WOOD,sw=5)
s.raw_path("M 196,560 L 226,552 L 240,628 L 214,636 Z",fill=WOOD,sw=2.5)
s.line(150,388,190,372,stroke=INK,sw=5)                              # tiller
# water line over the hull
s.line(50,WL,830,WL,stroke="#7f9aa0",sw=2)
for x in range(70,820,60): s.raw_path(f"M {x},{WL+22} q 10,-6 20,0",stroke="#7f9aa0",sw=1.5)

# inset: a cut across the hull
CX,CY,RR=1010,450,150
s.inset(CX,CY,RR)
W2=CY+40                                             # waterline in the inset
s.add(f'<path d="M {CX-148},{W2} L {CX+148},{W2} L {CX+130},{CY+75} L {CX-130},{CY+75} Z" fill="{WATER}" stroke="none"/>')
# planks: each side four strakes, each overlapping the one below on the outside
RIV=[]
def strakes(sign):
    pts=[(14,92),(52,86),(82,66),(102,34),(114,-4),(120,-46)]
    T=11
    for j in range(len(pts)-1):
        (x0,y0),(x1,y1)=pts[j],pts[j+1]
        dx,dy=x1-x0,y1-y0; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L
        nx,ny=-uy,ux                                   # outward (away from the centre line)
        if j>0: x0,y0=x0-ux*14,y0-uy*14                # reach down over the plank below
        off=T if j>0 else 0
        a_in=(x0+nx*off,y0+ny*off); b_in=(x1,y1)
        q=[a_in,b_in,(b_in[0]+nx*T,b_in[1]+ny*T),(a_in[0]+nx*T,a_in[1]+ny*T)]
        s.path([(CX+sign*x,CY+y) for x,y in q],fill=ACC,close=True,sw=2.2)
        if j>0:
            rx,ry=x0+ux*7,y0+uy*7
            s.line(round(CX+sign*(rx-nx*2),1),round(CY+ry-ny*2,1),round(CX+sign*(rx+nx*(2*T+2)),1),round(CY+ry+ny*(2*T+2),1),stroke=INK,sw=3)
            RIV.append((CX+sign*(rx+nx*T),CY+ry+ny*T))
strakes(1); strakes(-1)
# rivets drawn across each overlap
# the keel
s.path([(CX-16,CY+90),(CX+16,CY+90),(CX+12,CY+118),(CX-12,CY+118)],fill=OAK,close=True,sw=2.5)
# a rib inside, and a crossbeam
s.raw_path(f"M {CX-112},{CY+4} C {CX-100},{CY+62} {CX-60},{CY+88} {CX},{CY+88} C {CX+60},{CY+88} {CX+100},{CY+62} {CX+112},{CY+4}",stroke=WOOD,sw=9)
s.raw_path(f"M {CX-112},{CY+4} C {CX-100},{CY+62} {CX-60},{CY+88} {CX},{CY+88} C {CX+60},{CY+88} {CX+100},{CY+62} {CX+112},{CY+4}",stroke=INK,sw=1.5)
s.line(CX-112,CY+6,CX+112,CY+6,stroke=INK,sw=6); s.line(CX-112,CY+6,CX+112,CY+6,stroke=WOOD,sw=3)
s.line(CX-148,W2,CX+148,W2,stroke="#7f9aa0",sw=2)
s.text(CX+50,CY+RR+36,"A cut across the hull",anchor="end",italic=True)

s.callout(1,MX+150,262,690,190,"One square sail|of wool")
px,py=ports[5]; s.callout(2,round(px),round(py),620,690,"Holes for the oars, shut|when the sail is up")
s.callout(3,218,600,120,690,"A steering oar on the|right-hand side")
s.callout(4,round(RIV[2][0]),round(RIV[2][1]),1150,190,"Planks overlapped|and riveted together",anchor="end")
s.callout(5,CX+14,CY+108,1150,690,"A keel, and a metre|of water is enough",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","35-longship","longship"))
