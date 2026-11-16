import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The battleship","Mikasa, built in England for Japan, 1902")
HULL="#8d9396"; DARK="#4b4f52"; BELT="#3f4446"; WATER="#cfdde0"; SMOKE="#9a9590"; DECKC="#c9bfae"; RED="#8e3c2a"
WL=450; DECK=388; KEEL=512
ST,BW=110,1080                                                         # stern and bow, about 7.5 px to the metre

# ================= water (behind the lower hull) =================
s.path([(50,WL),(1150,WL),(1150,530),(50,530)],fill=WATER,close=True,sw=0,stroke="none")

# ================= masts with fighting tops =================
for (mx,top) in ((395,170),(820,150)):
    s.line(mx,DECK-40,mx,top,stroke=DARK,sw=7)
    s.path([(mx-22,top+60),(mx+22,top+60),(mx+16,top+80),(mx-16,top+80)],fill=HULL,close=True,sw=2)

# ================= funnels and smoke =================
for fx in (560,665):
    s.path([(fx-22,DECK-62),(fx+22,DECK-62),(fx+22,215),(fx-22,215)],fill="#c7bba5",close=True,sw=2.5)
    s.path([(fx-22,215),(fx+22,215),(fx+22,228),(fx-22,228)],fill=DARK,close=True,sw=2)
s.raw_path("M 560,210 C 540,180 500,175 460,160",stroke=SMOKE,sw=18)
s.raw_path("M 665,210 C 640,185 610,180 580,165",stroke=SMOKE,sw=16)

# ================= superstructure and bridge =================
s.path([(450,DECK),(760,DECK),(760,DECK-62),(450,DECK-62)],fill=DECKC,close=True,sw=2.5)
s.path([(790,DECK),(870,DECK),(870,DECK-80),(790,DECK-80)],fill=DECKC,close=True,sw=2.5)
s.path([(780,DECK-80),(880,DECK-80),(880,DECK-90),(780,DECK-90)],fill=HULL,close=True,sw=2)
s.path([(360,DECK),(430,DECK),(430,DECK-46),(360,DECK-46)],fill=DECKC,close=True,sw=2.5)

# ================= the hull =================
hull=(f"M {ST},{DECK+6} L {BW-20},{DECK} L {BW},{DECK} L {BW-12},{WL+30} Q {BW-10},{KEEL-8} {BW-40},{KEEL} "
      f"L {ST+80},{KEEL} Q {ST+20},{KEEL-10} {ST},{WL+10} Z")
s.raw_path(hull,fill=HULL,sw=3)
s.raw_path(f"M {ST+20},{WL-14} L {BW-14},{WL-14} L {BW-12},{WL+26} L {ST+40},{WL+26} Z",fill=BELT,sw=2)   # armour belt
for x in range(ST+80,BW-40,70): s.line(x,WL-14,x,WL+26,stroke="#6a7073",sw=1)
# six-inch guns in casemates along the side
for x in range(470,790,52):
    s.path([(x-14,DECK+14),(x+14,DECK+14),(x+14,DECK+38),(x-14,DECK+38)],fill=DARK,close=True,sw=2)
    s.line(x,DECK+26,x+36,DECK+26,stroke=INK,sw=5)
for x in range(490,760,64):                                            # a second row, on the deck above
    s.line(x,DECK-30,x+30,DECK-30,stroke=INK,sw=4)

# ================= the two main turrets, twelve-inch guns =================
for (tx,d) in ((300,-1),(930,1)):
    s.path([(tx-45,DECK),(tx+45,DECK),(tx+38,DECK-42),(tx-38,DECK-42)],fill=ACC,close=True,sw=3)
    for dy in (-30,-20):
        s.path([(tx+30*d,DECK+dy-4),(tx+150*d,DECK+dy-4),(tx+150*d,DECK+dy+3),(tx+30*d,DECK+dy+3)],fill=RED,close=True,sw=2)

# ================= propeller and rudder =================
s.raw_path(f"M {ST+40},{KEEL-30} q -14,-18 0,-30 q 14,12 0,30 q 14,18 0,30 q -14,-12 0,-30",fill=METAL,sw=2)
s.path([(ST+2,WL+16),(ST+18,WL+16),(ST+18,KEEL-6),(ST+2,KEEL-6)],fill=DARK,close=True,sw=2)

# waterline waves over the hull
for x in range(60,1150,46):
    s.raw_path(f"M {x},{WL} q 11,-6 22,0 q 11,6 22,0",stroke="#7f9aa1",sw=2)

# length
s.line(ST,560,BW,560,stroke=SOFT,sw=1.2)
for x in (ST,BW): s.line(x,552,x,568,stroke=SOFT,sw=1.2)
s.text(240,588,"132 metres long",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,300,DECK-30,335,245,"Two 12-inch guns in a|turret at each end",anchor="end")
s.callout(2,900,WL+8,860,650,"A belt of armour along|the waterline, 23 cm thick")
s.callout(3,600,DECK+26,520,650,"Fourteen 6-inch|guns in the sides")
s.callout(4,680,232,880,135,"Coal fires under 25|boilers, two funnels")
s.callout(5,ST+40,KEEL-30,120,650,"Two engines, two|propellers, 18 knots")
s.save(os.path.join(os.path.dirname(__file__),"..","66-battleship","battleship"))
