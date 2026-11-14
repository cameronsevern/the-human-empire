import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The qanat","about 3,000 years ago")
EARTH="#efe3cc"; WET="#cfdde0"; WATER="#9fbccb"; GREEN="#8a9a6a"
def surf(x):
    if x<120: return 190+(x-14)*40/106
    if x<905: return 230+(x-120)*290/785
    return 520+(x-905)*8/280
def tun(x): return 470+(x-200)*50/705
# earth
pts=[(14,surf(14)),(120,surf(120)),(905,surf(905)),(1186,surf(1186)),(1186,746),(14,746)]
s.path(pts,fill=EARTH,sw=0,close=True)
# water-bearing gravel under the hills (below the water table)
s.path([(14,400),(470,tun(470)-8),(470,tun(470)+26),(14,620)],fill=WET,sw=0,close=True)
s.line(14,400,470,tun(470)-8,stroke=WATER,sw=3,dash="12 7")
# surface
s.path([(14,surf(14)),(120,surf(120)),(905,surf(905)),(1186,surf(1186))],sw=3)
# tunnel (accent) with water
s.path([(185,tun(200)-14),(905,tun(905)-14),(905,tun(905)+6),(185,tun(200)+6)],fill=WATER,stroke=ACC,sw=3.5,close=True)
# shafts, with a ring of spoil at each mouth
for x in range(200,900,100):
    y0=surf(x)
    s.path([(x-9,y0),(x-9,tun(x)-14),(x+9,tun(x)-14),(x+9,y0)],fill=PAPER,sw=2.5)
    s.raw_path(f"M {x-34},{y0+ -2+ (x-34-x)*0.37:.1f} Q {x-20},{y0-22:.1f} {x-9},{y0-4:.1f}",fill=EARTH,sw=2.5)
    s.raw_path(f"M {x+9},{y0+4:.1f} Q {x+22},{y0-10:.1f} {x+34},{y0+12:.1f}",fill=EARTH,sw=2.5)
# outlet, channel and fields
s.raw_path(f"M 905,{tun(905)-4:.1f} L 1186,{surf(1186)+4:.1f}",stroke=WATER,sw=7)
for x in range(960,1170,26):
    y=surf(x)
    s.line(x,y-2,x,y-26,stroke=GREEN,sw=3); s.line(x,y-14,x-8,y-26,stroke=GREEN,sw=3); s.line(x,y-14,x+8,y-26,stroke=GREEN,sw=3)
s.callout(1,200,360,400,150,"The mother well, sunk|down to the buried water")
s.callout(2,500,surf(500)+40,640,235,"A shaft every thirty metres|or so, for air and for|lifting out the earth")
s.callout(3,650,tun(650)-4,520,640,"The tunnel slopes very gently,|about a metre in a kilometre",halo=EARTH)
s.callout(4,110,470,60,640,"Water seeps in from the wet|gravel under the hills",halo=EARTH)
s.callout(5,935,tun(905)+2,900,370,"The water runs out|onto the plain and|into the fields")
s.save(os.path.join(os.path.dirname(__file__),"..","13-qanat","qanat"))
