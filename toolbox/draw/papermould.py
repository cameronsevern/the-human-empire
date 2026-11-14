import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The paper mould","China, about 2,000 years ago")
PULP="#dfe3d6"; SHEET="#f4f0e4"; SCREEN="#ead9b5"
G=690
s.line(60,G,1140,G,stroke=SOFT,sw=1.5)
# the vat: a wooden tub seen from the front and a little above
s.path([(260,470),(610,470),(610,G),(260,G)],fill=WOOD,close=True,sw=3)
s.path([(260,470),(340,420),(690,420),(610,470)],fill=WOOD,close=True,sw=3)
s.path([(610,470),(690,420),(690,G-50),(610,G)],fill="#d6c3a0",close=True,sw=3)
s.path([(282,464),(350,428),(676,428),(600,464)],fill=PULP,close=True,sw=2)
for x in (330,400,470,540):
    s.line(x,470,x,G,stroke=SOFT,sw=1.2)
# fibres floating in the vat
for (x,y) in ((400,446),(450,452),(520,438),(560,450),(370,456)):
    s.raw_path(f"M {x-10},{y} C {x-4},{y-4} {x+4},{y+4} {x+10},{y}",stroke=SOFT,sw=1.3)
# the mould lifted above the vat: a wooden frame with the screen laid in it
P=[(250,300),(600,300),(670,370),(320,370)]   # outer corners, seen in perspective
s.path(P,fill=WOOD,close=True,sw=3)
def lerp(a,b,t): return (a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t)
inner=[(270,306),(588,306),(648,364),(332,364)]
s.path(inner,fill=SCREEN,close=True,sw=2)
# bamboo strips run the long way; threads lace them together across
for k in range(1,15):
    t=k/15
    a=lerp(inner[0],inner[3],t); b=lerp(inner[1],inner[2],t)
    s.line(round(a[0],1),round(a[1],1),round(b[0],1),round(b[1],1),stroke=ACC,sw=1.6)
for k in range(1,6):
    t=k/6
    a=lerp(inner[0],inner[1],t); b=lerp(inner[3],inner[2],t)
    s.line(round(a[0],1),round(a[1],1),round(b[0],1),round(b[1],1),stroke=INK,sw=1.1)
# ribs under the screen, and the front edge of the frame
s.path([(320,370),(670,370),(670,380),(320,380)],fill="#d6c3a0",close=True,sw=2.5)
# water draining back into the vat
for x in (360,410,460,520,580,630):
    s.line(x,388,x-2,404,stroke="#8fb0c0",sw=2.5,dash="4 7")
# the pile of wet sheets on a board, with a screen being peeled off the newest one
s.path([(760,G-30),(1100,G-30),(1100,G),(760,G)],fill=WOOD,close=True,sw=3)
for k in range(5):
    y=G-36-k*9
    s.path([(780,y),(1080,y),(1080,y-8),(780,y-8)],fill=SHEET,close=True,sw=1.6)
top=G-36-4*9-8
s.raw_path(f"M 1080,{top} C 1030,{top-6} 980,{top-30} 930,{top-70}",stroke=ACC,sw=7)
s.raw_path(f"M 1080,{top} C 1030,{top-6} 980,{top-30} 930,{top-70}",stroke=SCREEN,sw=3)
s.arrow(942,top-74,922,top-90)
s.callout(1,330,560,230,590,"A vat of water|and beaten fibre",anchor="end")
s.callout(2,440,330,500,190,"A screen of fine bamboo strips,|laced together with thread")
s.callout(3,636,345,760,250,"A wooden frame|holds it flat")
s.callout(4,520,396,800,335,"The water drains through.|A mat of fibre stays|on the screen")
s.callout(5,860,G-52,800,440,"The screen is peeled off,|and the wet sheet stays|on the pile")
s.save(os.path.join(os.path.dirname(__file__),"..","30-paper-mould","paper-mould"))
