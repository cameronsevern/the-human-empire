import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The safety bicycle","Coventry, 1885; air-filled tyres from 1888")
STEEL="#5e646a"; TYRE="#3a3430"; RIM="#9aa1a5"; LEATHER="#8a5a3a"; AIR="#d8e6ea"; RUBBER="#4b4542"

def wheel(cx,cy,r,spokes=24,tyre=10):
    s.circle(cx,cy,r,stroke=TYRE,sw=tyre)
    s.circle(cx,cy,r-tyre/2-3,stroke=RIM,sw=3)
    for k in range(spokes):
        a=2*math.pi*k/spokes
        s.line(cx,cy,round(cx+(r-8)*math.cos(a),1),round(cy+(r-8)*math.sin(a),1),stroke="#8a8178",sw=1)
    s.circle(cx,cy,6,fill=STEEL,sw=1.5)

# ================= the safety bicycle =================
R=105; RX,FX,WY=250,620,500; BB=(400,515)
s.line(60,WY+R+5,760,WY+R+5,stroke=SOFT,sw=1.5)
wheel(RX,WY,R); wheel(FX,WY,R)
ST=(372,330); HT=(575,322); HB=(588,375)
for (a,b) in ((BB,ST),(ST,HT),(HB,BB)):                                 # the diamond: seat, top and down tubes
    s.line(a[0],a[1],b[0],b[1],stroke=STEEL,sw=8)
s.line(HT[0],HT[1],HB[0],HB[1],stroke=STEEL,sw=10)                    # head tube
s.line(RX,WY,BB[0],BB[1],stroke=STEEL,sw=6)                          # chain stay
s.line(RX,WY,ST[0],ST[1],stroke=STEEL,sw=6)                          # seat stay
s.raw_path(f"M {HB[0]},{HB[1]} Q {HB[0]+12},{WY-50} {FX},{WY}",stroke=STEEL,sw=6)   # fork
s.line(HT[0],HT[1],HT[0]-8,HT[1]-40,stroke=STEEL,sw=6)                # stem
s.raw_path(f"M {HT[0]-50},{HT[1]-30} C {HT[0]-30},{HT[1]-48} {HT[0]},{HT[1]-44} {HT[0]-8},{HT[1]-40}",stroke=STEEL,sw=6)  # bars
s.line(ST[0],ST[1],ST[0]-6,ST[1]-26,stroke=STEEL,sw=6)
s.raw_path(f"M {ST[0]-40},{ST[1]-30} Q {ST[0]-6},{ST[1]-42} {ST[0]+28},{ST[1]-28} L {ST[0]-30},{ST[1]-18} Z",fill=LEATHER,sw=2)   # saddle
# chain drive: a big chainring at the pedals, a small sprocket at the back wheel
CR,SR=38,15
s.line(BB[0],BB[1]-CR,RX,WY-SR,stroke=ACC,sw=5)
s.line(BB[0],BB[1]+CR,RX,WY+SR,stroke=ACC,sw=5)
s.circle(BB[0],BB[1],CR,fill="none",stroke=ACC,sw=6)
s.circle(RX,WY,SR,fill="none",stroke=ACC,sw=5)
s.line(BB[0],BB[1],BB[0]+30,BB[1]+55,stroke=STEEL,sw=6)              # crank and pedal
s.path([(BB[0]+18,BB[1]+55),(BB[0]+44,BB[1]+55),(BB[0]+44,BB[1]+63),(BB[0]+18,BB[1]+63)],fill=RUBBER,close=True,sw=1.5)
s.circle(BB[0],BB[1],7,fill=STEEL,sw=1.5)
s.text(430,725,"a safety bicycle of the 1890s",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the tyre, cut through =================
TX,TY=990,255
s.circle(TX,TY,78,fill="#ffffff",sw=2.5)
s.raw_path(f"M {TX-44},{TY+30} Q {TX},{TY+62} {TX+44},{TY+30} L {TX+34},{TY+30} Q {TX},{TY+50} {TX-34},{TY+30} Z",fill=RIM,sw=2)   # rim
s.raw_path(f"M {TX-40},{TY+26} C {TX-62},{TY-10} {TX-34},{TY-52} {TX},{TY-52} C {TX+34},{TY-52} {TX+62},{TY-10} {TX+40},{TY+26}",stroke=RUBBER,sw=10)  # casing
s.circle(TX,TY-6,34,fill=AIR,stroke="#8193a3",sw=2.5)                 # inner tube of air
s.text(TX,TY-2,"air",anchor="middle",italic=True,fill=SOFT,size=18)
s.text(TX,TY+108,"the tyre, cut through",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= before: the penny-farthing =================
PX,PY,PR=1035,565,100
s.line(860,PY+PR+5,1150,PY+PR+5,stroke=SOFT,sw=1.5)
wheel(PX,PY,PR,spokes=30,tyre=5)
wheel(890,PY+PR-20,20,spokes=10,tyre=4)
s.raw_path(f"M {PX-8},{PY-PR+4} C {PX-80},{PY-PR+10} {900},{PY} {890},{PY+PR-20}",stroke=STEEL,sw=6)
s.line(PX,PY,PX+12,PY+30,stroke=STEEL,sw=5)                           # pedal on the hub
s.text(PX-25,PY+PR+40,"before: the penny-farthing",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,330,WY+31,330,640,"A chain turns the back wheel|faster than the pedals turn")
s.callout(2,RX-70,WY-80,100,240,"Two wheels the same|size, the rider low")
s.callout(3,TX+18,TY-26,840,135,"A tube of air inside|the rubber tyre",anchor="end")
s.callout(4,470,327,520,195,"A diamond frame|of steel tubes")
s.callout(5,PX+10,PY+20,800,420,"Pedals fixed to a huge|front wheel")
s.save(os.path.join(os.path.dirname(__file__),"..","70-safety-bicycle","safety-bicycle"))
