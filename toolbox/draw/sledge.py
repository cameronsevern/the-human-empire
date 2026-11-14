import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The sledge","about 4,600 years ago")
# sloping ground from left to right
x0,y0,x1,y1=40,640,1160,500
slope=(y1-y0)/(x1-x0); ang=math.degrees(math.atan(slope))
def gy(x): return y0+slope*(x-x0)
s.path([(x0,y0),(x1,y1),(x1,720),(x0,720)],fill="#efe3c8",sw=0,close=True)
s.line(x0,y0,x1,y1,sw=3)
# wet sand patch in front of sledge
s.path([(520,gy(520)),(690,gy(690)),(690,gy(690)+16),(520,gy(520)+16)],fill=ACC,stroke=ACC,sw=1,close=True)
# sledge + block, drawn level then rotated to the slope about the sledge's rear foot
sx=250; sy=gy(sx)
s.add(f'<g transform="rotate({ang:.2f} {sx} {sy})">')
s.raw_path(f"M {sx},{sy-6} L {sx+250},{sy-6} Q {sx+290},{sy-8} {sx+300},{sy-44} L {sx+286},{sy-44} Q {sx+278},{sy-22} {sx+250},{sy-22} L {sx},{sy-22} Z",fill=WOOD)
for k in (30,110,190): s.add(f'<rect x="{sx+k}" y="{sy-36}" width="26" height="14" fill="{WOOD}" stroke="{INK}" stroke-width="2.5"/>')
s.add(f'<rect x="{sx+18}" y="{sy-196}" width="215" height="160" fill="{STONE}" stroke="{INK}" stroke-width="3"/>')
s.line(sx+40,sy-170,sx+90,sy-176,stroke=SOFT,sw=1.5); s.line(sx+120,sy-80,sx+200,sy-88,stroke=SOFT,sw=1.5); s.line(sx+60,sy-120,sx+110,sy-112,stroke=SOFT,sw=1.5)
s.add('</g>')
# front of sledge in page coordinates
def rot(px,py):
    a=math.radians(ang); dx,dy=px-sx,py-sy
    return (sx+dx*math.cos(a)-dy*math.sin(a), sy+dx*math.sin(a)+dy*math.cos(a))
fx,fy=rot(sx+296,sy-40)
# pullers
feet=[820,900,980,1060]
hands=[]
for f in feet:
    hx,hy=f-22,gy(f)-108
    s.person(f,gy(f),lean=0.55,arm_to=(round(hx,1),round(hy,1))); hands.append((hx,hy))
s.path([(fx,fy)]+hands,stroke=INK,sw=3)
# water pourer
pf=610
sh=s.person(pf,gy(pf),lean=-0.25,arm_to=(pf-58,gy(pf)-112))
s.raw_path(f"M {pf-78},{gy(pf)-128} L {pf-48},{gy(pf)-122} L {pf-56},{gy(pf)-96} L {pf-74},{gy(pf)-100} Z",fill=CLAY,sw=2.5)
s.raw_path(f"M {pf-76},{gy(pf)-102} Q {pf-92},{gy(pf)-60} {pf-84},{gy(pf)-14}",stroke=ACC,sw=5)
bx,by=rot(sx+125,sy-120)
s.callout(1,round(bx),round(by),120,250,"A block of stone that|weighs as much as|two cars")
rx,ry=rot(sx+150,sy-14)
s.callout(2,round(rx),round(ry),150,690,"A wooden sledge with|upturned runners",halo="#efe3c8")
t3=(700-fx)/(hands[0][0]-fx); s.callout(3,700,round(fy+t3*(hands[0][1]-fy)),760,250,"Ropes, and a team|of about twenty")
s.callout(4,pf-84,round(gy(pf)-40),470,190,"Water is poured on the|sand in front. Damp sand|is firm, and the pull|needed is halved")
s.callout(5,1000,round(gy(1000)+2),1090,680,"A ramp of rubble|and mud brick",anchor="end",halo="#efe3c8")
s.save(os.path.join(os.path.dirname(__file__),"..","07-sledge","sledge"))
