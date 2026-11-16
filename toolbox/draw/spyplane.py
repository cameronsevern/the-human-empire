import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The spy plane","The Lockheed U-2, seen from above, with its camera bay, 1950s")
SKIN="#6f7477"; SKIN2="#5c6164"; GLASSC="#a9c3cc"; FILM="#d8c9a3"; DARK="#2f3437"

K=29.0                      # pixels per metre
CX=470; NY=200              # centre line, and the tip of the nose
def P(xm,ym): return (round(CX+xm*K,1),round(NY+ym*K,1))   # xm across, ym back from the nose

# ================= the wings: 24 metres from tip to tip, long and narrow like a glider's =================
LE,ROOT,TIP=6.2,3.6,1.3
for sg in (1,-1):
    s.path([P(sg*0.6,LE),P(sg*12.2,LE+0.9),P(sg*12.2,LE+0.9+TIP),P(sg*0.6,LE+ROOT)],fill=SKIN,close=True,sw=3)
    s.path([P(sg*12.0,LE+0.9),P(sg*12.4,LE+0.9),P(sg*12.4,LE+0.9+TIP),P(sg*12.0,LE+0.9+TIP)],fill=DARK,close=True,sw=1.5)  # wingtip skid
# ================= the tailplane =================
for sg in (1,-1):
    s.path([P(sg*0.4,13.0),P(sg*3.8,13.5),P(sg*3.8,14.3),P(sg*0.4,14.6)],fill=SKIN,close=True,sw=2.5)
# ================= the fuselage =================
body=[P(0,0),P(0.45,0.6),P(0.75,2.0),P(0.8,9.0),P(0.55,14.4),P(0.35,15.1),P(-0.35,15.1),P(-0.55,14.4),P(-0.8,9.0),P(-0.75,2.0),P(-0.45,0.6)]
s.path(body,fill=SKIN,close=True,sw=3)
s.path([P(0,1.5),P(0.4,2.0),P(0.4,3.1),P(0,3.4),P(-0.4,3.1),P(-0.4,2.0)],fill=GLASSC,close=True,sw=2)   # canopy
s.line(*P(0,13.0),*P(0,15.0),stroke=DARK,sw=4)                                                       # the fin, edge on
for sg in (1,-1):
    s.path([P(sg*0.8,4.4),P(sg*1.15,4.9),P(sg*1.15,5.9),P(sg*0.8,6.2)],fill=SKIN2,close=True,sw=2)   # air intakes
# the camera bay, behind the cockpit, with its hatch outlined
QY0,QY1=3.7,5.6
s.path([P(-0.62,QY0),P(0.62,QY0),P(0.62,QY1),P(-0.62,QY1)],fill=ACC,close=True,sw=2)
# span arrow under the wing
s.line(*P(-12.2,LE+3.7),*P(12.2,LE+3.7),stroke=SOFT,sw=1.5)
for sg in (1,-1): s.line(*P(sg*12.2,LE+3.3),*P(sg*12.2,LE+4.1),stroke=SOFT,sw=1.5)
s.text(CX-200,NY+(LE+3.7)*K+28,"24 metres",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the inset: the camera bay, cut across and seen from behind =================
IX,IY,IR=985,430,135
s.inset(IX,IY,IR)
s.text(IX-60,IY+IR+40,"the camera, from behind",anchor="middle",italic=True)
s.circle(IX,IY-10,92,fill="#d9dcdd",sw=2.5)                 # the fuselage cut across
# the fan of seven views down through the belly windows
for k in range(-3,4):
    a=math.radians(90+k*19)
    s.line(IX,IY+20,round(IX+120*math.cos(a),1),round(IY+20+120*math.sin(a),1),stroke=SOFT,sw=1.2,dash="5 5")
# two film reels, one each side
for sg in (1,-1):
    s.circle(IX+sg*52,IY-40,26,fill=FILM,sw=2); s.circle(IX+sg*52,IY-40,7,fill=DARK,sw=1)
# the lens barrel, pointing down and to one side
a=math.radians(90-19)
bx,by=IX+52*math.cos(a),IY+20+52*math.sin(a)
s.path([(IX-16,IY-10),(IX+16,IY-10),(round(bx+14,1),round(by,1)),(round(bx-14,1),round(by,1))],fill=ACC,close=True,sw=2.5)
s.circle(IX,IY-6,20,fill=ACC,sw=2.5)

s.callout(1,IX+14,IY+40,1150,690,"A 91 cm lens swings|from side to side",anchor="end")
s.callout(2,IX-52,IY-40,800,180,"Two reels of film, wound|opposite ways for balance")
s.callout(3,*P(-11.5,LE+1.5),110,700,"Wings like a glider's")
s.callout(4,*P(0,4.6),330,330,"The camera bay,|behind the cockpit",anchor="end")
s.callout(5,*P(0.95,5.4),620,700,"Air intakes for|one jet engine")
s.save(os.path.join(os.path.dirname(__file__),"..","92-spy-plane","spy-plane"))
