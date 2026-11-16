import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The guidance computer","The Apollo guidance computer and its keyboard, 1960s")
CASE="#c9b98a"; CASE2="#a99a6c"; PANEL="#55595c"; KEYC="#d8d4c8"; LITE="#9fdc8a"; WIRE="#b87333"; FERR="#4b4f52"

# ================= the display and keyboard (DSKY) =================
DX0,DY0,DW,DH=80,230,300,400
s.path([(DX0,DY0),(DX0+DW,DY0),(DX0+DW,DY0+DH),(DX0,DY0+DH)],fill=PANEL,close=True,sw=3)
# status lights on the left of the upper half
for r in range(6):
    for c in range(2):
        s.path([(DX0+16+c*52,DY0+16+r*26),(DX0+62+c*52,DY0+16+r*26),(DX0+62+c*52,DY0+36+r*26),(DX0+16+c*52,DY0+36+r*26)],fill="#e9e4d4",close=True,sw=1)
# the green number display on the right of the upper half
NX0=DX0+128
s.path([(NX0,DY0+14),(DX0+DW-14,DY0+14),(DX0+DW-14,DY0+236),(NX0,DY0+236)],fill="#2b2f2c",close=True,sw=2)
MONO='font-family="DejaVu Sans Mono, monospace" font-weight="bold"'
for (x,y,txt) in ((NX0+14,DY0+50,"PROG"),(NX0+14,DY0+92,"VERB"),(NX0+92,DY0+92,"NOUN")):
    s.add(f'<text x="{x}" y="{y}" font-size="13" fill="#e9e4d4" {MONO}>{txt}</text>')
for (x,y,txt) in ((NX0+100,DY0+62,"63"),(NX0+16,DY0+120,"06"),(NX0+94,DY0+120,"62")):
    s.add(f'<text x="{x}" y="{y}" font-size="26" fill="{LITE}" {MONO}>{txt}</text>')
for k,txt in enumerate(("+00431","-00125","+21842")):
    s.add(f'<text x="{NX0+12}" y="{DY0+152+k*28}" font-size="24" fill="{LITE}" {MONO}>{txt}</text>')
# the keyboard: seven columns of square keys
KY=DY0+254; KS=34
cols=[2,3,3,3,3,3,2]
for c,n in enumerate(cols):
    x=DX0+14+c*40
    off=KS/2+4 if n==2 else 0
    for r in range(n):
        y=KY+off+r*(KS+12)
        fill="#b9b3a4" if (c==0) else KEYC
        s.path([(x,y),(x+KS,y),(x+KS,y+KS),(x,y+KS)],fill=fill,close=True,sw=1.5)
s.text(DX0+DW/2+20,DY0+DH+36,"the display and keyboard",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the computer itself: a sealed metal case =================
CX0,CY0,CW,CH=440,330,330,190
s.path([(CX0,CY0),(CX0+CW,CY0),(CX0+CW,CY0+CH),(CX0,CY0+CH)],fill=CASE,close=True,sw=3)
s.path([(CX0,CY0),(CX0+40,CY0-34),(CX0+CW+40,CY0-34),(CX0+CW,CY0)],fill="#d8cba0",close=True,sw=2.5)
s.path([(CX0+CW,CY0),(CX0+CW+40,CY0-34),(CX0+CW+40,CY0+CH-34),(CX0+CW,CY0+CH)],fill=CASE2,close=True,sw=2.5)
# trays of logic chips on the left, six rope modules on the right
for k in range(8):
    x=CX0+16+k*20
    s.path([(x,CY0+18),(x+14,CY0+18),(x+14,CY0+CH-18),(x,CY0+CH-18)],fill="#b7a878",close=True,sw=1.2)
for k in range(6):
    x=CX0+190+k*22
    s.path([(x,CY0+18),(x+16,CY0+18),(x+16,CY0+CH-18),(x,CY0+CH-18)],fill="#e2d6ad",close=True,sw=1.5)
    s.circle(x+8,CY0+34,3,fill=INK,sw=0)
s.text(CX0+CW/2+75,CY0+CH+44,"the computer, 61 cm long, 32 kg",anchor="middle",italic=True,fill=SOFT,size=18)
# cable to the keyboard
s.raw_path(f"M {DX0+DW},{DY0+DH-40} C {DX0+DW+50},{DY0+DH-40} {CX0-50},{CY0+CH-20} {CX0},{CY0+CH-30}",stroke=INK,sw=4)

# ================= the inset: rope memory, wires through or around rings =================
IX,IY,IR=985,420,165
s.inset(IX,IY,IR)
s.text(IX-40,IY+IR+40,"rope memory, enlarged",anchor="middle",italic=True)
cores=[IX-90,IX,IX+90]
for cx in cores:
    s.circle(cx,IY,40,fill=ACC,stroke=INK,sw=2.5)
    s.circle(cx,IY,17,fill="#ffffff",stroke=INK,sw=2)
# three sense wires: each passes through a ring (a one) or loops round it (a nought)
pattern=[(1,0,1),(0,1,1),(1,1,0)]
for w,bits in enumerate(pattern):
    dy=(w-1)*7
    d=f"M {IX-150},{IY+dy}"
    for cx,b in zip(cores,bits):
        if b: d+=f" L {cx-24},{IY+dy} L {cx+24},{IY+dy}"
        else:
            yb=IY-56-w*9
            d+=f" L {cx-52},{IY+dy} Q {cx-48},{yb} {cx},{yb} Q {cx+48},{yb} {cx+52},{IY+dy}"
    d+=f" L {IX+150},{IY+dy}"
    s.raw_path(d,stroke=WIRE,sw=2.5)

s.callout(1,IX+90,IY+38,1150,690,"A wire through a ring is a 1,|a wire around it a 0",anchor="end")
s.callout(2,CX0+245,CY0+110,700,190,"Six rope modules:|the programs, fixed for good")
s.callout(3,CX0+30,CY0+150,560,690,"About 2,800 chips|of simple logic")
s.callout(4,DX0+31,KY+52,110,700,"Verb and noun keys:|two numbers for each command")
s.callout(5,NX0+60,DY0+178,330,170,"Green digits show|the answers",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","93-guidance-computer","guidance-computer"))
