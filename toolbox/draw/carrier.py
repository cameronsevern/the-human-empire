import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The aircraft carrier","The Shōkaku, Japan, 1941, cut open along its length")
GREY="#a9aca6"; DARK="#5e6366"; HANG="#e9e3d6"; SEA="#9fb4bd"; PLANE="#c9c2a6"
FD=330; WL=424; KEEL=462                      # flight deck top, waterline, keel

def plane(x,y,k=1.0,hook=False):
    """Side view of a single-engine aircraft facing right, wheels at (x,y)."""
    f=[(x-34*k,y-12*k),(x-20*k,y-14*k),(x+18*k,y-17*k),(x+26*k,y-13*k),(x+26*k,y-6*k),(x-20*k,y-8*k)]
    s.path([(round(a,1),round(b,1)) for a,b in f],fill=PLANE,close=True,sw=1.6)
    s.path([(round(x-34*k,1),round(y-12*k,1)),(round(x-38*k,1),round(y-25*k,1)),(round(x-27*k,1),round(y-13*k,1))],fill=PLANE,close=True,sw=1.4)
    s.line(round(x-10*k,1),round(y-11*k,1),round(x+12*k,1),round(y-11*k,1),stroke=INK,sw=3*k)      # wing seen edge-on
    s.line(round(x+28*k,1),round(y-19*k,1),round(x+28*k,1),round(y-1*k,1),stroke=INK,sw=1.4)        # propeller
    s.line(round(x+6*k,1),round(y-8*k,1),round(x+6*k,1),round(y,1),stroke=INK,sw=1.5)               # undercarriage
    s.circle(round(x+6*k,1),round(y-1*k,1),round(2.5*k,1),fill=INK,sw=0)
    if hook: s.line(round(x-26*k,1),round(y-8*k,1),round(x-34*k,1),round(y+6*k,1),stroke=INK,sw=1.6)

# ================= the sea =================
for x0 in range(60,1150,40):
    s.raw_path(f"M {x0},{WL} q 10,-5 20,0 t 20,0",stroke="#6f8892",sw=1.5)

# ================= the hull =================
hull_d=(f"M 170,{FD+14} L 1040,{FD+14} L 1086,{FD+2} Q 1060,{KEEL-30} 1010,{KEEL} "
        f"L 300,{KEEL} Q 230,{KEEL} 205,{KEEL-40} Q 190,{FD+60} 170,{FD+14} Z")
s.raw_path(hull_d,fill=GREY,sw=3)
# the hull cut open aft of the funnels: two hangars, one above the other
CX0,CX1=235,660
s.path([(CX0,FD+20),(CX1,FD+20),(CX1,KEEL-12),(CX0+30,KEEL-12)],fill="#d8d4c8",close=True,sw=2.5)
s.path([(CX0+8,FD+26),(CX1-8,FD+26),(CX1-8,374),(CX0+8,374)],fill=HANG,close=True,sw=1.5)
s.path([(CX0+16,380),(CX1-8,380),(CX1-8,416),(CX0+16,416)],fill=HANG,close=True,sw=1.5)
for x in (330,425,520): s.line(x,424,x,KEEL-16,stroke="#8c908a",sw=1.5)
for x in (300,450,540,625): plane(x,372,0.85)
for x in (320,410,500): plane(x,414,0.85)
# two of the three lifts: shafts through both hangars, one platform down with an aircraft on it
for (x0,x1) in ((255,290),(565,620)):
    s.line(x0,FD+14,x0,416,stroke=INK,sw=1.2,dash="6 5"); s.line(x1,FD+14,x1,416,stroke=INK,sw=1.2,dash="6 5")
s.path([(565,416),(620,416),(620,421),(565,421)],fill=DARK,close=True,sw=1.5)
# portholes along the closed part of the hull
for x in range(700,1020,26): s.circle(x,FD+50,3,fill=DARK,sw=0)
# the third lift, forward, seen as a joint in the deck
for x in (880,935): s.line(x,FD+1,x,FD+13,stroke=INK,sw=2)

# ================= the funnels, bent down over the side =================
for dx in (0,30):
    s.raw_path(f"M {700+dx},{FD+16} L {716+dx},{FD+16} Q {722+dx},{FD+16} {722+dx},{FD+40} L {722+dx},{FD+72} L {706+dx},{FD+72} L {706+dx},{FD+44} Q {706+dx},{FD+30} {700+dx},{FD+30} Z",fill="#3f4346",sw=2)

# ================= the flight deck =================
s.path([(150,FD),(1062,FD),(1062,FD+14),(150,FD+14)],fill=ACC,close=True,sw=3)
for x in range(170,1062,24): s.line(x,FD+3,x,FD+11,stroke="#7a3424",sw=1)
# arrester wires: short posts at the deck edge, aft
for x in range(205,445,28):
    s.line(x,FD,x,FD-7,stroke=INK,sw=2.2)
# the island, on the right-hand side of the deck
s.path([(770,FD),(770,FD-34),(790,FD-48),(826,FD-48),(826,FD)],fill=GREY,close=True,sw=2.5)
s.line(782,FD-30,816,FD-30,stroke=INK,sw=2)
s.line(808,FD-48,808,FD-92,stroke=INK,sw=2.5); s.line(796,FD-80,820,FD-80,stroke=INK,sw=2)
# aircraft ranged on deck, and one coming in to land with its hook down
for x in (520,600,680): plane(x,FD,1.3)
plane(250,FD-60,1.3,hook=True)
s.arrow(175,FD-92,212,FD-76)

s.callout(1,960,FD+7,1000,170,"A flat wooden deck,|242 metres long",anchor="end")
s.callout(2,401,FD-4,430,175,"Wires across the deck|catch a hook on|the landing aircraft")
s.callout(3,592,419,600,630,"Lifts carry aircraft|between deck and hangars")
s.callout(4,380,398,130,580,"Two hangars,|for 72 aircraft")
s.callout(5,744,FD+70,1080,560,"Funnels bent down|over the side, to keep|smoke off the deck",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","80-aircraft-carrier","carrier"))
