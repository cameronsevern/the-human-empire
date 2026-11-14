import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The clay envelope","about 4,000 years ago")
def lines(x,y,w,n,gap,col=INK,sw=2):
    for i in range(n): s.line(x,y+i*gap,x+w,y+i*gap,stroke=col,sw=sw,dash="10 5")
# 1 the tablet
s.add(f'<rect x="110" y="300" width="190" height="230" rx="22" fill="{CLAY}" stroke="{INK}" stroke-width="3"/>')
lines(130,330,150,9,22)
# 2 half wrapped: tablet inside a cut-open shell
s.add(f'<rect x="440" y="280" width="250" height="270" rx="34" fill="{CLAY}" stroke="{INK}" stroke-width="3"/>')
s.add(f'<path d="M 560,280 L 656,280 Q 690,280 690,314 L 690,516 Q 690,550 656,550 L 560,550 L 590,480 L 550,410 L 590,340 Z" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>')
s.add(f'<rect x="540" y="310" width="125" height="210" rx="16" fill="{CLAY}" stroke="{INK}" stroke-width="3"/>')
lines(575,335,75,8,22)
lines(460,320,70,9,22)
# 3 sealed envelope with seal band
s.add(f'<rect x="830" y="280" width="250" height="270" rx="34" fill="{CLAY}" stroke="{INK}" stroke-width="3"/>')
lines(855,315,200,4,22)
s.add(f'<rect x="830" y="405" width="250" height="56" fill="none" stroke="{ACC}" stroke-width="4"/>')
for i in range(5):
    x=856+i*48; s.circle(x,425,7,stroke=ACC,sw=3); s.line(x,432,x,452,stroke=ACC,sw=3); s.line(x-9,440,x+9,440,stroke=ACC,sw=3)
lines(855,485,200,3,22)
s.arrow(320,415,420,415); s.arrow(710,415,810,415)
s.callout(1,205,300,150,200,"The agreement is|written on a tablet")
s.callout(2,470,290,420,180,"A thin sheet of clay is|wrapped round it and|pinched shut")
s.callout(3,955,330,1090,200,"The same words are|written again on|the outside",anchor="end")
s.callout(4,955,433,1090,640,"The parties and witnesses|roll their seals across it",anchor="end")
s.callout(5,640,500,430,670,"If the two sides ever disagree,|a judge breaks the envelope|and reads the tablet inside")
s.save(os.path.join(os.path.dirname(__file__),"..","09-clay-envelope","clay-envelope"))
