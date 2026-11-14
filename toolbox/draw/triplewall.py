import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The triple wall","the years 413 to 447")
EARTH="#d9c6a0"; TOWER="#ddd6ca"
k=13  # pixels per metre
def crenel(x0,x1,top,h=10,w=10):
    pts=[]; x=x0; up=True
    while x<x1-1:
        nx=min(x+w,x1)
        y=top-h if up else top
        pts+= [(x,y),(nx,y)]; up=not up; x=nx
    return pts
# ground profile, outside at the left, the city at the right
OUT=500; PARA=492; PERI=476; CITY=466
MO0,MO1=110,110+20*k           # moat, 20 m wide
MBOT=OUT+9*k
LW=MO1+14                      # low wall on the moat's inner edge
OW0=LW+15*k; OW1=OW0+2*k       # outer wall, 2 m thick
IW0=OW1+15*k; IW1=IW0+5*k      # inner wall, 5 m thick
# towers, seen behind the walls
s.add(f'<rect x="{OW0-10}" y="{PARA-13*k}" width="{4*k+12}" height="{13*k}" fill="{TOWER}" stroke="{SOFT}" stroke-width="2"/>')
s.path(crenel(OW0-10,OW0+4*k+2,PARA-13*k,h=9,w=9),stroke=SOFT,sw=2)
s.add(f'<rect x="{IW0-40}" y="{PERI-20*k}" width="{10*k}" height="{20*k}" fill="{TOWER}" stroke="{SOFT}" stroke-width="2"/>')
s.path(crenel(IW0-40,IW0-40+10*k,PERI-20*k,h=10,w=10),stroke=SOFT,sw=2)
# earth, cut through
s.path([(60,OUT),(MO0,OUT),(MO0+30,MBOT),(MO1-6,MBOT),(MO1,PARA),(OW0,PARA),(OW0,PERI),(IW0,PERI),(IW0,CITY),(1150,CITY),(1150,662),(60,662)],
       fill=EARTH,sw=0,close=True)
s.path([(60,OUT),(MO0,OUT),(MO0+30,MBOT),(MO1-6,MBOT),(MO1,PARA)],sw=3)
s.line(OW1,PERI,IW0,PERI,sw=3); s.line(IW1,CITY,1150,CITY,sw=3); s.line(LW+14,PARA,OW0,PARA,sw=3)
s.line(60,662,1150,662,stroke=SOFT,sw=1.5)
# the low wall: the moat's inner face, carried up as a breastwork
s.path([(MO1-6,MBOT),(MO1,MBOT)]+[(MO1,PARA-20)]+crenel(MO1,LW+14,PARA-20,h=8,w=7)[1:]+[(LW+14,PARA-20),(LW+14,PARA)]+[(MO1-6,PARA)],fill=STONE,close=True,sw=2.5)
s.add(f'<rect x="{MO1-6}" y="{PARA-20}" width="{LW+14-MO1+6}" height="{MBOT-PARA+20}" fill="{STONE}" stroke="{INK}" stroke-width="2.5"/>')
s.path(crenel(MO1-6,LW+14,PARA-20,h=8,w=7),fill="none",sw=2.5)
# the outer wall
top=PARA-9*k
s.add(f'<rect x="{OW0}" y="{top}" width="{OW1-OW0}" height="{PARA-top}" fill="{STONE}" stroke="{INK}" stroke-width="3"/>')
s.path(crenel(OW0,OW1,top,h=10,w=9),sw=3)
# the inner wall, the main defence
top2=PERI-12*k
s.add(f'<rect x="{IW0}" y="{top2}" width="{IW1-IW0}" height="{PERI-top2}" fill="{ACC}" stroke="{INK}" stroke-width="3"/>')
s.path(crenel(IW0,IW1,top2,h=12,w=11),sw=3)
for y in range(top2+24,PERI,26):
    s.line(IW0+3,y,IW1-3,y,stroke="#8f3f2c",sw=4)    # bands of brick
s.text(70,470,"Outside",italic=True,size=19,fill=SOFT)
s.text(1140,440,"The city",anchor="end",italic=True,size=19,fill=SOFT)
s.callout(1,(MO0+MO1)/2,MBOT-30,120,700,"A moat over 20 metres wide and up to 10 deep")
s.callout(2,MO1+8,PARA-24,330,280,"A low wall along the|edge of the moat",anchor="end")
s.callout(3,OW0+12,PARA-70,560,170,"The outer wall, 9 metres|high, with its own towers",anchor="end")
s.callout(4,(OW1+IW0)/2+40,PERI+4,720,700,"A terrace between the walls")
s.callout(5,(IW0+IW1)/2,top2+60,1150,120,"The inner wall, 12 metres|high and 5 thick, with|towers up to 20 metres",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","27-triple-wall","triple-wall"))
