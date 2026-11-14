import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The siege ram","about 2,700 years ago")
WATER="#7fa3b8"
def gy(x): return 610-(x-120)*0.16          # the ramp's surface
# ramp and wall
s.path([(120,610),(900,gy(900)),(900,640),(120,640)],fill=STONE,close=True)
for i in range(26):
    x=150+i*29; s.circle(x,gy(x)+12+(i%3)*5,5,sw=1.2)
s.add(f'<rect x="900" y="190" width="110" height="450" fill="{CLAY}" stroke="{INK}" stroke-width="3"/>')
for k in range(4): s.add(f'<rect x="{900+k*30}" y="168" width="18" height="24" fill="{CLAY}" stroke="{INK}" stroke-width="2.5"/>')
for j in range(9):
    y=230+j*46; s.line(900,y,1010,y,sw=1.2)
    for k in range(3): s.line(925+k*36+(j%2)*14,y,925+k*36+(j%2)*14,y+46,sw=1.2)
# the machine
x1,x2=520,740; y1,y2=gy(x1),gy(x2)
s.path([(x1,y1-44),(x2,y2-44),(x2,y2-165),(690,y2-172),(690,y2-240),(625,y2-240),(625,y2-168),(x1,y1-156)],fill=HIDE,close=True)
for (wx) in (565,695): s.circle(wx,gy(wx)-24,24,fill=WOOD,sw=3); s.circle(wx,gy(wx)-24,5,fill=INK,sw=0)
for i in range(5): s.line(x1+20+i*44,y1-150+i*2,x1+20+i*44,y1-50-i*6,sw=1.2)
# the beam
bx1,by1,bx2,by2=700,y2-120,898,y2-168
s.line(bx1,by1,bx2,by2,stroke=ACC,sw=11); s.path([(bx2-4,by2-14),(bx2+10,by2-3),(bx2+2,by2+12)],fill=ACC,stroke=ACC,close=True)
# the water ladle and a falling torch
s.line(660,y2-236,800,y2-205,sw=3); s.raw_path(f"M 796,{y2-212} l 16,2 l -3,14 l -12,-2 Z",fill=METAL,sw=2)
for d in range(3): s.line(806+d*5,y2-190+d*4,806+d*5,y2-170+d*6,stroke=WATER,sw=2.5)
s.raw_path(f"M 840,{y2-250} q 10,-22 2,-40 q 16,16 12,40 Z",fill="#e0a030",sw=1.5); s.line(846,y2-250,832,y2-226,sw=3)
# the chain
s.line(905,200,880,by2+6,sw=3,dash="5 5")
s.callout(1,600,y1-100,300,400,"A frame on wheels,|covered against|arrows and fire",anchor="end")
s.callout(2,790,(by1+by2)/2,640,180,"A long beam is driven|at the brickwork",anchor="end")
s.callout(3,300,gy(300)+16,330,700,"A ramp of stones brings it|up to the wall")
s.callout(4,770,y2-212,430,260,"A man pours water|where torches land",anchor="end")
s.callout(5,892,300,1150,700,"The defenders lower a|chain to catch the beam",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","12-siege-ram","siege-ram"))
