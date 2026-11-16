import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The solar panel","A panel of sixty cells, and one cell cut across")
FRAME="#c4c9cc"; CELLC="#2f4a6b"; SILVER="#e3e6e8"; NLAY="#9cc0d8"; PLAY="#5f7f9e"; BACK="#a7adb1"; SUN="#e8b84a"

# ================= the panel, seen from the front =================
PX,PY,CW,CH=80,190,40,46
NC,NR=6,10
s.path([(PX-14,PY-14),(PX+NC*CW+14,PY-14),(PX+NC*CW+14,PY+NR*CH+14),(PX-14,PY+NR*CH+14)],fill=FRAME,close=True,sw=3)
s.path([(PX-4,PY-4),(PX+NC*CW+4,PY-4),(PX+NC*CW+4,PY+NR*CH+4),(PX-4,PY+NR*CH+4)],fill="#e9eef1",close=True,sw=1.5)
for c in range(NC):
    for r in range(NR):
        x=PX+c*CW+2; y=PY+r*CH+2
        s.path([(x,y),(x+CW-4,y),(x+CW-4,y+CH-4),(x,y+CH-4)],fill=CELLC,close=True,sw=1)
        for k in (1,2):
            s.line(x+k*(CW-4)/3,y+1,x+k*(CW-4)/3,y+CH-5,stroke=SILVER,sw=1.2)
# the spot that is enlarged
EX,EY=PX+3*CW+2,PY+4*CH+2
s.path([(EX,EY),(EX+CW-4,EY),(EX+CW-4,EY+CH-4),(EX,EY+CH-4)],stroke=ACC,sw=2.5)

# ================= inset: one cell cut across =================
IX,IY,IR=840,455,215
s.line(EX+CW-4,EY,IX-IR*0.9,IY-IR*0.45,stroke=SOFT,sw=1.2,dash="5 5")
s.line(EX+CW-4,EY+CH-4,IX-IR*0.9,IY+IR*0.45,stroke=SOFT,sw=1.2,dash="5 5")
s.inset(IX,IY,IR)
def band(y0,y1):
    pts=[]
    for k in range(41):
        y=y0+(y1-y0)*k/40; pts.append((IX+math.sqrt(max(IR*IR-(y-IY)**2,0))-3,y))
    for k in range(40,-1,-1):
        y=y0+(y1-y0)*k/40; pts.append((IX-math.sqrt(max(IR*IR-(y-IY)**2,0))+3,y))
    return pts
TOP,JN,BK,BOT=340,400,560,592
s.path(band(TOP,JN),fill=NLAY,close=True,sw=0)
s.path(band(JN+8,BK),fill=PLAY,close=True,sw=0)
s.path(band(JN,JN+8),fill=ACC,close=True,sw=1.5)
s.path(band(BK,BOT),fill=BACK,close=True,sw=0)
for y in (TOP,BK): s.path([(IX-math.sqrt(IR*IR-(y-IY)**2)+3,y),(IX+math.sqrt(IR*IR-(y-IY)**2)-3,y)],sw=2)
# silver lines on the face, seen end on
for x in (700,960):
    s.path([(x-14,TOP-22),(x+14,TOP-22),(x+14,TOP),(x-14,TOP)],fill=SILVER,close=True,sw=2)
s.text(955,TOP+46,"phosphorus added",anchor="middle",italic=True,fill="#2f3f4c",size=16,halo=NLAY)
s.text(IX,BK-40,"boron added",anchor="middle",italic=True,fill="#f4f1ea",size=16,halo=PLAY)
# sunlight coming in
s.line(740,280,800,462,stroke=SUN,sw=6)
s.line(740,280,800,462,stroke=INK,sw=1.2)
s.circle(803,470,9,fill=SUN,sw=1.5)
# the freed electron is driven up across the junction, to the silver line and out
s.circle(835,450,8,fill="#f4f1ea",sw=1.5)
s.text(835,456,"–",anchor="middle",size=16,bold=True,halo="#f4f1ea")
s.arrow(835,438,835,TOP+8)
s.arrow(850,TOP+14,935,TOP+14)
s.arrow(960,TOP-26,960,285)

s.callout(1,PX-10,PY+NR*CH-40,110,690,"Glass and a metal frame|keep out the weather")
s.callout(2,790,440,400,250,"Light knocks an electron|loose in the silicon")
s.callout(3,690,JN+4,690,695,"The junction drives it one way")
s.callout(4,972,TOP-12,1150,205,"Silver lines collect it",anchor="end")
s.callout(5,PX+NC*CW-20,PY+NR*CH-20,420,625,"Cells joined in a row|add up their voltage")
s.save(os.path.join(os.path.dirname(__file__),"..","111-solar-panel","solar-panel"))
