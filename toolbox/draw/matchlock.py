import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The matchlock","Europe by the 1470s; Japan from 1543")
IRON="#7d8488"; BRASS="#d4b25a"; CORD="#7a5a3c"; GLOW="#f0c040"; STOCK="#b98a5a"
# ---- the whole gun, small, top right: muzzle at the left
GY=170; G0=640
s.path([(G0,GY-5),(G0+420,GY-6),(G0+420,GY+6),(G0,GY+5)],fill=IRON,close=True,sw=2.5)
s.path([(G0+30,GY+5),(G0+420,GY+6),(G0+460,GY+8),(G0+520,GY+34),(G0+514,GY+48),(G0+456,GY+28),(G0+410,GY+18),(G0+30,GY+13)],fill=STOCK,close=True,sw=2.5)
s.path([(G0+356,GY+6),(G0+392,GY+6),(G0+392,GY+15),(G0+356,GY+15)],fill=BRASS,close=True,sw=1.5)
s.raw_path(f"M {G0+384},{GY+18} C {G0+384},{GY+30} {G0+376},{GY+34} {G0+370},{GY+32}",sw=2.5)
s.path([(G0+330,GY-22),(G0+420,GY-22),(G0+420,GY+44),(G0+330,GY+44)],stroke=SOFT,sw=1.5,close=True,extra='stroke-dasharray="5 6"')
# ---- the lock, enlarged: barrel above, stock below, muzzle to the left
BY=470
s.path([(60,BY),(1140,BY),(1140,BY+40),(60,BY+40)],fill=IRON,close=True,sw=3)
s.path([(60,BY+40),(1140,BY+40),(1140,BY+150),(960,BY+150),(900,BY+120),(60,BY+120)],fill=STOCK,close=True,sw=3)
s.path([(420,BY+48),(900,BY+48),(900,BY+108),(420,BY+108)],fill=BRASS,close=True,sw=3)      # lock plate
# the pan, with its cover swung open
PX,PY=500,BY+44
s.raw_path(f"M {PX-36},{PY-8} L {PX+36},{PY-8} C {PX+34},{PY+14} {PX-34},{PY+14} {PX-36},{PY-8} Z",fill=BRASS,sw=2.5)
s.ellipse(PX,PY-8,32,5,fill="#3a3430",sw=1.5)
s.path([(PX-36,PY-10),(PX-50,PY-52),(PX-38,PY-56),(PX-26,PY-10)],fill=BRASS,close=True,sw=2.5)
# the serpentine, cocked back, pivoting on the lock plate
QX,QY=720,BY+80
s.raw_path(f"M {QX-10},{QY+6} C {QX-12},{QY-50} {QX+10},{QY-130} {QX+66},{QY-196} L {QX+86},{QY-184} C {QX+36},{QY-120} {QX+14},{QY-50} {QX+12},{QY+6} Z",fill=ACC,sw=3)
s.circle(QX,QY,9,fill=BRASS,sw=2.5)
JX,JY=QX+76,QY-192
s.path([(JX-16,JY-2),(JX+14,JY-24),(JX+22,JY-14),(JX-8,JY+8)],fill=ACC,close=True,sw=2.5)
s.raw_path(f"M {JX-12},{JY+2} C {JX-40},{JY-20} {JX+20},{JY-60} {JX+80},{JY-40} C {JX+130},{JY-24} {JX+150},{JY+20} {JX+200},{JY+30}",stroke=CORD,sw=6)
s.circle(JX-16,JY+4,7,fill=GLOW,sw=1.5)
# where it falls: a dashed arc from the cocked jaws down to the pan, with an arrow
s.raw_path(f"M {JX-30},{JY+20} C {JX-120},{JY+40} {PX+80},{PY-80} {PX+14},{PY-18}",stroke=SOFT,sw=2,extra='stroke-dasharray="6 6"')
s.arrow(PX+80,PY-90,PX+28,PY-26)
# the brass spring, U-shaped, reaching forward from the pivot and pressing on the serpentine's tail
for c,w in ((INK,7),(BRASS,3.5)):
    s.raw_path(f"M {QX-14},{QY-4} L {QX-150},{QY-12} C {QX-176},{QY-12} {QX-176},{QY+14} {QX-150},{QY+14} L {QX-40},{QY+12}",stroke=c,sw=w)
# the trigger, below the stock
TX=QX+70
s.raw_path(f"M {TX},{BY+120} C {TX+4},{BY+160} {TX-10},{BY+184} {TX-34},{BY+192} L {TX-30},{BY+180} C {TX-16},{BY+172} {TX-10},{BY+154} {TX-12},{BY+120} Z",fill=BRASS,sw=2.5)

s.callout(1,1060,BY+20,1130,650,"An iron barrel,|about a metre long",anchor="end")
s.callout(2,QX+30,QY-110,640,300,"The serpentine, an arm|holding a burning cord",anchor="end")
s.callout(3,PX-10,PY-6,330,400,"The pan of fine powder,|its cover swung open",anchor="end")
s.callout(4,QX-166,QY,440,650,"A brass spring snaps|the arm forward",anchor="end")
s.callout(5,TX-30,BY+186,700,660,"The trigger|releases it",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","45-matchlock","matchlock"))
