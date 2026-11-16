import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The spinning wheel","The Indian charkha, as Gandhi used it")
TEAK="#c49a6c"; DARKW="#8a6440"; CORD="#efe6d0"; STEEL="#6f7579"; COTTON="#ffffff"

# ================= the charkha, from the spinner's side =================
WX,WY,WR=900,410,165
BASE=600
s.path([(400,BASE),(1110,BASE),(1110,BASE+24),(400,BASE+24)],fill=TEAK,close=True,sw=3)        # the base plank
for dx in (-14,14):                                                                             # uprights for the wheel
    s.path([(WX+dx-9,BASE),(WX+dx-5,WY),(WX+dx+5,WY),(WX+dx+9,BASE)],fill=DARKW,close=True,sw=2)
# spokes, and the rim of cord laced zigzag between their tips
N=12
tips=[(WX+WR*math.cos(2*math.pi*k/N),WY+WR*math.sin(2*math.pi*k/N)) for k in range(N)]
for (x,y) in tips: s.line(WX,WY,round(x,1),round(y,1),stroke=DARKW,sw=5)
lace=[]
for k in range(N):
    a=2*math.pi*k/N; b=2*math.pi*(k+0.5)/N
    lace.append((WX+WR*math.cos(a),WY+WR*math.sin(a)))
    lace.append((WX+(WR-12)*math.cos(b),WY+(WR-12)*math.sin(b)))
s.path(lace,stroke="#b8ab8e",sw=2,close=True)
s.circle(WX,WY,WR,stroke=CORD,sw=2)
s.circle(WX,WY,18,fill=DARKW,sw=2.5)                                                            # hub
# the crank handle
s.line(WX,WY,WX+95,WY-90,stroke=DARKW,sw=8)
s.path([(WX+88,WY-120),(WX+104,WY-120),(WX+104,WY-80),(WX+88,WY-80)],fill=TEAK,close=True,sw=2.5)
# the spindle stand at the other end, the spindle lying along the top of its post
SX,SY=450,462
s.path([(SX-8,BASE),(SX-6,SY+8),(SX+6,SY+8),(SX+8,BASE)],fill=DARKW,close=True,sw=2)
s.path([(SX+30,SY-3),(SX+30,SY+3),(SX-70,SY+1),(SX-70,SY-1)],fill=ACC,close=True,sw=2)
s.path([(SX+14,SY-10),(SX+28,SY-10),(SX+28,SY+10),(SX+14,SY+10)],fill=STEEL,close=True,sw=2)
# the drive band: from the wheel's rim round the spindle's little pulley
s.line(SX+21,SY-10,WX,WY-WR,stroke="#7d6a50",sw=2.5)
s.line(SX+21,SY+10,WX,WY+WR,stroke="#7d6a50",sw=2.5)
s.path([(SX-70,SY),(SX-95,SY-6),(SX-110,SY-10)],stroke=INK,sw=1.5)
s.ellipse(SX-122,SY-12,14,8,fill=COTTON,stroke=SOFT,sw=1.5)
s.text(920,700,"from the spinner's side",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the spindle tip, magnified =================
IX,IY,IR=200,330,140
s.inset(IX,IY,IR)
s.line(IX+108,IY-14,IX+118,IY-55,stroke="#7d6a50",sw=2.5)                                  # band, going off to the wheel
s.line(IX+108,IY+14,IX+118,IY+55,stroke="#7d6a50",sw=2.5)
s.path([(IX+125,IY-9),(IX+125,IY+9),(IX-45,IY+2),(IX-45,IY-2)],fill=ACC,close=True,sw=2.5)   # the spindle, tapering to a point
s.path([(IX+95,IY-14),(IX+120,IY-14),(IX+120,IY+14),(IX+95,IY+14)],fill=STEEL,close=True,sw=2)   # the pulley
s.path([(IX+10,IY-13),(IX+60,IY-13),(IX+60,IY+13),(IX+10,IY+13)],fill="#f4ecd8",close=True,sw=1.5) # thread wound on
pts=[(IX-45,IY)]
for k in range(1,9):
    pts.append((IX-45-k*6.0,IY+k*4.2+2.2*math.sin(k*1.9)))
s.path(pts,stroke=INK,sw=1.5)
s.ellipse(IX-100,IY+44,22,13,fill=COTTON,stroke=SOFT,sw=2,rot=30)
s.text(IX,IY+IR+36,"the spindle tip, magnified",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,WX+96,WY-104,1100,175,"A handle turns|the big wheel",anchor="end")
s.callout(2,WX-WR+8,WY+30,610,300,"Spokes laced with cord|make a light rim",anchor="end")
s.callout(3,675,521,640,690,"A cord band runs|to the spindle",anchor="end")
s.callout(4,IX+75,IY,400,200,"The spindle turns dozens of|times for each turn of the wheel")
s.callout(5,IX-75,IY+20,110,580,"Cotton drawn off the tip|twists into thread")
s.save(os.path.join(os.path.dirname(__file__),"..","76-spinning-wheel","spinning-wheel"))
