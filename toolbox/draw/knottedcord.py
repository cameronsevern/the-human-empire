import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The knotted cord","the Andes, by about 600")
MAIN="#d9c7a3"
YM=200; ROWS={"h":315,"t":425,"u":545}; BOT=640
# the main cord, twisted
s.line(70,YM,1130,YM,stroke=INK,sw=15); s.line(70,YM,1130,YM,stroke=MAIN,sw=9)
for x in range(80,1125,14):
    s.line(x,YM+4,x+8,YM-4,stroke="#a8916a",sw=1.6)
s.raw_path(f"M 70,{YM} C 50,{YM+10} 48,{YM+40} 60,{YM+60}",stroke=INK,sw=6)
def cord(x,col):
    s.line(x,YM+8,x,BOT,stroke=INK,sw=9); s.line(x,YM+8,x,BOT,stroke=col,sw=5)
    s.ellipse(x,YM+4,9,12,fill=col,sw=2.5)
    for d in (-4,0,4):                                           # frayed end
        s.line(x,BOT,x+d*1.6,BOT+16,stroke=col,sw=2)
def single(x,y,col):
    s.ellipse(x,y,10,8,fill=col,sw=2.2); s.line(x-6,y+5,x+6,y-5,stroke=INK,sw=1.4)
def cluster(x,y,n,col):
    for k in range(n): single(x,y+(k-(n-1)/2)*17,col)
def long(x,y,n,col):
    h=10*n+8; y0=y-h/2
    s.raw_path(f"M {x-10},{y0+6} C {x-10},{y0-2} {x+10},{y0-2} {x+10},{y0+6} L {x+10},{y0+h-6} C {x+10},{y0+h+2} {x-10},{y0+h+2} {x-10},{y0+h-6} Z",fill=col,sw=2.2)
    for k in range(n):
        yy=y0+8+k*10; s.line(x-9,yy+5,x+9,yy-1,stroke=INK,sw=1.4)
def eight(x,y,col):
    s.circle(x,y-7,7,fill=col,sw=2); s.circle(x,y+7,7,fill=col,sw=2)
# five cords: 105, 230, 71, 26, and 342 in red
C=[(200,"#9b7653",(1,0,("L",5))),(330,"#ede4cf",(2,3,None)),(460,"#7d93a6",(0,7,("E",1))),
   (590,"#d8b65a",(0,2,("L",6))),(720,ACC,(3,4,("L",2)))]
for x,col,(h,t,u) in C:
    cord(x,col)
    if h: cluster(x,ROWS["h"],h,col)
    if t: cluster(x,ROWS["t"],t,col)
    if u:
        (long if u[0]=="L" else eight)(*( (x,ROWS["u"],u[1],col) if u[0]=="L" else (x,ROWS["u"],col) ))
for x,col,(h,t,u) in C:
    n=h*100+t*10+(u[1] if u else 0)
    s.text(x,BOT+52,str(n),anchor="middle",italic=True,bold=(col==ACC))
for k,lab in (("h","hundreds"),("t","tens"),("u","units")):
    s.text(160,ROWS[k]+7,lab,size=19,anchor="end",italic=True,fill=SOFT)
    s.line(172,ROWS[k],750,ROWS[k],stroke=SOFT,sw=1,dash="3 9")
s.callout(1,960,YM,900,140,"The main cord")
s.callout(2,720,600,860,640,"Hanging cords: the colour|told what was counted")
s.callout(3,730,ROWS["h"]-20,860,280,"Hundreds: three|single knots, 300")
s.callout(4,730,ROWS["t"]+10,860,410,"Tens: four knots, 40")
s.callout(5,730,ROWS["u"]+12,860,530,"Units: a long knot|with two turns, 2")
s.save(os.path.join(os.path.dirname(__file__),"..","36-knotted-cord","knotted-cord"))
