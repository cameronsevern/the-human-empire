import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The iron steamship","Nemesis, built at Birkenhead in 1839")
IRON="#6f7579"; DARK="#4b4f52"; WATER="#cfdde0"; SAIL="#efe6d0"; MUD="#c9b48e"; SMOKE="#9a9590"; GUN="#3a3430"
WL=440                                                                 # waterline
DECK=405; KEEL=470                                                     # 56 m long at about 16 px to the metre
BOW,STERN=1060,130

# ================= the river: water and a shallow bed =================
s.path([(50,WL),(1150,WL),(1150,505),(50,505)],fill=WATER,close=True,sw=0,stroke="none")
s.raw_path("M 50,505 Q 300,498 600,506 T 1150,503 L 1150,522 L 50,522 Z",fill=MUD,sw=1.5)

# ================= masts and sails (drawn first, behind the hull) =================
for (mx,top,sx0) in ((330,150,175),(880,160,725)):
    s.raw_path(f"M {sx0},{DECK-30} L {mx-6},{DECK-30} L {mx-6},{top+40} L {sx0+40},{top+80} Z",fill=SAIL,sw=2)
    s.line(mx,DECK,mx,top,stroke="#a87e55",sw=6)
s.line(330,160,880,170,stroke=INK,sw=1.2)
s.line(330,160,STERN+10,DECK-6,stroke=INK,sw=1.2)

# ================= funnel and smoke =================
s.path([(626,DECK-6),(654,DECK-6),(654,215),(626,215)],fill=DARK,close=True,sw=2.5)
s.raw_path("M 640,212 C 630,180 600,160 560,150 C 520,140 500,150 470,135",stroke=SMOKE,sw=16)

# ================= the hull, cut open to show its iron walls =================
hull=(f"M {STERN},{DECK} L {BOW-30},{DECK} Q {BOW+10},{DECK+4} {BOW+30},{DECK-14} "
      f"Q {BOW+10},{KEEL-10} {BOW-40},{KEEL} L {STERN+40},{KEEL} Q {STERN+6},{KEEL-6} {STERN},{DECK} Z")
s.raw_path(hull,fill=IRON,sw=3)
for x in range(STERN+30,BOW-20,24):                                     # rows of rivets along the plates
    for y in (DECK+14,DECK+38):
        s.circle(x,y,2,fill=DARK,sw=0)
for x in range(STERN+60,BOW-40,62): s.line(x,DECK+6,x,KEEL-4,stroke=DARK,sw=1)   # plate seams
for x in (300,470,770,920):                                             # watertight bulkheads
    s.line(x,DECK+4,x,KEEL-4,stroke=PAPER,sw=3,dash="7 6")
s.line(BOW+30,DECK-14,1140,DECK-50,stroke="#a87e55",sw=5)               # bowsprit
s.line(STERN,DECK,BOW-30,DECK,stroke=INK,sw=3)

# ================= the paddle wheel in its box =================
PX,PY,PR=560,398,56
s.raw_path(f"M {PX-PR-12},{DECK-4} A {PR+12} {PR+12} 0 0 1 {PX+PR+12},{DECK-4} Z",fill="#d8d0c0",sw=2.5)
s.circle(PX,PY,PR,fill=ACC,sw=3)
for k in range(10):
    a=math.radians(k*36)
    s.line(PX,PY,round(PX+PR*math.cos(a),1),round(PY+PR*math.sin(a),1),stroke="#7a2f20",sw=3)
    s.path([(round(PX+(PR-14)*math.cos(a)-5*math.sin(a),1),round(PY+(PR-14)*math.sin(a)+5*math.cos(a),1)),
            (round(PX+(PR+2)*math.cos(a)-5*math.sin(a),1),round(PY+(PR+2)*math.sin(a)+5*math.cos(a),1)),
            (round(PX+(PR+2)*math.cos(a)+5*math.sin(a),1),round(PY+(PR+2)*math.sin(a)-5*math.cos(a),1)),
            (round(PX+(PR-14)*math.cos(a)+5*math.sin(a),1),round(PY+(PR-14)*math.sin(a)-5*math.cos(a),1))],fill="#8e3c2a",close=True,sw=1)
s.circle(PX,PY,9,fill=INK,sw=0)

# ================= a pivot gun at each end =================
for (gx,d) in ((990,1),(205,-1)):
    s.path([(gx-22,DECK-2),(gx+22,DECK-2),(gx+16,DECK-14),(gx-16,DECK-14)],fill="#a87e55",close=True,sw=2)
    s.path([(gx-26*d,DECK-26),(gx+40*d,DECK-30),(gx+40*d,DECK-20),(gx-26*d,DECK-16)],fill=GUN,close=True,sw=2)

# waves at the waterline, over the hull
for x in range(60,1150,46):
    s.raw_path(f"M {x},{WL} q 11,-6 22,0 q 11,6 22,0",stroke="#7f9aa1",sw=2)

# ================= draught, measured =================
DX=1105
s.line(DX,WL,DX,KEEL,stroke=INK,sw=1.5)
s.line(DX-10,WL,DX+10,WL,stroke=INK,sw=1.5); s.line(DX-10,KEEL,DX+10,KEEL,stroke=INK,sw=1.5)
s.line(BOW-40,KEEL,DX-10,KEEL,stroke=SOFT,sw=1,dash="4 4")
s.text(780,572,"56 metres long",anchor="middle",italic=True,fill=SOFT,size=18)
s.line(STERN,545,BOW+30,545,stroke=SOFT,sw=1.2)
for x in (STERN,BOW+30): s.line(x,537,x,553,stroke=SOFT,sw=1.2)

s.callout(1,240,DECK+38,150,610,"Riveted|iron plates")
s.callout(2,PX,PY+40,560,610,"A paddle wheel each|side, turned by steam")
s.callout(3,DX,455,1100,610,"Less than two metres|below the waterline",anchor="end")
s.callout(4,1000,DECK-26,920,240,"A big gun on a|pivot at each end")
s.callout(5,300,DECK+50,460,690,"Iron walls inside kept|a leak to one part")
s.save(os.path.join(os.path.dirname(__file__),"..","65-iron-steamship","iron-steamship"))
