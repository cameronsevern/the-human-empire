import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The ammonia converter","A converter of the 1910s cut open, with the loop of gas around it")
SHELL="#7d858a"; LINER="#c9ced1"; PIPE="#9aa2a7"; WATERC="#cfdde3"; LIQ="#dfe9ee"; MOTOR="#6f777c"

def pipe(pts,w=14):
    s.path(pts,stroke=INK,sw=w+4); s.path(pts,stroke=PIPE,sw=w)

# ================= pipework first, so the vessels sit on top =================
CX=640                       # converter centre line
TOPY,BOTY=200,640            # converter top and bottom
CMPX,CMPY=210,590            # compressor centre
SEPX,SEPY=1080,600           # separator centre
# fresh gas comes in from the left; recycled gas comes down to meet it
pipe([(44,CMPY),(CMPX-70,CMPY)])
pipe([(SEPX,SEPY-70),(SEPX,150),(110,150),(110,CMPY)])
# compressor up and across to the converter's top
pipe([(CMPX-30,CMPY-50),(CMPX-30,250),(CX-60,250)])
# converter bottom round to the cooler
pipe([(CX,BOTY),(CX,690),(870,690),(870,560)])
# cooler to separator
pipe([(870,380),(870,340),(SEPX-40,340),(SEPX-40,SEPY-70)])
# liquid ammonia drawn off
pipe([(SEPX,SEPY+70),(SEPX,722)],w=10)
s.arrow(SEPX-30,680,SEPX-30,720)
s.text(SEPX-45,712,"liquid ammonia",anchor="end",italic=True,fill=SOFT,size=18)
s.arrow(50,CMPY+34,100,CMPY+34)
s.arrow(420,150-28,360,150-28)

# ================= the compressor =================
s.path([(CMPX-70,CMPY-50),(CMPX+70,CMPY-50),(CMPX+70,CMPY+50),(CMPX-70,CMPY+50)],fill=SHELL,close=True,sw=3)
s.circle(CMPX,CMPY,36,fill=LINER,sw=2.5)
for k in range(6):
    a=k*math.pi/3
    s.line(CMPX,CMPY,CMPX+30*math.cos(a),CMPY+30*math.sin(a),sw=2)
s.path([(CMPX-60,CMPY+50),(CMPX+60,CMPY+50),(CMPX+66,CMPY+66),(CMPX-66,CMPY+66)],fill=MOTOR,close=True,sw=2)

# ================= the converter, cut open =================
RO,RI=62,46                      # outer radius of shell, inner face of shell
# outer steel shell, a thick wall
s.path([(CX-RO,TOPY+20),(CX+RO,TOPY+20),(CX+RO,BOTY-20),(CX-RO,BOTY-20)],fill=SHELL,close=True,sw=3)
# flanged heads, top and bottom
for y in (TOPY,BOTY-30):
    s.path([(CX-RO-12,y),(CX+RO+12,y),(CX+RO+12,y+30),(CX-RO-12,y+30)],fill=SHELL,close=True,sw=3)
    for bx in (-RO-4,RO+4): s.circle(CX+bx,y+15,4,fill=INK,sw=0)
# inside: the thin soft lining, then the catalyst
s.path([(CX-RI,TOPY+30),(CX+RI,TOPY+30),(CX+RI,BOTY-30),(CX-RI,BOTY-30)],fill=LINER,close=True,sw=2)
s.path([(CX-RI+8,TOPY+30),(CX+RI-8,TOPY+30),(CX+RI-8,BOTY-30),(CX-RI+8,BOTY-30)],fill="#f2f0ea",close=True,sw=1.2)
CATY0,CATY1=300,540
s.path([(CX-RI+8,CATY0),(CX+RI-8,CATY0),(CX+RI-8,CATY1),(CX-RI+8,CATY1)],fill=ACC,close=True,sw=2.5)
import random; random.seed(4)
for _ in range(70):
    x=CX+random.uniform(-RI+14,RI-14); y=random.uniform(CATY0+6,CATY1-6)
    s.circle(round(x,1),round(y,1),3,fill="#7a3324",sw=0)
# the small holes in the shell that let stray hydrogen out
for y in range(250,600,36):
    for sx in (-1,1):
        s.circle(CX+sx*(RO+RI)/2,y,3,fill=PAPER,stroke=INK,sw=1)
# flow arrows inside
s.arrow(CX,TOPY+60,CX,CATY0-14)
s.arrow(CX,CATY1+14,CX,BOTY-50)
s.text(CX,TOPY-12,"the converter",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the cooler =================
s.path([(820,380),(920,380),(920,560),(820,560)],fill=WATERC,close=True,sw=3)
for k in range(6):
    y=400+k*26
    s.raw_path(f"M 840,{y} Q 870,{y+14} 900,{y}",stroke=INK,sw=2)
s.text(980,470,"the cooler",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the separator =================
s.path([(SEPX-60,SEPY-70),(SEPX+60,SEPY-70),(SEPX+60,SEPY+70),(SEPX-60,SEPY+70)],fill=LINER,close=True,sw=3)
s.path([(SEPX-56,SEPY+10),(SEPX+56,SEPY+10),(SEPX+56,SEPY+66),(SEPX-56,SEPY+66)],fill="#a9c6d4",close=True,sw=0)
s.line(SEPX-56,SEPY+10,SEPX+56,SEPY+10,stroke=INK,sw=1.5)

s.callout(1,60,CMPY,90,690,"Nitrogen from the air and|hydrogen, one part to three")
s.callout(2,CMPX+40,CMPY-30,330,620,"Squeezed to about|200 atmospheres")
s.callout(3,CX-20,420,470,330,"Hot iron catalyst joins|them into ammonia",anchor="end")
s.callout(4,CX-(RO+RI)/2,556,490,480,"Holes in the steel shell|let stray hydrogen out",anchor="end")
s.callout(5,950,150,1000,230,"Unchanged gas|goes round again",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","110-ammonia-converter","ammonia-converter"))
