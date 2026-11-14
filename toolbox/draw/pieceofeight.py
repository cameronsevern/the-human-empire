import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The piece of eight","struck by hand at Potosí from 1575")
SILVER="#d4d8da"; DARK="#9aa2a6"; IRON="#8e959a"
# ---- left: from bar to coin, top to bottom
# 1. the cast bar
s.path([(70,200),(330,200),(318,236),(82,236)],fill=SILVER,close=True,sw=3)
s.path([(70,200),(330,200),(322,188),(80,188)],fill="#e8ebec",close=True,sw=2.5)
s.line(300,188,300,236,stroke=INK,sw=1.5,dash="5 5")      # where the next lump is cut
s.arrow(200,262,200,300)
# 2. a lump cut from the end, one corner clipped off to bring it to weight
s.path([(160,330),(236,326),(246,350),(236,372),(166,376),(152,352)],fill=SILVER,close=True,sw=3)
s.path([(252,334),(268,330),(266,346)],fill=SILVER,close=True,sw=2)   # the clipping
s.arrow(200,396,200,420)
# 3. the dies: a lower die set in a block of wood, an upper die held over the blank, a hammer
s.path([(130,612),(290,612),(298,700),(122,700)],fill=WOOD,close=True,sw=3)
s.path([(176,566),(244,566),(244,612),(176,612)],fill=IRON,close=True,sw=3)
s.path([(176,566),(244,566),(244,576),(176,576)],fill="#5f666b",close=True,sw=2)
s.ellipse(210,558,40,8,fill=SILVER,sw=2.5)                               # the blank
s.path([(184,470),(236,470),(236,540),(184,540)],fill=IRON,close=True,sw=3)
s.path([(184,530),(236,530),(236,540),(184,540)],fill="#5f666b",close=True,sw=2)
s.path([(160,430),(258,430),(258,458),(160,458)],fill=IRON,close=True,sw=3)  # hammer head
s.line(258,444,370,436,stroke=INK,sw=10); s.line(258,444,370,436,stroke=WOOD,sw=6)
# ---- right: the finished coin, shield side
CX,CY=930,450
pts=[(CX-175,CY-120),(CX-110,CY-190),(CX+20,CY-205),(CX+150,CY-160),(CX+200,CY-40),(CX+178,CY+100),
     (CX+110,CY+180),(CX-30,CY+200),(CX-150,CY+150),(CX-196,CY+30)]
s.path(pts,fill=SILVER,close=True,sw=3.5)
for a in range(0,360,9):                                                    # beaded border
    r=168; x=CX+r*math.cos(math.radians(a)); y=CY+r*math.sin(math.radians(a))
    s.circle(round(x,1),round(y,1),3,fill=DARK,sw=0)
# crown
s.path([(CX-70,CY-100),(CX-80,CY-150),(CX-40,CY-128),(CX,CY-160),(CX+40,CY-128),(CX+80,CY-150),(CX+70,CY-100)],fill="#c3c8ca",close=True,sw=2.5)
# shield, quartered
s.raw_path(f"M {CX-80},{CY-96} L {CX+80},{CY-96} L {CX+80},{CY+40} C {CX+80},{CY+100} {CX+20},{CY+120} {CX},{CY+130} "
           f"C {CX-20},{CY+120} {CX-80},{CY+100} {CX-80},{CY+40} Z",fill="#c3c8ca",sw=3)
s.line(CX,CY-96,CX,CY+128,stroke=INK,sw=2); s.line(CX-80,CY-10,CX+80,CY-10,stroke=INK,sw=2)
for (qx,qy) in ((CX-40,CY-52),(CX+40,CY+40)):                             # castles
    s.path([(qx-16,qy+18),(qx-16,qy-10),(qx-10,qy-10),(qx-10,qy-16),(qx-3,qy-16),(qx-3,qy-10),(qx+3,qy-10),(qx+3,qy-16),(qx+10,qy-16),(qx+10,qy-10),(qx+16,qy-10),(qx+16,qy+18)],fill=DARK,close=True,sw=1.6)
for (qx,qy) in ((CX+40,CY-52),(CX-40,CY+40)):                             # bars
    for d in (-12,-4,4,12): s.line(qx+d,qy-22,qx+d,qy+22,stroke=INK,sw=2)
# the marks, in terracotta: mint and assayer at left, value at right
s.text(CX-122,CY-8,"P",size=40,anchor="middle",bold=True,fill=ACC,halo=SILVER)
s.text(CX-122,CY+48,"E",size=40,anchor="middle",bold=True,fill=ACC,halo=SILVER)
s.text(CX+122,CY+18,"8",size=46,anchor="middle",bold=True,fill=ACC,halo=SILVER)

s.callout(1,326,212,430,170,"A bar of silver,|cast at the mint")
s.callout(2,240,350,430,330,"A lump cut off,|then clipped to weight")
s.callout(3,236,548,410,520,"Struck between two dies|with a hammer")
s.callout(4,CX-138,CY-30,770,680,"P for Potosí, and the|assayer's initial below it",anchor="end")
s.callout(5,CX+136,CY,1130,680,"8: worth eight reales",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","43-piece-of-eight","piece-of-eight"))
