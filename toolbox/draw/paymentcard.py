import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The payment card","A card, back and front, and the path of one payment, 2020s")
CARD="#6f8fa6"; CARD2="#5b7a90"; GOLD="#d9b25a"; BOX="#efe6d0"; SIG="#f2efe6"
MONO='font-family="DejaVu Sans Mono, monospace"'

def card(x,y,w=400,fill=CARD):
    h=round(w*53.98/85.6,1); r=18
    s.raw_path(f"M {x+r},{y} L {x+w-r},{y} Q {x+w},{y} {x+w},{y+r} L {x+w},{y+h-r} Q {x+w},{y+h} {x+w-r},{y+h} L {x+r},{y+h} Q {x},{y+h} {x},{y+h-r} L {x},{y+r} Q {x},{y} {x+r},{y} Z",fill=fill,sw=3)
    return h

# ================= the back of the card, behind =================
BX,BY=60,168
bh=card(BX,BY,fill=CARD2)
s.path([(BX,BY+26),(BX+400,BY+26),(BX+400,BY+76),(BX,BY+76)],fill=ACC,close=True,sw=2)        # the magnetic stripe
for k in (1,2): s.line(BX+4,BY+26+k*50/3,BX+396,BY+26+k*50/3,stroke="#8e3c2b",sw=1)          # its three tracks
s.path([(BX+24,BY+92),(BX+230,BY+92),(BX+230,BY+124),(BX+24,BY+124)],fill=SIG,close=True,sw=1.5)  # signature strip

# ================= the front of the card, in front =================
FX,FY=110,268
fh=card(FX,FY)
# the chip: gold contact pad with its segments
cx0,cy0=FX+48,FY+78
s.raw_path(f"M {cx0+8},{cy0} L {cx0+62},{cy0} Q {cx0+70},{cy0} {cx0+70},{cy0+8} L {cx0+70},{cy0+46} Q {cx0+70},{cy0+54} {cx0+62},{cy0+54} L {cx0+8},{cy0+54} Q {cx0},{cy0+54} {cx0},{cy0+46} L {cx0},{cy0+8} Q {cx0},{cy0} {cx0+8},{cy0} Z",fill=GOLD,sw=2)
s.line(cx0+35,cy0,cx0+35,cy0+54,stroke=INK,sw=1.2)
for y in (18,36): s.line(cx0,cy0+y,cx0+24,cy0+y,stroke=INK,sw=1.2); s.line(cx0+46,cy0+y,cx0+70,cy0+y,stroke=INK,sw=1.2)
s.path([(cx0+24,cy0+14),(cx0+46,cy0+14),(cx0+46,cy0+40),(cx0+24,cy0+40)],fill="none",sw=1.2)
# the contactless sign: three arcs
for k,r in enumerate((10,18,26)):
    s.raw_path(f"M {FX+340+r*0.5},{FY+60-r} A {r} {r} 0 0 1 {FX+340+r*0.5},{FY+60+r}",stroke="#f4f1ea",sw=3)
# number, expiry and name
s.add(f'<text x="{FX+40}" y="{FY+178}" font-size="27" fill="#f4f1ea" {MONO} letter-spacing="1">4000 1234 5678 9010</text>')
s.add(f'<text x="{FX+40}" y="{FY+212}" font-size="16" fill="#f4f1ea" {MONO}>VALID 09/29   A N OTHER</text>')
s.line(FX+40,FY+186,FX+132,FY+186,stroke=ACC,sw=3)     # the first digits underlined
s.text(FX+200,FY+fh+38,"a card, 85.6 by 54 mm",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the path of one payment =================
nodes=[(135,"the shop's|terminal"),(425,"the shop's|bank"),(715,"the card|network"),(1005,"the cardholder's|bank")]
NY0,NY1=610,676
for x,l in nodes:
    s.path([(x-105,NY0),(x+105,NY0),(x+105,NY1),(x-105,NY1)],fill=BOX,close=True,sw=2)
    s.text(x,NY0+28,l,anchor="middle",size=19,halo=BOX)
for (a,_),(b,_) in zip(nodes,nodes[1:]):
    s.arrow(a+112,NY0+16,b-112,NY0+16)
    s.arrow(b-112,NY1-14,a+112,NY1-14)
s.text(570,NY0-14,"the question goes out, the answer comes back",anchor="middle",italic=True,fill=SOFT,size=17)

s.callout(1,BX+380,BY+50,560,190,"The stripe holds the number|in three magnetic tracks")
s.callout(2,cx0+60,cy0+46,560,310,"The chip works out a fresh|code for every payment")
s.callout(3,FX+50,FY+186,560,447,"The first digits name|the bank that issued it")
s.callout(4,715,NY1,700,714,"The network routes the question to that bank",anchor="end")
s.callout(5,1060,NY0,1150,520,"The cardholder's bank|says yes or no",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","108-payment-card","payment-card"))
