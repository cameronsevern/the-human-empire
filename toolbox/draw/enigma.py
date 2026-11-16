import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The Enigma machine","The army's Enigma I, Germany, 1930s, lid open")
BOX="#b48a5c"; PANEL="#3d3833"; KEY="#2f2a26"; GLASS="#e8e2cf"; LIT="#f2d36b"; RIB="#7a3424"

X0,X1=380,820; Y0,Y1=150,600
s.path([(X0,Y0),(X1,Y0),(X1,Y1),(X0,Y1)],fill=BOX,close=True,sw=3)
s.path([(X0+16,Y0+14),(X1-16,Y0+14),(X1-16,Y1-12),(X0+16,Y1-12)],fill=PANEL,close=True,sw=2)

# ================= the rotors, seen from above with the lid open =================
RY0,RY1=180,262
s.path([(X0+30,RY0-6),(X1-30,RY0-6),(X1-30,RY1+6),(X0+30,RY1+6)],fill="#57504a",close=True,sw=1.5)
def wheel(x0,x1,fill,ribs=True,sw=2.5):
    s.path([(x0,RY0),(x1,RY0),(x1,RY1),(x0,RY1)],fill=fill,close=True,sw=sw)
    if ribs:
        for y in range(RY0+6,RY1-2,7): s.line(x0+3,y,x0+14,y,stroke=RIB,sw=1.5)
s.path([(470,RY0+8),(500,RY0+8),(500,RY1-8),(470,RY1-8)],fill=METAL,close=True,sw=2.5)      # reflector
for (a,b) in ((515,570),(580,635),(645,700)): wheel(a,b,ACC)
for (a,b,l) in ((515,570,"Q"),(580,635,"E"),(645,700,"V")):
    s.path([(a+24,RY0+28),(b-6,RY0+28),(b-6,RY0+54),(a+24,RY0+54)],fill=GLASS,close=True,sw=1.5)
    s.text((a+b)/2+9,RY0+48,l,size=16,anchor="middle",halo=GLASS)
s.path([(712,RY0+8),(736,RY0+8),(736,RY1-8),(712,RY1-8)],fill=METAL,close=True,sw=2.5)        # entry wheel

# ================= lamps and keys =================
ROWS=["QWERTZUIO","ASDFGHJK","PYXCVBNML"]
def board(y0,dy,r,fill,tfill,lit=None):
    for j,row in enumerate(ROWS):
        n=len(row); x=600-(n-1)*42/2
        for i,c in enumerate(row):
            cx=round(x+i*42,1); cy=y0+j*dy
            f=LIT if c==lit else fill
            s.circle(cx,cy,r,fill=f,stroke=INK,sw=1.8)
            s.text(cx,cy+6,c,size=16,anchor="middle",fill=tfill if c!=lit else INK,halo=f)
board(305,40,15,GLASS,INK,lit="A")
s.line(X0+20,Y0+275,X1-20,Y0+275,stroke="#57504a",sw=2)
board(450,46,16,KEY,PAPER)


# ================= the plugboard, on the front of the box =================
PY0,PY1=608,692
s.path([(X0,PY0),(X1,PY0),(X1,PY1),(X0,PY1)],fill="#4a443e",close=True,sw=3)
pl="QWERTZUIOASDFGHJKPYXCVBNML"
for i,c in enumerate(pl):
    row=0 if i<13 else 1; k=i%13
    cx=round(410+k*31.5,1); cy=630+row*40
    s.circle(cx-5,cy,3.5,fill="#111",sw=1); s.circle(cx+5,cy,3.5,fill="#111",sw=1)
# two cables, each swapping a pair of letters
s.raw_path("M 473,630 C 480,700 560,700 568,670",stroke="#2b2b2b",sw=6)
s.raw_path("M 662,630 C 670,700 740,705 756,670",stroke="#2b2b2b",sw=6)
for (x,y) in ((473,630),(568,670),(662,630),(756,670)):
    s.circle(x,y,8,fill="#6b6460",stroke=INK,sw=1.5)

s.callout(1,416,542,300,575,"Press a key, and|current flows",anchor="end")
s.callout(2,520,693,300,690,"Cables swap pairs|of letters",anchor="end")
s.callout(3,690,RY1-10,880,215,"Three wired wheels|scramble the letter,|and one steps on|at every key press")
s.callout(4,485,RY0+30,300,190,"A reflector sends|the current back|by another path",anchor="end")
s.callout(5,438,345,300,345,"A lamp lights|the coded letter",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","81-enigma","enigma"))
