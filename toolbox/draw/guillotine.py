import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The guillotine","Paris, first used in 1792")
OAK="#c9a174"; DARKW="#a87e55"; IRON="#6f7579"; ROPE="#8a6a48"
G=690
s.line(60,G,1140,G,stroke=SOFT,sw=1.5)

# ================= front view =================
X1,X2=350,510; PW=34; TOP=170
s.path([(230,G-26),(630,G-26),(630,G),(230,G)],fill=DARKW,close=True,sw=3)          # the platform
for x in (X1-PW,X2):
    s.path([(x,TOP+20),(x+PW,TOP+20),(x+PW,G-26),(x,G-26)],fill=OAK,close=True,sw=3)
for x in (X1-6,X2+6):                                                               # grooves on the inner faces
    s.line(x,TOP+28,x,G-40,stroke=DARKW,sw=3)
s.path([(X1-PW-26,TOP),(X2+PW+26,TOP),(X2+PW+26,TOP+24),(X1-PW-26,TOP+24)],fill=OAK,close=True,sw=3)   # crossbeam
s.circle(X2+PW+14,TOP+12,11,fill=BRASS if False else "#c98a5a",sw=2)               # pulley
# the weight (mouton) and the blade, raised
MY=230
s.path([(X1,MY),(X2,MY),(X2,MY+52),(X1,MY+52)],fill=IRON,close=True,sw=3)
for x in (X1+20,X2-20): s.circle(x,MY+26,5,fill=INK,sw=0)
s.path([(X1,MY+52),(X2,MY+52),(X2,MY+68),(X1,MY+172)],fill=ACC,close=True,sw=3)
s.line(X1+6,MY+164,X2-6,MY+72,stroke="#f0d2c6",sw=2)                               # the edge
s.circle((X1+X2)/2,MY-8,7,stroke=INK,sw=2.5)                                       # ring for the cord
# the cord: from the ring, over the pulley, down to a cleat
s.raw_path(f"M {(X1+X2)/2},{MY-15} L {(X1+X2)/2},{TOP+40} L {X2+PW+4},{TOP+14}",stroke=ROPE,sw=3)
s.raw_path(f"M {X2+PW+25},{TOP+14} L {X2+PW+25},{G-160}",stroke=ROPE,sw=3)
s.path([(X2+PW+12,G-160),(X2+PW+40,G-160),(X2+PW+40,G-148),(X2+PW+12,G-148)],fill=IRON,close=True,sw=2)
# the collar (lunette): two boards, a round hole between them
LY=G-150; CXL=(X1+X2)/2
s.path([(X1,LY-40),(X2,LY-40),(X2,LY),(X1,LY)],fill=OAK,close=True,sw=3)
s.path([(X1,LY),(X2,LY),(X2,LY+40),(X1,LY+40)],fill=OAK,close=True,sw=3)
s.circle(CXL,LY,22,fill="#3a3430",sw=2.5)
s.path([(X1,LY+40),(X2,LY+40),(X2,LY+78),(X1,LY+78)],fill=DARKW,close=True,sw=2.5)  # the block below
s.text(430,740-6,"from the front",anchor="middle",italic=True,fill=SOFT)

# ================= side view =================
SX=1010
s.path([(720,G-26),(1140,G-26),(1140,G),(720,G)],fill=DARKW,close=True,sw=3)
s.path([(SX,TOP+20),(SX+PW,TOP+20),(SX+PW,G-26),(SX,G-26)],fill=OAK,close=True,sw=3)
s.path([(SX-30,TOP),(SX+PW+30,TOP),(SX+PW+30,TOP+24),(SX-30,TOP+24)],fill=OAK,close=True,sw=3)
s.line(SX+PW,TOP+150,SX+PW+70,G-26,stroke=DARKW,sw=8)                               # back brace
# blade and weight seen edge on, in the groove
s.path([(SX+8,MY),(SX+26,MY),(SX+26,MY+52),(SX+8,MY+52)],fill=IRON,close=True,sw=2.5)
s.path([(SX+12,MY+52),(SX+22,MY+52),(SX+20,MY+170),(SX+14,MY+170)],fill=ACC,close=True,sw=2.5)
# the collar and block, seen from the side
s.path([(SX-36,LY-40),(SX+4,LY-40),(SX+4,LY+78),(SX-36,LY+78)],fill=OAK,close=True,sw=3)
# the plank, lying flat on its frame, ending at the collar
PL=LY+20
s.path([(750,PL),(SX-40,PL),(SX-40,PL+16),(750,PL+16)],fill=OAK,close=True,sw=3)
s.circle(860,PL+30,8,fill=IRON,sw=2)                                                # its pivot
s.path([(840,PL+38),(880,PL+38),(890,G-26),(830,G-26)],fill=DARKW,close=True,sw=2.5)
s.line(770,PL+16,770,G-26,stroke=INK,sw=4)
s.text(930,740-6,"from the side",anchor="middle",italic=True,fill=SOFT)

s.callout(1,X1-PW+10,420,210,330,"Two oak posts,|grooved inside",anchor="end")
s.callout(2,X1+60,MY+100,700,200,"A slanted blade,|weighted from above")
s.callout(3,X2+PW+25,430,700,320,"A cord holds it up;|let go, it falls")
s.callout(4,CXL-50,LY-10,210,520,"A collar holds|the neck",anchor="end")
s.callout(5,790,PL+8,700,440,"A plank, tipped|flat to the collar")
s.save(os.path.join(os.path.dirname(__file__),"..","57-guillotine","guillotine"))
