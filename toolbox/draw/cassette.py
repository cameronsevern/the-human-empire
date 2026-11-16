import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The cassette tape","A compact cassette, playing, with the player's parts beneath it, 1970s")
SHELL="#4a4643"; SHELL2="#5d5854"; LABEL="#efe6d0"; HUB="#f4f1ea"; PACK="#7b3f2c"; FELT="#d9cfb6"; HEADC="#b9c0c4"; RUBBER="#2b2826"

K=6.0; X0,Y0=95,170          # 6 px per millimetre; the cassette is 100 x 64 mm
def P(x,y): return (round(X0+x*K,1),round(Y0+y*K,1))

# ================= the shell =================
s.path([P(0,0),P(100.4,0),P(100.4,63.8),P(0,63.8)],fill=SHELL,close=True,sw=3)
# the raised lower panel that carries the openings
s.path([P(17,63.8),P(22,50),P(78.4,50),P(83.4,63.8)],fill=SHELL2,close=True,sw=2)
# write-protect tabs on the top edge
for x in (6,90): s.path([P(x,0),P(x+4.5,0),P(x+4.5,3),P(x,3)],fill="#6c6762",close=True,sw=1.5)

# ================= the two packs of tape on their hubs =================
HL,HR,HY=(28.6,71.8,30.5)
s.circle(*P(HL,HY),round(16.5*K,1),fill=PACK,stroke=INK,sw=2)
s.circle(*P(HR,HY),round(10.5*K,1),fill=PACK,stroke=INK,sw=2)
# tape from the packs down round the guide rollers and along the bottom edge
TY=61.0
left=[P(HL-19,HY),P(5,55),P(8,TY)]
s.path([P(HL-16.2,HY+4),P(4.5,56)],stroke=ACC,sw=4)
s.path([P(HR+10.3,HY+2),P(95.9,56)],stroke=ACC,sw=4)
for x in (6.5,93.9): s.circle(*P(x,57.5),round(2.8*K,1),fill=HUB,stroke=INK,sw=2)   # guide rollers
s.path([P(5,59.5),P(8,TY),P(92.4,TY),P(95.4,59.5)],stroke=ACC,sw=5)
# the label, with a window showing the hubs
lx0,ly0,lx1,ly1=4,4,96.4,47
wx0,wy0,wx1,wy1=22,22,78.4,39
d=(f"M {P(lx0,ly0)[0]},{P(lx0,ly0)[1]} L {P(lx1,ly0)[0]},{P(lx1,ly0)[1]} L {P(lx1,ly1)[0]},{P(lx1,ly1)[1]} L {P(lx0,ly1)[0]},{P(lx0,ly1)[1]} Z "
   f"M {P(wx0,wy0)[0]},{P(wx0,wy0)[1]} L {P(wx1,wy0)[0]},{P(wx1,wy0)[1]} L {P(wx1,wy1)[0]},{P(wx1,wy1)[1]} L {P(wx0,wy1)[0]},{P(wx0,wy1)[1]} Z")
s.raw_path(d,fill=LABEL,sw=2,extra='fill-rule="evenodd"')
for y in (10,15): s.line(*P(10,y),*P(90,y),stroke=SOFT,sw=1.2)
s.text(P(8,9)[0],P(8,9)[1]+4,"A",size=26,bold=True,halo=LABEL)
# hubs: white rings with teeth for the spindles
for hx in (HL,HR):
    cx,cy=P(hx,HY)
    s.circle(cx,cy,round(6.5*K,1),fill=HUB,stroke=INK,sw=2)
    s.circle(cx,cy,round(4*K,1),fill=SHELL,stroke=INK,sw=1.5)
    for k in range(6):
        a=math.radians(k*60)
        s.line(round(cx+2.4*K*math.cos(a),1),round(cy+2.4*K*math.sin(a),1),round(cx+4*K*math.cos(a),1),round(cy+4*K*math.sin(a),1),stroke=HUB,sw=4)

# ================= inside the shell at the bottom: pressure pad and capstan holes =================
s.raw_path(f"M {P(41,56.2)[0]},{P(41,56.2)[1]} Q {P(50,53.8)[0]},{P(50,53.8)[1]} {P(59,56.2)[0]},{P(59,56.2)[1]}",stroke=HEADC,sw=3)  # leaf spring
s.path([P(46.5,57.2),P(53.5,57.2),P(53.5,60.3),P(46.5,60.3)],fill=FELT,close=True,sw=1.5)   # felt pad
for x in (25.6,74.8): s.circle(*P(x,57.5),round(1.9*K,1),fill="#1f1d1b",stroke=INK,sw=1.5)   # capstan holes
s.circle(*P(74.8,57.5),round(1.0*K,1),fill=HEADC,stroke=INK,sw=1.5)                          # the capstan, through its hole

# ================= the player's parts, below the cassette =================
# playback head, touching the tape at the centre opening
s.path([P(44,TY+0.6),P(56,TY+0.6),P(57,TY+9),P(43,TY+9)],fill=HEADC,close=True,sw=2.5)
s.line(*P(50,TY+0.8),*P(50,TY+4),stroke=INK,sw=1.5)
# pinch roller pressing the tape against the capstan
s.circle(*P(74.8,TY+3.6),round(3.4*K,1),fill=RUBBER,stroke=INK,sw=2)
s.circle(*P(74.8,TY+3.6),round(1.0*K,1),fill=HEADC,stroke=INK,sw=1.5)
# direction of travel
s.arrow(*P(30,TY+5.5),*P(40,TY+5.5))
s.text(P(50,TY+13)[0],P(50,TY+13)[1]+6,"the player's head",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= callouts =================
s.callout(1,*P(15,TY),130,700,"Plastic tape coated with|iron oxide, 3.8 mm wide")
s.callout(2,*P(HR+4.5,HY-4),830,340,"Two hubs: the tape winds|from one to the other")
s.callout(3,*P(52,58.7),830,470,"A felt pad on a spring|holds the tape to the head")
s.callout(4,*P(76.5,TY+6),830,660,"Capstan and roller pull the|tape at 4.75 cm a second")
s.callout(5,*P(92,1.5),830,215,"Break off a tab, and|that side cannot be erased")
s.save(os.path.join(os.path.dirname(__file__),"..","99-cassette-tape","cassette-tape"))
