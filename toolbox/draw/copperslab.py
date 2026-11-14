import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The copper slab","about 3,500 years ago")
# oxhide ingot outline, concave sides, four horns
d="M 250,270 Q 300,300 380,305 Q 560,330 740,305 Q 820,300 870,270 Q 850,330 845,420 Q 850,510 870,570 Q 820,540 740,535 Q 560,510 380,535 Q 300,540 250,570 Q 270,510 275,420 Q 270,330 250,270 Z"
s.raw_path(d,fill=METAL,sw=3)
for (x,y) in [(250,270),(870,270),(250,570),(870,570)]: s.circle(x,y,26,stroke=ACC,sw=4)
for i in range(14):
    x=340+ (i*37)%440; y=350+(i*53)%150; s.circle(x,y,5,sw=1.5)
s.raw_path("M 600,400 L 640,400 M 620,380 L 620,420",stroke=INK,sw=4)
# scale bar
s.line(250,620,870,620,sw=3); s.line(250,610,250,630,sw=3); s.line(870,610,870,630,sw=3); s.text(560,655,"about 60 cm",anchor="middle")
# carrying figure
s.person(1010,540,lean=0.1,scale=1.0)
s.add(f'<rect x="965" y="385" width="100" height="26" rx="6" fill="{METAL}" stroke="{INK}" stroke-width="3"/>')
s.callout(1,480,318,90,170,"A slab of nearly pure copper,|as heavy as a full suitcase")
s.callout(2,870,270,1130,170,"Four corners drawn out|into handles",anchor="end")
s.callout(3,420,470,60,665,"One face is rough and blistered,|where the metal cooled|in an open mould")
s.callout(4,620,400,560,170,"A mark cut in by the|maker or the shipper")
s.callout(5,1015,398,1150,330,"One man carries it|on his shoulder",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","11-copper-slab","copper-slab"))
