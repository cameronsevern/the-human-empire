import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The tank","The British Mark I, 1916")
HULL="#8c8a6c"; DARK="#4b4f52"; EARTH="#a88a66"; GROUND=560

# ================= the ground and the trench =================
s.line(60,GROUND,470,GROUND,stroke=SOFT,sw=1.5)
s.line(650,GROUND,1150,GROUND,stroke=SOFT,sw=1.5)
s.path([(470,GROUND),(478,680),(642,680),(650,GROUND)],fill="#cdb594",stroke=SOFT,sw=2)
s.text(560,718,"crossing a trench 2.4 metres wide",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the steering tail =================
s.path([(310,470),(180,515)],stroke=DARK,sw=8)
s.path([(330,505),(180,522)],stroke=DARK,sw=6)
s.circle(175,522,38,fill="#a7a093",stroke=INK,sw=3)
s.circle(175,522,8,fill=DARK,sw=0)

# ================= the hull, wrapped in its track =================
outer=[(300,372),(820,372),(852,380),(866,400),(860,420),(700,GROUND),(400,GROUND),(258,440),(262,400),(278,380)]
s.path(outer,fill=ACC,close=True,sw=3)
# track shoes, as short cross lines along the band
def shoes(a,b,n):
    for k in range(n+1):
        u=k/n; x=a[0]+(b[0]-a[0])*u; y=a[1]+(b[1]-a[1])*u
        dx,dy=b[0]-a[0],b[1]-a[1]; L=math.hypot(dx,dy); nx,ny=-dy/L,dx/L
        s.line(round(x,1),round(y,1),round(x+nx*20,1),round(y+ny*20,1),stroke="#7a3424",sw=2)
shoes((300,372),(820,372),21); shoes((700,GROUND),(400,GROUND),12); shoes((860,420),(700,GROUND),8); shoes((400,GROUND),(258,440),7)
inner=[(305,394),(815,394),(836,400),(842,412),(690,538),(410,538),(284,440),(285,410),(292,398)]
s.path(inner,fill=HULL,close=True,sw=2.5)
for x in range(320,800,40):
    s.circle(x,404,2.5,fill=INK,sw=0)
for x in range(440,690,40):
    s.circle(x,528,2.5,fill=INK,sw=0)
for x in (430,620):
    s.line(x,400,x,532,stroke="#6c6a52",sw=2)
# road wheels seen through the gap are hidden; the sponson stands out from the side
s.path([(470,425),(620,425),(640,445),(640,505),(470,505)],fill="#7c7a5e",close=True,sw=3)
s.path([(640,456),(720,456),(720,468),(640,468)],fill=DARK,close=True,sw=2)        # six-pounder barrel
s.circle(505,465,9,fill=DARK,sw=1.5)                                              # sponson door / vision port
# driver's cab on the roof at the front
s.path([(690,372),(690,345),(780,345),(790,372)],fill=HULL,close=True,sw=2.5)
s.line(710,358,770,358,stroke=INK,sw=3)

s.callout(1,560,549,880,640,"Tracks run right|round the hull")
s.callout(2,858,395,990,250,"The high nose climbs|a trench wall",anchor="end")
s.callout(3,700,462,560,240,"A gun in a box|on each side",anchor="end")
s.callout(4,360,470,110,250,"Riveted steel,|6 to 12 mm thick")
s.callout(5,175,522,110,650,"Two wheels behind|help it turn")
s.save(os.path.join(os.path.dirname(__file__),"..","72-tank","tank"))
