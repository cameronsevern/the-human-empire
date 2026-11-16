import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The helicopter","The Bell UH-1 ‘Huey’, as flown in Vietnam, 1960s")
OD="#6d7552"; OD2="#59603f"; GLASSC="#a9c3cc"; DARK="#3c3f36"; GROUND=650
s.line(60,GROUND,1150,GROUND,stroke=SOFT,sw=1.5)

# ================= the skids =================
for (dx,dy,col) in ((14,-8,OD2),(0,0,DARK)):
    s.raw_path(f"M {250+dx},{GROUND-14+dy} Q {226+dx},{GROUND-14+dy} {222+dx},{GROUND-40+dy} M {250+dx},{GROUND-14+dy} L {560+dx},{GROUND-14+dy}",stroke=col,sw=7)
for x in (300,500):
    s.line(x,GROUND-14,x+18,592,stroke=DARK,sw=6)

# ================= the tail boom, fin and tail rotor =================
s.path([(560,525),(900,532),(900,550),(560,585)],fill=OD,close=True,sw=3)
s.path([(870,532),(905,440),(935,440),(915,550),(900,550)],fill=OD,close=True,sw=3)
s.path([(730,540),(790,536),(790,546),(730,550)],fill=OD2,close=True,sw=2)           # small tailplane
s.circle(940,462,58,fill="none",stroke=SOFT,sw=1.5)
s.line(940,404,940,520,stroke=DARK,sw=6); s.circle(940,462,7,fill=DARK,sw=1.5)

# ================= the cabin =================
cab=[(200,560),(206,530),(226,506),(262,490),(300,486),(560,486),(580,520),(580,590),(250,600),(214,590)]
s.path(cab,fill=OD,close=True,sw=3)
s.path([(208,538),(226,508),(262,492),(296,489),(296,540)],fill=GLASSC,close=True,sw=2)   # windscreen
s.path([(212,560),(296,556),(296,590),(250,596),(218,588)],fill=GLASSC,close=True,sw=2)   # chin window
# the wide sliding door, open, with the cabin dark inside
s.path([(320,500),(470,500),(470,592),(320,596)],fill="#2f332a",close=True,sw=2.5)
s.path([(470,500),(540,500),(540,590),(470,592)],fill=OD2,close=True,sw=2)               # door slid back
s.circle(500,520,8,fill=GLASSC,sw=1.5)
# seats glimpsed through the door
for x in (350,410):
    s.line(x,560,x+30,560,stroke="#777b6e",sw=4); s.line(x+30,560,x+34,528,stroke="#777b6e",sw=4)

# ================= the engine on the roof, behind the mast =================
s.path([(390,486),(400,456),(560,456),(590,470),(590,486)],fill=OD2,close=True,sw=2.5)
s.path([(420,460),(570,460),(580,470),(580,482),(420,482)],fill=ACC,close=True,sw=2.5)
s.path([(586,462),(622,450),(628,474),(590,482)],fill=DARK,close=True,sw=2)                # exhaust
for x in (440,470,500,530): s.line(x,462,x,480,stroke="#7a3424",sw=1.5)

# ================= the mast, the stabiliser bar and the two-bladed rotor =================
s.path([(372,486),(388,486),(386,430),(374,430)],fill=DARK,close=True,sw=2)
s.line(52,424,708,424,stroke=DARK,sw=7)
s.path([(360,432),(400,432),(396,418),(364,418)],fill=OD2,close=True,sw=2)
s.line(330,412,430,412,stroke=DARK,sw=3)
for x in (330,430): s.circle(x,412,6,fill=DARK,sw=1)

s.callout(1,470,470,640,250,"A turbine engine: much power|from little weight")
s.callout(2,140,424,110,250,"Two blades,|15 metres across")
s.callout(3,395,545,110,700,"Wide doors on both sides")
s.callout(4,520,GROUND-14,560,700,"Skids, not wheels")
s.callout(5,940,500,1140,700,"A small rotor on the tail|stops the body spinning",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","94-helicopter","helicopter"))
