import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The swan-neck flask","Louis Pasteur, Paris, about 1860")
GLASS="#e6eef0"; BROTH="#e9cf8a"; CLOUDY="#c9a86a"; FLAME="#e0a030"; DUST="#5e554e"; LAMP="#b9a27a"

R=78; BY=530                                                           # bulb radius and centre height
def neck_d(cx,by):
    t=by-R+6
    return (f"M {cx},{t} L {cx},{t-110} C {cx},{t-190} {cx+95},{t-190} {cx+100},{t-110} "
            f"L {cx+100},{t-60} C {cx+100},{t-20} {cx+150},{t-20} {cx+150},{t-60} L {cx+150},{t-95}")
def flask(cx,by,broth=BROTH,specks=False):
    s.raw_path(neck_d(cx,by),stroke=INK,sw=17)
    s.raw_path(neck_d(cx,by),stroke=GLASS,sw=11)
    s.circle(cx,by,R,fill=GLASS,sw=3)
    s.raw_path(f"M {cx-R+4},{by+12} L {cx+R-4},{by+12} A {R-4} {R-4} 0 0 1 {cx-R+4},{by+12} Z",fill=broth,sw=1.5)
    s.path([(cx-11,by-R+2),(cx+11,by-R+2),(cx+11,by-R+14),(cx-11,by-R+14)],fill=GLASS,close=True,sw=0,stroke="none")
    s.raw_path(f"M {cx-30},{by-R+30} q 10,-12 26,-14",stroke="#ffffff",sw=4)
    if specks:
        for k in range(26):
            s.circle(cx-55+(k*37)%110,by+22+(k*13)%48,2.5,fill="#7a5a30",sw=0)
    return by-R+6                                                      # top of the bulb

# ================= 1: boiled =================
C1=200
t=flask(C1,BY)
s.path([(C1-34,BY+R+56),(C1+34,BY+R+56),(C1+26,BY+R+16),(C1-26,BY+R+16)],fill=LAMP,close=True,sw=2.5)  # spirit lamp
s.raw_path(f"M {C1},{BY+R+16} C {C1-16},{BY+R} {C1-6},{BY+R-10} {C1},{BY+R-2} C {C1+6},{BY+R-10} {C1+16},{BY+R} {C1},{BY+R+16} Z",fill=FLAME,sw=1.5)
for k in range(5):                                                     # bubbles in the boiling broth
    s.circle(C1-40+k*20,BY+30+(k%2)*14,5,fill=GLASS,sw=1.2)
for k in range(3):                                                     # steam from the open end
    s.raw_path(f"M {C1+150},{t-105-k*22} q 8,-6 0,-12 q -8,-6 0,-12",stroke=SOFT,sw=2)
s.text(C1+20,725,"boiled",anchor="middle",italic=True,fill=SOFT)

# ================= 2: left to stand =================
C2=540
t2=flask(C2,BY)
s.raw_path(f"M {C2+100},{t2-60} C {C2+100},{t2-20} {C2+150},{t2-20} {C2+150},{t2-60}",stroke=ACC,sw=11)   # the bend
for (dx,dy) in ((112,-36),(122,-31),(132,-33),(140,-40),(118,-42),(128,-38)):
    s.circle(C2+dx,t2+dy,3.2,fill=DUST,sw=0)
s.arrow(C2+150,t2-170,C2+150,t2-112)                                   # air comes in
s.text(C2+150,t2-180,"air",anchor="middle",italic=True,fill=SOFT,size=18)
s.text(C2+20,725,"left to stand",anchor="middle",italic=True,fill=SOFT)

# ================= 3: tipped =================
C3=900
t3=flask(C3,BY,broth=CLOUDY,specks=True)
for (dx,dy) in ((112,-36),(132,-33),(122,-42)):
    s.circle(C3+dx,t3+dy,3.2,fill=DUST,sw=0)
s.raw_path(f"M {C3-R-30},{BY+30} A {R+30} {R+30} 0 0 1 {C3-40},{BY-R-26}",stroke=INK,sw=2.5)   # tipped and back
s.arrow(C3-R-30,BY+20,C3-R-30,BY+40)
s.arrow(C3-50,BY-R-23,C3-35,BY-R-27)
s.text(C3+20,725,"tipped, then set back",anchor="middle",italic=True,fill=SOFT)

s.callout(1,C1-30,BY+40,90,330,"Broth, boiled|in the flask")
s.callout(2,C1+48,t-150,300,170,"The neck, softened in a|flame and drawn into an S")
s.callout(3,C2+125,t2-22,790,235,"Air passes, but dust|settles in the bend")
s.callout(4,C2+40,BY+40,610,660,"The broth stays|clear for months")
s.callout(5,C3+30,BY+60,1150,660,"Tipped onto the dust,|it clouds in days",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","67-swan-neck-flask","swan-neck-flask"))
