import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The coin die","about 2,600 years ago")
G=690
s.line(40,G,1160,G,sw=3)
# anvil block, cut open
s.path([(430,G),(450,500),(750,500),(770,G)],fill=WOOD,close=True)
for y in (540,585,630): s.line(455,y,745,y+6,stroke=SOFT,sw=1.5)
# lower die set into the block (accent), hollow picture in its top face
s.path([(560,600),(560,476),(640,476),(640,600)],fill=ACC,close=True)
s.raw_path("M 578,476 Q 600,492 622,476",fill=PAPER,sw=2.5)
# blank resting on the die
s.ellipse(600,462,30,12,fill="#d8c98a")
# upper die (punch), held above
s.path([(574,420),(570,250),(630,250),(626,420)],fill=METAL,close=True)
s.raw_path("M 584,420 Q 600,410 616,420",fill=PAPER,sw=2.5)
s.ellipse(600,250,30,8,fill=METAL)
# hammer
s.add(f'<rect x="545" y="135" width="130" height="62" rx="8" fill="{METAL}" stroke="{INK}" stroke-width="3"/>')
s.path([(675,158),(960,118),(962,136),(675,176)],fill=WOOD,close=True)
s.arrow(520,150,520,225)
# finished coin
s.circle(990,585,62,fill="#d8c98a")
s.circle(990,585,50,sw=1.5,stroke=SOFT)
s.raw_path("M 962,600 Q 955,570 980,560 Q 1005,548 1022,570 Q 1030,590 1012,598 L 1022,610 Q 990,622 962,600 Z",sw=2.5)
s.circle(1000,575,4,fill=INK,sw=0)
s.callout(1,572,540,400,570,"The lower die, set in an|anvil, its picture cut hollow|and back to front",anchor="end")
s.callout(2,575,462,400,400,"The blank: a weighed|lump of metal",anchor="end")
s.callout(3,622,330,820,330,"The upper die, held|upright like a chisel")
s.callout(4,660,185,820,215,"A hard blow|of the hammer")
s.callout(5,978,524,950,395,"The coin comes out|with a picture|on each face")
s.save(os.path.join(os.path.dirname(__file__),"..","15-coin-die","coin-die"))
