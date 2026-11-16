import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The cowrie","West Africa, 1300s to 1800s; shells from the Maldives")
LAND="#e4dac6"; SEA="#faf6ee"; HI="#e0a08a"; DARK="#8e3c2a"

def outline(cx,cy,rx,ry):
    """Egg-shaped, broad behind (left) and narrower in front, with a small notch at each end."""
    pts=[]
    for i in range(60):
        a=2*math.pi*i/60
        w=1-0.12*math.cos(a)                              # narrower at the right-hand end
        x=cx+rx*math.cos(a); y=cy+ry*w*math.sin(a)
        if abs(math.sin(a))<0.12: x-= (6 if math.cos(a)>0 else -6)   # end notches
        pts.append((x,y))
    return pts
def shell_top(cx,cy,rx,ry):
    s.path(outline(cx,cy,rx,ry),fill=ACC,close=True,sw=3)
    s.path(outline(cx,cy-4,rx*0.8,ry*0.72),fill="#c4654c",stroke="none",close=True,sw=0)   # the dome, inside the thick margin
    s.ellipse(cx-rx*0.15,cy-ry*0.3,rx*0.4,ry*0.13,fill=HI,stroke="none",sw=0,rot=-6)       # gloss
def shell_under(cx,cy,rx,ry):
    """The underside: flatter, with the long slit lined with teeth."""
    s.path(outline(cx,cy,rx,ry),fill=ACC,close=True,sw=3)
    s.raw_path(f"M {cx-rx*0.97},{cy} C {cx-rx*0.4},{cy-13} {cx+rx*0.4},{cy-13} {cx+rx*0.97},{cy} "
               f"C {cx+rx*0.4},{cy+11} {cx-rx*0.4},{cy+11} {cx-rx*0.97},{cy} Z",fill="#3a2a22",sw=2)
    for k in range(-7,7):
        x=cx+(k+0.5)*rx*0.115
        s.line(round(x,1),cy-9,round(x,1),cy-24,stroke=DARK,sw=2.6)
        s.line(round(x,1),cy+8,round(x,1),cy+23,stroke=DARK,sw=2.6)

# ---- the shell, from above and from below
shell_top(200,240,105,68)
shell_under(200,410,105,68)
s.text(200,335,"from above",anchor="middle",italic=True,fill=SOFT)
s.text(200,505,"from below",anchor="middle",italic=True,fill=SOFT)

# ---- a string of forty, laid in a loop
LX,LY,LRX,LRY=300,625,230,72
s.ellipse(LX,LY,LRX,LRY,stroke="#7a5a3c",sw=2)
for i in range(40):
    a=-math.pi/2+2*math.pi*(i+0.5)/40
    x=LX+LRX*math.cos(a); y=LY+LRY*math.sin(a)
    t=math.degrees(math.atan2(LRY*math.cos(a),-LRX*math.sin(a)))
    s.ellipse(round(x,1),round(y,1),11,7,fill=ACC,sw=1.8,rot=round(t,1))
s.raw_path(f"M {LX},{LY-LRY} C {LX-14},{LY-LRY-26} {LX-30},{LY-LRY-30} {LX-44},{LY-LRY-24}",stroke="#7a5a3c",sw=2)
s.raw_path(f"M {LX},{LY-LRY} C {LX+14},{LY-LRY-26} {LX+30},{LY-LRY-30} {LX+44},{LY-LRY-24}",stroke="#7a5a3c",sw=2)

# ---- the journey, on a sketch of Africa and Europe
def P(lon,lat): return (round(790+lon*5.0,1),round(430-lat*5.0,1))
africa=[(-6,36),(10,37),(11,33),(20,31),(25,32),(32,31),(34,28),(38,18),(43,12),(51,12),(51,10),(45,2),(40,-3),(40,-10),
        (40,-16),(35,-24),(32,-29),(27,-33),(20,-35),(18,-33),(15,-27),(12,-17),(13,-12),(9,-1),(9,4),(5,6),(-2,5),(-8,4),
        (-13,8),(-17,14),(-17,21),(-13,27),(-10,30)]
s.path([P(*p) for p in africa],fill=LAND,close=True,sw=2,stroke=SOFT)
s.path([P(*p) for p in [(44,-13),(50,-15),(47,-25),(44,-22)]],fill=LAND,close=True,sw=2,stroke=SOFT)
europe=[(-9,37),(-9,43),(-2,44),(-4,48),(2,51),(5,53),(9,54),(10,57),(16,56),(16,45),(13,45),(16,41),(16,38),(12,42),(8,44),(3,43),(-1,37)]
s.path([P(*p) for p in europe],fill=LAND,close=True,sw=2,stroke=SOFT)
s.path([P(*p) for p in [(-5,50),(1,51),(1,53),(-1,55),(-3,58),(-6,57),(-3,54),(-5,52)]],fill=LAND,close=True,sw=2,stroke=SOFT)
arabia=[(34,28),(36,30),(48,30),(56,24),(59,22),(52,16),(44,12),(42,16),(38,22)]
s.path([P(*p) for p in arabia],fill=LAND,close=True,sw=2,stroke=SOFT)
MAL=P(73,3)
for dx,dy in ((0,-14),(3,0),(-2,14),(2,26)):
    s.circle(MAL[0]+dx,MAL[1]+dy,4,fill=ACC,sw=1.2)
# outward to Europe in the holds of ships from Asia, round the Cape
r1=[MAL,(1080,560),(930,650),(840,640),(700,540),(625,430),(630,300),(690,215)]
s.raw_path("M "+" ".join(f"{x},{y}" if i==0 else f"L {x},{y}" for i,(x,y) in enumerate(r1)),stroke=INK,sw=2,extra='stroke-dasharray="8 7"')
s.arrow(690,215,758,178)
# south again on the slave ships to West Africa
r2=[(780,190),(735,232),(705,300),(706,380)]
s.raw_path("M "+" ".join(f"{x},{y}" if i==0 else f"L {x},{y}" for i,(x,y) in enumerate(r2)),stroke=INK,sw=2.5)
s.arrow(706,380,794,402)
s.text(806,430,"West Africa",italic=True,fill=SOFT)
s.text(MAL[0]-14,MAL[1]+64,"Maldives",anchor="middle",italic=True,fill=SOFT)

s.callout(1,240,215,420,170,"A glossy back,|about 2 cm long")
s.callout(2,250,401,420,420,"A slit lined|with teeth")
s.callout(3,LX-80,LY+LRY*0.96,170,620,"Forty to a string,|fifty strings a head")
s.callout(4,MAL[0],MAL[1]-14,1150,220,"Fished from the|lagoons",anchor="end")
s.callout(5,P(0,52)[0],P(0,52)[1],905,140,"Auctioned in London|or Amsterdam")
s.save(os.path.join(os.path.dirname(__file__),"..","52-cowrie","cowrie"))
