import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The begging bowl","about 2,500 years ago")
ROBE="#d6a56a"; RICE="#f4efe2"; DARK="#5a4a40"; CLOTH="#b9c49a"
GROUND=650
s.line(60,GROUND,720,GROUND,stroke=SOFT,sw=1.5)
# --- the monk, standing in profile facing right, the bowl held in both hands ---
MX=250
s.circle(MX+6,262,30,fill=BONE,sw=3)                                   # shaven head
s.raw_path(f"M {MX-30},{300} C {MX-58},{380} {MX-66},{520} {MX-60},{644} L {MX+58},{644} C {MX+62},{540} {MX+56},{400} {MX+34},{300} C {MX+12},{290} {MX-10},{290} {MX-30},{300} Z",fill=ROBE,sw=3)
s.raw_path(f"M {MX-28},{304} C {MX-10},{380} {MX+20},{460} {MX+56},{520}",sw=2)
for x in (MX-30,MX-10,MX+12,MX+34):
    s.line(x,560,x+4,640,stroke=DARK,sw=1.2)
# forearms forward to the bowl
s.raw_path(f"M {MX+20},{350} C {MX+30},{400} {MX+60},{430} {MX+96},{432}",stroke=INK,sw=16); s.raw_path(f"M {MX+20},{350} C {MX+30},{400} {MX+60},{430} {MX+96},{432}",stroke=ROBE,sw=11)
BX,BY=MX+130,422
s.raw_path(f"M {BX-44},{BY} C {BX-42},{BY+42} {BX+42},{BY+42} {BX+44},{BY} Z",fill=ACC,sw=3)
s.ellipse(BX,BY,44,8,fill=DARK,sw=2.5)
# --- the giver, kneeling in profile facing left, ladling food in ---
GX=540
s.circle(GX-4,400,28,fill=BONE,sw=3)
s.path([(GX-26,436),(GX+26,436),(GX+34,600),(GX+40,646),(GX-112,646),(GX-116,604),(GX-30,598)],fill=CLOTH,close=True,sw=3)
s.line(GX-30,598,GX+34,600,sw=1.5)
s.raw_path(f"M {GX-20},{460} C {GX-50},{470} {GX-80},{460} {GX-100},{440}",stroke=INK,sw=14); s.raw_path(f"M {GX-20},{460} C {GX-50},{470} {GX-80},{460} {GX-100},{440}",stroke=CLOTH,sw=9)
s.line(GX-100,440,BX+20,BY-24,sw=4)
s.raw_path(f"M {BX-4},{BY-30} C {BX-4},{BY-12} {BX+26},{BY-12} {BX+26},{BY-30} Z",fill=WOOD,sw=2.5)
s.ellipse(BX+11,BY-36,6,4,fill=RICE,sw=1.2)
# a pot of food beside the giver
PX=GX+170
s.raw_path(f"M {PX-20},{646} C {PX-62},{646} {PX-62},{576} {PX-30},{570} L {PX+30},{570} C {PX+62},{576} {PX+62},{646} {PX+20},{646} Z",fill=CLAY,sw=3)
s.ellipse(PX,570,34,7,fill=DARK,sw=2)
# --- inset: the bowl, cut through ---
ix,iy,r=960,300,160
s.inset(ix,iy,r)
s.text(ix,iy+r+40,"The bowl, cut through",anchor="middle",italic=True)
# hollow of the bowl, then the food heaped in it
s.raw_path(f"M {ix-108},{iy-6} C {ix-104},{iy+92} {ix+104},{iy+92} {ix+108},{iy-6} Z",fill="#ffffff",sw=0)
s.raw_path(f"M {ix-100},{iy+20} C {ix-90},{iy-50} {ix+90},{iy-50} {ix+100},{iy+20} C {ix+80},{iy+80} {ix-80},{iy+80} {ix-100},{iy+20} Z",fill=RICE,sw=2.5)
for (x,y,c) in ((ix-46,iy-6,"#7f9a55"),(ix+18,iy-16,"#b0773f"),(ix+58,iy+4,"#d8b74a"),(ix-8,iy+16,"#7f9a55"),(ix-60,iy+28,"#b0773f")):
    s.ellipse(x,y,13,8,fill=c,sw=1.5)
# the bowl's wall: round-bottomed, with no foot
s.raw_path(f"M {ix-122},{iy-10} C {ix-120},{iy+110} {ix+120},{iy+110} {ix+122},{iy-10} L {ix+108},{iy-6} C {ix+104},{iy+92} {ix-104},{iy+92} {ix-108},{iy-6} Z",fill=ACC,sw=3)
# a mend: a crack stitched across
cx0,cy0=ix+92,iy+46
s.raw_path(f"M {cx0-4},{cy0-22} L {cx0+3},{cy0-8} L {cx0-3},{cy0+6} L {cx0+2},{cy0+18}",stroke=INK,sw=2)
for d in (-14,0,13):
    s.line(cx0-12,cy0+d-2,cx0+12,cy0+d+2,stroke=INK,sw=3.5)
s.callout(1,ix-112,iy+30,760,540,"Iron or baked clay,|never gold or silver")
s.callout(2,cx0+10,cy0+6,1150,620,"A crack is mended. Only|after five mends may he|ask for a new bowl",anchor="end")
s.callout(3,ix-46,iy-6,760,130,"Whatever is given|goes in together")
s.callout(4,MX-20,240,320,150,"The monk takes|what comes, and|eats before noon")
s.callout(5,GX-30,540,560,700,"The giver earns merit")
s.save(os.path.join(os.path.dirname(__file__),"..","26-begging-bowl","begging-bowl"))
