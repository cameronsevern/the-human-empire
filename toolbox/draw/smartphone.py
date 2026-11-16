import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The smartphone","A phone from the front and with its back taken off, 2020s")
BODY="#3a3c40"; SCREEN="#26323b"; FRAME="#9aa2a8"; BATT="#c9b37a"; BOARD="#4f7a5a"; CHIPC="#2b2826"; GLASSC="#cfe0e6"; ICON=["#b5523b","#d9a441","#6f8fa6","#8a9a6b","#a5645a","#7d8f9a"]

def rrect(x,y,w,h,r,fill,sw=3,stroke=INK):
    s.raw_path(f"M {x+r},{y} L {x+w-r},{y} Q {x+w},{y} {x+w},{y+r} L {x+w},{y+h-r} Q {x+w},{y+h} {x+w-r},{y+h} L {x+r},{y+h} Q {x},{y+h} {x},{y+h-r} L {x},{y+r} Q {x},{y} {x+r},{y} Z",fill=fill,sw=sw,stroke=stroke)

# ================= the front =================
FX,FY,FW,FH=95,175,230,470
rrect(FX,FY,FW,FH,32,BODY)
rrect(FX+10,FY+10,FW-20,FH-20,24,SCREEN,sw=1.5)
s.circle(FX+FW/2,FY+28,7,fill="#11161a",sw=1.5)                         # front camera
for r in range(5):
    for c in range(4):
        x=FX+28+c*46; y=FY+70+r*58
        rrect(x,y,34,34,8,ICON[(r*4+c)%6],sw=1.2)
s.text(FX+FW/2,FY+FH+40,"the front",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the inside, back taken off =================
BX,BY=400,175
rrect(BX,BY,FW,FH,32,FRAME)
rrect(BX+12,BY+12,FW-24,FH-24,24,"#5a5e63",sw=1.5)
# the gaps in the metal frame that let the aerials work
for (x,y) in ((BX+40,BY),(BX+FW-40,BY),(BX+40,BY+FH),(BX+FW-40,BY+FH)):
    s.path([(x-4,y-5),(x+4,y-5),(x+4,y+5),(x-4,y+5)],fill="#e9e3d3",close=True,sw=1.2)
# the board along the top, with the main chip
s.path([(BX+22,BY+24),(BX+FW-22,BY+24),(BX+FW-22,BY+170),(BX+22,BY+170)],fill=BOARD,close=True,sw=2)
s.path([(BX+110,BY+70),(BX+176,BY+70),(BX+176,BY+136),(BX+110,BY+136)],fill=CHIPC,close=True,sw=2)
for k in range(1,4): s.line(BX+110+k*16.5,BY+76,BX+110+k*16.5,BY+130,stroke="#55585c",sw=0.8)
for (x,y,w,h) in ((BX+40,BY+120,40,26),(BX+186,BY+40,22,40),(BX+186,BY+100,22,22)):
    s.path([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],fill="#2f3337",close=True,sw=1.2)
# the cameras, top left
for (cx,cy,r) in ((BX+58,BY+56,20),(BX+58,BY+56+0,0)):
    if r: s.circle(cx,cy,r,fill="#1d2124",sw=2.5); s.circle(cx,cy,r-9,fill="#3d5566",sw=1.5)
s.circle(BX+96,BY+48,13,fill="#1d2124",sw=2); s.circle(BX+96,BY+48,5,fill="#3d5566",sw=1)
# the battery, filling most of the rest
s.path([(BX+26,BY+186),(BX+FW-26,BY+186),(BX+FW-26,BY+FH-60),(BX+26,BY+FH-60)],fill=BATT,close=True,sw=2.5)
s.text(BX+FW/2,BY+300,"Li-ion",anchor="middle",size=20,halo=BATT,fill="#6b5a2a")
# speaker and port at the bottom
s.path([(BX+80,BY+FH-44),(BX+150,BY+FH-44),(BX+150,BY+FH-28),(BX+80,BY+FH-28)],fill="#2f3337",close=True,sw=1.2)
s.text(BX+FW/2,BY+FH+40,"the inside",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= inset: a finger on the glass, cut across =================
IX,IY,IR=990,330,150
s.inset(IX,IY,IR)
s.text(IX,IY+IR+38,"the screen, cut across",anchor="middle",italic=True)
GY=IY+10
# display underneath, with its coloured dots
s.path([(IX-142,GY+42),(IX+142,GY+42),(IX+130,GY+90),(IX-130,GY+90)],fill="#2b2f33",close=True,sw=2)
for k in range(-6,7):
    s.circle(IX+k*20,GY+62,4,fill=["#c9473a","#6fb26a","#5a86c9"][(k+6)%3],sw=0)
# touch layer: rows of fine transparent wires, seen end on
s.path([(IX-146,GY+18),(IX+146,GY+18),(IX+146,GY+42),(IX-146,GY+42)],fill="#e6eef0",close=True,sw=1.5)
for k in range(-6,7): s.circle(IX+k*20,GY+30,4.5,fill=ACC,sw=1)
# cover glass on top
s.path([(IX-148,GY-16),(IX+148,GY-16),(IX+148,GY+18),(IX-148,GY+18)],fill=GLASSC,close=True,sw=2)
# the fingertip resting on the glass
s.raw_path(f"M {IX-62},{GY-130} L {IX-52},{GY-40} Q {IX-40},{GY-14} {IX},{GY-16} Q {IX+40},{GY-14} {IX+52},{GY-40} L {IX+62},{GY-130}",fill="#e3b99a",sw=2.5)
# field lines from the wires to the finger
for dx in (-20,0,20):
    s.raw_path(f"M {IX+dx},{GY+26} Q {IX+dx*1.6},{GY+4} {IX+dx*0.8},{GY-16}",stroke=ACC,sw=1.5,extra='stroke-dasharray="3 4"')

s.callout(1,IX+60,GY+30,1150,560,"A grid of fine wires|feels the finger's charge",anchor="end")
s.callout(2,BX+FW-30,BY+330,730,700,"A lithium battery fills|most of the inside")
s.callout(3,BX+143,BY+103,730,620,"One chip does|the computing")
s.callout(4,BX+FW-40,BY-1,700,150,"Gaps in the frame|let radio waves out")
s.callout(5,BX+58,BY+56,370,140,"Cameras, back and front",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","109-smartphone","smartphone"))
