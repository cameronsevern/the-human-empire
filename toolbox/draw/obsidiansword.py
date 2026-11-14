import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The obsidian sword","Mesoamerica, by about 1000")
OBS="#3b3a40"
# the club lies across the sheet: grip at the left, broad blade to the right
Y=330; X0=80; XG=330; X1=1000
TOP=lambda x: Y-28-(x-XG)*0.035 if x>XG else Y-14
BOT=lambda x: Y+28+(x-XG)*0.035 if x>XG else Y+14
# obsidian blades first, so the wood overlaps their roots
def blades(edge,sgn):
    x=XG+30
    while x<X1-20:
        y=edge(x)
        s.path([(x-17,y+sgn*4),(x-15,y-sgn*13),(x-4,y-sgn*15),(x+8,y-sgn*14),(x+16,y-sgn*12),(x+17,y+sgn*4)],fill=ACC,close=True,sw=2)
        x+=46
blades(TOP,1); blades(BOT,-1)
# the wooden paddle
s.raw_path(f"M {X0},{Y-14} L {XG},{Y-14} C {XG+20},{Y-14} {XG+20},{TOP(XG+30)} {XG+40},{TOP(XG+40)} "
           f"L {X1},{TOP(X1)} C {X1+20},{TOP(X1)} {X1+20},{BOT(X1)} {X1},{BOT(X1)} "
           f"L {XG+40},{BOT(XG+40)} C {XG+20},{BOT(XG+30)} {XG+20},{Y+14} {XG},{Y+14} L {X0},{Y+14} Z",fill=WOOD,sw=3)
# grain
for k in (-12,0,12):
    s.raw_path(f"M {XG+60},{Y+k} C {XG+300},{Y+k*1.2-4} {X1-300},{Y+k*1.5+4} {X1-20},{Y+k*1.6}",stroke="#b89a70",sw=1.4)
# the grooves along both edges
s.line(XG+40,TOP(XG+40)+7,X1-6,TOP(X1-6)+7,stroke="#8a6a48",sw=2)
s.line(XG+40,BOT(XG+40)-7,X1-6,BOT(X1-6)-7,stroke="#8a6a48",sw=2)
# leather-wrapped grip with a knob at the end
for x in range(X0+16,XG-10,18):
    s.line(x,Y-15,x+12,Y+15,stroke="#7a5a3c",sw=3)
s.ellipse(X0-6,Y,16,20,fill=WOOD,sw=3)

# inset: a cut across the edge, showing one blade set in its groove
CX,CY,R=980,560,120
s.inset(CX,CY,R)
# the wood, end on, with a slot in its top edge
s.path([(CX-60,CY+100),(CX-60,CY-10),(CX-14,CY-10),(CX-14,CY+40),(CX+14,CY+40),(CX+14,CY-10),(CX+60,CY-10),(CX+60,CY+100)],fill=WOOD,sw=3)
# glue in the slot
s.path([(CX-14,CY-10),(CX-14,CY+40),(CX+14,CY+40),(CX+14,CY-10),(CX+8,CY-16),(CX-8,CY-16)],fill="#2a2420",close=True,sw=2)
# the blade standing in the glue, thin edge up
s.path([(CX-8,CY+36),(CX-8,CY-30),(CX,CY-62),(CX+8,CY-30),(CX+8,CY+36)],fill=ACC,close=True,sw=2.5)

s.callout(1,560,Y+10,560,490,"A flat wooden club,|about a metre long")
s.callout(2,200,Y,200,470,"A grip wrapped|in leather")
s.callout(3,560,TOP(560)+7,420,170,"A groove cut|along each edge",anchor="end")
s.callout(4,958,TOP(958)-10,1130,200,"Blades of obsidian, about|3 cm long, set in a row",anchor="end")
s.callout(5,CX-6,CY+20,780,650,"Bitumen holds each|blade in its groove",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","42-obsidian-sword","obsidian-sword"))
