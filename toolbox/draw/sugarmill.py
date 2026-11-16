import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The sugar mill","Brazil from the early 1600s; the Caribbean from the 1640s")
IRON="#7d8488"; CANE="#b9c27a"; JUICE="#e2c46a"; OX="#c9b08c"; HOUSE="#e2d3b8"; COPPER="#c98a5a"
G=640
s.line(60,G,1140,G,stroke=SOFT,sw=1.5)

# ---- the mill: three upright rollers in a wooden frame, standing on a bed that catches the juice
MX=560                                         # middle roller
RW=56; RG=6; RT=380; RB=572
s.path([(400,RB),(720,RB),(720,G),(400,G)],fill=STONE,close=True,sw=3)            # the masonry base
s.path([(410,RB-10),(710,RB-10),(716,RB+8),(404,RB+8)],fill=WOOD,close=True,sw=2.5)  # the bed
for x in (418,690):                                                                # the frame
    s.path([(x,300),(x+14,300),(x+14,RB-10),(x,RB-10)],fill=WOOD,close=True,sw=2.5)
s.path([(398,300),(722,300),(722,326),(398,326)],fill=WOOD,close=True,sw=2.5)
for k in (-1,0,1):
    x0=MX+k*(RW+RG)-RW/2
    s.path([(x0,RT),(x0+RW,RT),(x0+RW,RB-12),(x0,RB-12)],fill=ACC,close=True,sw=3)
    for y in (RT+40,RT+110,RT+170):                                                # iron hoops
        s.line(x0+2,y,x0+RW-2,y,stroke="#7a3a2a",sw=2)
    # cogs round the top of each roller
    s.path([(x0-4,RT-30),(x0+RW+4,RT-30),(x0+RW+4,RT-4),(x0-4,RT-4)],fill=WOOD,close=True,sw=2.5)
    for j in range(5):
        tx=x0+2+j*(RW/4.6)
        s.path([(tx,RT-38),(tx+7,RT-38),(tx+7,RT-30),(tx,RT-30)],fill=WOOD,close=True,sw=1.6)
# a stalk of cane going in between the middle and the right-hand roller
s.path([(MX+30,470),(MX+190,430),(MX+194,440),(MX+32,480)],fill=CANE,close=True,sw=2)
for f in (0.35,0.7): s.line(MX+30+160*f,470-40*f,MX+34+160*f,480-40*f,stroke="#6f7a3a",sw=2)
# the upright shaft of the middle roller, rising through the frame to the sweep
s.path([(MX-9,326),(MX+9,326),(MX+9,206),(MX-9,206)],fill=WOOD,close=True,sw=2.5)
s.path([(MX-9,RT-38),(MX+9,RT-38),(MX+9,300),(MX-9,300)],fill=WOOD,close=True,sw=2.5)
# ---- the sweep, a long pole sloping down to the oxen
SX,SY=300,452
s.path([(MX,214),(MX,230),(SX,SY+6),(SX-4,SY-6)],fill=WOOD,close=True,sw=2.5)
# the ox, walking to the left and dragging the end of the sweep after it
OY=518
for lx in (175,200,290,315):
    s.path([(lx-11,OY+20),(lx+11,OY+20),(lx+9,G),(lx-9,G)],fill=OX,close=True,sw=2)
s.ellipse(245,OY,98,48,fill=OX,sw=2.5)
s.path([(165,486),(118,494),(84,528),(88,552),(112,558),(160,536)],fill=OX,close=True,sw=2.5)   # neck and head
s.raw_path("M 112,496 C 100,484 98,470 108,462",sw=3)
s.raw_path("M 124,492 C 128,478 140,470 150,472",sw=3)
s.circle(108,518,3,fill=INK,sw=0)
s.raw_path("M 340,500 C 352,520 350,560 344,590",sw=2.5)
s.path([(150,472),(162,472),(162,540),(150,540)],fill=WOOD,close=True,sw=2)                    # yoke
s.raw_path(f"M {SX-2},{SY} L 162,486",stroke="#7a5a3c",sw=3)                                     # trace

# ---- the gutter, running down from the bed to the boiling house
s.path([(712,RB+4),(930,612),(930,624),(712,RB+16)],fill=JUICE,close=True,sw=2.5)
s.raw_path(f"M 712,{RB+16} L 930,624",sw=3)
# the boiling house, cut open to show its kettles over the furnace
s.path([(930,500),(1150,500),(1150,G),(930,G)],fill=HOUSE,close=True,sw=3)
s.path([(918,500),(1040,430),(1162,500)],fill="#b98a5e",close=True,sw=3)
s.path([(1100,456),(1124,456),(1124,410),(1100,410)],fill=STONE,close=True,sw=2.5)
s.path([(945,585),(1135,585),(1135,G),(945,G)],fill=STONE,close=True,sw=2.5)
for i,x in enumerate((975,1025,1070,1110)):
    r=22-i*3
    s.raw_path(f"M {x-r},585 C {x-r},{585+r} {x+r},{585+r} {x+r},585 Z",fill=COPPER,sw=2)
    s.ellipse(x,585,r,4,fill=JUICE,sw=1.5)
for x in (990,1060): s.raw_path(f"M {x},{G-6} C {x-8},{G-26} {x+8},{G-30} {x},{G-44}",stroke=ACC,sw=2.5)

# ---- inset: the rollers from above, and the path of the cane
CX,CY,RR=1000,250,118
s.inset(CX,CY,RR)
for k in (-1,0,1):
    s.circle(CX+k*58,CY,27,fill=ACC,sw=2.5)
# in between the middle and right rollers, coming from below
s.path([(CX+29,CY+105),(CX+29,CY-20)],stroke=CANE,sw=9)
s.raw_path(f"M {CX+29},{CY-20} C {CX+29},{CY-80} {CX-29},{CY-80} {CX-29},{CY-20}",stroke=CANE,sw=7)
s.path([(CX-29,CY-20),(CX-29,CY+100)],stroke=CANE,sw=5)
s.arrow(CX+60,CY+96,CX+60,CY+48)
s.arrow(CX-60,CY+48,CX-60,CY+96)
s.text(CX,CY-RR-14,"From above",anchor="middle",italic=True)

s.callout(1,MX,500,560,690,"Three upright rollers,|cased in iron",anchor="end")
s.callout(2,MX+RW+RG-10,RT-20,800,385,"Cogs at the top|turn the outer two")
s.callout(3,420,360,300,250,"Oxen drag a sweep that|turns the middle one",anchor="end")
s.callout(4,CX-29,CY-62,850,110,"Cane fed in, then|passed back again",anchor="end")
s.callout(5,820,598,770,690,"Juice runs down a gutter|to the boiling house")
s.save(os.path.join(os.path.dirname(__file__),"..","53-sugar-mill","sugar-mill"))
