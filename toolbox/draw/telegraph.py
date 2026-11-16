import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The telegraph","American Civil War, 1861 to 1865")
BRASS="#d4b25a"; GLASS="#dfe8e6"; ZINC="#8f979b"; COPPER="#c98a5a"; IRON="#6f7579"; SOIL="#cbb48f"
G=590                                                                  # ground level

# ================= the ground, with a metal plate buried at each end =================
s.line(50,G,1150,G,stroke=SOFT,sw=1.5)
for x in range(60,1150,26): s.line(x,G+6,x-12,G+18,stroke=SOIL,sw=1.5)
for px in (115,905):
    s.path([(px-30,G+28),(px+30,G+28),(px+30,G+38),(px-30,G+38)],fill=COPPER,close=True,sw=2)

# ================= the sending end: battery and key =================
# battery: three glass jars, each with a zinc and a copper plate
for k in range(3):
    jx=72+k*34
    s.path([(jx,488),(jx+28,488),(jx+28,560),(jx,560)],fill=GLASS,close=True,sw=2)
    s.line(jx+9,474,jx+9,548,stroke=ZINC,sw=4); s.line(jx+19,474,jx+19,548,stroke=COPPER,sw=4)
    if k<2: s.raw_path(f"M {jx+19},{474} Q {jx+30},{462} {jx+43},{474}",stroke=INK,sw=1.5)
s.line(81,474,81,450,stroke=INK,sw=1.5); s.line(81,450,190,450,stroke=INK,sw=1.5)   # battery to key
s.line(115,560,115,G+28,stroke=INK,sw=1.5)                             # battery to the earth plate
# key: a brass lever on a pivot, a knob at the front, contacts beneath
s.path([(190,450),(390,450),(390,480),(190,480)],fill=WOOD,close=True,sw=2.5)
s.path([(212,450),(238,450),(238,425),(212,425)],fill=BRASS,close=True,sw=2)
s.circle(225,420,10,fill=BRASS,sw=2)                                     # pivot
s.path([(200,414),(365,400),(365,414),(200,428)],fill=BRASS,close=True,sw=2.5)   # lever
s.raw_path("M 252,424 l 6,5 l -10,4 l 8,5 l -6,4 l 4,8",stroke=INK,sw=2)             # spring at the back
s.line(358,402,358,388,stroke=INK,sw=4)
s.ellipse(358,382,24,10,fill="#3a3430",sw=2)                            # knob
s.path([(326,450),(342,450),(342,430),(326,430)],fill=BRASS,close=True,sw=2)                                 # lower contact
s.line(334,410,334,422,stroke=INK,sw=3)
s.line(390,465,560,465,stroke=INK,sw=1.5)                               # from the key to the line

# ================= the line: one wire on poles =================
P1,P2,PT=560,830,205
for px in (P1,P2):
    s.path([(px-7,PT),(px+7,PT),(px+7,G),(px-7,G)],fill="#a87e55",close=True,sw=2)
    s.path([(px-30,PT+10),(px+30,PT+10),(px+30,PT+20),(px-30,PT+20)],fill="#a87e55",close=True,sw=2)
    s.ellipse(px+22,PT+2,6,8,fill=GLASS,sw=1.5)                         # glass insulator
s.line(560,465,P1+22,PT+2,stroke=INK,sw=1.5)
s.raw_path(f"M {P1+22},{PT-6} Q {(P1+P2)/2},{PT+40} {P2+22},{PT-6}",stroke=INK,sw=2.5)
s.raw_path(f"M {P2+22},{PT-6} L 880,{PT+30} L 880,452",stroke=INK,sw=1.5)
s.text((P1+P2)/2,G-20,"miles of wire",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the receiving end: the sounder =================
s.path([(870,452),(1120,452),(1120,480),(870,480)],fill=WOOD,close=True,sw=2.5)
for cx in (935,975):                                                    # the electromagnet: two coils
    s.path([(cx-15,385),(cx+15,385),(cx+15,452),(cx-15,452)],fill=ACC,close=True,sw=2.5)
    for y in range(392,450,8): s.line(cx-15,y,cx+15,y+3,stroke="#7a2f20",sw=1)
s.path([(918,368),(992,368),(992,380),(918,380)],fill=IRON,close=True,sw=2)   # iron armature
s.path([(1070,452),(1090,452),(1090,340),(1070,340)],fill=BRASS,close=True,sw=2)  # pivot post
s.path([(890,354),(1080,350),(1080,360),(890,364)],fill=BRASS,close=True,sw=2.5)  # lever
s.circle(1080,355,6,fill=INK,sw=0)
s.line(955,364,955,368,stroke=INK,sw=3)
s.path([(890,330),(902,330),(902,452),(890,452)],fill=BRASS,close=True,sw=2)   # stop post
s.line(896,330,896,350,stroke=INK,sw=3)                                 # upper stop screw
s.raw_path("M 905,480 L 905,618",stroke=INK,sw=1.5)   # to the earth plate

# ================= the code: SEND MEN =================
MX=400; MY=670; DOT=10; DASH=30; GAP=9; LGAP=26; WGAP=50
code=[("S","..."),("E","."),("N","-."),("D","-.."),(" ",""),("M","--"),("E","."),("N","-.")]
x=MX
for (ch,c) in code:
    if ch==" ": x+=WGAP; continue
    x0=x
    for sym in c:
        w=DOT if sym=="." else DASH
        s.path([(x,MY-5),(x+w,MY-5),(x+w,MY+5),(x,MY+5)],fill=INK,close=True,sw=1)
        x+=w+GAP
    s.text((x0+x-GAP)/2,MY+36,ch,anchor="middle",size=19,fill=SOFT,bold=True)
    x+=LGAP-GAP

s.callout(1,358,380,330,250,"Press the key, and|the circuit closes")
s.callout(2,100,500,100,330,"A battery|drives a current")
s.callout(3,(P1+P2)/2,PT+19,700,120,"One wire on poles; the|ground completes the circuit")
s.callout(4,975,430,1150,530,"A magnet pulls the|lever down: click",anchor="end")
s.callout(5,MX+5,MY,350,670,"Short and long|clicks spell letters",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","64-telegraph","telegraph"))
