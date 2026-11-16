import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The Maxim gun","London, 1884")
JACKET="#b9c0c4"; DARK="#4b4f52"; BRASS="#d4b25a"; BELT="#c9b48e"; TRIPOD="#6f7579"; GROUND=575

s.line(60,GROUND,780,GROUND,stroke=SOFT,sw=1.5)
s.path([(800,405),(1150,405),(1150,672),(800,672)],fill="#f6efe2",close=True,stroke=SOFT,sw=1.5)

# ================= tripod and ammunition box =================
s.line(500,330,360,GROUND,stroke=TRIPOD,sw=9)
s.line(520,330,680,GROUND,stroke=TRIPOD,sw=9)
s.circle(510,325,12,fill=DARK,sw=2)
s.path([(200,GROUND-46),(300,GROUND-46),(300,GROUND),(200,GROUND)],fill="#a87e55",close=True,sw=2.5)
# the belt, from the box up into the feed block
s.raw_path("M 250,529 C 260,430 440,420 528,312",stroke=BELT,sw=16)
for t in range(9):
    u=t/8; x=(1-u)**3*250+3*(1-u)**2*u*260+3*(1-u)*u*u*440+u**3*528
    y=(1-u)**3*529+3*(1-u)**2*u*430+3*(1-u)*u*u*420+u**3*312
    s.circle(round(x,1),round(y,1),4,fill=BRASS,sw=1)

# ================= the gun =================
s.path([(140,248),(485,248),(485,302),(140,302)],fill=JACKET,close=True,sw=3)            # water jacket
for x in (200,300,400): s.line(x,248,x,302,stroke="#8f979b",sw=1.5)
s.circle(250,240,7,fill=DARK,sw=1.5)                                                    # filler cap
s.path([(100,268),(140,268),(140,282),(100,282)],fill=DARK,close=True,sw=2)              # muzzle
s.path([(485,236),(720,236),(720,312),(485,312)],fill=DARK,close=True,sw=3)              # receiver box
s.path([(505,226),(560,226),(560,236),(505,236)],fill=DARK,close=True,sw=2)              # feed block
s.path([(590,252),(690,252),(690,296),(590,296)],fill=ACC,close=True,sw=2.5)             # lock and toggle, seen through the side
s.line(640,296,668,334,stroke=INK,sw=6); s.circle(668,336,7,fill=INK,sw=0)               # crank handle
s.path([(600,312),(700,312),(700,326),(600,326)],fill="#8f979b",close=True,sw=2)         # spring box on the side
s.raw_path("M 720,250 C 760,250 770,232 770,218",stroke=INK,sw=7)                        # spade grips
s.raw_path("M 720,298 C 760,298 770,316 770,330",stroke=INK,sw=7)
s.line(728,274,748,274,stroke=INK,sw=6)                                                  # thumb trigger

# ================= inside the lock, before and after the kick =================
def lockstate(y,folded):
    s.path([(820,y-8),(905,y-8),(905,y+8),(820,y+8)],fill=JACKET,close=True,sw=2)        # rear of barrel
    lx=905 if not folded else 950
    s.path([(lx,y-20),(lx+48,y-20),(lx+48,y+20),(lx,y+20)],fill=ACC,close=True,sw=2.5)   # the lock
    px=1110
    s.circle(px,y,7,fill=INK,sw=0)
    if not folded:
        s.line(lx+48,y,1030,y,stroke=INK,sw=6); s.line(1030,y,px,y,stroke=INK,sw=6)
        s.circle(1030,y,6,fill=PAPER,sw=2)
    else:
        kx,ky=1050,y+45
        s.line(lx+48,y,kx,ky,stroke=INK,sw=6); s.line(kx,ky,px,y,stroke=INK,sw=6)
        s.circle(kx,ky,6,fill=PAPER,sw=2)
        s.path([(lx+6,y-34),(lx+40,y-34),(lx+40,y-24),(lx+6,y-24)],fill=BRASS,close=True,sw=1.5)   # new round
        s.path([(lx+6,y+26),(lx+34,y+26),(lx+34,y+36),(lx+6,y+36)],fill="#b08d3a",close=True,sw=1.5) # empty case
s.text(965,430,"locked, at the shot",anchor="middle",italic=True,fill=SOFT,size=18)
lockstate(475,False)
s.arrow(860,450,900,450)
s.text(965,560,"a moment later",anchor="middle",italic=True,fill=SOFT,size=18)
lockstate(605,True)

s.callout(1,330,275,260,170,"Water round the barrel|keeps it from overheating")
s.callout(2,319,445,200,395,"A cloth belt|of 250 rounds",anchor="end")
s.callout(3,640,262,800,170,"The kick drives the barrel|and lock back together")
s.callout(4,1050,650,760,690,"The toggle folds: the lock pulls out|the empty case and a new round",anchor="end")
s.callout(5,690,320,880,330,"A spring sends it|all forward to fire")
s.save(os.path.join(os.path.dirname(__file__),"..","69-maxim-gun","maxim-gun"))
