import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The airlift transport","The Douglas C-54 Skymaster, Berlin, 1948")
SKIN="#c9ced1"; SKIN2="#b3b9bd"; DARK="#4b4f52"; SACK="#a88a66"; GLASSC="#5b6870"; GROUND=650

s.line(60,GROUND,1150,GROUND,stroke=SOFT,sw=1.5)

# ================= the fuselage: a long tube, nose to the right =================
CY=505; R=56; XT,XN=140,1085
nose=[(XN-60+60*math.sin(a*math.pi/40),CY+6-(R+4)*math.cos(a*math.pi/40)) for a in range(0,41)]
body=[(XT,CY-30),(300,CY-R)]+nose+[(330,CY+R),(XT,CY-12)]
s.path(body,fill=SKIN,close=True,sw=3)
# tall tail fin and the tailplane
s.path([(XT+6,CY-30),(118,CY-180),(178,CY-180),(310,CY-R+2)],fill=SKIN,close=True,sw=3)
s.path([(110,CY-20),(270,CY-20),(270,CY-8),(130,CY-8)],fill=SKIN2,close=True,sw=2)
# cockpit and cabin windows
s.path([(1040,CY-40),(1062,CY-34),(1072,CY-20),(1040,CY-20)],fill=GLASSC,close=True,sw=2)
for x in list(range(610,720,36))+list(range(860,990,36)):
    s.path([(x,CY-30),(x+16,CY-30),(x+16,CY-14),(x,CY-14)],fill=GLASSC,close=True,sw=1.5)

# ================= the cargo door behind the wing =================
s.path([(220,CY-40),(300,CY-40),(300,CY+40),(220,CY+40)],fill="#aab1b5",close=True,sw=2.5)
s.line(260,CY-40,260,CY+40,stroke=INK,sw=1.5)
s.circle(290,CY,3,fill=INK,sw=0)

# ================= the cut-away: a level floor stacked with sacks of coal =================
WX0,WX1=340,580; FY=CY+34
s.path([(WX0,CY-42),(WX1,CY-42),(WX1,FY+9),(WX0,FY+9)],fill="#f1ece0",close=True,sw=2)
for row,(y,n) in enumerate(((FY-14,6),(FY-36,6),(FY-58,5))):
    x0=WX0+12+(row%2)*18
    for k in range(n):
        s.ellipse(x0+k*36+17,y+2,17,11,fill=SACK,stroke=INK,sw=1.5)
s.path([(WX0,FY),(WX1,FY),(WX1,FY+9),(WX0,FY+9)],fill=ACC,close=True,sw=2)

# ================= the wing and the engines =================
s.path([(600,CY+34),(760,CY+28),(770,CY+40),(600,CY+52)],fill=SKIN2,close=True,sw=2.5)
for (nx,ny,big) in ((800,CY+10,False),(830,CY+30,True)):
    s.path([(nx-105,ny-14),(nx,ny-19),(nx+14,ny-11),(nx+14,ny+12),(nx,ny+20),(nx-105,ny+16)],fill=SKIN,close=True,sw=2.5)
    s.line(nx+18,ny-64,nx+18,ny+64,stroke=DARK,sw=5)     # propeller seen edge on
    s.circle(nx+18,ny,7,fill=DARK,sw=1.5)

# ================= the landing gear: two main wheels under the wing, one under the nose =================
s.line(705,CY+48,705,GROUND-30,stroke=DARK,sw=7)
s.circle(705,GROUND-30,30,fill=DARK,sw=2.5); s.circle(705,GROUND-30,9,fill="#a7a093",sw=1.5)
s.line(1010,CY+R-4,1010,GROUND-22,stroke=DARK,sw=6)
s.circle(1010,GROUND-22,22,fill=DARK,sw=2.5); s.circle(1010,GROUND-22,7,fill="#a7a093",sw=1.5)

s.callout(1,1010,GROUND-22,1080,700,"A wheel under the nose holds the body level",anchor="end")
s.callout(2,460,FY+4,110,700,"A level floor, not a slope")
s.callout(3,260,CY-20,110,215,"A wide door, with|a hoist and winch")
s.callout(4,848,CY-30,1050,250,"Four engines of|1,450 horsepower",anchor="end")
s.callout(5,440,FY-56,520,250,"About ten tons|of coal, in sacks")
s.save(os.path.join(os.path.dirname(__file__),"..","88-airlift-transport","airlift-transport"))
