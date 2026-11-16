import math,sys,os,random
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("Penicillin","Norman Heatley's culture vessel, Oxford, 1940, cut open")
POT="#ece6d8"; GLAZE="#fbf9f3"; BROTH="#e3c27a"; COTTON="#ffffff"
random.seed(4)

# ================= the pottery vessel, lying flat, cut down the middle =================
X0,X1,Y0,Y1=230,880,300,490; T=16
def rbox(x0,y0,x1,y1,r,fill,sw=3):
    s.raw_path(f"M {x0+r},{y0} L {x1-r},{y0} Q {x1},{y0} {x1},{y0+r} L {x1},{y1-r} Q {x1},{y1} {x1-r},{y1} L {x0+r},{y1} Q {x0},{y1} {x0},{y1-r} L {x0},{y0+r} Q {x0},{y0} {x0+r},{y0} Z",fill=fill,sw=sw)
# the spout, coming out of the right-hand end and angled upwards
s.path([(X1-10,Y0+50),(X1+60,Y0-10),(X1+92,Y0+26),(X1-10,Y0+104)],fill=POT,close=True,sw=3)
s.path([(X1-10,Y0+64),(X1+64,Y0+4),(X1+80,Y0+22),(X1-10,Y0+90)],fill=GLAZE,close=True,sw=1)
rbox(X0,Y0,X1,Y1,22,POT)
rbox(X0+T,Y0+T,X1-T,Y1-T,12,GLAZE,sw=2)
# re-open the spout's bore through the end wall
s.path([(X1-T-2,Y0+66),(X1+4,Y0+62),(X1+4,Y0+88),(X1-T-2,Y0+88)],fill=GLAZE,stroke=GLAZE,close=True,sw=1)
# the cotton-wool plug in the mouth of the spout
for (dx,dy,r) in ((0,0,20),(14,-10,15),(-10,-14,14),(16,10,13),(-6,14,13),(4,-20,12)):
    s.circle(X1+76+dx,Y0+4+dy,r,fill=COTTON,stroke="#9a948a",sw=1.5)

# the broth, a shallow layer on the floor of the vessel
BT=440
s.path([(X0+T+2,BT),(X1-T-2,BT),(X1-T-2,Y1-T-4),(X0+T+2,Y1-T-4)],fill=BROTH,close=True,sw=2)
# a few specks of penicillin spreading down through the broth
for i in range(26):
    x=random.uniform(X0+40,X1-40); y=random.uniform(BT+10,Y1-T-10)
    s.circle(round(x,1),round(y,1),2.2,fill="#9b6b1e",sw=0)
# the mould: a wrinkled felt floating on top of the broth
pts=[]; x=X0+T+2
while x<=X1-T-2:
    pts.append((round(x,1),round(BT-10-6*abs(math.sin(x/23))-random.uniform(0,4),1))); x+=9
mould=pts+[(X1-T-2,BT+4),(X0+T+2,BT+4)]
s.path(mould,fill=ACC,close=True,sw=2.5)
# tufts of spores on the felt
for x in range(X0+40,X1-30,34):
    s.circle(x,BT-14-6*abs(math.sin(x/23)),5,fill="#d07a62",stroke=INK,sw=1)

s.callout(1,X0+8,Y0+70,110,185,"A glazed pottery box,|flat, so that hundreds|could be stacked")
s.callout(2,X1+70,Y0-14,880,180,"A spout, plugged with|cotton wool, to fill|and empty it",anchor="end")
s.callout(3,640,Y1-T-12,700,650,"A shallow pool of|broth to feed the mould")
s.callout(4,400,BT-14,330,620,"The mould grows as a|felt on the surface",anchor="end")
s.callout(5,800,BT+20,1100,540,"Penicillin seeps into|the broth, which is|drawn off and purified",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","81-penicillin","culture-vessel"))
