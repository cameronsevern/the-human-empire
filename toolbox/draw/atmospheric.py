import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The atmospheric engine","Newcomen, near Dudley Castle, 1712")
BRICK="#d7a17e"; COPPER="#c98a5a"; OAK="#c9a174"; IRON="#7d8488"; WATER="#9fc2cf"; STEAM="#eeeae2"; FIRE="#e0a030"
G=640
s.line(60,G,1140,G,stroke=SOFT,sw=1.5)

CX=430; CW=120; CT=290; CB=470          # cylinder
PV=(680,205)                             # beam pivot on the wall
# ---- the engine house wall that carries the beam
s.path([(660,PV[1]+18),(700,PV[1]+18),(700,G),(660,G)],fill=BRICK,close=True,sw=3)
# ---- the boiler under the cylinder, and its fire
s.raw_path(f"M {CX-110},{G} L {CX-110},{CB+70} C {CX-110},{CB+10} {CX+110},{CB+10} {CX+110},{CB+70} L {CX+110},{G} Z",fill=COPPER,sw=3)
s.path([(CX-130,G),(CX+130,G),(CX+130,G+70),(CX-130,G+70)],fill=BRICK,close=True,sw=3)
for dx in (-60,-20,20,60):
    s.raw_path(f"M {CX+dx-14},{G+66} C {CX+dx-14},{G+40} {CX+dx},{G+30} {CX+dx},{G+12} C {CX+dx+6},{G+30} {CX+dx+14},{G+40} {CX+dx+14},{G+66} Z",fill=FIRE,sw=1.5)
# steam pipe and valve from boiler top to cylinder bottom
s.path([(CX-12,CB+30),(CX+12,CB+30),(CX+12,CB),(CX-12,CB)],fill=IRON,close=True,sw=2.5)
s.circle(CX,CB+16,7,fill=METAL,sw=2)
# ---- the cylinder, open at the top, and the piston inside it
s.path([(CX-CW/2,CT),(CX+CW/2,CT),(CX+CW/2,CB),(CX-CW/2,CB)],fill="#e7c7bb",close=True,sw=0,stroke="none")
for k in range(5): s.line(CX-CW/2+16,CB-14-k*30,CX+CW/2-16,CB-14-k*30,stroke="#ffffff",sw=6)       # steam inside
s.path([(CX-CW/2-10,CT),(CX-CW/2,CT),(CX-CW/2,CB),(CX-CW/2-10,CB)],fill=ACC,close=True,sw=3)
s.path([(CX+CW/2,CT),(CX+CW/2+10,CT),(CX+CW/2+10,CB),(CX+CW/2,CB)],fill=ACC,close=True,sw=3)
s.path([(CX-CW/2-10,CB),(CX+CW/2+10,CB),(CX+CW/2+10,CB+10),(CX-CW/2-10,CB+10)],fill=ACC,close=True,sw=3)
PY=330
s.path([(CX-CW/2+2,PY),(CX+CW/2-2,PY),(CX+CW/2-2,PY+24),(CX-CW/2+2,PY+24)],fill=ACC,close=True,sw=3)  # piston
s.path([(CX-CW/2+3,PY-10),(CX+CW/2-3,PY-10),(CX+CW/2-3,PY),(CX-CW/2+3,PY)],fill=WATER,close=True,sw=1.5)  # water seal
s.line(CX,PY-10,CX,PV[1]+12,stroke=INK,sw=6)                                            # piston chain
# ---- the cold water: a tank up in the house, a pipe down, a jet into the cylinder
s.path([(530,270),(660,270),(660,310),(530,310)],fill=WATER,close=True,sw=2.5)
s.raw_path(f"M 545,310 L 545,{CB-12} L {CX+CW/2+10},{CB-12}",stroke=IRON,sw=7)
s.circle(545,400,8,fill=METAL,sw=2)                                                    # injection cock
x0,y0=CX+CW/2-6,CB-12
for dx,dy in ((-50,-40),(-62,-20),(-40,-58),(-66,-2)):
    s.line(x0,y0,x0+dx,y0+dy,stroke="#5f8fa0",sw=2.5)
# ---- the great beam, rocking on the wall, with an arch head at each end
s.path([(CX,PV[1]-14),(930,PV[1]-14),(930,PV[1]+14),(CX,PV[1]+14)],fill=OAK,close=True,sw=3)
for xe in (CX,930):
    d=-1 if xe<PV[0] else 1
    R=abs(xe-PV[0])
    pts=[(PV[0]+R*math.sin(math.radians(t))*d,PV[1]-R*math.cos(math.radians(t))+R) for t in range(84,97,2)]
    pts=[(PV[0]+d*R*math.cos(math.radians(a)),PV[1]+R*math.sin(math.radians(a))) for a in range(-8,9,2)]
    s.path(pts,stroke=INK,sw=10); s.path(pts,stroke=OAK,sw=6)
s.circle(PV[0],PV[1],10,fill=IRON,sw=2.5)
# ---- the pump rod, down the shaft
SX=930
s.path([(SX-30,G),(SX+30,G),(SX+30,742),(SX-30,742)],fill="#5a4c40",close=True,sw=2.5)
s.line(SX,PV[1]+12,SX,742,stroke=OAK,sw=10); s.line(SX,PV[1]+12,SX,742,stroke=INK,sw=1.5)
s.path([(SX+30,G-8),(SX+90,G-8),(SX+90,G),(SX+30,G)],fill=IRON,close=True,sw=2)
s.raw_path(f"M {SX+90},{G-4} C {SX+104},{G-4} {SX+108},{G+10} {SX+108},{G+30}",stroke="#5f8fa0",sw=4)
# motion arrows
s.arrow(CX-CW/2-40,PY-70,CX-CW/2-40,PY-14)
s.arrow(SX+40,440,SX+40,360)

s.callout(1,CX,CB+16,300,560,"Steam from the boiler|fills the cylinder",anchor="end")
s.callout(2,CX+CW/2-30,CB-34,300,445,"A jet of cold water|turns it back to water",anchor="end")
s.callout(3,CX-CW/2+20,PY+12,300,330,"The air presses the|piston down",anchor="end")
s.callout(4,800,PV[1],780,125,"The beam rocks and|lifts the pump rod")
s.callout(5,SX,500,985,560,"Its weight pulls|the piston up")
s.save(os.path.join(os.path.dirname(__file__),"..","61-atmospheric-engine","atmospheric-engine"))
