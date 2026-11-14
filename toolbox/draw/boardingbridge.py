import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The boarding bridge","about 2,285 years ago")
WATER="#9fb8c8"
DECK=500; WL=590
# oars under the hull
for i in range(13):
    x=90+i*36
    s.line(x,DECK+40,x-30,WL+70,sw=1.6)
# the bow of a galley, broken off at the left; the bronze ram at the waterline
s.raw_path(f"M 60,{DECK} L 740,{DECK} C 775,{DECK-6} 800,{DECK+30} 812,{WL-10} L 60,{WL-10} "
           f"L 70,{WL-30} L 55,{DECK+50} L 68,{DECK+25} Z",fill=WOOD)
s.line(66,DECK+18,752,DECK+18,sw=1.5)
s.raw_path(f"M 806,{WL-32} L 885,{WL-16} L 806,{WL} Z",fill=METAL,sw=2.5)
s.raw_path(f"M 60,{WL} Q 90,{WL-8} 120,{WL} T 180,{WL}",stroke=WATER,sw=2.5)
s.line(830,WL+6,940,WL+6,stroke=WATER,sw=2.5)
# the pole, with a pulley at the top
PX,PT=540,200
s.line(PX,DECK,PX,PT,sw=11); s.line(PX,DECK,PX,PT,stroke=WOOD,sw=6)
s.circle(PX,PT,12,fill=WOOD,sw=3)
# the gangway, hoisted: hinged on the deck behind the pole, rising forward through a slot round it
HX,L,ang=460,440,math.radians(38)
EX,EY=HX+L*math.cos(ang),DECK-L*math.sin(ang)
nx,ny=-math.sin(ang),-math.cos(ang)   # unit normal pointing up-left
t=14
s.path([(HX,DECK),(EX,EY),(EX+nx*t,EY+ny*t),(HX+nx*t,DECK+ny*t)],fill=WOOD,close=True,sw=3)
# knee-high rail along the gangway
r=30
s.line(HX+nx*(t+r)+40*math.cos(ang),DECK+ny*(t+r)-40*math.sin(ang),EX+nx*(t+r),EY+ny*(t+r),sw=2.5)
for k in range(6):
    f=0.09+k*0.18
    bx,by=HX+(EX-HX)*f+nx*t,DECK+(EY-DECK)*f+ny*t
    s.line(bx,by,bx+nx*r,by+ny*r,sw=2)
# the iron spike under the far end
s.path([(EX-7,EY+2),(EX+7,EY+2),(EX,EY+64)],fill=ACC,stroke=INK,sw=2.5,close=True)
s.circle(EX,EY-6,6,fill=PAPER,sw=2.5)
# the rope: from the ring at the end, over the pulley, down the pole to the crew
s.line(EX,EY-6,PX+8,PT-8,sw=2.2)
s.line(PX-12,PT,PX-12,DECK-6,sw=2.2)
# where it falls: forward and down onto the enemy's deck
s.line(HX+330,DECK-8,HX+L+20,DECK-8,sw=2.5,dash="10 9")
a0,a1=math.radians(28),math.radians(6)
p0=(HX+L*math.cos(a0),DECK-L*math.sin(a0)); p1=(HX+L*math.cos(a1),DECK-L*math.sin(a1))
s.raw_path(f"M {p0[0]:.1f},{p0[1]:.1f} A {L} {L} 0 0 1 {p1[0]:.1f},{p1[1]:.1f}",sw=2.5,stroke=INK,extra='stroke-dasharray="5 8"')
s.arrow(p1[0]-5,p1[1]-14,p1[0],p1[1])
s.callout(1,PX,290,420,230,"A pole about seven|metres tall, with a|pulley at the top",anchor="end")
s.callout(2,(EX+PX)/2,(EY+PT)/2-4,860,120,"A rope holds it up.|The crew let it go")
s.callout(3,HX+30+nx*14,DECK-30*math.tan(ang)+ny*14,420,380,"A gangway eleven|metres long, with a|rail on each side",anchor="end")
s.callout(4,EX+5,EY+38,970,250,"An iron spike|bites into the|enemy's deck")
s.callout(5,PX+6,DECK-80*math.tan(ang)-4,620,410,"A slot round the|pole lets it swing|to either side")
s.save(os.path.join(os.path.dirname(__file__),"..","23-boarding-bridge","boarding-bridge"))
