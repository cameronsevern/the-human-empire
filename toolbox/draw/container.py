import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The shipping container","One standard box, moved between ship, crane, lorry and train")
BOXC=["#7d8f9a","#b0794f","#8a9a6b","#a5645a","#c2a35e","#6f8296"]
STEEL="#8e959a"; HULL="#4f5a63"; WATER="#cfdde3"; CRANE="#d9a441"; WHEELC="#2b2826"; QUAY=STONE

def box(x,y,w,h,fill,corners=True,ribs=True):
    s.path([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],fill=fill,close=True,sw=2)
    if ribs:
        for k in range(1,int(w//9)):
            s.line(x+k*9,y+3,x+k*9,y+h-3,stroke=INK,sw=0.6)
    if corners:
        for (cx,cy) in ((x,y),(x+w-6,y),(x,y+h-6),(x+w-6,y+h-6)):
            s.path([(cx,cy),(cx+6,cy),(cx+6,cy+6),(cx,cy+6)],fill=ACC,close=True,sw=1)

BW,BH=96,40         # a twenty-foot box at this scale
QY=560              # top of the quay

# ================= water and the ship =================
s.path([(28,QY+20),(400,QY+20),(400,738),(28,738)],fill=WATER,close=True,sw=0)
s.path([(40,QY-40),(395,QY-40),(380,QY+70),(70,QY+70)],fill=HULL,close=True,sw=3)
# boxes on deck, three high
cols=[48+k*(BW+2) for k in range(3)]
n=0
for j in range(3):
    for i,x in enumerate(cols):
        if (i,j)==(2,2): continue
        box(x,QY-40-BH*(j+1),BW,BH,BOXC[n%6]); n+=1
s.text(215,QY+55,"the ship",anchor="middle",italic=True,fill="#f4f1ea",halo=HULL,size=18)

# ================= the quay and the crane =================
s.path([(400,QY),(1172,QY),(1172,QY+26),(400,QY+26)],fill=QUAY,close=True,sw=2)
LX1,LX2=430,560
for x in (LX1,LX2):
    s.path([(x-7,QY),(x+7,QY),(x+7,200),(x-7,200)],fill=CRANE,close=True,sw=2)
s.line(LX1,QY-120,LX2,QY-120,stroke=INK,sw=6); s.line(LX1,QY-120,LX2,QY-120,stroke=CRANE,sw=3)
# boom reaching over the ship
s.path([(60,186),(600,186),(600,206),(60,206)],fill=CRANE,close=True,sw=2)
s.path([(LX1-10,170),(LX2+10,170),(LX2+10,186),(LX1-10,186)],fill=CRANE,close=True,sw=2)
# trolley, cables and spreader holding a box over the ship
TX=330
s.path([(TX-22,206),(TX+22,206),(TX+22,220),(TX-22,220)],fill=STEEL,close=True,sw=2)
SPY=330
for dx in (-14,14): s.line(TX+dx,220,TX+dx*2.5,SPY,stroke=INK,sw=1.5)
s.path([(TX-BW/2-4,SPY),(TX+BW/2+4,SPY),(TX+BW/2+4,SPY+9),(TX-BW/2-4,SPY+9)],fill=STEEL,close=True,sw=2)
box(TX-BW/2,SPY+9,BW,BH,BOXC[3])
s.text(345,165,"the crane",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= a lorry under the crane =================
LXo=600
box(LXo,QY-62,BW,BH,BOXC[4])
s.path([(LXo-6,QY-22),(LXo+BW+40,QY-22),(LXo+BW+40,QY-14),(LXo-6,QY-14)],fill=WHEELC,close=True,sw=1.5)  # trailer bed
s.path([(LXo+BW+8,QY-66),(LXo+BW+44,QY-66),(LXo+BW+52,QY-44),(LXo+BW+52,QY-14),(LXo+BW+8,QY-14)],fill="#c9473a",close=True,sw=2)  # cab
s.path([(LXo+BW+28,QY-60),(LXo+BW+42,QY-60),(LXo+BW+47,QY-46),(LXo+BW+28,QY-46)],fill="#cfe0e6",close=True,sw=1.2)
for x in (LXo+10,LXo+26,LXo+BW+32): s.circle(x,QY-8,8,fill=WHEELC,sw=1.5)
s.text(LXo+140,QY+60,"the lorry",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= a railway wagon, two boxes stacked =================
RX=830
s.line(RX-20,QY+2,1160,QY+2,stroke=INK,sw=3)
s.path([(RX,QY-26),(RX+2*BW+14,QY-26),(RX+2*BW+14,QY-16),(RX,QY-16)],fill=WHEELC,close=True,sw=1.5)
for x in (RX+24,RX+48,RX+2*BW-34,RX+2*BW-10): s.circle(x,QY-8,8,fill=WHEELC,sw=1.5)
box(RX+6,QY-26-BH,BW,BH,BOXC[0]); box(RX+8+BW,QY-26-BH,BW,BH,BOXC[2])
s.text(RX+BW+110,QY+60,"the train",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= inset: a corner fitting and a twistlock =================
IX,IY,IR=1030,255,110
s.inset(IX,IY,IR)
s.text(IX,IY+IR+36,"a corner, enlarged",anchor="middle",italic=True)
f=0.85
def Q(dx,dy): return (round(IX+dx*f,1),round(IY+dy*f,1))
# upper box's bottom corner and lower box's top corner, with a gap between them
s.path([Q(-100,-100),Q(40,-100),Q(40,-14),Q(-100,-14)],fill=BOXC[0],close=True,sw=2)
s.path([Q(-100,14),Q(40,14),Q(40,100),Q(-100,100)],fill=BOXC[4],close=True,sw=2)
for (y0,y1) in ((-60,-14),(14,60)):
    s.path([Q(-10,y0),Q(40,y0),Q(40,y1),Q(-10,y1)],fill=ACC,close=True,sw=2.5)
for y in (-16,16): s.ellipse(*Q(15,y),round(16*f,1),round(5*f,1),fill="#3a2a22",sw=1.5)
# the twistlock: a cone each side of a flat plate, turned a quarter turn
s.path([Q(3,-4),Q(27,-4),Q(22,-30),Q(8,-30)],fill=STEEL,close=True,sw=2)
s.path([Q(3,4),Q(27,4),Q(22,30),Q(8,30)],fill=STEEL,close=True,sw=2)
s.path([Q(-14,-4),Q(44,-4),Q(44,4),Q(-14,4)],fill=STEEL,close=True,sw=2)
s.line(*Q(44,0),*Q(76,8),stroke=INK,sw=3)   # handle

s.callout(1,*Q(30,-45),1150,430,"A steel fitting at each|of the eight corners",anchor="end")
s.callout(2,*Q(-12,0),880,325,"A twistlock, turned a|quarter turn, locks|two boxes together",anchor="end")
s.callout(3,TX+BW/2+2,SPY+4,620,240,"The spreader grips|the four top corners")
s.callout(4,LXo+48,QY-42,640,700,"The same box rides|on a lorry's trailer")
s.callout(5,RX+BW+8+BW/2,QY-46,890,700,"or on a|railway wagon")
s.save(os.path.join(os.path.dirname(__file__),"..","101-shipping-container","shipping-container"))
