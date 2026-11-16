import math,sys,os,random
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The little red book","Quotations from Chairman Mao, Chinese edition, 1960s")
RED=ACC; RED2="#8f3a2a"; GOLD="#d6b04a"; PAGE="#f6f1e4"; GREY="#8f8a82"
random.seed(4)

# ================= the closed book, standing, cover facing us =================
BX0,BY0,BW,BH=140,250,270,381          # 9.5 by 13.4: the same proportions as the real book
s.path([(BX0+10,BY0+8),(BX0+BW+12,BY0+8),(BX0+BW+12,BY0+BH+10),(BX0+10,BY0+BH+10)],fill=PAGE,close=True,sw=2)   # page block behind
s.path([(BX0,BY0),(BX0+BW,BY0),(BX0+BW,BY0+BH),(BX0,BY0+BH)],fill=RED,close=True,sw=3)
s.path([(BX0+14,BY0),(BX0+14,BY0+BH)],stroke=RED2,sw=2)                    # the hinge of the soft cover
# the gold title, set across the top of the cover
s.add(f'<text x="{BX0+BW/2+7}" y="{BY0+92}" text-anchor="middle" font-size="40" fill="{GOLD}" font-family="Noto Serif CJK TC, Noto Sans CJK TC, serif" font-weight="bold" letter-spacing="2">毛主席语录</text>')
s.line(BX0+50,BY0+118,BX0+BW-36,BY0+118,stroke=GOLD,sw=2)

# ================= the open book: an inscription on the left, quotations on the right =================
OX,OY,PW,PH=545,262,270,370
s.path([(OX-8,OY-6),(OX+2*PW+8,OY-6),(OX+2*PW+8,OY+PH+8),(OX-8,OY+PH+8)],fill=RED,close=True,sw=3)  # cover showing round the pages
s.path([(OX,OY),(OX+PW,OY+8),(OX+PW,OY+PH+2),(OX,OY+PH-4)],fill=PAGE,close=True,sw=2)
s.path([(OX+PW,OY+8),(OX+2*PW,OY),(OX+2*PW,OY+PH-4),(OX+PW,OY+PH+2)],fill=PAGE,close=True,sw=2)
# left page: Lin Biao's inscription in three columns, read top to bottom, right to left
cols=["读毛主席的书","听毛主席的话","照毛主席的指示办事"]
for c,col in enumerate(cols):
    x=OX+PW-70-c*62
    for j,ch in enumerate(col):
        s.add(f'<text x="{x}" y="{OY+62+j*30}" text-anchor="middle" font-size="26" fill="{INK}" font-family="Noto Serif CJK TC, serif" font-weight="900">{ch}</text>')
s.raw_path(f"M {OX+28},{OY+PH-36} q 14,-20 30,0 t 30,0",stroke=INK,sw=3)        # signature
# right page: a chapter heading and short numbered quotations in print
s.path([(OX+PW+40,OY+46),(OX+2*PW-40,OY+44),(OX+2*PW-40,OY+50),(OX+PW+40,OY+52)],fill=INK,close=True,sw=1)
y=OY+92
for para in (4,3,5,2):
    for k in range(para):
        x0=OX+PW+(46 if k==0 else 30); x1=OX+2*PW-30-(random.randint(30,110) if k==para-1 else 0)
        s.line(x0,y,x1,y,stroke=GREY,sw=4); y+=17
    y+=16
s.line(OX+PW,OY+8,OX+PW,OY+PH+2,stroke=SOFT,sw=2)

s.callout(1,190,590,90,700,"Red vinyl over card")
s.callout(2,250,340,110,190,"The title in gold: ‘Quotations|from Chairman Mao’")
s.callout(3,640,330,640,190,"Lin Biao's tribute in his own hand,|cut out by order after 1971")
s.callout(4,1000,430,1130,700,"427 quotations,|in 33 chapters",anchor="end")
s.callout(5,395,BY0+BH,470,700,"About 13 cm tall:|a pocket book")
s.save(os.path.join(os.path.dirname(__file__),"..","91-little-red-book","little-red-book"))
