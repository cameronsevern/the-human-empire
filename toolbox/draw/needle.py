import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The needle","about 40,000 years ago")
# needle: point at P, head at Q
P=(150,610); Q=(760,300)
dx,dy=Q[0]-P[0],Q[1]-P[1]; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L; nx,ny=-uy,ux
def at(t,w): return (P[0]+ux*L*t+nx*w, P[1]+uy*L*t+ny*w)
up=[at(t/20,(3+15*min(1,(t/20)*1.6))) for t in range(0,21)]
dn=[at(t/20,-(3+15*min(1,(t/20)*1.6))) for t in range(20,-1,-1)]
head=[at(1.02,12),at(1.035,0),at(1.02,-12)]
s.path([P]+up+head+dn,fill=BONE,close=True)
ex,ey=at(0.94,0)
ang=math.degrees(math.atan2(uy,ux))
s.ellipse(round(ex,1),round(ey,1),22,7,fill=PAPER,stroke=ACC,sw=5,rot=round(ang,1))
# thread through the eye
s.raw_path(f"M {ex-6:.0f},{ey+2:.0f} C {ex+40:.0f},{ey+90:.0f} {ex-80:.0f},{ey+150:.0f} {ex-10:.0f},{ey+230:.0f} S {ex+120:.0f},{ey+300:.0f} {ex+60:.0f},{ey+390:.0f}",stroke=INK,sw=2.5)
s.raw_path(f"M {ex+6:.0f},{ey-2:.0f} C {ex+60:.0f},{ey-40:.0f} {ex+110:.0f},{ey-10:.0f} {ex+150:.0f},{ey-60:.0f}",stroke=INK,sw=2.5)
mx,my=at(0.45,0)
s.callout(1,round(mx),round(my),90,250,"A splinter of bone,|ground smooth on|a stone")
s.callout(2,round(ex),round(ey-8),520,170,"The eye, bored with|a point of flint")
s.callout(3,round(ex-22),round(ey+215),470,640,"Thread of animal|sinew")
# inset: a seam
ix,iy,r=985,400,165
s.inset(ix,iy,r,"A sewn seam")
s.add(f'<clipPath id="c"><circle cx="{ix}" cy="{iy}" r="{r-3}"/></clipPath><g clip-path="url(#c)">')
s.raw_path(f"M {ix-200},{iy-200} L {ix+30},{iy-200} C {ix+10},{iy-80} {ix+45},{iy+60} {ix+20},{iy+200} L {ix-200},{iy+200} Z",fill=HIDE,sw=2.5)
s.raw_path(f"M {ix+200},{iy-200} L {ix-25},{iy-200} C {ix-45},{iy-80} {ix-10},{iy+60} {ix-35},{iy+200} L {ix+200},{iy+200} Z",fill="#cfae88",sw=2.5)
for k in range(-5,6):
    y=iy+k*30; xo=ix+2+8*math.sin(k/1.7)
    s.line(round(xo-26,1),y-7,round(xo+26,1),y+7,stroke=ACC,sw=5)
s.add('</g>')
s.callout(4,ix+12,iy+52,1085,640,"Stitches pull two|skins tight, so no|wind gets through",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","02-needle","needle"))
