import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The cavity magnetron","Randall and Boot's six-hole magnetron, Birmingham, 1940")
COPPER="#d9a77a"; DARKC="#a8714a"; VAC="#f3ecdc"; MAG="#6e7478"; ELEC="#3d5a80"

# ================= the copper block, cut across =================
CX,CY,R=520,430,175
s.circle(CX,CY,R,fill=COPPER,stroke=INK,sw=3)
BORE=58; RC=112; RH=30
# slots from each hole to the central space, then the holes, then the central space
for k in range(6):
    a=math.radians(90+60*k); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux
    p=[(CX+ux*(BORE-4)+px*7,CY+uy*(BORE-4)+py*7),(CX+ux*RC+px*7,CY+uy*RC+py*7),
       (CX+ux*RC-px*7,CY+uy*RC-py*7),(CX+ux*(BORE-4)-px*7,CY+uy*(BORE-4)-py*7)]
    s.path([(round(x,1),round(y,1)) for x,y in p],fill=VAC,close=True,sw=2)
for k in range(6):
    a=math.radians(90+60*k)
    s.circle(round(CX+RC*math.cos(a),1),round(CY+RC*math.sin(a),1),RH,fill=ACC,stroke=INK,sw=2.5)
s.circle(CX,CY,BORE,fill=VAC,stroke=INK,sw=2.5)
# re-open the slot mouths over the bore outline
for k in range(6):
    a=math.radians(90+60*k); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux
    p=[(CX+ux*(BORE-6)+px*6,CY+uy*(BORE-6)+py*6),(CX+ux*(BORE+6)+px*6,CY+uy*(BORE+6)+py*6),
       (CX+ux*(BORE+6)-px*6,CY+uy*(BORE+6)-py*6),(CX+ux*(BORE-6)-px*6,CY+uy*(BORE-6)-py*6)]
    s.path([(round(x,1),round(y,1)) for x,y in p],fill=VAC,stroke=VAC,close=True,sw=1)
# the electron cloud: curved spokes whirling round the cathode
for k in range(6):
    a0=math.radians(60*k+20)
    pts=[]
    for i in range(9):
        r=20+i*4.2; a=a0+i*0.11
        pts.append((round(CX+r*math.cos(a),1),round(CY+r*math.sin(a),1)))
    s.path(pts,stroke=ELEC,sw=2.5)
# the cathode in the middle
s.circle(CX,CY,16,fill="#5c5650",stroke=INK,sw=2.5)
# the output loop in the upper-right hole, led out through the block in a pipe
a=math.radians(330); ux,uy=math.cos(a),math.sin(a); px,py=-uy,ux
hx,hy=CX+RC*ux,CY+RC*uy
s.circle(round(hx,1),round(hy,1),11,fill="none",stroke=INK,sw=2.5)
for off in (-8,8):
    s.line(round(hx+ux*11+px*off,1),round(hy+uy*11+py*off,1),round(CX+(R+70)*ux+px*off,1),round(CY+(R+70)*uy+py*off,1),stroke=INK,sw=2.2)
s.text(CX,CY+R+40,"the copper block, cut across",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= from the side, between the magnet's poles =================
MX=960
s.raw_path(f"M {MX-80},{480} L {MX-80},{290} Q {MX-80},{230} {MX-20},{230} L {MX+20},{230} Q {MX+80},{230} {MX+80},{290} L {MX+80},{480} L {MX+48},{480} L {MX+48},{295} Q {MX+48},{262} {MX+15},{262} L {MX-15},{262} Q {MX-48},{262} {MX-48},{295} L {MX-48},{480} Z",fill=MAG,sw=2.5)
s.path([(MX-80,370),(MX-48,370),(MX-48,480),(MX-80,480)],fill="#9aa1a5",close=True,sw=2)   # pole faces
s.path([(MX+48,370),(MX+80,370),(MX+80,480),(MX+48,480)],fill="#9aa1a5",close=True,sw=2)
s.path([(MX-40,350),(MX+40,350),(MX+40,500),(MX-40,500)],fill=COPPER,close=True,sw=2.5)      # the block, edge on
s.line(MX,500,MX,560,stroke=INK,sw=3); s.line(MX-6,560,MX+6,560,stroke=INK,sw=3)               # cathode leads
s.text(MX,590,"seen from the side",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,512,444,330,640,"A hot cathode|gives off electrons",anchor="end")
s.callout(2,MX+64,450,1100,690,"A magnet bends|their paths",anchor="end")
s.callout(3,round(CX+RC*math.cos(math.radians(210)),1)-20,round(CY+RC*math.sin(math.radians(210)),1),280,300,"Six holes in the|copper ring like|whistles as the|electrons sweep past",anchor="end")
s.callout(4,500,395,320,170,"The electrons whirl|round in spokes",anchor="end")
s.callout(5,round(CX+(R+66)*math.cos(math.radians(330)),1),round(CY+(R+66)*math.sin(math.radians(330)),1),720,150,"A loop leads the|10 cm waves out|to the aerial")
s.save(os.path.join(os.path.dirname(__file__),"..","81-radar","magnetron"))
