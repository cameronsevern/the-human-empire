import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The atomic pile","Chicago Pile-1, under the football stands, December 1942")
GRAPH="#4d4c4a"; GRAPH2="#6a6966"; TIMBER="#c79a62"; ROD="#a7adb0"; FLOOR=650

# ================= the outline: square lower part, rounded dome above =================
L,R,SH=380,860,470          # sides, and the height where the dome begins
CXP=(L+R)/2; TOP=235
dome=[]
for i in range(41):
    a=math.pi*i/40
    dome.append((round(CXP-(R-L)/2*math.cos(a),1),round(SH-(SH-TOP)*math.sin(a),1)))
outline=[(L,FLOOR)]+dome+[(R,FLOOR)]
s.path(outline,fill=GRAPH,close=True,sw=3)
# courses of graphite bricks, with staggered joints
def half_width(y):
    if y>=SH: return (R-L)/2
    t=(SH-y)/(SH-TOP); return (R-L)/2*math.sqrt(max(0,1-t*t))
y=FLOOR-16; row=0
while y>TOP+6:
    hw=half_width(y)-3
    s.line(round(CXP-hw,1),y,round(CXP+hw,1),y,stroke=GRAPH2,sw=1.5)
    off=0 if row%2 else 22
    x=CXP-hw+off
    while x<CXP+hw:
        s.line(round(x,1),y,round(x,1),y+16,stroke=GRAPH2,sw=1.2); x+=44
    y-=16; row+=1

# ================= the cut-away: graphite, with uranium lumps in every other layer =================
WX0,WX1,WY0,WY1=440,630,326,450
s.path([(WX0,WY0),(WX1,WY0),(WX1,WY1),(WX0,WY1)],fill="#2f2e2c",close=True,sw=2.5)
yy=WY0; k=0
while yy+24<=WY1:
    s.path([(WX0+4,yy+2),(WX1-4,yy+2),(WX1-4,yy+22),(WX0+4,yy+22)],fill=GRAPH2,close=True,sw=1)
    if k%2==1:
        for xx in range(WX0+22,WX1-10,34):
            s.circle(xx,yy+12,7,fill=ACC,stroke=INK,sw=1.5)
    yy+=24; k+=1

# ================= the timber frame round the lower part =================
for x in (L-8,L+90,L+190,R-190,R-90,R+8):
    if x in (L+190,R-190): continue
    s.path([(x-7,SH-10),(x+7,SH-10),(x+7,FLOOR),(x-7,FLOOR)],fill=TIMBER,close=True,sw=2)
s.path([(L-16,SH-18),(R+16,SH-18),(R+16,SH-6),(L-16,SH-6)],fill=TIMBER,close=True,sw=2)
s.line(300,FLOOR,1140,FLOOR,stroke=SOFT,sw=1.5)

# ================= control rods, partly pulled out on the right =================
for (yr,x1) in ((500,1000),(570,960)):
    s.path([(R-30,yr-6),(x1,yr-6),(x1,yr+6),(R-30,yr+6)],fill=ROD,close=True,sw=2)
    s.path([(x1,yr-10),(x1+14,yr-10),(x1+14,yr+10),(x1,yr+10)],fill=TIMBER,close=True,sw=1.5)

# ================= the emergency rod "zip", held out by a rope on the left =================
ZY=560
s.path([(L+30,ZY-6),(200,ZY-6),(200,ZY+6),(L+30,ZY+6)],fill=ROD,close=True,sw=2)
s.line(L-4,ZY-6,L+4,ZY-6,stroke=INK,sw=1)
s.path([(110,360),(240,360)],stroke=INK,sw=4)                 # the balcony rail
for x in (120,160,200,240): s.line(x,360,x,392,stroke=INK,sw=2)
s.line(205,ZY,215,392,stroke="#8a6a3a",sw=2.5)               # the rope that holds it out
s.text(170,346,"balcony",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,760,330,880,250,"Graphite bricks slow the|neutrons, so that they|split uranium more easily")
s.callout(2,534,388,660,165,"Lumps of uranium in|every other layer")
s.callout(3,945,570,1140,670,"Cadmium strips soak up|neutrons; pulling them|out starts the reaction",anchor="end")
s.callout(4,206,566,90,690,"Emergency rod: cut its|rope, and a weight pulls it in")
s.callout(5,L-12,SH-12,100,190,"A timber frame|holds the pile in shape")
s.save(os.path.join(os.path.dirname(__file__),"..","83-atomic-pile","atomic-pile"))
