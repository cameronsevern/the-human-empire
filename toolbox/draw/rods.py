import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The rods and axe","about 2,150 years ago")
ROD="#c9a56b"; STRAP="#8a5a3c"

def bundle(cx,top,bot,w,axe=True,sc=1.0,straps=4,detail=True):
    n=9 if detail else 5
    if axe:
        # the axe's handle stands among the rods; its head sticks out at the side
        hx=cx+w*0.2
        s.line(hx,top-46*sc,hx,top+40*sc,sw=9*sc); s.line(hx,top-46*sc,hx,top+40*sc,stroke=WOOD,sw=5*sc)
        s.raw_path(f"M {hx},{top-34*sc} L {hx+44*sc},{top-40*sc} L {hx+78*sc},{top-62*sc} C {hx+96*sc},{top-30*sc} {hx+96*sc},{top+4*sc} {hx+78*sc},{top+30*sc} L {hx+44*sc},{top+4*sc} L {hx},{top-4*sc} Z",
                   fill=ACC,sw=3*sc)
    s.add(f'<rect x="{cx-w/2}" y="{top}" width="{w}" height="{bot-top}" rx="{6*sc}" fill="{ROD}" stroke="{INK}" stroke-width="{3*sc}"/>')
    for i in range(1,n):
        x=cx-w/2+i*w/n
        s.line(x,top+4*sc,x,bot-4*sc,stroke=INK,sw=1.3*sc)
    if detail:
        for i in range(n):
            x=cx-w/2+(i+0.5)*w/n
            s.ellipse(x,top+2*sc,w/n/2-1,4*sc,fill=WOOD,sw=1.3*sc)
    # crossing straps
    seg=(bot-top-40*sc)/straps
    for k in range(straps):
        y0=top+20*sc+k*seg
        s.path([(cx-w/2,y0),(cx+w/2,y0+seg*0.5),(cx+w/2,y0+seg*0.5+8*sc),(cx-w/2,y0+8*sc)],fill=STRAP,sw=1.5*sc,close=True)
        s.path([(cx+w/2,y0),(cx-w/2,y0+seg*0.5),(cx-w/2,y0+seg*0.5+8*sc),(cx+w/2,y0+8*sc)],fill=STRAP,sw=1.5*sc,close=True)
    s.add(f'<rect x="{cx-w/2}" y="{top+6*sc}" width="{w}" height="{8*sc}" fill="{STRAP}" stroke="{INK}" stroke-width="{1.5*sc}"/>')
    s.add(f'<rect x="{cx-w/2}" y="{bot-14*sc}" width="{w}" height="{8*sc}" fill="{STRAP}" stroke="{INK}" stroke-width="{1.5*sc}"/>')

# the big bundle
CX,TOP,BOT,BW=330,250,650,110
bundle(CX,TOP,BOT,BW)
# inset: inside the city, the axe taken out
ix,iy,r=1000,250,110
s.inset(ix,iy,r,caption="Inside Rome")
bundle(ix,iy-76,iy+84,44,axe=False,sc=0.45,straps=3,detail=False)
# a consul's twelve, in a row
for k in range(12):
    bundle(770+k*34,575,640,15,axe=True,sc=0.2,straps=2,detail=False)

s.callout(1,CX+40,400,560,390,"Rods of wood,|for a beating")
s.callout(2,CX+BW*0.2+70,TOP-40,560,190,"An axe, for|a beheading")
s.callout(3,CX+BW/2-10,505,560,505,"Straps hold the axe's|handle among the rods")
s.callout(4,ix-6,iy-10,850,470,"There the axe came out:|a citizen could appeal|against a death sentence")
s.callout(5,770,600,740,690,"A consul had twelve, each|carried by an attendant")
s.save(os.path.join(os.path.dirname(__file__),"..","24-rods-and-axe","rods-and-axe"))
