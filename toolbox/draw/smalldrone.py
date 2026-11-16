import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The small drone","A racing drone armed for war, and its pilot, Ukraine, 2020s")
CARBON="#3b3d40"; CARBON2="#55585c"; MOTOR="#9aa2a8"; PROP="#c9d3d8"; BATT="#d9b54a"; OLIVE="#7d7f5a"; GOG="#2b2826"

# ================= the drone, side view, nose to the left, flying slightly nose-down =================
CX,CY=760,400; S=1.15
ang=-8                                     # degrees: nose tipped down
def R(x,y):
    a=math.radians(ang); x*=S; y*=S
    return (round(CX+x*math.cos(a)-y*math.sin(a),1),round(CY+x*math.sin(a)+y*math.cos(a),1))
def prop(x,y,rx,ry,stroke=INK):
    cx,cy=R(x,y)
    s.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx*S:.1f}" ry="{ry*S:.1f}" fill="{PROP}" fill-opacity="0.55" stroke="{stroke}" stroke-width="1.5" transform="rotate({ang} {cx} {cy})"/>')
# rear pair of arms and propellers (behind, paler)
for x in (-150,150):
    s.path([R(x*0.92,-20),R(0,-12),R(0,-6),R(x*0.92,-14)],fill=CARBON2,close=True,sw=1.5)
    s.path([R(x*0.92-9,-56),R(x*0.92+9,-56),R(x*0.92+9,-18),R(x*0.92-9,-18)],fill=MOTOR,close=True,sw=1.5)
    prop(x*0.92,-62,105,6,stroke=SOFT)
# the central body: two carbon plates with the electronics between
s.path([R(-120,-8),R(120,-8),R(120,4),R(-120,4)],fill=CARBON,close=True,sw=2.5)
s.path([R(-90,4),R(100,4),R(100,24),R(-90,24)],fill=CARBON2,close=True,sw=2)
s.path([R(-120,24),R(120,24),R(120,34),R(-120,34)],fill=CARBON,close=True,sw=2.5)
# battery strapped on top
s.path([R(-70,-52),R(70,-52),R(70,-8),R(-70,-8)],fill=BATT,close=True,sw=2.5)
for x in (-30,30): s.path([R(x-6,-56),R(x+6,-56),R(x+6,-6),R(x-6,-6)],fill=INK,close=True,sw=1)
# camera in the nose, tilted up
s.path([R(-150,-6),R(-118,-6),R(-118,30),R(-150,30)],fill=ACC,close=True,sw=2.5)
s.circle(*R(-156,8),15,fill=ACC,sw=2.5); s.circle(*R(-160,6),6,fill=INK,sw=1)
# front pair of arms, motors and propellers
for x in (-150,150):
    s.path([R(0,0),R(x,-8),R(x,4),R(0,12)],fill=CARBON,close=True,sw=2)
    s.path([R(x-11,-50),R(x+11,-50),R(x+11,-6),R(x-11,-6)],fill=MOTOR,close=True,sw=2)
    s.line(*R(x,-50),*R(x,-58),stroke=INK,sw=3)
    prop(x,-58,115,7)
# antennas at the back: a whip for commands, a stubby one for video
s.line(*R(118,0),*R(185,-30),stroke=INK,sw=3)
s.line(*R(110,26),*R(150,52),stroke=INK,sw=3); s.circle(*R(154,56),8,fill=INK,sw=1)
# the charge, strapped underneath, pointing forward
s.path([R(-70,40),R(80,40),R(80,74),R(-70,74)],fill=OLIVE,close=True,sw=2.5)
s.path([R(-70,40),R(-110,57),R(-70,74)],fill=OLIVE,close=True,sw=2.5)
s.path([R(80,46),R(110,46),R(110,68),R(80,68)],fill="#5f6145",close=True,sw=2)
for x in (-30,40): s.path([R(x-5,30),R(x+5,30),R(x+5,78),R(x-5,78)],fill="#2b2826",close=True,sw=1)

# ================= the pilot, with goggles and a hand controller =================
PX,PY=175,660
sh=s.person(PX,PY,lean=0.05,scale=1.5)
hx,hy=sh[0]+16*1.5*math.sin(0.05),sh[1]-20*1.5*math.cos(0.05)
s.path([(hx-14,hy-10),(hx+24,hy-10),(hx+24,hy+6),(hx-14,hy+6)],fill=GOG,close=True,sw=2)   # goggles
CTX,CTY=sh[0]+46,sh[1]+40
s.line(sh[0],sh[1]+10,CTX-10,CTY,stroke=SOFT,sw=4)
s.path([(CTX-16,CTY-12),(CTX+30,CTY-12),(CTX+30,CTY+12),(CTX-16,CTY+12)],fill=CARBON2,close=True,sw=2)
s.line(CTX-4,CTY-12,CTX-4,CTY-26,stroke=INK,sw=2.5); s.line(CTX+18,CTY-12,CTX+18,CTY-26,stroke=INK,sw=2.5)
s.line(CTX+26,CTY-12,CTX+44,CTY-50,stroke=INK,sw=2)
# the radio link: commands out, video back
s.raw_path(f"M {CTX+50},{CTY-58} Q 430 350 572 372",stroke=SOFT,sw=2,extra='stroke-dasharray="8 8"')
s.raw_path(f"M 572 398 Q 430 430 {hx+40},{hy+4}",stroke=SOFT,sw=2,extra='stroke-dasharray="3 7"')
s.text(PX,PY+40,"the pilot",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,*R(-156,8),430,600,"A camera in the nose:|the pilot sees what it sees")
s.callout(2,*R(150,-30),940,235,"Four motors; their|speeds steer it")
s.callout(3,*R(-40,-46),640,190,"A battery|strapped on top")
s.callout(4,*R(70,64),1150,660,"An anti-tank grenade|strapped underneath",anchor="end")
s.callout(5,hx+24,hy-2,140,180,"Goggles show the video,|sent back by radio")
s.save(os.path.join(os.path.dirname(__file__),"..","104-small-drone","small-drone"))
