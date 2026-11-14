import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The bow","more than 60,000 years ago")
# drawn bow: stave bent, string pulled back to the left
tx,ty=560,150; bx,by=560,650; hx,hy=330,400   # tips and the drawing hand
s.raw_path(f"M {tx},{ty} C {tx+140},{ty+120} {bx+140},{by-120} {bx},{by}",stroke=INK,sw=16)
s.raw_path(f"M {tx},{ty} C {tx+140},{ty+120} {bx+140},{by-120} {bx},{by}",stroke=WOOD,sw=11)
s.line(tx,ty,hx,hy,stroke=ACC,sw=4); s.line(hx,hy,bx,by,stroke=ACC,sw=4)
# arrow
s.line(hx,hy,820,400,sw=5)
s.raw_path("M 820,388 L 862,400 L 820,412 Z",fill=STONE,sw=2.5)
for k in (0,14,28): s.line(hx+10+k,400,hx-4+k,386,sw=2.5); s.line(hx+10+k,400,hx-4+k,414,sw=2.5)
# faint undrawn string
s.line(tx,ty,bx,by,stroke=SOFT,sw=2,dash="8 8")
s.callout(1,650,300,820,200,"A stave of springy|wood")
s.callout(2,440,275,330,170,"A string of twisted|sinew or plant fibre",anchor="end")
s.callout(3,hx,hy,290,520,"Pulling the string|bends the stave, and|the stave stores|the pull",anchor="end")
s.callout(4,660,520,860,560,"Let go, and the stave|springs back and|throws the arrow")
s.callout(5,841,400,930,310,"A point of stone,|glued and bound")
s.save(os.path.join(os.path.dirname(__file__),"..","04-bow","bow"))
