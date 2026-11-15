import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The telescope","the Netherlands, 1608; Galileo's, 1609")
TUBE="#c9a676"; GLASS="#dbe7ea"; LIGHT="#e0b040"; MOON="#e9e2cf"
Y=330; XO=170; XE=900; XF=1090          # objective, eyepiece, focus (not to scale)
# the tube
s.path([(XO,Y-34),(XE+20,Y-24),(XE+20,Y+24),(XO,Y+34)],fill=TUBE,close=True,sw=3)
for x in range(XO+80,XE,110):
    s.line(x,Y-33+(x-XO)*0.0125,x,Y+33-(x-XO)*0.0125,stroke="#9b7c55",sw=1.4)
# light from a distant object: three rays in, bent to a focus that the eyepiece never reaches
H=46
for d in (-H,0,H):
    s.line(40,Y+d,XO,Y+d,stroke=LIGHT,sw=3)
    e=d*(XF-XE)/(XF-XO)
    s.line(XO,Y+d,XE,Y+e,stroke=LIGHT,sw=3)
    s.line(XE,Y+e,1086,Y+e,stroke=LIGHT,sw=3)                         # straightened again, narrower
    s.line(XE,Y+e,XF,Y,stroke=SOFT,sw=1.4,dash="4 6")                 # where they would have met
# the objective: a convex lens
s.raw_path(f"M {XO},{Y-62} C {XO+22},{Y-30} {XO+22},{Y+30} {XO},{Y+62} C {XO-22},{Y+30} {XO-22},{Y-30} {XO},{Y-62} Z",fill=GLASS,sw=3)
# the eyepiece: a concave lens, in terracotta
s.raw_path(f"M {XE-12},{Y-34} L {XE+12},{Y-34} C {XE+4},{Y-10} {XE+4},{Y+10} {XE+12},{Y+34} L {XE-12},{Y+34} C {XE-4},{Y+10} {XE-4},{Y-10} {XE-12},{Y-34} Z",fill=ACC,sw=3)
# the eye
s.raw_path(f"M 1084,{Y} C 1096,{Y-18} 1130,{Y-20} 1146,{Y} C 1130,{Y+20} 1096,{Y+18} 1084,{Y} Z",fill=PAPER,sw=2.5)
s.circle(1098,Y,9,fill=INK,sw=0)
# inset: what the eye sees, a field narrower than the Moon
CX,CY,R=300,590,105
s.inset(CX,CY,R)
s.circle(CX,CY,R-3,fill="#4a5262",sw=0)          # night sky
MX,MR=CX+210,210
d=210
phi=math.degrees(math.acos((R*R+d*d-MR*MR)/(2*R*d)))
ang=math.degrees(math.acos((MR*MR+d*d-R*R)/(2*MR*d)))
field=[(CX+R*math.cos(math.radians(a)),CY+R*math.sin(math.radians(a))) for a in range(-int(phi),int(phi)+1,3)]
limb=[(MX+MR*math.cos(math.radians(180+t)),CY+MR*math.sin(math.radians(180+t))) for t in range(-int(ang),int(ang)+1,2)]
s.path(field+limb,fill=MOON,close=True,sw=2)
for (x,y,r) in ((CX+60,CY-30,12),(CX+50,CY+40,8),(CX+85,CY+10,6)):
    s.circle(x,y,r,fill="#d6cdb4",sw=1.2)

s.callout(1,XO+8,Y-50,250,180,"A convex lens bends|the light inward")
s.callout(2,560,Y+28,620,480,"A tube about a metre long,|covered in paper")
s.callout(3,XE+4,Y-30,900,180,"A concave lens near the eye|catches the rays before|they meet",anchor="end")
s.callout(4,1120,Y+14,1130,560,"14 to 20 times nearer:|the ratio of the two|lenses' strengths",anchor="end")
s.callout(5,CX+60,CY+60,440,680,"The field: less than|half the Moon at once")
s.save(os.path.join(os.path.dirname(__file__),"..","51-telescope","telescope"))
