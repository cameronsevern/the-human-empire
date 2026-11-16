import math,sys,os,random
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The rehydration sachet","One sachet, one litre of water, and what the mixture does in the gut")
FOIL="#d7dde0"; BAND="#5f8fae"; GLASS="#e8f0f2"; WATERC="#bcd6e0"; POWDER="#f4f2ec"
LUMEN="#f3ead2"; CELL="#e7c3b0"; BLOOD="#d99a8c"; NA="#4f7f9e"; GLU="#e0b64a"

# ================= the sachet, top corner torn off, tipping powder =================
random.seed(2)
SX,SY=110,170
s.path([(SX,SY+20),(SX+150,SY),(SX+178,SY+190),(SX+28,SY+210)],fill=FOIL,close=True,sw=3)
s.path([(SX+6,SY+62),(SX+156,SY+42),(SX+164,SY+98),(SX+14,SY+118)],fill=BAND,close=True,sw=1.5)
for k in range(1,7):                                   # crimped seal along the top
    x0=SX+k*21; y0=SY+20-k*2.8
    s.line(x0,y0,x0+2,y0+14,stroke=INK,sw=1)
# torn corner and falling powder
s.path([(SX+150,SY),(SX+128,SY+3),(SX+156,SY+40)],fill=PAPER,close=True,sw=2)
for _ in range(40):
    x=random.uniform(SX+150,SX+180); y=random.uniform(SY+50,SY+250)
    s.circle(round(x+0.08*(y-SY),1),round(y,1),1.8,fill="#cfc8b8",sw=0)

# ================= the litre jug =================
JX,JY=105,440
s.path([(JX,JY),(JX+200,JY),(JX+186,JY+230),(JX+14,JY+230)],fill=GLASS,close=True,sw=3)
s.path([(JX+6,JY+46),(JX+194,JY+46),(JX+186,JY+226),(JX+14,JY+226)],fill=WATERC,close=True,sw=0)
s.line(JX+6,JY+46,JX+194,JY+46,stroke=INK,sw=1.5)
s.raw_path(f"M {JX+200},{JY+40} Q {JX+250},{JY+60} {JX+236},{JY+110} Q {JX+226},{JY+150} {JX+193},{JY+150}",sw=4)
s.line(JX+20,JY+46,JX+48,JY+46,stroke=INK,sw=2.5)
s.text(JX+58,JY+34,"1 litre",italic=True,fill=SOFT,size=17)

# ================= inset: the lining of the gut =================
IX,IY,IR=880,440,215
s.inset(IX,IY,IR)
def clip(y0,y1):   # horizontal band of the circle between y0 and y1, as a polygon
    pts=[]
    for k in range(0,41):
        y=y0+(y1-y0)*k/40; dx=math.sqrt(max(IR*IR-(y-IY)**2,0))-3; pts.append((IX+dx,y))
    for k in range(40,-1,-1):
        y=y0+(y1-y0)*k/40; dx=math.sqrt(max(IR*IR-(y-IY)**2,0))-3; pts.append((IX-dx,y))
    return pts
MEM=380      # top surface of the lining cells
BOT=520      # bottom of the lining cells
s.path(clip(IY-IR+3,MEM),fill=LUMEN,close=True,sw=0)
s.path(clip(BOT+28,IY+IR-3),fill=BLOOD,close=True,sw=0)
# three lining cells
for k in (-1,0,1):
    x0=IX+k*130-62; x1=IX+k*130+62
    s.path([(x0,MEM),(x1,MEM),(x1,BOT),(x0,BOT)],fill=CELL,close=True,sw=2.5)
    s.circle(IX+k*130,BOT-40,14,fill="#c9907a",sw=1.5)
s.line(IX-IR,BOT+28,IX+IR,BOT+28,stroke=INK,sw=1.5)
s.text(IX,IY+IR-24,"blood",anchor="middle",italic=True,fill="#5a2c24",size=17,halo=BLOOD)
s.text(IX,IY-IR+42,"inside the gut",anchor="middle",italic=True,fill=SOFT,size=17,halo=LUMEN)
# salt and sugar in the gut
for (x,y) in ((760,330),(800,300),(1000,320),(955,295),(840,350),(1020,350),(905,285)):
    s.circle(x,y,6,fill=NA,sw=1.2)
def hexa(x,y,r=9,fill=GLU):
    s.path([(x+r*math.cos(a*math.pi/3),y+r*math.sin(a*math.pi/3)) for a in range(6)],fill=fill,close=True,sw=1.2)
for (x,y) in ((780,280),(985,345),(1040,300),(820,320)):
    hexa(x,y)
# the carrier in the middle cell: salt and sugar go in together
s.path([(IX-22,MEM-16),(IX+22,MEM-16),(IX+22,MEM+30),(IX-22,MEM+30)],fill=ACC,close=True,sw=2.5)
s.circle(IX-9,MEM-30,6,fill=NA,sw=1.2); s.circle(IX+9,MEM-30,6,fill=NA,sw=1.2); hexa(IX,MEM-48)
s.arrow(IX,MEM+36,IX,MEM+80)
# water following, down into the blood
for x in (IX+100,IX+150):
    s.arrow(x,MEM-30,x,BOT+60)
# cholera's leak: salt and water pushed out of the left cell
s.arrow(IX-130,MEM+60,IX-130,MEM-60)

s.callout(1,SX+90,SY+150,380,230,"One sachet: about 20 grams|of salts and sugar")
s.callout(2,JX+150,JY+150,380,600,"Stirred into one litre|of clean water")
s.callout(3,IX-18,MEM-12,640,170,"A carrier takes salt and|sugar in together")
s.callout(4,IX+150,BOT+20,1150,672,"Water follows|the salt",anchor="end")
s.callout(5,IX-130,MEM+40,620,450,"Cholera pushes salt out,|but the carrier still works",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","110-rehydration-sachet","rehydration-sachet"))
