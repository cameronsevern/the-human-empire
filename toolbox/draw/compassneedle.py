import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The compass needle","China, by the 1000s")
WATER="#c9d6dc"; LODE="#5a5550"; WAX="#e8d38a"; SILK="#9a8f80"
G=650
s.line(60,G,1140,G,stroke=SOFT,sw=1.5)
# a wooden stand: a base, an upright at the right and an arm reaching left
s.path([(290,G-24),(700,G-24),(700,G),(290,G)],fill=WOOD,close=True,sw=3)
s.line(660,G-24,660,180,stroke=INK,sw=16); s.line(660,G-24,660,180,stroke=WOOD,sw=10)
s.line(668,190,380,190,stroke=INK,sw=16); s.line(668,190,380,190,stroke=WOOD,sw=10)
# the silk fibre and the needle hanging level from it
NX,NY=470,430
s.line(NX,196,NX,NY-6,stroke=SILK,sw=1.6)
s.path([(330,NY),(NX,NY-4),(610,NY),(NX,NY+4)],fill=ACC,close=True,sw=2)
s.ellipse(NX,NY-2,9,7,fill=WAX,sw=2)
s.text(318,NY+8,"N",anchor="end",italic=True,fill=SOFT,size=20)
s.text(622,NY+8,"S",italic=True,fill=SOFT,size=20)
# a lodestone, the magnetic rock the needle was rubbed on
s.raw_path(f"M 400,{G-24} C 390,{G-60} 420,{G-80} 460,{G-76} C 505,{G-72} 520,{G-50} 510,{G-24} Z",fill=LODE,sw=2.5)
# inset: a needle floating in a bowl of water
cx,cy,r=950,330,140
s.inset(cx,cy,r)
s.raw_path(f"M {cx-105},{cy-10} C {cx-95},{cy+90} {cx+95},{cy+90} {cx+105},{cy-10} Z",fill=CLAY,sw=3)
s.ellipse(cx,cy-10,105,22,fill=WATER,sw=2.5)
s.path([(cx-72,cy-14),(cx,cy-17),(cx+72,cy-10),(cx,cy-7)],fill=ACC,close=True,sw=1.8)
s.callout(1,360,NY,250,470,"A steel needle,|rubbed on a|lodestone",anchor="end")
s.callout(2,NX,290,380,260,"One fibre|of new silk",anchor="end")
s.callout(3,NX-6,NY-6,250,340,"Fixed at its|middle with a|speck of wax",anchor="end")
s.callout(4,440,G-56,250,590,"A lodestone",anchor="end")
s.callout(5,cx+30,cy-12,860,560,"Ships' pilots floated|it in a bowl of water")
s.save(os.path.join(os.path.dirname(__file__),"..","32-compass-needle","compass-needle"))
