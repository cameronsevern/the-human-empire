import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The fire lance","China, by the 1100s")
FLAME="#e9a35c"; FLAME2="#f3cf7a"; POWDER="#4a4440"; BAMBOO="#c9b36b"
Y=470
# the spear shaft, running off the frame at the left
s.line(60,Y+10,880,Y+10,stroke=INK,sw=14); s.line(60,Y+10,880,Y+10,stroke=WOOD,sw=8)
# the iron spearhead
s.path([(870,Y+3),(880,Y-4),(985,Y+10),(880,Y+24),(870,Y+17)],fill=METAL,close=True,sw=3)
# the tube, tied on above the shaft just behind the head
T0,T1,TY,TR=520,830,Y-34,24
s.path([(T0,TY-TR),(T1,TY-TR),(T1,TY+TR),(T0,TY+TR)],fill=ACC,close=True,sw=3)
s.ellipse(T1,TY,8,TR,fill="#7a3426",sw=2.5)
s.ellipse(T0,TY,8,TR,fill=ACC,sw=2.5)
for x in (600,690,770):                                    # bamboo nodes
    s.line(x,TY-TR+2,x,TY+TR-2,stroke="#8f3f2c",sw=3)
# a cut-away window showing the powder and the shards packed inside
s.path([(625,TY-14),(760,TY-14),(760,TY+14),(625,TY+14)],fill=POWDER,close=True,sw=2)
for (x,y) in ((640,TY-6),(662,TY+6),(690,TY-4),(712,TY+5),(735,TY-7),(748,TY+4)):
    s.path([(x-5,y-3),(x+5,y-5),(x+4,y+4),(x-4,y+5)],fill=STONE,close=True,sw=1.2)
# cords lashing the tube to the shaft
for x in (545,700,805):
    for d in (0,9):
        s.line(x+d,TY-TR-2,x+d-6,Y+20,stroke=INK,sw=2.5)
# the fuse at the back of the tube, with a spark
s.raw_path(f"M {T0},{TY} C {T0-30},{TY-4} {T0-40},{TY-30} {T0-70},{TY-34}",sw=2.5)
s.circle(T0-72,TY-35,6,fill=FLAME,sw=1.5)
for a in range(0,360,60):
    r=math.radians(a); s.line(T0-72+9*math.cos(r),TY-35+9*math.sin(r),T0-72+15*math.cos(r),TY-35+15*math.sin(r),stroke=FLAME,sw=2)
# the jet of flame from the mouth of the tube, past the spearhead
s.raw_path(f"M {T1+6},{TY-16} C 900,{TY-60} 1010,{TY-80} 1140,{TY-50} C 1080,{TY-30} 1110,{TY-10} 1145,{TY+18} "
           f"C 1040,{TY+30} 940,{TY+26} {T1+6},{TY+16} Z",fill=FLAME,sw=2)
s.raw_path(f"M {T1+10},{TY-8} C 900,{TY-30} 980,{TY-36} 1060,{TY-24} C 990,{TY-6} 920,{TY+6} {T1+10},{TY+8} Z",fill=FLAME2,sw=1.2)
for (x,y) in ((1000,TY-90),(1060,TY+50),(1110,TY-100),(960,TY+44)):
    s.path([(x-4,y-3),(x+4,y-4),(x+3,y+3),(x-3,y+4)],fill=STONE,close=True,sw=1.2)
s.callout(1,600,TY-TR,470,220,"A tube of bamboo,|or later of thick paper",anchor="end")
s.callout(2,700,TY+8,640,650,"Packed with gunpowder, and before long|with broken pottery and bits of iron")
s.callout(3,551,Y+2,380,620,"Lashed to a|spear shaft",anchor="end")
s.callout(4,T0-60,TY-34,230,330,"A fuse, lit|by the soldier",anchor="end")
s.callout(5,1040,TY-50,880,220,"A jet of flame and|sparks, a few metres long")
s.save(os.path.join(os.path.dirname(__file__),"..","32-fire-lance","fire-lance"))
