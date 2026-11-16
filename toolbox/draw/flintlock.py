import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The flintlock musket","France, about 1610; in most armies by 1700")
IRON="#7d8488"; STOCK="#b98a5a"; FLINT="#55524e"; PLATE="#d98e78"; SMOKE="#e6e1d8"; BRASS="#d4b25a"

# ---- the whole musket, butt at the left, bayonet fixed at the muzzle
GY=190
s.path([(70,GY+8),(250,GY-2),(300,GY-4),(830,GY-4),(830,GY+12),(300,GY+16),(270,GY+22),(80,GY+64),(64,GY+58)],fill=STOCK,close=True,sw=2.5)
s.path([(240,GY-10),(860,GY-10),(860,GY+2),(240,GY+2)],fill=IRON,close=True,sw=2.5)   # barrel
for x in (480,640,780): s.line(x,GY-10,x,GY+14,stroke=BRASS,sw=3)                      # bands
s.path([(250,GY+2),(318,GY+2),(318,GY+14),(250,GY+14)],fill=ACC,close=True,sw=1.6)    # the lock
s.raw_path(f"M 272,{GY+2} C 268,{GY-10} 276,{GY-18} 284,{GY-18}",stroke=ACC,sw=4)      # its cock
s.raw_path(f"M 262,{GY+18} C 264,{GY+30} 256,{GY+36} 248,{GY+36}",sw=2.5)              # trigger
# the socket bayonet: a tube over the muzzle, a bent neck, and a blade alongside
s.path([(842,GY-14),(884,GY-14),(884,GY+6),(842,GY+6)],fill=METAL,close=True,sw=2.5)
s.path([(878,GY+4),(892,GY+4),(900,GY+18),(886,GY+18)],fill=METAL,close=True,sw=2)
s.path([(890,GY+12),(1120,GY+16),(890,GY+24)],fill=METAL,close=True,sw=2.5)
# a dashed ring round the small lock, and lines to the enlarged view
s.circle(284,GY+4,32,stroke=SOFT,sw=1.5)
CX,CY,RR=330,500,200
s.line(256,GY+20,CX-150,CY-132,stroke=SOFT,sw=1.5,dash="5 6")
s.line(314,GY+20,CX+150,CY-132,stroke=SOFT,sw=1.5,dash="5 6")

# ---- the lock, enlarged (muzzle to the right, as the gun lies)
s.inset(CX,CY,RR)
s.add(f'<clipPath id="lk"><circle cx="{CX}" cy="{CY}" r="{RR-3}"/></clipPath>')
s.add('<g clip-path="url(#lk)">')
s.path([(CX-RR,CY-70),(CX+RR,CY-70),(CX+RR,CY-36),(CX-RR,CY-36)],fill=IRON,close=True,sw=3)          # barrel
s.path([(CX-RR,CY-36),(CX+RR,CY-36),(CX+RR,CY+120),(CX-RR,CY+150)],fill=STOCK,close=True,sw=3)       # stock
s.raw_path(f"M {CX-150},{CY-20} L {CX+130},{CY-20} C {CX+160},{CY-20} {CX+170},{CY+10} {CX+150},{CY+30} "
           f"L {CX-120},{CY+40} C {CX-160},{CY+40} {CX-170},{CY-10} {CX-150},{CY-20} Z",fill=PLATE,sw=3)  # lock plate
# the pan, just under the barrel, and the frizzen standing over it
PX,PY=CX+70,CY-26
s.raw_path(f"M {PX-30},{PY} L {PX+30},{PY} C {PX+28},{PY+18} {PX-28},{PY+18} {PX-30},{PY} Z",fill=ACC,sw=2.5)
s.ellipse(PX,PY,26,4,fill="#3a3430",sw=1.2)
s.path([(PX-30,PY-6),(PX+34,PY-6),(PX+34,PY-1),(PX-30,PY-1)],fill=ACC,close=True,sw=2)            # pan cover
s.raw_path(f"M {PX+22},{PY-6} C {PX+30},{PY-50} {PX+22},{PY-90} {PX+8},{PY-118} L {PX+22},{PY-122} "
           f"C {PX+40},{PY-92} {PX+44},{PY-50} {PX+36},{PY-6} Z",fill=ACC,sw=2.5)                    # striking face
# the frizzen spring, forward on the plate
s.raw_path(f"M {PX+40},{PY+30} C {PX+70},{PY+28} {PX+90},{PY+40} {PX+60},{PY+48} L {PX+10},{PY+50}",stroke=INK,sw=5)
# the cock, a swan neck pivoting on the plate, its jaws holding the flint
QX,QY=CX-60,CY+12
s.raw_path(f"M {QX-16},{QY+12} C {QX-26},{QY-40} {QX-10},{QY-110} {QX+30},{QY-150} L {QX+48},{QY-136} "
           f"C {QX+12},{QY-100} {QX+4},{QY-40} {QX+16},{QY+12} Z",fill=ACC,sw=3)
s.circle(QX,QY,10,fill=METAL,sw=2.5)
JX,JY=QX+40,QY-146
s.path([(JX-14,JY-26),(JX+34,JY-30),(JX+34,JY-22),(JX-12,JY-16)],fill=ACC,close=True,sw=2.5)        # top jaw
s.path([(JX-12,JY+4),(JX+34,JY+2),(JX+34,JY+10),(JX-10,JY+12)],fill=ACC,close=True,sw=2.5)          # lower jaw
s.path([(JX+6,JY-18),(JX+56,JY-14),(JX+62,JY-4),(JX+6,JY+2)],fill=FLINT,close=True,sw=2)            # the flint
s.line(JX+10,JY-32,JX+10,JY+14,stroke=INK,sw=4)                                                       # jaw screw
# the cock's swing, and the sparks
s.raw_path(f"M {JX+30},{JY-50} C {JX+80},{JY-60} {PX+20},{PY-140} {PX+10},{PY-128}",stroke=SOFT,sw=2,extra='stroke-dasharray="6 6"')
for a in (-20,0,20,40):
    r=math.radians(a+90)
    s.line(round(PX+12+8*math.cos(r),1),round(PY-60+8*math.sin(r),1),round(PX+12+24*math.cos(r),1),round(PY-60+24*math.sin(r),1),stroke="#e0a030",sw=2.5)
# the trigger, under the stock
TX=CX-80
s.raw_path(f"M {TX},{CY+140} C {TX+4},{CY+170} {TX-10},{CY+186} {TX-30},{CY+192} L {TX-26},{CY+180} C {TX-14},{CY+172} {TX-10},{CY+156} {TX-12},{CY+140} Z",fill=BRASS,sw=2.5)
s.add('</g>')
s.circle(CX,CY,RR,sw=2.5)

# ---- a line three deep, firing to the right
G=700
s.line(640,G,1150,G,stroke=SOFT,sw=1.5)
def soldier(x,kneel=False,tall=0):
    if kneel:
        s.line(x-30,G,x-6,G-38,stroke=SOFT,sw=5); s.line(x-6,G-38,x+26,G-38,stroke=SOFT,sw=5)
        s.line(x+26,G-38,x+26,G,stroke=SOFT,sw=5)
        hip=(x-6,G-38); sh=(x+6,G-104)
    else:
        s.line(x-20,G,x,G-74-tall,stroke=SOFT,sw=5); s.line(x+18,G,x,G-74-tall,stroke=SOFT,sw=5)
        hip=(x,G-74-tall); sh=(x+8,G-140-tall*2)
    s.line(hip[0],hip[1],sh[0],sh[1],stroke=SOFT,sw=5)
    s.circle(sh[0]+12,sh[1]-20,13,fill=PAPER,stroke=SOFT,sw=4)
    gy=sh[1]+6
    s.line(sh[0]-14,gy+6,sh[0]+130,gy-2,stroke=INK,sw=4)
    s.line(sh[0]+130,gy-2,sh[0]+168,gy-3,stroke=METAL,sw=3)
    s.line(sh[0]+8,gy+6,sh[0]+40,gy,stroke=SOFT,sw=4)
    return (sh[0]+168,gy-3)
tips=[soldier(785,tall=18),soldier(865),soldier(945,kneel=True)]
for (x,y) in tips[2:]:
    for dx,dy,r in ((12,-3,10),(24,-10,13),(38,0,11)):
        s.circle(x+dx,y+dy,r,fill=SMOKE,stroke=SOFT,sw=1.5)

s.callout(1,JX+40,JY-10,620,280,"A flint, gripped|in the cock's jaws")
s.callout(2,PX+30,PY-80,620,380,"The steel: struck,|it flies open")
s.callout(3,PX-10,PY+8,620,480,"Sparks fall|into the pan")
s.callout(4,1000,GY+18,1150,280,"A socket bayonet,|fixed outside the muzzle",anchor="end")
s.callout(5,963,G-124,895,445,"Three ranks deep,|the front one kneeling")
s.save(os.path.join(os.path.dirname(__file__),"..","54-flintlock-musket","flintlock-musket"))
