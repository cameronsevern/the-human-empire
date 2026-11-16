import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The separate condenser","James Watt, 1765; patented 1769")
IRON="#7d8488"; WATER="#9fc2cf"; HOT="#efcfb4"; STEAM="#f6f1ea"; COPPER="#c98a5a"; BRICK="#d7a17e"
G=710

# ================= Watt's arrangement =================
CL,CR,CT,CB=230,370,230,500          # the cylinder
# the steam jacket round it, kept full of steam
s.path([(CL-26,CT-24),(CR+26,CT-24),(CR+26,CB+24),(CL-26,CB+24)],fill=HOT,close=True,sw=3)
for y in range(CT,CB+1,40):
    s.raw_path(f"M {CL-20},{y} c 4,-8 8,8 12,0",stroke="#c98a5a",sw=1.5)
    s.raw_path(f"M {CR+8},{y} c 4,-8 8,8 12,0",stroke="#c98a5a",sw=1.5)
s.path([(CL,CT),(CR,CT),(CR,CB),(CL,CB)],fill=STEAM,close=True,sw=3)
PY=330
s.path([(CL+2,PY),(CR-2,PY),(CR-2,PY+22),(CL+2,PY+22)],fill=IRON,close=True,sw=2.5)      # piston
s.line((CL+CR)/2,PY,(CL+CR)/2,140,stroke=INK,sw=6)                                    # piston rod, through the closed top
s.path([((CL+CR)/2-14,CT-24),((CL+CR)/2+14,CT-24),((CL+CR)/2+14,CT-44),((CL+CR)/2-14,CT-44)],fill=METAL,close=True,sw=2)
# steam in from the boiler at the top
s.raw_path(f"M 80,{CT+10} L {CL-26},{CT+10}",stroke=IRON,sw=10)
s.arrow(100,CT-14,170,CT-14)
s.text(80,CT+50,"from the|boiler",italic=True,fill=SOFT)
# out at the bottom, through a valve, down to the condenser
EX=(CL+CR)/2
s.raw_path(f"M {EX},{CB+24} L {EX},{620} L 500,620",stroke=IRON,sw=12)
s.circle(EX,CB+52,9,fill=METAL,sw=2)
s.arrow(EX+40,620-26,EX+120,620-26)
# the cold-water cistern, with the condenser and the air pump standing in it
s.path([(450,520),(800,520),(800,G),(450,G)],fill=WATER,close=True,sw=3)
for y in (545,600,655): s.raw_path(f"M 460,{y} c 20,-6 40,6 60,0 c 20,-6 40,6 60,0",stroke="#7aa6b6",sw=1.5)
s.path([(500,560),(570,560),(570,690),(500,690)],fill=ACC,close=True,sw=3)            # the condenser
for y in (590,620,650): s.raw_path(f"M 512,{y} c 8,-6 16,6 24,0 c 8,-6 16,6 24,0",stroke="#f0d2c6",sw=1.5)
# the air pump: a small pump that draws off the water and air from the condenser
AL,AR,AT=640,710,470
s.path([(AL,AT),(AR,AT),(AR,690),(AL,690)],fill=METAL,close=True,sw=3)
s.path([(AL+3,600),(AR-3,600),(AR-3,616),(AL+3,616)],fill=IRON,close=True,sw=2)
s.line((AL+AR)/2,600,(AL+AR)/2,380,stroke=INK,sw=5)
s.raw_path(f"M 570,680 L {AL},680",stroke=IRON,sw=8)

# ================= Newcomen's way, for comparison =================
NX,NY,NR=1015,245,118
s.inset(NX,NY,NR)
s.text(NX,NY-NR-14,"Newcomen's way",anchor="middle",italic=True)
nl,nr,nt,nb=NX-34,NX+34,NY-70,NY+40
s.path([(nl,nt),(nr,nt),(nr,nb),(nl,nb)],fill="#dfe6e8",close=True,sw=2.5)
s.path([(nl+2,NY-40),(nr-2,NY-40),(nr-2,NY-28),(nl+2,NY-28)],fill=IRON,close=True,sw=2)
s.line(NX,NY-40,NX,NY-NR+6,stroke=INK,sw=4)
s.raw_path(f"M {NX-70},{nb+60} L {NX-70},{nb+30} C {NX-70},{nb+6} {NX+70},{nb+6} {NX+70},{nb+30} L {NX+70},{nb+60} Z",fill=COPPER,sw=2.5)
s.raw_path(f"M {nr+40},{NY-90} L {nr+40},{nb-14} L {nr},{nb-14}",stroke=IRON,sw=5)
for dx,dy in ((-30,-30),(-40,-14),(-22,-44)):
    s.line(nr-4,nb-14,nr-4+dx,nb-14+dy,stroke="#5f8fa0",sw=2.5)

s.callout(1,CR+14,300,420,150,"The cylinder stays hot,|wrapped in steam")
s.callout(2,535,600,830,470,"Steam rushes out to|a cold condenser")
s.callout(3,770,560,830,560,"The condenser stands|in cold water")
s.callout(4,(AL+AR)/2,640,830,650,"An air pump draws off|the water and air")
s.callout(5,nr-24,nb-34,880,410,"Newcomen cooled the|cylinder itself")
s.save(os.path.join(os.path.dirname(__file__),"..","61-separate-condenser","separate-condenser"))
