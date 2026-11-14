import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The edict pillar","about 2,270 years ago")
EARTH="#d9c7a6"
cx=600; G=600          # centre line, ground level
top=250; foot=695      # top of shaft, bottom of shaft
wt,wb=15,22            # half-width at top and at foot
# earth, cut away in section, with the pit
s.path([(60,G),(cx-70,G),(cx-60,foot+22),(cx+60,foot+22),(cx+70,G),(1140,G),(1140,738),(60,738)],fill=EARTH,sw=0,close=True)
s.path([(cx-70,G),(cx-60,foot+22),(cx+60,foot+22),(cx+70,G)],fill="#efe3c8",sw=2)
s.line(60,G,cx-70,G,sw=3); s.line(cx+70,G,1140,G,sw=3)
for x in range(90,1130,46):
    if abs(x-cx)>90:
        for y in (G+30,G+72,G+112):
            s.line(x,y,x+14,y,stroke=SOFT,sw=1.5)
# slab under the foot
s.add(f'<rect x="{cx-52}" y="{foot}" width="104" height="20" fill="{STONE}" stroke="{INK}" stroke-width="3"/>')
# shaft
s.path([(cx-wt,top),(cx+wt,top),(cx+wb,foot),(cx-wb,foot)],fill="#ead9b4",sw=3,close=True)
s.line(cx-6,top+20,cx-9,G-20,stroke=PAPER,sw=4)   # gloss
# rough, unpolished foot below ground
for y in range(G+12,foot-4,14):
    s.line(cx-14,y,cx-4,y+5,stroke=SOFT,sw=1.5); s.line(cx+3,y+4,cx+13,y,stroke=SOFT,sw=1.5)
# inscription band, at reading height
for i in range(7):
    y=G-150+i*9
    s.line(cx-17,y,cx+17,y,stroke=ACC,sw=2.5,dash="5 3")
# capital: bell, platform, lion
s.raw_path(f"M {cx-wt},{top} C {cx-40},{top-8} {cx-34},{top-44} {cx-13},{top-52} L {cx+13},{top-52} C {cx+34},{top-44} {cx+40},{top-8} {cx+wt},{top} Z",fill=STONE,sw=3)
for dx in (-16,-6,6,16):
    s.line(cx+dx*0.75,top-48,cx+dx*1.5,top-4,stroke=SOFT,sw=1.5)
s.add(f'<rect x="{cx-30}" y="{top-66}" width="60" height="14" rx="3" fill="{STONE}" stroke="{INK}" stroke-width="3"/>')
b=top-66
# seated lion in profile, facing left
s.raw_path(f"M {cx+26},{b} L {cx+26},{b-22} C {cx+26},{b-46} {cx+8},{b-62} {cx-6},{b-64} C {cx-14},{b-76} {cx-30},{b-72} {cx-30},{b-58} L {cx-36},{b-50} L {cx-28},{b-44} C {cx-26},{b-34} {cx-24},{b-28} {cx-20},{b-22} L {cx-22},{b} L {cx-10},{b} L {cx-8},{b-20} L {cx+2},{b-20} L {cx+2},{b} Z",fill=STONE,sw=3)
s.raw_path(f"M {cx-8},{b-62} C {cx+2},{b-52} {cx-2},{b-38} {cx-14},{b-30}",sw=1.5,stroke=SOFT)
s.raw_path(f"M {cx+26},{b-6} C {cx+40},{b-10} {cx+38},{b-30} {cx+32},{b-34}",sw=3)
# person for scale
s.person(cx-150,G,lean=0.05,scale=0.5)
s.callout(1,cx+17,400,775,330,"The shaft: one piece of|sandstone, rubbed until it shines")
s.callout(2,cx+24,top-22,775,210,"The bell of the capital, shaped like|a lotus turned upside down")
s.callout(3,cx-22,b-48,400,150,"An animal on top,|most often a lion",anchor="end")
s.callout(4,cx-17,G-122,400,400,"The king's words, cut into|the stone in neat rows",anchor="end")
s.callout(5,cx+22,foot-30,775,505,"The buried foot stands|on a slab of stone")
s.save(os.path.join(os.path.dirname(__file__),"..","20-edict-pillar","edict-pillar"))
