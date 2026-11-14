import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The ration bowl","about 5,500 years ago")
# the bowl, cut in half: left side whole, right side in section
s.raw_path("M 250,330 L 330,560 L 590,560 L 670,330 L 640,318 L 560,520 L 360,520 L 280,318 Z",fill=CLAY)
s.raw_path("M 280,318 Q 460,350 640,318",sw=2)
for i in range(22): s.line(300+((i*53)%330),360+((i*37)%170),308+((i*53)%330),366+((i*37)%170),sw=1.5,stroke="#8a6a48")
# barley inside
s.raw_path("M 300,372 Q 460,340 620,372 L 560,520 L 360,520 Z",fill="#d9c27a",sw=1.5)
s.line(250,610,670,610,sw=2); s.line(250,601,250,619,sw=2); s.line(670,601,670,619,sw=2); s.text(460,642,"about 16 cm",anchor="middle",italic=True,size=19)
# the two written signs
def sign_bowl(x,y,col=INK,sw=5): s.raw_path(f"M {x-34},{y-16} L {x-18},{y+22} L {x+18},{y+22} L {x+34},{y-16} Z",stroke=col,sw=sw)
sign_bowl(900,250,ACC)
s.text(900,310,"ration",anchor="middle",italic=True,size=19)
s.raw_path("M 850,470 Q 850,420 890,420 Q 930,422 930,470 L 930,520 L 870,520 Q 850,500 850,470 Z",sw=5)   # a head, in profile
s.circle(905,455,4,fill=INK,sw=0); s.line(850,490,826,496,sw=5)
sign_bowl(790,500,ACC)
s.text(860,570,"to eat",anchor="middle",italic=True,size=19)
s.callout(1,330,470,100,470,"Coarse clay|mixed with|straw")
s.callout(2,300,335,150,200,"Shaped in moments by|hand, not thrown|on a wheel")
s.callout(3,655,326,560,200,"A thick wall and|a slanted rim")
s.callout(4,460,440,470,700,"Filled, it probably held one worker's ration")
s.callout(5,934,250,1150,180,"The written signs|for a ration, and|for eating",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","06-ration-bowl","ration-bowl"))
