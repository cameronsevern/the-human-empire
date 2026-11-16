import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The tax stamp","London, for the American colonies, 1765")
SHEET="#f4ecd8"; LIGHT="#fffaf0"; SHADE="#b3a487"; VELLUM="#ead9b4"; BLUE="#a9b8c6"; STEEL="#9aa1a5"; WRITE="#7d6f60"

# ================= a deed, written on stamped paper =================
DX0,DY0,DX1,DY1=50,190,290,700
s.path([(DX0,DY0),(DX1,DY0),(DX1,DY1),(DX0,DY1)],fill=SHEET,close=True,sw=2.5)
ex,ey=105,245                                                        # the colourless stamp in the corner
s.circle(ex,ey,32,fill=SHEET,stroke=SHADE,sw=3)
s.raw_path(f"M {ex-25},{ey-20} A 32 32 0 0 1 {ex+20},{ey-25}",stroke=LIGHT,sw=4)
s.circle(ex,ey,12,fill="none",stroke=SHADE,sw=2)
for k in range(17):                                                  # lines of handwriting
    y=310+k*21; x0=DX0+25 if k else DX0+55
    s.raw_path(f"M {x0},{y} q 12,-6 24,0"+" t 24,0"*(7 if k else 6),stroke=WRITE,sw=1.5)
s.raw_path(f"M {DX0+110},{DY1-30} c 20,-20 40,10 60,-6 s 30,-10 50,4",stroke=WRITE,sw=2)  # signature
s.text((DX0+DX1)/2,740-6,"a deed",anchor="middle",italic=True,fill=SOFT)

# ================= the stamp, enlarged =================
CX,CY,R=600,380,90
s.circle(CX,CY,R+35,fill=SHEET,stroke=SHADE,sw=2)                  # the paper around it
# raised garter band: light on the upper left, shadow on the lower right
s.circle(CX,CY,R,fill=SHEET,stroke=SHADE,sw=4)
s.circle(CX,CY,R-26,fill=SHEET,stroke=SHADE,sw=3)
s.raw_path(f"M {CX-R*0.95},{CY-R*0.3} A {R} {R} 0 0 1 {CX+R*0.3},{CY-R*0.95}",stroke=LIGHT,sw=6)
s.raw_path(f"M {CX+R*0.95},{CY+R*0.3} A {R} {R} 0 0 1 {CX-R*0.3},{CY+R*0.95}",stroke="#b3a68b",sw=5)
for k in range(20):                                                  # the motto round the garter, as dashes
    a=math.radians(k*18+9); rr=R-13
    s.line(round(CX+rr*math.cos(a)-5*math.sin(a),1),round(CY+rr*math.sin(a)+5*math.cos(a),1),
           round(CX+rr*math.cos(a)+5*math.sin(a),1),round(CY+rr*math.sin(a)-5*math.cos(a),1),stroke=SHADE,sw=3)
# the rose in the middle: five petals round a centre
for k in range(5):
    a=math.radians(k*72-90)
    s.circle(round(CX+26*math.cos(a),1),round(CY+26*math.sin(a),1),21,fill=SHEET,stroke=SHADE,sw=3)
s.circle(CX,CY,16,fill=SHEET,stroke=SHADE,sw=3)
s.circle(CX-5,CY-5,6,fill=LIGHT,stroke="none",sw=0)
# the crown on top
CT=CY-R-8
s.path([(CX-50,CT),(CX-58,CT-46),(CX-30,CT-26),(CX,CT-58),(CX+30,CT-26),(CX+58,CT-46),(CX+50,CT)],fill=SHEET,stroke=SHADE,close=True,sw=3)
s.line(CX-50,CT-4,CX+50,CT-4,stroke=LIGHT,sw=3)
s.circle(CX,CT-66,7,fill=SHEET,stroke=SHADE,sw=2.5)
s.text(CX,CY-R-90,"AMERICA",anchor="middle",size=20,fill="#9c8f78",bold=True)
s.text(CX,CY+R+26,"II SHILLINGS VI PENCE",anchor="middle",size=16,fill="#9c8f78",bold=True)
s.text(CX,740-6,"the stamp, enlarged",anchor="middle",italic=True,fill=SOFT)

# ================= how it was struck: die above, paper, counter below =================
SX0,SX1=860,1120; SY=230
bumps=[(SX0+60,30),(SX0+130,40),(SX0+200,30)]
def profile(y0,sign):
    d=f"M {SX0},{y0}"
    for (bx,w) in bumps:
        d+=f" L {bx-w},{y0} Q {bx},{y0+sign*36} {bx+w},{y0}"
    return d+f" L {SX1},{y0}"
# the die, coming down (red): flat back, hollows cut in its face
s.raw_path(f"{profile(SY-24,-1)} L {SX1},{SY-110} L {SX0},{SY-110} Z",fill=ACC,sw=2.5)
# the paper, pressed into a ridge
s.raw_path(profile(SY,-1),stroke=INK,sw=4)
# the counter below (grey): raised where the die is hollow
s.raw_path(f"{profile(SY+24,-1)} L {SX1},{SY+110} L {SX0},{SY+110} Z",fill=STEEL,sw=2.5)
s.arrow(SX1+35,SY-110,SX1+35,SY-36)
s.arrow(SX1+35,SY+110,SX1+35,SY+36)
s.text((SX0+SX1)/2,100,"struck, seen edge on",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= for parchment: a blue paper stamp, stapled on =================
VX0,VY0,VX1,VY1=900,545,1140,700
s.path([(VX0,VY0),(VX1,VY0),(VX1,VY1),(VX0,VY1)],fill=VELLUM,close=True,sw=2.5)
bx,by=965,605
s.path([(bx-48,by-46),(bx+48,by-46),(bx+48,by+46),(bx-48,by+46)],fill=BLUE,close=True,sw=2)
s.circle(bx,by,28,fill=BLUE,stroke="#8193a3",sw=3)
s.circle(bx,by,12,fill=BLUE,stroke="#8193a3",sw=2)
s.path([(bx-8,by+56),(bx-8,by+36),(bx+8,by+36),(bx+8,by+56)],stroke="#5d6468",sw=4)   # the metal staple
for k in range(5):
    y=VY0+85+k*14
    s.raw_path(f"M {VX0+110 if k<2 else VX0+20},{y-55 if k<2 else y} q 10,-5 20,0 t 20,0 t 20,0 t 20,0 t 20,0",stroke=WRITE,sw=1.5)
s.text((VX0+VX1)/2,740-6,"on parchment",anchor="middle",italic=True,fill=SOFT)

s.callout(1,ex+18,ey-26,330,140,"Sold already stamped,|then written on")
s.callout(2,CX+R-6,CY+20,760,470,"Crown, garter and rose,|raised in the paper")
s.callout(3,CX-60,CY+R+20,430,560,"AMERICA above, and|the sum paid below")
s.callout(4,SX0+14,SY-50,770,400,"An engraved die presses|the paper into a counter")
s.callout(5,bx-8,by+50,850,650,"For parchment, a blue|paper stamp, stapled on",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","56-tax-stamp","tax-stamp"))
