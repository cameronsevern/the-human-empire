import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The hand axe","about 1.7 million years ago")
cx,cy=430,420
d=f"M {cx},{cy-250} C {cx+70},{cy-170} {cx+150},{cy-20} {cx+140},{cy+110} C {cx+130},{cy+210} {cx+60},{cy+250} {cx},{cy+250} C {cx-60},{cy+250} {cx-130},{cy+210} {cx-140},{cy+110} C {cx-150},{cy-20} {cx-70},{cy-170} {cx},{cy-250} Z"
s.raw_path(d,fill=STONE,stroke=ACC,sw=7)
s.raw_path(d,fill="none",sw=2)
for (a,b,c,e) in ((cx,cy-200,cx-20,cy+180),(cx-60,cy-60,cx-110,cy+60),(cx+50,cy-80,cx+105,cy+40),(cx-40,cy+60,cx-80,cy+170),(cx+30,cy+40,cx+80,cy+160),(cx-10,cy-120,cx+40,cy-30)):
    s.line(a,b,c,e,stroke=SOFT,sw=1.5)
# side view
sx=760
s.raw_path(f"M {sx},{cy-250} C {sx+30},{cy-120} {sx+50},{cy+60} {sx+40},{cy+170} C {sx+30},{cy+235} {sx+10},{cy+250} {sx},{cy+250} C {sx-10},{cy+250} {sx-30},{cy+235} {sx-40},{cy+170} C {sx-50},{cy+60} {sx-30},{cy-120} {sx},{cy-250} Z",fill=STONE)
s.text(sx,cy+300,"From the side",anchor="middle",italic=True)
s.callout(1,cx,cy-235,300,160,"A point for piercing|and digging",anchor="end")
s.callout(2,cx+142,cy+60,560,640,"Two long cutting|edges")
s.callout(3,cx-40,cy+240,300,680,"A rounded end that|fits the palm",anchor="end")
s.callout(4,cx+60,cy-20,900,230,"Shaped by knocking|flakes off both|faces of a stone")
s.callout(5,sx+38,cy+120,940,560,"Thin, and the same|on both sides")
s.save(os.path.join(os.path.dirname(__file__),"..","01-hand-axe","hand-axe"))
