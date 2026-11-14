import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The memorised verse","about 2,500 years ago")
def block(x,y,w,h,n,size=24):
    acc=(n==3)
    s.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{ACC if acc else BONE}" stroke="{INK}" stroke-width="2.5"/>')
    s.text(x+w/2,y+h/2+size*0.35,str(n),size=size,anchor="middle",bold=True,fill=(PAPER if acc else INK),halo="none")
def pair(x,y,a,b,w=38,h=46):
    block(x,y,w,h,a,20); block(x+w,y,w,h,b,20)
def seated(x,y,sc=1.0):
    """Cross-legged figure, seat point (x,y) at the ground."""
    s.raw_path(f"M {x-62*sc},{y} Q {x},{y-34*sc} {x+62*sc},{y} Z",fill=HIDE,stroke=SOFT,sw=4)
    s.raw_path(f"M {x-30*sc},{y-12*sc} Q {x-36*sc},{y-95*sc} {x},{y-104*sc} Q {x+36*sc},{y-95*sc} {x+30*sc},{y-12*sc} Z",fill=BONE,stroke=SOFT,sw=4)
    s.circle(x,y-128*sc,22*sc,fill=PAPER,stroke=SOFT,sw=4)
# teacher (larger, left) and pupil (smaller, facing him)
seated(130,520,1.15); seated(300,520,0.8)
s.line(40,522,390,522,stroke=SOFT,sw=2)
# sound marks from the teacher
for r in (26,40,54):
    s.raw_path(f"M {168+r*0.5:.0f},{372-r*0.7:.0f} A {r},{r} 0 0 1 {168+r*0.5:.0f},{372+r*0.7:.0f}",stroke=SOFT,sw=2)
X0=470
# row 1: the words one at a time
for i in range(5): block(X0+i*118,215,92,58,i+1)
# row 2: the step pattern 1-2, 2-3, 3-4, 4-5
for i in range(4): pair(X0+i*118,385,i+1,i+2)
# row 3: the braid, 1-2 2-1 1-2 then 2-3 3-2 2-3
seq=[(1,2),(2,1),(1,2),(2,3),(3,2),(2,3)]
for i,(a,b) in enumerate(seq): pair(X0+i*100+(24 if i>2 else 0),545,a,b)
s.callout(1,130,350,70,235,"The teacher chants a line and|the pupil chants it back")
s.callout(2,X0+20,215,X0+19,165,"The verse is learned again, one word at a time")
s.callout(3,X0+20,385,X0+19,335,"The step pattern: each word with the next")
s.callout(4,X0+20,545,X0+19,495,"The braid: each pair forwards, backwards, forwards")
s.callout(5,X0+5*100+24+57,591,X0+5*100+24+57,668,"Word three is said twice in the step|pattern and six times in the braid",anchor="end")
s.text(X0+6*100+30,578,"…",size=30)
s.save(os.path.join(os.path.dirname(__file__),"..","16-memorised-verse","memorised-verse"))
