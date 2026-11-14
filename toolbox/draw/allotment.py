import math,sys,os,random
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
random.seed(7)
BRONZE="#b08a4e"
s=Sheet("The allotment machine","about 2,400 years ago")
# the stone slab
SX,SY,SWd,SH=400,215,330,485
s.add(f'<rect x="{SX}" y="{SY}" width="{SWd}" height="{SH}" rx="6" fill="{STONE}" stroke="{INK}" stroke-width="3"/>')
s.add(f'<rect x="{SX-20}" y="{SY+SH}" width="{SWd+40}" height="26" fill="{STONE}" stroke="{INK}" stroke-width="3"/>')
letters=["Α","Β","Γ","Δ","Ε"]
CX0,CW,RY0,RH,ROWS=SX+78,48,SY+66,36,11
for c in range(5):
    x=CX0+c*CW
    s.text(x+19,SY+48,letters[c],size=24,anchor="middle",bold=True,halo="none")
    for r in range(ROWS):
        y=RY0+r*RH
        if r<8:
            s.add(f'<rect x="{x}" y="{y}" width="38" height="20" rx="2" fill="{BRONZE}" stroke="{INK}" stroke-width="2"/>')
            s.line(x+6,y+7,x+32,y+7,sw=1.2); s.line(x+6,y+13,x+26,y+13,sw=1.2)
        else:
            s.add(f'<rect x="{x}" y="{y+6}" width="38" height="8" fill="{INK}" stroke="{INK}" stroke-width="1"/>')
# the tube down the left side, with a funnel
TX=SX+34
s.raw_path(f"M {TX-30},{SY-38} L {TX+30},{SY-38} L {TX+11},{SY+4} L {TX-11},{SY+4} Z",fill=ACC,sw=3)
s.add(f'<rect x="{TX-11}" y="{SY+4}" width="22" height="{SH-70}" fill="{PAPER}" stroke="{ACC}" stroke-width="5"/>')
cols=[0,1,1,0]   # eight cubes in all, one for each row of tickets: one out, four in the tube, three going in
for i,c in enumerate(cols):
    y=SY+SH-70-18-i*20
    s.add(f'<rect x="{TX-8}" y="{y}" width="16" height="16" fill="{"#ffffff" if c else "#3a3531"}" stroke="{INK}" stroke-width="1.8"/>')
# stop at the bottom and a cube that has come out
s.line(TX-18,SY+SH-64,TX+18,SY+SH-64,sw=5)
s.add(f'<rect x="{TX-8}" y="{SY+SH-44}" width="16" height="16" fill="#ffffff" stroke="{INK}" stroke-width="1.8"/>')
# loose cubes about to go in
for (x,y,c) in ((TX-16,SY-62,0),(TX+4,SY-66,1),(TX-6,SY-84,1)):
    s.add(f'<rect x="{x}" y="{y}" width="16" height="16" fill="{"#ffffff" if c else "#3a3531"}" stroke="{INK}" stroke-width="1.8" transform="rotate(14 {x+8} {y+8})"/>')
# bracket on the first row
y=RY0+10
s.raw_path(f"M {CX0+5*CW+2},{y-14} l 10,0 l 0,28 l -10,0",sw=2)
s.callout(1,CX0+5*CW-2,SY+40,815,190,"Five columns of slots,|each under its own letter")
s.callout(2,CX0+4*CW+30,RY0+4*RH+10,815,430,"A juror's bronze ticket goes|into the column for his letter")
s.callout(3,TX-22,SY-30,330,200,"Black and white cubes|are poured into the funnel",anchor="end")
s.callout(4,TX-11,SY+SH-64,330,570,"The tube lets them out|at the bottom, one at a time",anchor="end")
s.callout(5,CX0+5*CW+12,y,815,300,"A white cube picks the whole|row. A black one sends it home")
s.save(os.path.join(os.path.dirname(__file__),"..","18-allotment-machine","allotment-machine"))
