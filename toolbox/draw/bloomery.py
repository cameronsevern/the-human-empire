import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The bloomery","about 3,000 years ago")
G=650  # ground line
CHAR="#4a433d"; ORE="#a58a6a"; SLAG="#6b625b"
s.line(40,G,1160,G,sw=3)
# shaft, cut open: outer wall and inner space (tapering upwards)
def xl(y,inner=False): return 470+(G-y)*40/460+(38 if inner else 0)
def xr(y,inner=False): return 730-(G-y)*40/460-(38 if inner else 0)
top=190
s.path([(xl(G),G),(xl(top),top),(xr(top),top),(xr(G),G)],fill=CLAY,close=True)
# charge in layers
ys=list(range(210,580,37))
for i,y in enumerate(ys):
    y2=y+37
    s.path([(xl(y,1),y),(xr(y,1),y),(xr(y2,1),y2),(xl(y2,1),y2)],fill=(CHAR if i%2==0 else ORE),sw=1.5,close=True)
# hearth at the bottom: slag pool and bloom
s.path([(xl(580,1),580),(xr(580,1),580),(xr(G-12,1),G-12),(xl(G-12,1),G-12)],fill=SLAG,sw=1.5,close=True)
s.raw_path("M 560,628 Q 548,600 575,590 Q 600,578 628,592 Q 655,604 640,628 Q 600,640 560,628 Z",fill=ACC,sw=3)
for (x,y) in ((580,606),(604,598),(622,612),(596,620)): s.circle(x,y,3.5,fill=SLAG,sw=0)
# inner outline
s.path([(xl(G-12,1),G-12),(xl(top,1),top)],sw=3); s.path([(xr(G-12,1),G-12),(xr(top,1),top)],sw=3)
# tap hole and slag running out to the right
s.path([(xr(626,1)-2,622),(742,626),(742,640),(xr(640,1)-2,638)],fill=SLAG,sw=1.5,close=True)
s.raw_path("M 738,628 Q 800,640 860,646 Q 900,650 915,662 L 915,668 Q 820,676 745,650 Z",fill=SLAG,sw=2.5)
# air pipe through the left wall, sloping down, and bag bellows
s.path([(395,548),(xl(590,1)+6,586),(xl(604,1)+6,602),(390,566)],fill=CLAY,close=True)
s.raw_path("M 395,540 Q 330,490 250,520 Q 200,545 215,600 Q 240,640 330,625 Q 380,612 395,574 Z",fill=HIDE,sw=3)
s.raw_path("M 262,522 Q 250,470 300,455",sw=5,stroke=INK)
s.line(250,560,360,590,sw=1.5,stroke=SOFT); s.line(245,590,340,612,sw=1.5,stroke=SOFT)
s.arrow(420,548,470,560)
s.callout(2,600,228,790,150,"Charcoal and broken ore|go in at the top, in layers")
s.callout(1,xr(330)-12,330,840,290,"A clay shaft about|as tall as a child")
s.callout(3,300,500,350,390,"Bellows blow air in|through a clay pipe",anchor="end")
s.callout(5,612,604,840,430,"The bloom: a spongy lump|of iron, left at the bottom")
s.callout(4,850,650,840,555,"Molten slag runs out|through a hole at the base")
s.save(os.path.join(os.path.dirname(__file__),"..","12-bloomery","bloomery"))
