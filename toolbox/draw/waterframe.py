import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The water frame","Arkwright, patented 1769; Cromford, 1771")
OAK="#c9a174"; WATER="#9fc2cf"; COTTON="#f4f1ea"; LEATHER="#8e3c2a"; BELT="#7a5a3c"; IRON="#7d8488"
G=700

# ---- the waterwheel, bottom left, and the stream that turns it
WX,WY,WR=190,560,118
s.path([(60,G-30),(420,G-30),(420,G),(60,G)],fill=WATER,close=True,sw=2.5)
s.circle(WX,WY,WR,fill=OAK,sw=3); s.circle(WX,WY,WR-18,fill=PAPER,sw=2.5)
for k in range(8):
    a=math.radians(k*45+10)
    s.line(round(WX+20*math.cos(a),1),round(WY+20*math.sin(a),1),round(WX+(WR-18)*math.cos(a),1),round(WY+(WR-18)*math.sin(a),1),stroke=INK,sw=4)
for k in range(16):
    a=math.radians(k*22.5)
    x1,y1=WX+(WR-2)*math.cos(a),WY+(WR-2)*math.sin(a); x2,y2=WX+(WR+18)*math.cos(a),WY+(WR+18)*math.sin(a)
    s.line(round(x1,1),round(y1,1),round(x2,1),round(y2,1),stroke=INK,sw=5)
s.circle(WX,WY,26,fill=IRON,sw=2.5)                                  # the pulley on the axle
s.arrow(WX-150,G-44,WX-90,G-44)

# ---- the belt from the wheel to the drum under the spindles
DX,DY=720,640
s.line(WX,WY-26,DX,DY-22,stroke=BELT,sw=4)
s.line(WX,WY+26,DX,DY+22,stroke=BELT,sw=4)
s.path([(DX,DY-24),(1000,DY-24),(1000,DY+24),(DX,DY+24)],fill=OAK,close=True,sw=3)
s.ellipse(DX,DY,10,24,fill=OAK,sw=3)

# ---- the roller beam, the roving bobbin above, and the three pairs of rollers
s.path([(470,300),(840,300),(840,318),(470,318)],fill=OAK,close=True,sw=2.5)
RB=(470,150)
s.path([(RB[0]-40,RB[1]-28),(RB[0]+40,RB[1]-28),(RB[0]+40,RB[1]+28),(RB[0]-40,RB[1]+28)],fill=COTTON,close=True,sw=2.5)
for k in range(-30,31,10): s.line(RB[0]+k,RB[1]-26,RB[0]+k,RB[1]+26,stroke="#d9d2c4",sw=2)
s.line(RB[0]-50,RB[1],RB[0]+50,RB[1],stroke=INK,sw=4)
pairs=[(560,250,20),(650,262,18),(740,274,16)]
# the strand of cotton, thinning as it passes each pair
s.raw_path(f"M {RB[0]+30},{RB[1]+20} C {RB[0]+60},{RB[1]+70} 520,240 {pairs[0][0]},{pairs[0][1]}",stroke=COTTON,sw=14)
s.raw_path(f"M {RB[0]+30},{RB[1]+20} C {RB[0]+60},{RB[1]+70} 520,240 {pairs[0][0]},{pairs[0][1]}",stroke=SOFT,sw=1)
widths=[9,5]
for i in range(2):
    (x1,y1,_),(x2,y2,_)=pairs[i],pairs[i+1]
    s.line(x1,y1,x2,y2,stroke=COTTON,sw=widths[i]+2); s.line(x1,y1,x2,y2,stroke=SOFT,sw=1)
FX,FT=840,390
s.raw_path(f"M {pairs[2][0]},{pairs[2][1]} C {FX-30},{pairs[2][1]+20} {FX},{FT-60} {FX},{FT}",stroke=INK,sw=2)
for (x,y,r) in pairs:
    s.circle(x,y-r-1,r,fill=ACC,sw=2.5)                            # top roller, leather covered
    s.circle(x,y+r+1,r,fill=ACC,sw=2.5)                            # bottom roller, fluted
    s.circle(x,y-r-1,r-6,fill="none",stroke=LEATHER,sw=2)
    for k in range(10):
        a=math.radians(k*36)
        s.line(round(x+(r-6)*math.cos(a),1),round(y+r+1+(r-6)*math.sin(a),1),round(x+r*math.cos(a),1),round(y+r+1+r*math.sin(a),1),stroke="#7a2f20",sw=1.5)
for (x,y,r),t in zip(pairs,("slow","faster","fastest")):
    s.text(x,y+2*r+36,t,anchor="middle",italic=True,fill=SOFT,size=18)

# ---- the spindle, bobbin and flyer
s.line(FX,FT-8,FX,DY-24,stroke=IRON,sw=5)                            # spindle
s.path([(FX-18,FT+30),(FX+18,FT+30),(FX+18,FT+150),(FX-18,FT+150)],fill=OAK,close=True,sw=2.5)   # bobbin
for y in range(FT+40,FT+146,8): s.line(FX-16,y,FX+16,y,stroke=COTTON,sw=3)
s.raw_path(f"M {FX-44},{FT+150} L {FX-44},{FT+20} C {FX-44},{FT-6} {FX+44},{FT-6} {FX+44},{FT+20} L {FX+44},{FT+150}",stroke=INK,sw=5)   # flyer
s.raw_path(f"M {FX},{FT} C {FX-20},{FT+10} {FX-44},{FT+20} {FX-44},{FT+60} L {FX-18},{FT+90}",stroke=INK,sw=1.5)
s.circle(FX,FT+200,14,fill=IRON,sw=2)                                # the whorl, driven by a band from the drum
s.line(FX-14,FT+200,FX-14,DY-24,stroke=BELT,sw=2.5)
s.line(FX+14,FT+200,FX+14,DY-24,stroke=BELT,sw=2.5)

s.callout(1,RB[0]-20,RB[1],330,150,"A soft rope of|cotton, unwinding",anchor="end")
s.callout(2,560,229,330,280,"Pairs of rollers, each|pair turning faster",anchor="end")
s.callout(3,FX+44,FT+40,930,330,"The flyer spins|and twists it")
s.callout(4,FX+18,FT+120,930,470,"The bobbin lags|and winds it on")
s.callout(5,450,602,560,505,"A belt from the|waterwheel")
s.save(os.path.join(os.path.dirname(__file__),"..","61-water-frame","water-frame"))
