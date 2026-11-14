import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The grinding stone","more than 30,000 years ago")
s.line(80,600,1120,600,sw=2)
# the slab, seen from the side, worn hollow
s.raw_path("M 250,600 L 230,500 Q 240,470 280,470 Q 560,540 880,455 Q 930,450 945,480 L 960,600 Z",fill=STONE)
# flour at the far end, grain at the near end
s.raw_path("M 800,474 Q 860,440 920,458 Q 905,470 880,470 Z",fill=BONE,sw=1.5)
for i in range(16): s.ellipse(300+i*11,478+((i*7)%9)+i*1.2,5,3,fill="#c9a56b",sw=1,rot=(i*31)%60)
# the rubbing stone
s.ellipse(560,478,110,34,fill=ACC,sw=3,rot=-3)
s.arrow(450,400,300,400); s.arrow(670,400,820,400)
# hands pressing down
for hx in (510,610): s.raw_path(f"M {hx-26},{452} Q {hx},{420} {hx+26},{450}",sw=5,stroke=SOFT)
s.line(510,440,430,250,stroke=SOFT,sw=5); s.line(610,438,470,250,stroke=SOFT,sw=5)
s.callout(1,330,560,150,690,"A slab of rough, hard stone,|worn hollow by years of use")
s.callout(2,620,480,900,300,"A rubbing stone, held|in both hands")
s.callout(3,330,486,90,330,"Grain goes on at|the near end")
s.callout(4,560,400,560,200,"Pushed forward and dragged|back, with the whole weight|of the body")
s.callout(5,870,460,1150,640,"Flour gathers at|the far end",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","05-grinding-stone","grinding-stone"))
