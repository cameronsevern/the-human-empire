import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The Minié ball","France, 1849; American Civil War, 1861 to 1865")
IRON="#8b9296"; BORE="#e9e5dc"; POWDER="#3a3430"; FLASH="#e0a030"; DARKACC="#8e3c2a"

# ================= the barrel, cut open along its length =================
BX0,BX1,BT,BB=90,1100,190,250; bt,bb=BT+12,BB-12
s.path([(BX0,BT),(BX1,BT),(BX1,BB),(BX0,BB)],fill=IRON,close=True,sw=3)
s.path([(BX0+20,bt),(BX1,bt),(BX1,bb),(BX0+20,bb)],fill=BORE,close=True,sw=2)
for x in range(BX0+40,BX1-10,26):                                    # the spiral grooves, seen inside
    s.line(x,bt+1,x+22,bb-1,stroke="#a7a093",sw=3)
for k in range(14):                                                  # powder at the breech
    s.circle(BX0+30+(k%5)*9,bt+6+(k//5)*9,3,fill=POWDER,sw=0)
# the bullet, loose in the bore, on its way down
LX=1000
s.raw_path(f"M {LX-34},{bt+5} L {LX+6},{bt+5} C {LX+30},{bt+5} {LX+44},{(bt+bb)/2} {LX+44},{(bt+bb)/2} "
           f"C {LX+44},{(bt+bb)/2} {LX+30},{bb-5} {LX+6},{bb-5} L {LX-34},{bb-5} Z",fill=ACC,sw=2.5)
s.arrow(1070,BT-22,960,BT-22)
s.text(1010,BT-40,"rammed down",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= one bullet, cut in half =================
CX,CY=250,455; R=46
s.raw_path(f"M {CX-110},{CY-R} L {CX+40},{CY-R} C {CX+90},{CY-R} {CX+120},{CY-12} {CX+126},{CY} "
           f"C {CX+120},{CY+12} {CX+90},{CY+R} {CX+40},{CY+R} L {CX-110},{CY+R} Z",fill=ACC,sw=3)
for gx in (-70,-40,-10):                                             # grease grooves
    s.path([(CX+gx,CY-R-1),(CX+gx+12,CY-R-1),(CX+gx+12,CY-R+8),(CX+gx,CY-R+8)],fill=PAPER,close=True,sw=2)
    s.path([(CX+gx,CY+R+1),(CX+gx+12,CY+R+1),(CX+gx+12,CY+R-8),(CX+gx,CY+R-8)],fill=PAPER,close=True,sw=2)
s.path([(CX-110,CY-R+10),(CX-30,CY),(CX-110,CY+R-10)],fill=PAPER,close=True,sw=2.5)   # the hollow base
for k in range(6):                                                   # hatching on the cut face
    x=CX-20+k*22
    s.line(x,CY-R+12,x-16,CY+R-12,stroke=DARKACC,sw=1.2)
s.text(CX,CY+R+40,"cut in half",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the moment of firing =================
FX0,FX1,FT,FB=440,800,400,510; ft,fb=FT+16,FB-16
for (y0,y1,d) in ((FT,ft,1),(fb,FB,-1)):                             # the barrel wall, with grooves cut in it
    s.path([(FX0,y0),(FX1,y0),(FX1,y1),(FX0,y1)],fill=IRON,close=True,sw=2.5)
for x in range(FX0+20,FX1,40):
    s.path([(x,ft-7),(x+18,ft-7),(x+18,ft),(x,ft)],fill=BORE,close=True,sw=1.5)
    s.path([(x,fb),(x+18,fb),(x+18,fb+7),(x,fb+7)],fill=BORE,close=True,sw=1.5)
s.path([(FX0,ft),(FX1,ft),(FX1,fb),(FX0,fb)],fill=BORE,close=True,sw=0,stroke="none")
# bullet, its skirt pressed out into the grooves
BX=560
s.raw_path(f"M {BX},{ft-6} L {BX+110},{ft+2} C {BX+150},{ft+4} {BX+180},{(ft+fb)/2-6} {BX+190},{(ft+fb)/2} "
           f"C {BX+180},{(ft+fb)/2+6} {BX+150},{fb-4} {BX+110},{fb-2} L {BX},{fb+6} Z",fill=ACC,sw=2.5)
s.path([(BX,ft+6),(BX+60,(ft+fb)/2),(BX,fb-6)],fill="#f3d6c8",close=True,sw=2)
for dy in (-18,0,18):
    s.arrow(FX0+20,(ft+fb)/2+dy,BX+30,(ft+fb)/2+dy*0.4)
for k in range(8):
    s.circle(FX0+14+(k%3)*12,ft+16+(k//3)*24,6,fill=FLASH,sw=0)
s.text((FX0+FX1)/2,FB+36,"on firing",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= how far each could hit a man =================
AX0=330; PX=2.0                                                       # 2 px to the metre
for (y,m,name,fill) in ((620,90,"smoothbore musket","#cdc6ba"),(668,250,"rifle musket","#5e554e")):
    s.path([(AX0,y-12),(AX0+m*PX,y-12),(AX0+m*PX,y+12),(AX0,y+12)],fill=fill,close=True,sw=2)
    s.text(AX0-14,y+7,name,anchor="end",italic=True,size=19)
s.line(AX0,698,AX0+400*PX,698,stroke=INK,sw=1.5)
for m in range(0,401,100):
    s.line(AX0+m*PX,698,AX0+m*PX,708,stroke=INK,sw=1.5)
    s.text(AX0+m*PX,730,f"{m} m",anchor="middle",size=17,fill=SOFT)

s.callout(1,700,bb-6,700,320,"Spiral grooves cut|inside the barrel",anchor="end")
s.callout(2,LX+20,(bt+bb)/2,1150,330,"Narrower than the|bore, it drops in",anchor="end")
s.callout(3,CX-90,CY,140,320,"A hollow base")
s.callout(4,BX+10,ft-2,850,455,"The gas swells the|base into the grooves")
s.callout(5,AX0+250*PX,668,880,600,"Aimed fire, two or|three times as far")
s.save(os.path.join(os.path.dirname(__file__),"..","64-minie-ball","minie-ball"))
