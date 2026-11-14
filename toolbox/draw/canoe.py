import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The voyaging canoe","about 1,000 years ago")
WATER="#9fb8c8"
# hull from the side, bow to the right
s.raw_path("M 150,430 C 180,470 240,490 330,492 L 800,492 C 880,490 930,470 960,420 L 930,440 L 190,440 Z",fill=WOOD)
s.line(205,455,925,455,sw=1.5)
# deck and shelter
s.add(f'<rect x="330" y="418" width="470" height="22" fill="{BONE}" stroke="{INK}" stroke-width="2.5"/>')
s.raw_path("M 430,418 L 430,372 Q 500,350 570,372 L 570,418 Z",fill=HIDE,sw=2.5)
# two masts with claw-shaped sails
for mx in (380,650):
    s.line(mx,418,mx+40,180,sw=4)
    s.raw_path(f"M {mx+38},{190} Q {mx+150},{210} {mx+190},{300} Q {mx+120},{330} {mx+10},{400} Z",fill=ACC,sw=2.5)
    for k in range(4): s.raw_path(f"M {mx+36-k*6},{230+k*42} Q {mx+110},{250+k*26} {mx+178-k*18},{296+k*8}",sw=1,stroke=PAPER)
# steering paddle
s.line(230,380,120,520,sw=5); s.raw_path("M 130,508 L 96,548 L 112,556 L 142,518 Z",fill=WOOD,sw=2)
for x in range(60,1140,90): s.raw_path(f"M {x},500 q 22,-9 45,0 t 45,0",stroke=WATER,sw=2)
# from above
ix,iy,r=1000,215,105
s.inset(ix,iy,r,caption="From above")
for dy in (-34,34): s.raw_path(f"M {ix-80},{iy+dy} Q {ix},{iy+dy-16} {ix+80},{iy+dy} Q {ix},{iy+dy+16} {ix-80},{iy+dy} Z",fill=WOOD,sw=2.5)
s.add(f'<rect x="{ix-40}" y="{iy-36}" width="80" height="72" fill="{BONE}" stroke="{INK}" stroke-width="2.2"/>')
s.callout(1,ix-62,iy-36,760,130,"Two long hulls|lashed side by side",anchor="end")
s.callout(2,620,428,520,620,"A deck between them|for families, pigs,|dogs and seedlings")
s.callout(3,470,290,250,200,"Sails of|woven matting",anchor="end")
s.callout(4,160,470,150,640,"A long paddle|to steer by")
s.callout(5,860,470,1150,620,"Planks sewn together|with cord, without|a single nail",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","02-voyaging-canoe","voyaging-canoe"))
