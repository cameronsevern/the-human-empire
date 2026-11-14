import math,sys,os,random
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The relay tablet","the Mongol empire, 1200s and 1300s")
SILVER="#c9ccc8"; CORD="#8a6a48"; HORSE="#d9c4a2"; HFAR="#c9b18c"; ROOF="#8f8a80"
CX=400; X0,X1=CX-85,CX+85; Y0,Y1=190,700; R=85
# ---- the tablet, front view: a long silver plate with rounded ends
s.raw_path(f"M {X0},{Y0+R} A {R},{R} 0 0 1 {X1},{Y0+R} L {X1},{Y1-R} A {R},{R} 0 0 1 {X0},{Y1-R} Z",fill=SILVER,sw=3.5)
s.raw_path(f"M {X0+10},{Y0+R} A {R-10},{R-10} 0 0 1 {X1-10},{Y0+R} L {X1-10},{Y1-R} A {R-10},{R-10} 0 0 1 {X0+10},{Y1-R} Z",stroke=SOFT,sw=1.5)
# the cord, looped through the raised ring near the top
RY=250
s.raw_path(f"M {CX-6},{RY} C {CX-60},{RY-60} {CX-40},{140} {CX},{132} C {CX+40},{140} {CX+60},{RY-60} {CX+6},{RY}",stroke=INK,sw=8)
s.raw_path(f"M {CX-6},{RY} C {CX-60},{RY-60} {CX-40},{140} {CX},{132} C {CX+40},{140} {CX+60},{RY-60} {CX+6},{RY}",stroke=CORD,sw=4.5)
s.circle(CX,RY,24,fill=SILVER,sw=3); s.circle(CX,RY,10,fill=PAPER,sw=2.5)
# cloud scrolls either side of the ring
for d in (-1,1):
    x=CX+d*48
    s.raw_path(f"M {x-d*12},{RY+14} C {x-d*16},{RY-4} {x+d*10},{RY-14} {x+d*16},{RY} C {x+d*20},{RY+12} {x+d*4},{RY+16} {x},{RY+6}",stroke=SOFT,sw=2)
# the order: four columns of square letters read top to bottom, inlaid in gold
random.seed(7)
def glyph(x,y):
    k=random.randrange(5); w=10
    if k==0: s.path([(x-w,y-8),(x+w,y-8),(x+w,y+8),(x-w,y+8)],stroke=ACC,sw=3.2,close=True)
    elif k==1: s.path([(x-w,y-8),(x+w,y-8)],stroke=ACC,sw=3.2); s.path([(x,y-8),(x,y+8),(x+w,y+8)],stroke=ACC,sw=3.2)
    elif k==2: s.path([(x-w,y+8),(x-w,y-8),(x+w,y-8),(x+w,y+8)],stroke=ACC,sw=3.2); s.line(x-w,y,x+w,y,stroke=ACC,sw=3.2)
    elif k==3: s.path([(x-w,y-8),(x+w,y-8)],stroke=ACC,sw=3.2); s.path([(x-w+3,y+8),(x-w+3,y-2),(x+w-3,y-2),(x+w-3,y+8)],stroke=ACC,sw=3.2)
    else: s.path([(x-w,y-8),(x,y-8),(x,y+8),(x-w,y+8)],stroke=ACC,sw=3.2); s.line(x+4,y-8,x+w,y+8,stroke=ACC,sw=3.2)
COLS=[CX+54,CX+18,CX-18,CX-54]                      # read from the left in Phags-pa
for i,x in enumerate(sorted(COLS)):
    for j in range(8-i):
        glyph(x,340+j*36)
        if j<7-i: s.line(x,348+j*36,x,368+j*36,stroke=ACC,sw=2.2)   # letters of one word joined by a stem
# ---- a post station behind, and a fresh horse ready at it
G=690
s.line(600,G,1150,G,stroke=SOFT,sw=1.5)
s.path([(930,G),(930,560),(1130,560),(1130,G)],fill=WOOD,close=True,sw=2.5)
s.raw_path("M 900,572 C 950,556 1000,528 1030,500 C 1060,528 1110,556 1160,572 Z",fill=ROOF,sw=2.5)
s.path([(1010,G),(1010,610),(1050,610),(1050,G)],fill="#b79b74",close=True,sw=2)
s.add('<g transform="translate(551,334) scale(0.5)">')
def leg(top,knee,hoof,fill=HORSE,w=13):
    (xt,yt),(xk,yk),(xf,yf)=top,knee,hoof
    s.path([(xt-w-6,yt),(xk-w,yk),(xf-w+4,712-16),(xf+w-2,712-16),(xk+w,yk),(xt+w+8,yt)],fill=fill,close=True,sw=3.5)
    s.path([(xf-w+2,712-16),(xf+w,712-16),(xf+w+3,712),(xf-w-1,712)],fill=INK,close=True,sw=3)
leg((470,530),(452,620),(462,0),fill=HFAR); leg((800,530),(812,620),(806,0),fill=HFAR)
s.raw_path("M 455,385 C 520,372 590,392 640,394 C 700,396 760,380 790,360 C 820,330 850,290 880,262 "
           "C 892,248 910,240 925,246 C 950,262 985,300 1002,330 C 1008,344 996,356 982,352 "
           "C 960,346 935,330 915,322 C 895,340 875,380 865,420 C 858,470 845,520 815,545 "
           "C 760,560 560,566 480,550 C 440,540 420,500 418,460 C 416,420 430,392 455,385 Z",fill=HORSE,sw=5)
s.circle(930,268,5,fill=INK,sw=0)
s.raw_path("M 900,250 L 896,226 L 912,244",fill=HORSE,sw=4)
s.raw_path("M 795,356 C 820,326 850,288 884,256",stroke=SOFT,sw=3)
s.raw_path("M 422,410 C 392,430 380,500 392,590",sw=10)
leg((500,535),(488,622),(496,0)); leg((830,520),(842,622),(836,0))
s.raw_path("M 925,248 L 975,340 M 912,322 L 990,330",stroke="#9b7653",sw=5)
s.add('</g>')
def T(x,y): return (round(551+0.5*x,1),round(334+0.5*y,1))
# ---- labels
s.callout(1,CX+22,RY+6,620,170,"A ring for the cord|it hung from")
s.callout(2,CX+54,452,620,300,"The khan's order, in Mongolian,|inlaid in gold")
s.callout(3,CX-54,340,240,340,"It opens: “By|the power of|eternal Heaven”",anchor="end")
s.callout(4,X0+22,640,240,600,"Silver. Gold|was for higher|ranks",anchor="end")
x5,y5=T(470,420); s.callout(5,x5,y5,700,500,"What it bought:|a fresh horse at|every station",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","37-relay-tablet","relay-tablet"))
