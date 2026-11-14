import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The clay tablet","about 5,400 years ago")
DARK="#b98e69"
# stage 1: tokens
def cone(x,y,h=70,w=44):
    s.raw_path(f"M {x-w/2},{y} L {x},{y-h} L {x+w/2},{y} Z",fill=CLAY); s.ellipse(x,y,w/2,8,fill=CLAY)
def ball(x,y,r=26): s.circle(x,y,r,fill=CLAY); s.raw_path(f"M {x-r*0.5},{y-r*0.45} A {r*0.7},{r*0.7} 0 0 1 {x+r*0.2},{y-r*0.75}",stroke="#ffffff",sw=3)
cone(140,430); cone(200,440); cone(260,430); ball(170,330); ball(240,335)
s.callout(1,200,440,120,560,"Tokens. A cone is a|small measure of grain,|a ball a large one")
s.arrow(320,380,400,380)
# stage 2: hollow ball with cutaway
bx,by,br=560,380,120
s.circle(bx,by,br,fill=CLAY)
s.raw_path(f"M {bx},{by} L {bx+br*math.cos(math.radians(-70)):.1f},{by+br*math.sin(math.radians(-70)):.1f} A {br},{br} 0 0 1 {bx+br*math.cos(math.radians(10)):.1f},{by+br*math.sin(math.radians(10)):.1f} Z",fill=DARK)
s.raw_path(f"M {bx+10},{by-8} L {bx+48},{by-92} A 100,100 0 0 1 {bx+98},{by+10} Z",fill="#6f5a48",sw=2)
s.circle(bx+52,by-28,11,fill=CLAY,sw=2); s.circle(bx+72,by-48,9,fill=CLAY,sw=2)
s.raw_path(f"M {bx+34},{by-40} L {bx+44},{by-62} L {bx+54},{by-40} Z",fill=CLAY,sw=2)
for (mx,my,k) in ((-60,-40,"c"),(-30,-70,"t"),(-70,20,"t"),(-25,45,"c"),(-50,75,"t"),(10,70,"c"),(-5,-20,"c")):
    if k=="c": s.circle(bx+mx,by+my,10,fill=DARK,stroke=ACC,sw=4)
    else: s.raw_path(f"M {bx+mx-11},{by+my+9} L {bx+mx},{by+my-12} L {bx+mx+11},{by+my+9} Z",fill=DARK,stroke=ACC,sw=4)
s.callout(2,bx+60,by-35,560,190,"The tokens are sealed|inside a hollow ball|of clay",anchor="end")
s.callout(3,bx-50,by+75,470,620,"Each token is pressed|into the outside first,|so the count can be read")
s.arrow(700,380,780,380)
# stage 3: tablet
tx,ty=840,280
s.add(f'<rect x="{tx}" y="{ty}" width="270" height="200" rx="34" fill="{CLAY}" stroke="{INK}" stroke-width="3"/>')
s.line(tx+135,ty+14,tx+135,ty+186,sw=2); s.line(tx+14,ty+100,tx+256,ty+100,sw=2)
for i in range(3): s.circle(tx+40+i*30,ty+50,10,fill=DARK,stroke=ACC,sw=4)
for i in range(4): s.raw_path(f"M {tx+30+i*26},{ty+160} L {tx+38+i*26},{ty+128} L {tx+46+i*26},{ty+160} Z",fill=DARK,stroke=ACC,sw=4)
# barley sign
s.line(tx+195,ty+85,tx+195,ty+25,sw=3)
for k in range(4):
    y=ty+40+k*13; s.line(tx+195,y+8,tx+180,y-4,sw=2.5); s.line(tx+195,y+8,tx+210,y-4,sw=2.5)
# jar sign
s.raw_path(f"M {tx+175},{ty+125} L {tx+215},{ty+125} L {tx+222},{ty+150} Q {tx+195},{ty+185} {tx+168},{ty+150} Z",sw=2.5)
# reed stylus
s.raw_path(f"M {tx+60},{ty+290} L {tx+250},{ty+245} L {tx+254},{ty+259} L {tx+64},{ty+304} Z",fill=WOOD,sw=2.5)
s.callout(4,tx+70,ty+50,872,190,"With the marks outside,|the ball is not needed.|A flat pad will do")
s.callout(5,tx+195,ty+60,1100,650,"A drawing, made with|a pointed reed, says|what was counted",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","06-clay-tablet","clay-tablet"))
