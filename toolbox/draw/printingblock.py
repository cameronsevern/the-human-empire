import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The printing block","China, by about 700")
PEAR="#e3c99c"; SIDE="#cdb184"; SHEET="#f7f2e6"
TEXT="如是我聞一時佛在舍衛國祇樹給孤獨園與大比丘眾千二百五十人俱爾時世尊食時著衣持缽入舍"
CJK="'Noto Serif CJK TC','Noto Serif CJK KR',serif"
# the block, seen from the front and a little above (an oblique view)
BL,BR,FR,FL=(290,300),(770,300),(720,440),(240,440)
D=46  # thickness
s.path([BL,BR,FR,FL],fill=PEAR,close=True,sw=3)
s.path([FL,FR,(FR[0],FR[1]+D),(FL[0],FL[1]+D)],fill=SIDE,close=True,sw=3)
s.path([FR,BR,(BR[0],BR[1]+D),(FR[0],FR[1]+D)],fill="#bea274",close=True,sw=3)
# grain on the front face
for y in (452,462,474):
    s.raw_path(f"M {FL[0]+6},{y} C 400,{y-4} 560,{y+5} {FR[0]-6},{y-1}",stroke="#a88a5c",sw=1.2)
# the front edge shows the relief: strokes stand up, the ground between them is cut down
x=FL[0]+14; pts=[(FL[0],FL[1])]
while x<FR[0]-20:
    pts+=[(x,FL[1]),(x,FL[1]-8),(x+14,FL[1]-8),(x+14,FL[1])]; x+=36
pts+=[(FR[0],FR[1])]
s.path(pts,stroke=INK,sw=2)
# characters carved in reverse: a mirror-image text mapped onto the top face
W0,H0=BR[0]-BL[0],FL[1]-BL[1]
c=(FL[0]-BL[0])/H0
cols=[]
k=0
for i in range(10):
    u=W0-24-i*44            # Chinese reads from the right; on the block the first column is at the left
    col=TEXT[k:k+4]; k+=4
    for j,ch in enumerate(col):
        cols.append((u,26+j*30,ch))
def glyphs(dx,dy,fill,stroke,sw):
    g=[f'<g transform="matrix(-1,0,{c:.4f},1,{BR[0]},{BR[1]})">']
    for (u,v,ch) in cols:
        g.append(f'<text x="{u+dx}" y="{v+dy}" font-family="{CJK}" font-size="25" text-anchor="middle" fill="{fill}" stroke="{stroke}" stroke-width="{sw}">{ch}</text>')
    g.append('</g>')
    return "".join(g)
s.add(glyphs(2,3,"#8a6b42","none",0))       # the cut side of each raised stroke
s.add(glyphs(0,0,ACC,ACC,0.8))              # the top of the strokes, which takes the ink
# a round brush laying on ink
s.raw_path("M 418,236 C 432,246 430,268 404,292 C 396,268 398,246 418,236 Z",fill=INK,sw=2)
s.line(420,240,470,140,stroke=INK,sw=11); s.line(420,240,470,140,stroke=WOOD,sw=6)
# the print, lifted off: the same text reading the right way round
PX0,PY0,PW,PH=850,190,270,250
s.path([(PX0,PY0),(PX0+PW,PY0),(PX0+PW,PY0+PH),(PX0,PY0+PH)],fill=SHEET,close=True,sw=2.5)
g=['<g>']
k=0
for i in range(10):
    x=PX0+PW-20-i*25.5
    col=TEXT[k:k+4]; k+=4
    for j,ch in enumerate(col):
        g.append(f'<text x="{x}" y="{PY0+40+j*30}" font-family="{CJK}" font-size="20" text-anchor="middle" fill="{INK}">{ch}</text>')
g.append('</g>'); s.add("".join(g))
s.raw_path(f"M 790,330 C 805,300 815,290 830,282",sw=2.5)
s.arrow(820,288,842,276)
s.callout(1,520,470,560,640,"A smooth plank of pear wood")
s.callout(2,512,345,560,170,"Characters left standing,|cut in mirror image")
s.callout(3,FL[0]+50,FL[1]-4,300,620,"The wood around|every stroke|is cut away",anchor="end")
s.callout(4,412,262,250,190,"Ink is brushed|onto the block",anchor="end")
s.callout(5,PX0+PW-60,PY0+PH-30,850,560,"Paper rubbed on the block|takes a print that reads|the right way round")
s.save(os.path.join(os.path.dirname(__file__),"..","31-printing-block","printing-block"))
