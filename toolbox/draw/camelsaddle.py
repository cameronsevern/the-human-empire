import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The camel saddle","northern Arabia, by about 2,000 years ago")
CAMEL="#dcc39a"; PAD="#cfc0a2"; BAG="#b98a5e"; SKIN="#a08463"; CUSH="#c9a77a"
G=712
s.line(60,G,1140,G,stroke=SOFT,sw=1.5)
def leg(xt,yt,xk,yk,xf,w=15):
    s.raw_path(f"M {xt-w-6},{yt} C {xt-w},{yt+60} {xk-w},{yk-40} {xk-w+2},{yk} L {xf-8},{G-8} L {xf+8},{G-8} "
               f"L {xk+w-2},{yk} C {xk+w},{yk-40} {xt+w},{yt+60} {xt+w+8},{yt} Z",fill=CAMEL,sw=2.5)
    s.ellipse(xk,yk,w+1,13,fill=CAMEL,sw=2)
    s.ellipse(xf+4,G-5,20,7,fill=CAMEL,sw=2)
# far legs a shade darker, then the body, then the near legs
FAR="#cdb38a"
for (xt,xk,xf) in ((350,336,342),(668,680,672)):
    s.raw_path(f"M {xt-12},470 L {xk-10},590 L {xf-7},{G-8} L {xf+7},{G-8} L {xk+10},590 L {xt+12},470 Z",fill=FAR,sw=2)
    s.ellipse(xk,590,12,11,fill=FAR,sw=2)
    s.ellipse(xf+4,G-5,18,6,fill=FAR,sw=2)
# the body: rump at the left, hump in the middle, neck and head at the right
s.raw_path("M 318,318 C 350,270 390,250 428,250 C 470,250 515,290 545,332 C 580,348 620,350 650,356 "
           "C 720,370 770,330 800,280 C 815,250 840,236 870,240 C 900,244 918,256 912,270 "
           "C 905,280 880,280 868,284 C 850,300 835,340 800,400 C 770,445 720,470 680,478 "
           "C 600,496 420,500 340,478 C 270,470 230,430 232,390 C 235,350 280,330 318,318 Z",fill=CAMEL,sw=3)
s.circle(884,254,3.5,fill=INK,sw=0)
s.raw_path("M 858,244 C 860,232 868,230 874,236",sw=2)
s.raw_path("M 236,382 C 214,400 208,440 214,490",sw=3)    # tail
leg(306,462,296,590,300)
leg(626,470,640,590,632)
# stuffed pads on the flank, under the side bars
s.raw_path("M 318,350 C 340,340 380,338 400,342 L 400,372 C 370,370 340,374 318,380 Z",fill=PAD,sw=2.5)
s.raw_path("M 462,342 C 490,338 530,344 552,354 L 552,384 C 525,376 492,372 462,372 Z",fill=PAD,sw=2.5)
# a waterskin hung behind, from the rear post
s.raw_path("M 300,286 C 270,300 254,340 262,380 C 270,410 300,412 312,392 C 322,360 318,316 300,286 Z",fill=SKIN,sw=2.5)
s.line(350,214,300,288,sw=1.8)
# the frame seen from the side: each arch shows as one tall post; side bars join them
for (top,foot) in (((346,186),(362,350)),((506,186),(492,350))):
    s.line(*foot,*top,stroke=INK,sw=13); s.line(*foot,*top,stroke=ACC,sw=8)
    s.circle(top[0],top[1]-4,9,fill=ACC,sw=2.5)
for y in (300,336):
    s.line(330,y,530,y,stroke=INK,sw=10); s.line(330,y,530,y,stroke=WOOD,sw=5)
# the rider's cushion, laid over the hump between the posts
s.raw_path("M 360,250 C 400,236 450,236 494,250 L 490,276 C 450,264 400,264 364,276 Z",fill=CUSH,sw=2.5)
# a bag hung in front, from the front post
s.raw_path("M 520,300 L 600,300 C 612,350 604,400 580,420 L 540,420 C 516,400 510,350 520,300 Z",fill=BAG,sw=2.5)
for x in (548,568,588):
    s.line(x-4,420,x-8,456,stroke=BAG,sw=3); s.circle(x-8,460,4,fill=BAG,sw=1.5)
s.line(510,214,530,300,sw=1.8); s.line(510,214,590,300,sw=1.8)
# girth under the belly
s.line(430,350,430,484,stroke=INK,sw=2,dash="9 6")
# inset: the front arch seen from in front, standing over the hump
cx,cy,r=1030,250,105
s.inset(cx,cy,r)
s.text(cx,cy-r-14,"Seen from in front",anchor="middle",italic=True)
s.raw_path(f"M {cx-80},{cy+95} C {cx-70},{cy+30} {cx-35},{cy+5} {cx},{cy+2} C {cx+35},{cy+5} {cx+70},{cy+30} {cx+80},{cy+95}",fill=CAMEL,sw=2.5)
s.ellipse(cx-56,cy+48,15,24,fill=PAD,sw=2,rot=-30); s.ellipse(cx+56,cy+48,15,24,fill=PAD,sw=2,rot=30)
s.path([(cx-60,cy+40),(cx,cy-40),(cx+60,cy+40)],stroke=INK,sw=12)
s.path([(cx-60,cy+40),(cx,cy-40),(cx+60,cy+40)],stroke=ACC,sw=7)
s.line(cx,cy-40,cx,cy-82,stroke=INK,sw=11); s.line(cx,cy-40,cx,cy-82,stroke=ACC,sw=6)
s.circle(cx,cy-86,8,fill=ACC,sw=2.5)
s.callout(1,cx-45,cy+25,960,450,"Two wooden|arches stand|over the hump")
s.callout(2,345,300,240,230,"Side bars|join them",anchor="end")
s.callout(3,360,365,230,560,"Stuffed pads|keep the wood|off the camel",anchor="end")
s.callout(4,440,248,600,170,"The rider's cushion,|on top of the frame")
s.callout(5,582,398,800,600,"Bags and waterskins|hang from the posts")
s.save(os.path.join(os.path.dirname(__file__),"..","28-camel-saddle","camel-saddle"))
