import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The flying buttress","northern France, from about 1160")
GLASS="#b7c9d3"; ROOF="#a58c6f"; G=690; C=600
def both(fn):
    fn(1); fn(-1)
def X(sign,dx): return C+sign*dx
s.line(60,G,1140,G,stroke=SOFT,sw=1.5)
# timber roof over the vault
s.path([(X(-1,104),262),(C,140),(X(1,104),262)],fill=ROOF,close=True,sw=3)
for k in range(1,4):
    y=140+k*30; w=104*(y-140)/122; s.line(round(C-w),y,round(C+w),y,stroke=INK,sw=1.2)
def side(g):
    # nave pier and the wall above it, with the high window
    s.path([(X(g,80),G),(X(g,80),262),(X(g,98),262),(X(g,98),G)],fill=STONE,close=True,sw=3)
    s.path([(X(g,82),450),(X(g,82),340),(X(g,89),326),(X(g,96),340),(X(g,96),450)],fill=GLASS,close=True,sw=2)
    # the aisle: a low vault and a sloping roof
    s.path([(X(g,98),470),(X(g,210),520),(X(g,210),532),(X(g,98),484)],fill=ROOF,close=True,sw=2.5)
    s.raw_path(f"M {X(g,98)},560 Q {X(g,154)},520 {X(g,200)},560",sw=2.5)
    # the aisle's outer wall with a window, joined to the buttress pier
    s.path([(X(g,200),G),(X(g,200),532),(X(g,214),526),(X(g,214),G)],fill=STONE,close=True,sw=3)
    s.path([(X(g,203),660),(X(g,203),580),(X(g,207),570),(X(g,211),580),(X(g,211),660)],fill=GLASS,close=True,sw=1.5)
    # the outer buttress pier and its pinnacle
    s.path([(X(g,214),G),(X(g,214),410),(X(g,262),410),(X(g,262),G)],fill=STONE,close=True,sw=3)
    s.path([(X(g,220),410),(X(g,238),330),(X(g,256),410)],fill=STONE,close=True,sw=3)
    for y in (450,520,600): s.line(X(g,214),y,X(g,262),y,stroke=SOFT,sw=1.2)
    # the flying arm: a sloping top and an arched underside, from pier to wall
    s.raw_path(f"M {X(g,214)},418 L {X(g,98)},330 L {X(g,98)},356 Q {X(g,150)},372 {X(g,214)},460 Z",fill=ACC,sw=3)
both(side)
# the high vault: a pointed arch on ribs, springing from the piers
s.raw_path(f"M {X(-1,80)},340 Q {X(-1,74)},292 {C},270 Q {X(1,74)},292 {X(1,80)},340",fill="none",sw=5)
s.raw_path(f"M {X(-1,80)},340 Q {X(-1,40)},300 {C},286",stroke=SOFT,sw=2)
s.raw_path(f"M {X(1,80)},340 Q {X(1,40)},300 {C},286",stroke=SOFT,sw=2)
# where the weight goes: on the right, down the pier and out along the arm
def a(x1,y1,x2,y2): s.arrow(x1,y1,x2,y2)
a(X(1,30),300,X(1,64),336)                        # vault presses out and down
a(X(1,120),352,X(1,196),410)                     # along the flying arm
a(X(1,238),440,X(1,238),640)                     # down the outer pier
a(X(-1,89),500,X(-1,89),640)                     # and down the nave pier

s.callout(1,C-30,276,330,180,"A pointed vault on|thin stone ribs",anchor="end")
s.callout(2,X(-1,89),600,310,600,"The pier takes|the weight down",anchor="end")
s.callout(3,X(1,150),370,895,250,"The flying arm|carries the push|over the aisle")
s.callout(4,X(1,240),370,895,500,"The outer pier,|weighted by its|pinnacle")
s.callout(5,X(-1,89),370,310,300,"Glass, where a|wall used to be",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","36-flying-buttress","flying-buttress"))
