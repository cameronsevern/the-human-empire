import math,sys,os,random
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
random.seed(4)
s=Sheet("The scroll","about 5,000 years ago")
SKIN="#ead9b6"; ROLL="#dcc79e"
T,B=290,545
# open stretch
s.path([(345,T+8),(915,T+8),(915,B-8),(345,B-8)],fill=SKIN,close=True)
# columns of generic writing
for cx in (385,510,655,780):
    for j in range(10):
        y=T+38+j*22
        w=100 if j<9 else random.randint(45,80)
        s.line(cx+(100-w),y,cx+100,y,sw=2.2,dash=f"{random.randint(5,11)} 4 {random.randint(3,8)} 5 {random.randint(6,12)} 4")
# seam between sheets, sewn (accent)
s.line(631,T+8,631,B-8,sw=1.5)
for y in range(T+20,B-12,18): s.line(624,y,638,y+8,stroke=ACC,sw=3.5)
# the two rolls
for x in (320,890):
    s.add(f'<rect x="{x}" y="{T}" width="50" height="{B-T}" fill="{ROLL}" stroke="{INK}" stroke-width="3"/>')
    s.ellipse(x+25,T,25,9,fill=SKIN); s.ellipse(x+25,T,13,4.5,fill=ROLL,sw=2); 
    s.raw_path(f"M {x},{B} A 25 9 0 0 0 {x+50},{B}",fill=ROLL)
# ink pot and reed pen
s.raw_path("M 525,640 Q 500,650 502,680 Q 506,712 550,712 Q 594,712 598,680 Q 600,650 575,640 Z",fill=CLAY)
s.ellipse(550,640,26,8,fill="#3a3430")
s.path([(640,700),(808,628),(813,638),(646,708)],fill=WOOD,close=True,sw=2.5)
s.path([(640,700),(626,710),(646,708)],fill=INK,close=True,sw=2)
s.callout(1,760,T+22,900,170,"Sheets of skin|or papyrus")
s.callout(2,631,T+60,430,150,"The sheets are joined edge|to edge: skin is sewn,|papyrus is glued",anchor="end")
s.callout(3,410,B-22,150,672,"Narrow columns of writing,|side by side")
s.callout(4,745,660,880,655,"A reed pen, and ink of|soot, gum and water")
s.callout(5,330,450,275,330,"The reader unrolls|with one hand and|rolls up with|the other",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","14-scroll","scroll"))
