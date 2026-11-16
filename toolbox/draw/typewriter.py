import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The typewriter","Remington, Ilion, New York, 1874")
KEY="#f4ecd8"; STEEL="#6f7579"; BLACK="#3a3430"; RIB="#5e3a5e"; PAPERW="#ffffff"; RUBBER="#4b4542"

# ================= the keys, from above =================
rows=["QWERTYUIOP","ASDFGHJKL","ZXCVBNM"]
for r,row in enumerate(rows):
    for c,ch in enumerate(row):
        x=90+r*19+c*38; y=180+r*42
        s.circle(x,y,16,fill=KEY,stroke=BLACK,sw=2.5)
        s.text(x,y+6,ch,anchor="middle",size=16,bold=True,halo=KEY)
s.text(260,330,"the letter keys, from above",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= inside, from the side =================
PX,PY,PR=700,395,40                                                   # the roller (platen), seen end on
s.path([(560,PY-70),(840,PY-70),(840,PY-56),(560,PY-56)],fill=STEEL,close=True,sw=2)          # carriage rail
s.circle(PX,PY,PR,fill=RUBBER,sw=2.5)
s.raw_path(f"M {PX-PR-4},{PY-60} A {PR+4} {PR+4} 0 1 0 {PX+PR+4},{PY}",stroke="#c9c2b4",sw=3)   # paper round the roller
s.line(600,PY+PR+10,800,PY+PR+10,stroke=RIB,sw=6)                     # the inked ribbon, just below
PV=(620,575)                                                           # the type bars' pivot, on a ring
TIP=(PX,PY+PR+16)
# resting bars, fanned below, grey
for (ex,ey) in ((503,641),(521,666),(544,687)):
    s.line(PV[0],PV[1],ex,ey,stroke="#a7a093",sw=5)
# the bar that has been struck, swung up to the roller
s.line(PV[0],PV[1],TIP[0]-4,TIP[1]+12,stroke=ACC,sw=7)
s.path([(TIP[0]-14,TIP[1]+4),(TIP[0]+8,TIP[1]+4),(TIP[0]+8,TIP[1]+20),(TIP[0]-14,TIP[1]+20)],fill=ACC,close=True,sw=2)   # type slug
s.raw_path(f"M 497,628 A 135 135 0 0 1 680,452",stroke=SOFT,sw=1.5,extra='stroke-dasharray="5 5"')   # swing
s.circle(PV[0],PV[1],8,fill=INK,sw=0)
# the key and its lever
s.path([(120,585),(200,585),(200,600),(120,600)],fill=KEY,close=True,sw=2.5)          # key top
s.line(160,600,160,625,stroke=STEEL,sw=4)
s.line(150,628,450,672,stroke=STEEL,sw=6)                                              # key lever
s.circle(450,672,7,fill=INK,sw=0)                                                      # its pivot at the back
s.line(PV[0],PV[1],601,603,stroke=ACC,sw=7)
s.line(330,654,601,603,stroke=STEEL,sw=2.5)                                  # pull wire to the bar
s.arrow(160,550,160,578)
s.text(400,735,"inside, from the side",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the carriage, from above =================
CX0,CX1,CY0=830,1120,215
s.path([(CX0,CY0),(CX1,CY0),(CX1,CY0+70),(CX0,CY0+70)],fill="#d9d2c4",close=True,sw=2.5)          # carriage frame
s.path([(CX0+20,CY0+22),(CX1-20,CY0+22),(CX1-20,CY0+48),(CX0+20,CY0+48)],fill=RUBBER,close=True,sw=2) # roller
s.path([(900,150),(1030,150),(1030,CY0+40),(900,CY0+40)],fill=PAPERW,close=True,sw=2)               # paper
for k in range(4):
    s.line(912,168+k*14,1018-(k*23)%50,168+k*14,stroke="#8a8178",sw=3,dash="7 4")
s.circle(CX1+14,CY0+35,16,fill=STEEL,sw=2)                                                         # spring drum
s.raw_path(f"M {CX1+14},{CY0+35} m -8,0 a 8 8 0 1 1 8,8",stroke=INK,sw=1.5)
s.arrow(1000,CY0+95,930,CY0+95)
s.text(985,CY0+130,"one space after each letter",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,90+9*38,180,520,190,"The letters in|the QWERTY order")
s.callout(2,160,592,100,460,"A key pulls a|type bar up")
s.callout(3,655,520,800,600,"Bars in a ring below|all strike one spot")
s.callout(4,770,PY+PR+10,880,480,"Through an inked ribbon,|onto paper on a roller")
s.callout(5,CX1+14,CY0+35,1150,415,"A spring pulls the|carriage along",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","70-typewriter","typewriter"))
