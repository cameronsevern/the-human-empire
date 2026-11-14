import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The spear","more than 400,000 years ago")
# the whole spear
s.line(140,470,900,470,stroke=INK,sw=13); s.line(140,470,900,470,stroke="#c9a56b",sw=9)
s.path([(896,455),(980,470),(896,485)],fill=STONE,close=True)
for k in range(5): s.line(880-k*9,458,876-k*9,482,sw=2.5,stroke=ACC)
s.line(140,560,980,560,sw=2); s.line(140,551,140,569,sw=2); s.line(980,551,980,569,sw=2); s.text(560,592,"a little taller than the person who carries it",anchor="middle",italic=True,size=19)
# close view of the point
ix,iy,r=930,250,130
s.inset(ix,iy,r,caption="The point, close up")
s.add(f'<rect x="{ix-110}" y="{iy-14}" width="120" height="28" fill="#c9a56b" stroke="{INK}" stroke-width="2.5"/>')
s.path([(ix-10,iy-34),(ix+100,iy),(ix-10,iy+34),(ix-40,iy)],fill=STONE,close=True)
s.raw_path(f"M {ix-44},{iy-20} L {ix-6},{iy-26} L {ix-6},{iy+26} L {ix-44},{iy+20} Z",fill="#5a4a40",sw=2)
for k in range(5): s.line(ix-92+k*11,iy-16,ix-96+k*11,iy+16,sw=3,stroke=ACC)
s.callout(1,420,470,330,330,"A straight shaft of wood,|scraped smooth",anchor="end")
s.callout(2,ix+50,iy,760,130,"A point of stone,|added later",anchor="end")
s.callout(3,ix-24,iy+18,700,330,"Glue of resin or tar|holds it in a notch",anchor="end")
s.callout(4,ix-70,iy-10,640,220,"Sinew is bound|over the join",anchor="end")
s.callout(5,760,470,640,680,"Heaviest toward the front,|so that it flies point first")
s.save(os.path.join(os.path.dirname(__file__),"..","04-spear","spear"))
