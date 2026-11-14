import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The Nile boat","about 5,000 years ago")
WATER="#9fb8c8"
def hull(x,y):
    s.raw_path(f"M {x-190},{y-30} C {x-150},{y+26} {x-90},{y+34} {x},{y+34} C {x+90},{y+34} {x+150},{y+26} {x+190},{y-30} L {x+150},{y-6} L {x-150},{y-6} Z",fill=WOOD)
    s.line(x-160,y+60,x-120,y-6,sw=5)       # steering oar
# going south: sail up
x,y=320,470
hull(x,y); s.line(x,y-6,x,y-250,sw=5); s.line(x-110,y-240,x+110,y-240,sw=3); s.line(x-110,y-70,x+110,y-70,sw=3)
s.add(f'<rect x="{x-105}" y="{y-238}" width="210" height="166" fill="{ACC}" stroke="{INK}" stroke-width="2.5"/>')
s.text(x,y+108,"Going south",anchor="middle",italic=True)
# going north: sail and mast down, oars out
x2=820
hull(x2,y); s.line(x2-120,y-22,x2+120,y-22,sw=5)
for k in range(5): s.line(x2-80+k*40,y,x2-110+k*40,y+70,sw=3)
s.text(x2,y+108,"Going north",anchor="middle",italic=True)
for xx in range(60,1140,90): s.raw_path(f"M {xx},{y+44} q 22,-9 45,0 t 45,0",stroke=WATER,sw=2)
# wind and current
s.arrow(700,170,470,170); s.text(585,150,"wind from the north",anchor="middle",italic=True,size=19)
s.arrow(470,640,700,640); s.text(585,676,"current to the north",anchor="middle",italic=True,size=19)
s.callout(1,x+60,y-170,560,230,"A square sail, hoisted|to be blown upstream")
s.callout(2,x2,y-22,1140,300,"Sail and mast are laid|flat to drift down|with the current",anchor="end")
s.callout(3,x2+20,y+40,1000,640,"Oars keep her|in the stream")
s.callout(4,x-140,y+28,120,640,"A long oar at the|stern steers her")
s.callout(5,x+150,y+10,560,390,"A hull of planks|tied with rope")
s.save(os.path.join(os.path.dirname(__file__),"..","07-nile-boat","nile-boat"))
