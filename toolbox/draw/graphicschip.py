import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The graphics chip","A graphics card, part of its cooler taken off, and the chip enlarged")
BOARD="#3f6b4e"; CHIPC="#8f989e"; DIE="#c9cdd0"; MEM="#2e2e30"; GOLD="#d4a63a"; FAN="#4a4d50"; FIN="#c4c9cc"; CORE="#d98a75"

# ================= the card, seen from the front =================
BX0,BX1,BY0,BY1=80,590,250,540
s.path([(BX0-26,BY0-24),(BX0-8,BY0-24),(BX0-8,BY1+40),(BX0-26,BY1+40)],fill=FIN,close=True,sw=2.5)      # metal bracket
for k in range(3):
    y=BY0+20+k*62
    s.path([(BX0-22,y),(BX0-12,y),(BX0-12,y+40),(BX0-22,y+40)],fill="#2a2a2a",close=True,sw=1)
s.path([(BX0,BY0),(BX1,BY0),(BX1,BY1),(BX0,BY1)],fill=BOARD,close=True,sw=3)
# gold contacts along the bottom edge
s.path([(BX0+120,BY1),(BX1-60,BY1),(BX1-60,BY1+30),(BX0+120,BY1+30)],fill=BOARD,close=True,sw=2)
for x in range(BX0+128,BX1-64,9):
    s.path([(x,BY1+6),(x+5,BY1+6),(x+5,BY1+28),(x,BY1+28)],fill=GOLD,close=True,sw=0.6)
# the graphics chip in the middle, with memory chips round it
CX,CY=250,395
s.path([(CX-70,CY-70),(CX+70,CY-70),(CX+70,CY+70),(CX-70,CY+70)],fill=CHIPC,close=True,sw=2.5)
s.path([(CX-42,CY-42),(CX+42,CY-42),(CX+42,CY+42),(CX-42,CY+42)],fill=DIE,close=True,sw=2)
for (mx,my) in ((CX-100,CY-120),(CX-25,CY-120),(CX+50,CY-120),(CX-100,CY+92),(CX-25,CY+92),(CX+50,CY+92),(CX-128,CY-40),(CX-128,CY+12)):
    w,h=(50,28) if my in (CY-120,CY+92) else (28,50)
    if mx==CX-128: w,h=(28,50)
    s.path([(mx,my),(mx+w,my),(mx+w,my+h),(mx,my+h)],fill=MEM,close=True,sw=1.5)
# the cooler still on the right-hand half: fins and a fan
s.path([(BX0+300,BY0-14),(BX1+10,BY0-14),(BX1+10,BY1-10),(BX0+300,BY1-10)],fill=FIN,close=True,sw=2.5)
for x in range(BX0+312,BX1+4,12):
    s.line(x,BY0-6,x,BY1-18,stroke="#8e959a",sw=1.2)
FX,FY,FR=BX0+355+50,(BY0+BY1)/2-12,96
s.circle(FX,FY,FR+6,fill="#3a3d40",sw=2.5)
for k in range(9):
    a0=k*2*math.pi/9
    p=[(FX+18*math.cos(a0),FY+18*math.sin(a0)),(FX+FR*math.cos(a0+0.25),FY+FR*math.sin(a0+0.25)),(FX+FR*math.cos(a0+0.62),FY+FR*math.sin(a0+0.62)),(FX+18*math.cos(a0+0.5),FY+18*math.sin(a0+0.5))]
    s.path([(round(x,1),round(y,1)) for x,y in p],fill=FAN,close=True,sw=1.5)
s.circle(FX,FY,20,fill="#2a2a2a",sw=2)

# ================= inset: the chip itself, enlarged =================
IX,IY,IR=905,430,205
s.inset(IX,IY,IR)
s.text(IX,IY+IR+32,"the chip, enlarged",anchor="middle",italic=True)
G=135
s.path([(IX-G,IY-G),(IX+G,IY-G),(IX+G,IY+G),(IX-G,IY+G)],fill=DIE,close=True,sw=2.5)
# blocks of cores, each block a little grid
for bi in range(4):
    for bj in range(4):
        x0=IX-G+12+bi*65; y0=IY-G+12+bj*65
        for i in range(4):
            for j in range(4):
                x=x0+i*13; y=y0+j*13
                s.path([(x,y),(x+10,y),(x+10,y+10),(x,y+10)],fill=ACC if (bi,bj,i,j)!=(2,1,1,2) else "#5c2418",close=True,sw=0.6)
# one core picked out, with the sum it does
HX,HY=IX-G+12+2*65+1*13+5,IY-G+12+1*65+2*13+5
s.path([(IX+20,IY-G-58),(IX+150,IY-G-58),(IX+150,IY-G-18),(IX+20,IY-G-18)],fill=PAPER,close=True,sw=1.5)
s.line(HX,HY-5,IX+60,IY-G-18,stroke=INK,sw=1.2)
s.text(IX+85,IY-G-31,"a × b + c",anchor="middle",italic=True,size=20)

s.callout(1,IX+G-20,IY+G-20,1150,690,"Thousands of small cores,|all working at once",anchor="end")
s.callout(2,IX+150,IY-G-38,1150,170,"Each multiplies two numbers|and adds a third",anchor="end")
s.callout(3,CX-100+25,CY-120+14,200,170,"Memory chips feed|it the numbers")
s.callout(4,FX+60,FY+50,560,690,"A fan and metal fins|carry off the heat")
s.callout(5,BX0+150,BY1+20,110,690,"Gold contacts plug|into the computer")
s.save(os.path.join(os.path.dirname(__file__),"..","114-graphics-chip","graphics-chip"))
