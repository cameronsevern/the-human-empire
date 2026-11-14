import math,sys,os,random
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
random.seed(4)
BAMBOO="#e3cf96"
s=Sheet("The bamboo book","about 2,300 years ago")
X0,Y0,Y1,SW,N=190,225,605,24,19
# the rolled part, at the left
s.add(f'<rect x="96" y="{Y0-6}" width="96" height="{Y1-Y0+12}" rx="40" fill="{BAMBOO}" stroke="{INK}" stroke-width="3"/>')
for x in (118,140,162): s.line(x,Y0+4,x,Y1-4,sw=1.5)
s.ellipse(144,Y0-6,48,13,fill=BAMBOO,sw=3)
s.raw_path(f"M 112,{Y0-6} a 30,8 0 1 1 30,7 a 16,5 0 1 1 -14,-6",sw=1.5)
# the open strips
for i in range(N):
    x=X0+i*SW
    s.add(f'<rect x="{x}" y="{Y0}" width="{SW}" height="{Y1-Y0}" fill="{BAMBOO}" stroke="{INK}" stroke-width="2"/>')
    y=Y0+22
    while y<Y1-24:
        if not (300<y<326 or 500<y<526):
            h=random.choice((7,9,11)); w=random.choice((5,7,9))
            s.line(x+SW/2-w/2,y,x+SW/2+w/2,y+random.choice((-2,0,2)),sw=2.4)
            s.line(x+SW/2,y-3,x+SW/2+random.choice((-2,2)),y+h-3,sw=2.4)
        y+=17
# two cords, the working part
for cy in (313,513):
    s.line(96,cy,X0+N*SW,cy,stroke=ACC,sw=5)
    for i in range(N+1):
        s.line(X0+i*SW,cy-6,X0+i*SW,cy+6,stroke=ACC,sw=3)
    s.raw_path(f"M {X0+N*SW},{cy} q 22,4 30,26 M {X0+N*SW},{cy} q 26,-2 36,14",stroke=ACC,sw=4)
# ink stone, rubbing stone, brush and knife
s.add(f'<rect x="800" y="470" width="150" height="110" rx="10" fill="{STONE}" stroke="{INK}" stroke-width="3"/>')
s.ellipse(862,528,44,30,fill="#3a3531",sw=2)
s.add(f'<rect x="905" y="482" width="30" height="30" rx="5" fill="{STONE}" stroke="{INK}" stroke-width="2.5"/>')
s.line(990,610,1120,450,stroke=BAMBOO,sw=11); s.line(990,610,1120,450,sw=1.5)
s.raw_path("M 994,604 L 972,632 L 985,614 Z",fill="#3a3531",sw=3)
s.raw_path("M 812,445 L 917,432 Q 937,432 950,442 L 917,450 Z",fill=METAL,sw=2.5)
s.circle(802,447,11,fill="none",sw=4)
s.callout(1,X0+16*SW+12,Y0,640,150,"Bamboo is split into strips,|scraped smooth and dried over a fire")
s.callout(2,X0+18*SW+12,400,740,375,"One column of writing|runs down each strip")
s.callout(3,X0+N*SW-4,313,740,265,"Cords tie the strips|side by side, in order")
s.callout(4,112,300,70,150,"The book rolls up|like a mat")
s.callout(5,850,580,760,680,"A brush, ink made of soot, and|a knife to shave off mistakes")
s.save(os.path.join(os.path.dirname(__file__),"..","17-bamboo-book","bamboo-book"))
