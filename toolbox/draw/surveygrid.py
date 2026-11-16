import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The survey grid","United States, from 1785")
FIELD="#e9e0c4"; SCHOOL="#c9d3a4"; LINK="#9a9488"; BRASS="#d4b25a"

# ---- a township: six miles square, thirty-six sections numbered back and forth
TX,TY,C=60,140,70
rows=[[6,5,4,3,2,1],[7,8,9,10,11,12],[18,17,16,15,14,13],[19,20,21,22,23,24],[30,29,28,27,26,25],[31,32,33,34,35,36]]
for r in range(6):
    for c in range(6):
        n=rows[r][c]; x=TX+c*C; y=TY+r*C
        s.path([(x,y),(x+C,y),(x+C,y+C),(x,y+C)],fill=SCHOOL if n==16 else FIELD,close=True,sw=1.5)
        if n==33: s.path([(x+C/2,y),(x+C,y),(x+C,y+C/2),(x+C/2,y+C/2)],fill=ACC,close=True,sw=1.5)
s.path([(TX,TY),(TX+6*C,TY),(TX+6*C,TY+6*C),(TX,TY+6*C)],close=True,sw=4)
for r in range(6):
    for c in range(6):
        n=rows[r][c]; x=TX+c*C; y=TY+r*C
        if n==33: s.text(x+18,y+C-14,str(n),anchor="middle",size=17)
        else: s.text(x+C/2,y+C/2+7,str(n),anchor="middle",size=19)
s.text(TX+3*C,TY+6*C+34,"six miles",anchor="middle",italic=True,fill=SOFT)
s.add(f'<text x="{TX-14}" y="{TY+3*C}" text-anchor="middle" font-size="20" font-style="italic" fill="{SOFT}" transform="rotate(-90 {TX-14} {TY+3*C})">six miles</text>')

# ---- one section, enlarged, cut into four quarters of 160 acres
EX,EY,E=780,160,300
for (qx,qy) in ((0,0),(1,0),(0,1),(1,1)):
    s.path([(EX+qx*E/2,EY+qy*E/2),(EX+(qx+1)*E/2,EY+qy*E/2),(EX+(qx+1)*E/2,EY+(qy+1)*E/2),(EX+qx*E/2,EY+(qy+1)*E/2)],
           fill=ACC if (qx,qy)==(1,0) else FIELD,close=True,sw=2)
s.path([(EX,EY),(EX+E,EY),(EX+E,EY+E),(EX,EY+E)],close=True,sw=4)
# a farmhouse and furrows on the red quarter
s.path([(EX+E*0.62,EY+60),(EX+E*0.70,EY+40),(EX+E*0.78,EY+60),(EX+E*0.78,EY+86),(EX+E*0.62,EY+86)],fill=PAPER,close=True,sw=2)
for k in range(5): s.line(EX+E/2+14,EY+100+k*9,EX+E-14,EY+100+k*9,stroke="#7a2f20",sw=1.5)
s.text(EX+E/2,EY-16,"Section 33, enlarged",anchor="middle",italic=True)
s.text(EX+E/2,EY+E+30,"one mile",anchor="middle",italic=True,fill=SOFT)

# ---- Gunter's chain: a hundred iron links, sixty-six feet
CY0=665; X0,X1=600,1130; N=24
s.path([(X0-30,CY0-16),(X0-8,CY0-16),(X0-8,CY0+16),(X0-30,CY0+16)],fill=BRASS,close=True,sw=2)
s.path([(X1+8,CY0-16),(X1+30,CY0-16),(X1+30,CY0+16),(X1+8,CY0+16)],fill=BRASS,close=True,sw=2)
for i in range(N):
    x=X0+(X1-X0)*(i+0.5)/N
    s.ellipse(round(x,1),CY0,(X1-X0)/N/2+2,5,stroke=INK,sw=2.5)
    if i%6==5: s.circle(round(x+(X1-X0)/N/2,1),CY0,5,fill=BRASS,sw=1.5)
s.text((X0+X1)/2,CY0+42,"part of the chain",anchor="middle",italic=True,fill=SOFT)

s.callout(1,TX+6*C,TY+30,530,165,"A township, six|miles square")
s.callout(2,TX+5*C+40,TY+C+20,530,275,"Thirty-six sections,|a mile square each")
s.callout(3,TX+2*C+56,TY+2*C+62,530,385,"Section 16 paid|for a school")
s.callout(4,EX+E*0.85,EY+E*0.4,1150,520,"A quarter section,|160 acres",anchor="end")
s.callout(5,X0+60,CY0,560,560,"A chain of 100 links,|66 feet long")
s.save(os.path.join(os.path.dirname(__file__),"..","63-survey-grid","survey-grid"))
