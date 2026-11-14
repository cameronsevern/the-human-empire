import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The fire siphon","the 670s, as modern reconstructions draw it")
WATER="#9fb8c8"; FLAME="#e9a35c"; FLAME2="#f3cf7a"; BRONZE="#c9a46a"
DECK=470; WL=585
# water line
s.raw_path(f"M 60,{WL} Q 90,{WL-8} 120,{WL} T 180,{WL} T 240,{WL}",stroke=WATER,sw=2.5)
s.line(860,WL+4,1140,WL+4,stroke=WATER,sw=2.5)
# oars under the hull
for i in range(9):
    x=150+i*48
    s.line(x,DECK+50,x-34,WL+70,sw=1.6)
# the bow of a galley, broken off at the left, with a raised fore-deck
s.raw_path(f"M 70,{DECK} L 690,{DECK} L 700,{DECK-50} L 850,{DECK-50} C 880,{DECK-50} 900,{DECK-20} 905,{DECK+10} "
           f"C 900,{WL-40} 870,{WL-10} 820,{WL-10} L 70,{WL-10} L 80,{WL-30} L 64,{DECK+50} L 78,{DECK+25} Z",fill=WOOD)
s.line(76,DECK+18,690,DECK+18,sw=1.5)
s.line(700,DECK-30,890,DECK-30,sw=1.5)
# fire box on deck, and the sealed tank above it
s.add(f'<rect x="420" y="{DECK-40}" width="170" height="40" fill="{CLAY}" stroke="{INK}" stroke-width="3"/>')
for fx in (450,480,510,540,565):
    s.raw_path(f"M {fx-9},{DECK-2} C {fx-12},{DECK-20} {fx},{DECK-24} {fx},{DECK-38} C {fx+4},{DECK-24} {fx+12},{DECK-20} {fx+9},{DECK-2} Z",fill=FLAME,sw=1.5)
s.raw_path(f"M 430,{DECK-40} L 430,{DECK-130} C 430,{DECK-160} 580,{DECK-160} 580,{DECK-130} L 580,{DECK-40} Z",fill=METAL,sw=3)
# the pump: a cylinder worked by a lever
PX=640
s.add(f'<rect x="{PX-18}" y="{DECK-120}" width="36" height="120" fill="{METAL}" stroke="{INK}" stroke-width="3"/>')
s.line(PX,DECK-120,PX,DECK-160,sw=5)
s.line(PX-70,DECK-178,PX+20,DECK-150,sw=6)
s.circle(PX+20,DECK-150,6,fill=PAPER,sw=2.5)
s.line(PX+20,DECK-150,PX+20,DECK-120,sw=3)

# pipes: tank to pump, pump to the tube at the bow
s.line(580,DECK-60,PX-18,DECK-60,sw=9); s.line(580,DECK-60,PX-18,DECK-60,stroke=METAL,sw=4)
s.path([(PX+18,DECK-90),(760,DECK-90),(760,DECK-50)],sw=9)
s.path([(PX+18,DECK-90),(760,DECK-90),(760,DECK-50)],stroke=METAL,sw=4)
s.path([(760,DECK-50),(760,DECK-74),(820,DECK-74)],sw=9)
# the swivel mount and the bronze-covered tube at the bow
s.add(f'<rect x="812" y="{DECK-92}" width="26" height="42" fill="{BRONZE}" stroke="{INK}" stroke-width="2.5"/>')
s.path([(825,DECK-80),(930,DECK-104),(934,DECK-90),(828,DECK-64)],fill=ACC,close=True,sw=3)
s.raw_path(f"M 905,{DECK-140} A 60 60 0 0 1 905,{DECK-40}",sw=2,extra='stroke-dasharray="5 7"')
# the jet of fire, lit at the mouth, falling and burning on the water
s.raw_path(f"M 935,{DECK-100} C 990,{DECK-140} 1060,{DECK-140} 1120,{DECK-110} C 1080,{DECK-100} 1100,{DECK-70} 1130,{DECK-50} "
           f"C 1060,{DECK-60} 1000,{DECK-80} 935,{DECK-92} Z",fill=FLAME,sw=2)
s.raw_path(f"M 945,{DECK-98} C 990,{DECK-118} 1040,{DECK-118} 1080,{DECK-104} C 1040,{DECK-92} 990,{DECK-90} 945,{DECK-94} Z",fill=FLAME2,sw=1.2)
for (x,h) in ((1000,40),(1040,60),(1080,45),(1120,30)):
    s.raw_path(f"M {x-22},{WL+2} C {x-18},{WL-h*0.5} {x-6},{WL-h*0.6} {x},{WL-h} C {x+6},{WL-h*0.6} {x+18},{WL-h*0.5} {x+22},{WL+2} Z",fill=FLAME,sw=1.5)
s.callout(1,505,DECK-20,330,700,"A fire kept the liquid hot",anchor="end")
s.callout(2,470,DECK-110,300,250,"A sealed tank of the|secret liquid",anchor="end")
s.callout(3,PX,DECK-100,640,180,"A pump, or perhaps|bellows, drove it out")
s.callout(4,880,DECK-90,880,240,"A bronze-covered tube|at the bow, turned to aim")
s.callout(5,1060,WL-30,760,680,"Lit as it left the tube,|it burned on the water")
s.save(os.path.join(os.path.dirname(__file__),"..","29-fire-siphon","fire-siphon"))
