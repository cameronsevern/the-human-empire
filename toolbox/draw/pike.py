import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The long pike","about 2,380 years ago")
s.line(60,562,1140,562,sw=2)
# rear ranks, pikes held up
for x in (90,170):
    s.person(x,560,lean=0.12); s.line(x+22,515,x+70,215,sw=4)
# five ranks with pikes levelled: every point reaches past the front man
levels=(350,362,374,386,398)
for i,x in enumerate((250,330,410,490,570)):
    y=levels[i]
    s.line(x-100,y+8,x+380,y,sw=4)
    s.path([(x+380,y-7),(x+404,y),(x+380,y+7)],fill=ACC,stroke=ACC,close=True)
for i,x in enumerate((250,330,410,490,570)):
    s.person(x,560,lean=0.12,arm_to=(x+50,levels[i]+4))
    s.circle(x+6,455,17,fill=METAL,sw=2.5)
# its length
s.line(470,300,974,300,sw=2); s.line(470,291,470,309,sw=2); s.line(974,291,974,309,sw=2); s.text(722,286,"more than five metres",anchor="middle",italic=True,size=19)
s.callout(1,760,396,880,180,"A pike held|in both hands")
s.callout(2,576,455,700,660,"A small shield hangs|from a strap")
s.callout(3,972,398,1150,460,"Five rows of points|reach past the|front rank",anchor="end")
s.callout(4,150,300,330,170,"The rows behind hold theirs|up, where they stop arrows")
s.callout(5,250,560,330,690,"Sixteen rows deep,|drilled to move as one")
s.save(os.path.join(os.path.dirname(__file__),"..","19-long-pike","long-pike"))
