import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
SUN="#e3b23c"
s=Sheet("The shadow stick","about 2,250 years ago")
# The Earth is a big arc; the angle between the towns is drawn at 20 degrees (really 7.2) so it can be seen.
cx,cy,R,L=760,1500,1000,150
TH=math.radians(20)
def pt(a,r): return (cx-r*math.sin(a), cy-r*math.cos(a))   # a measured from straight up, towards the left
def ground(x): return cy-math.sqrt(R*R-(x-cx)**2)
s.add('<clipPath id="f"><rect x="15" y="15" width="1170" height="730"/></clipPath>')
s.add(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{CLAY}" stroke="{INK}" stroke-width="3" clip-path="url(#f)"/>')
sy=pt(0,R); sy_top=pt(0,R+L); al=pt(TH,R); al_top=pt(TH,R+L)
sh=(al_top[0],ground(al_top[0]))
# parallel rays of sunlight
for x in (500,630,890,1020,1130):
    s.line(x,215,x,ground(x)-4,stroke=SUN,sw=3)
s.line(sy_top[0],215,sy_top[0],sy_top[1]-8,stroke=SUN,sw=4)
s.line(sh[0],215,sh[0],sh[1]-3,stroke=SUN,sw=4)
# sticks: Syene plain, Alexandria accented
s.line(sy[0],sy[1],sy_top[0],sy_top[1],stroke=INK,sw=9)
s.line(al[0],al[1],al_top[0],al_top[1],stroke=ACC,sw=9)
# the shadow at Alexandria
s.line(al[0],al[1],sh[0],sh[1],stroke=INK,sw=8)
# the angle at the tip of the Alexandria stick
r=95; e=(al_top[0]+r*math.sin(TH), al_top[1]+r*math.cos(TH))
s.raw_path(f"M {al_top[0]:.1f},{al_top[1]+r:.1f} A {r},{r} 0 0 0 {e[0]:.1f},{e[1]:.1f}",sw=2.5)
# the distance between the towns, a dotted arc just under the surface
m0=pt(TH-0.012,R-16); m1=pt(0.012,R-16)
s.raw_path(f"M {m0[0]:.1f},{m0[1]:.1f} A {R-16},{R-16} 0 0 1 {m1[0]:.1f},{m1[1]:.1f}",sw=2.5,extra='stroke-dasharray="3 7"')
mid=pt(TH/2,R-16)
s.text(sy[0]-22,sy[1]+62,"Syene",size=22,italic=True,anchor="end",halo=CLAY)
s.text(al[0]-8,al[1]+92,"Alexandria",size=22,italic=True,anchor="end",halo=CLAY)
s.callout(1,630,270,800,150,"Sunlight reaches the Earth|in parallel rays")
s.callout(2,sy[0]+3,sy[1]-3,880,650,"At Syene the noon sun|is overhead, and a|stick casts no shadow",halo=CLAY)
s.callout(3,(al[0]+sh[0])/2-6,(al[1]+sh[1])/2+2,330,520,"At Alexandria a stick|casts a short shadow",anchor="end")
s.callout(4,al_top[0]+12,al_top[1]+r-2,330,290,"The stick meets the|sunlight at one fiftieth|of a circle",anchor="end")
s.callout(5,mid[0],mid[1],440,690,"The towns are 5,000 stades apart, so|the Earth is fifty times that around",halo=CLAY)
s.save(os.path.join(os.path.dirname(__file__),"..","19-shadow-stick","shadow-stick"))
