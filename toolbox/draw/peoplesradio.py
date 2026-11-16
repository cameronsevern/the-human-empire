import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The people's receiver","The Volksempfänger VE 301 W, Berlin, 1933")
BAKE="#4a3f38"; BAKE2="#5c5048"; CLOTH="#b98a5a"; IVORY="#efe6d0"; GLASS="#dfe7ea"; METALC="#8f979b"

def rrect(x0,y0,x1,y1,r,fill,sw=3,stroke=INK):
    s.raw_path(f"M {x0+r},{y0} L {x1-r},{y0} Q {x1},{y0} {x1},{y0+r} L {x1},{y1-r} Q {x1},{y1} {x1-r},{y1} L {x0+r},{y1} Q {x0},{y1} {x0},{y1-r} L {x0},{y0+r} Q {x0},{y0} {x0+r},{y0} Z",fill=fill,stroke=stroke,sw=sw)

# ================= from the front =================
FX0,FX1,FY0,FY1=200,500,170,570
CX=(FX0+FX1)/2
s.path([(FX0+30,FY1),(FX1-30,FY1),(FX1-30,FY1+14),(FX0+30,FY1+14)],fill=BAKE,close=True,sw=2)   # foot
rrect(FX0,FY0,FX1,FY1,16,BAKE)
rrect(FX0+12,FY0+12,FX1-12,FY1-12,8,BAKE2,sw=1.5)
s.circle(CX,300,112,fill=BAKE,stroke=INK,sw=3)                 # moulded ring round the speaker
s.circle(CX,300,96,fill=CLOTH,stroke=INK,sw=2)
for y in range(214,390,9):
    h=math.sqrt(max(0,96**2-(y-300)**2))
    s.line(round(CX-h+4,1),y,round(CX+h-4,1),y,stroke="#a5784b",sw=1.2)
# the arched panel with the dial and the middle knob
s.raw_path(f"M {CX-55},{FY1-14} L {CX-55},{470} A 55 55 0 0 1 {CX+55},{470} L {CX+55},{FY1-14} Z",fill=BAKE,sw=2.5)
s.raw_path(f"M {CX-46},{462} A 46 46 0 0 1 {CX+46},{462} L {CX+26},{468} A 26 26 0 0 0 {CX-26},{468} Z",fill=IVORY,sw=2)   # dial window
for k in range(9):
    a=math.pi*(0.15+0.7*k/8)
    s.line(round(CX-42*math.cos(a),1),round(462-42*math.sin(a),1),round(CX-34*math.cos(a),1),round(462-34*math.sin(a),1),stroke=INK,sw=1.2)
s.raw_path(f"M {CX-28},{FY1-14} L {CX-28},{500} A 28 28 0 0 1 {CX+28},{500} L {CX+28},{FY1-14}",stroke=INK,sw=1.5)
for kx in (FX0+50,CX,FX1-50):
    s.circle(kx,535,15,fill="#2f2a26",stroke=INK,sw=2)
    s.circle(kx,535,8,fill=BAKE,stroke=INK,sw=1)
s.text(CX,156,"from the front",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= from the back, cover off =================
BX0,BX1,BY0,BY1=820,1110,170,570
BC=(BX0+BX1)/2
rrect(BX0,BY0,BX1,BY1,16,"#d9d2c4")
# the loudspeaker's frame and magnet, seen from behind
s.circle(BC,290,95,fill="none",stroke=METALC,sw=5)
for a in (0.6,2.5,3.7,5.6):
    s.line(BC,290,round(BC+95*math.cos(a),1),round(290+95*math.sin(a),1),stroke=METALC,sw=4)
s.path([(BC-30,262),(BC+30,262),(BC+30,318),(BC-30,318)],fill="#5e6366",close=True,sw=2)
# the chassis shelf and three valves
s.path([(BX0+14,470),(BX1-14,470),(BX1-14,488),(BX0+14,488)],fill=METALC,close=True,sw=2)
def valve(x,fill,h=88):
    s.path([(x-16,470),(x+16,470),(x+16,452),(x-16,452)],fill="#3a3430",close=True,sw=1.5)
    s.raw_path(f"M {x-15},452 L {x-15},{452-h+18} Q {x},{452-h-8} {x+15},{452-h+18} L {x+15},452 Z",fill=fill,sw=2)
valve(BC-85,GLASS); valve(BC,ACC); valve(BC+85,GLASS,h=76)
s.path([(BC-40,500),(BC+40,500),(BC+40,540),(BC-40,540)],fill="#c7a77a",close=True,sw=2)   # tuning coil under the shelf
for y in range(506,540,6): s.line(BC-40,y,BC+40,y,stroke="#8e6a3e",sw=1.2)
s.text(BC,156,"from the back, opened",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,FX1-6,FY0+60,560,200,"A case of moulded|Bakelite")
s.callout(2,CX+50,330,560,320,"A loudspeaker|behind the cloth")
s.callout(3,CX+30,445,560,420,"A dial for long and|medium wave only")
s.callout(4,BC+85,420,1130,650,"Another valve turns|the mains into DC",anchor="end")
s.callout(5,BC,410,700,690,"One valve feeds its signal|back to itself, boosting it",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","79-peoples-radio","peoples-radio"))
