import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The caravel","Portugal, rebuilt for the ocean in the 1400s")
CANVAS="#efe6d0"; HULL="#a8835a"; DARKW="#7d5f3f"; SEA="#9fb4bf"
WL=560
def sail(T,P,Cl,fill):
    (tx,ty),(px,py),(cx,cy)=T,P,Cl
    # the leech and foot belly out a little
    s.raw_path(f"M {tx},{ty} L {px},{py} Q {(px+cx)/2-30},{(py+cy)/2+20} {cx},{cy} Q {(cx+tx)/2},{(cy+ty)/2+26} {tx},{ty} Z",fill=fill,sw=2.5)
    for k in range(1,6):                                  # seams
        f=k/6; x0,y0=tx+(px-tx)*f,ty+(py-ty)*f
        s.line(round(x0,1),round(y0,1),round(x0+(cx-x0)*0.85,1),round(y0+(cy-y0)*0.85,1),stroke=SOFT,sw=1.2)
    s.line(tx+8,ty+6,px-10,py-8,stroke=INK,sw=7); s.line(tx+8,ty+6,px-10,py-8,stroke=WOOD,sw=3.5)   # the yard
def mast(x,top):
    s.line(x,470,x,top,stroke=INK,sw=9); s.line(x,470,x,top,stroke=WOOD,sw=5)
# ---- masts and sails, back to front
mast(330,300); sail((420,462),(190,290),(270,478),CANVAS)
mast(500,215); sail((610,456),(300,196),(400,480),CANVAS)
mast(700,240); sail((905,442),(470,112),(612,482),ACC)
# ---- the hull: low in the bow, a raised deck at the stern
s.raw_path("M 228,430 L 330,436 C 450,458 650,466 800,462 C 860,460 905,452 940,436 "
           "C 930,500 900,560 840,600 C 700,624 420,626 300,606 C 262,580 240,520 228,430 Z",fill=HULL,sw=3)
s.raw_path("M 232,456 C 400,474 700,482 930,456",stroke=DARKW,sw=2)
s.raw_path("M 244,500 C 420,520 720,522 912,500",stroke=DARKW,sw=2)
s.path([(228,430),(330,436),(330,412),(234,404)],fill=DARKW,close=True,sw=2.5)       # stern deck rail
# rudder on the sternpost, with its tiller
s.path([(236,444),(222,446),(206,616),(244,612)],fill=DARKW,close=True,sw=2.5)
# ---- the sea, washed over the lower hull
wave=" ".join(f"Q {x+20},{WL-8} {x+40},{WL} Q {x+60},{WL+8} {x+80},{WL}" for x in range(60,940,80))
s.raw_path(f"M 60,{WL} {wave} L 940,640 L 60,640 Z",fill=SEA,stroke="none",sw=0,extra='fill-opacity="0.55"')
s.raw_path(f"M 60,{WL} {wave}",stroke=INK,sw=2)
# ---- inset: upwind by zigzags
CX,CY,R=1052,500,104
s.inset(CX,CY,R)
s.arrow(CX,CY-R+16,CX,CY-R+64); s.text(CX+14,CY-R+44,"wind",size=17,italic=True,fill=SOFT)
pts=[(CX-6,CY+R-14),(CX-46,CY+40),(CX+40,CY+2),(CX-34,CY-30),(CX+8,CY-46)]
s.path(pts,stroke=ACC,sw=4)
for (x,y) in pts[1:4]: s.circle(x,y,4,fill=ACC,sw=0)
# ---- labels
s.callout(1,700,330,800,170,"Triangular sails that swing|round to either side")
s.callout(2,560,180,250,150,"A long yard,|low in front,|high behind",anchor="end")
s.callout(3,214,600,140,680,"A rudder on|the sternpost")
s.callout(4,620,600,540,680,"A light hull, about 20 metres|long, drawing little water")
s.callout(5,CX+40,CY+2,1150,690,"Upwind, by zigzags",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","40-caravel","caravel"))
