import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The gas mask","The British small box respirator, 1916")
KHAKI="#9c8f6a"; RUBBER="#3f3a36"; TIN="#b9c0c4"; BRASS="#c9a55a"; CHAR="#5b5752"; CANVAS="#c8b98f"; GLASS="#dfe7ea"

# ================= the soldier, in profile, facing right =================
s.path([(170,700),(190,560),(250,520),(330,505),(420,520),(460,560),(470,700)],fill="#e9e2d4",stroke=SOFT,sw=4)   # shoulders and chest
s.path([(285,470),(285,515),(345,515),(345,460)],fill="#e9e2d4",stroke=SOFT,sw=4)                                 # neck
s.circle(300,320,105,fill="#e9e2d4",stroke=SOFT,sw=4)                                                               # head
s.raw_path("M 205,300 C 205,215 260,190 300,190 C 360,190 395,220 405,262",fill="#7d7a5c",stroke=SOFT,sw=4)        # steel helmet brim line
s.path([(196,268),(420,262)],stroke=SOFT,sw=6)
# the facepiece: rubberised cloth over the whole face
s.raw_path("M 330,262 C 380,262 412,275 418,300 C 425,340 420,390 402,425 C 385,450 350,452 330,440 C 336,400 336,300 330,262 Z",fill=KHAKI,sw=3)
s.circle(385,300,20,fill=GLASS,stroke=INK,sw=3)                       # eyepiece in a metal rim
s.path([(408,318),(424,326),(424,338),(408,338)],fill=RUBBER,close=True,sw=2)    # nose clip, through the cloth
s.path([(400,362),(420,362),(420,382),(400,382)],fill=RUBBER,close=True,sw=2)    # mouthpiece behind the cloth
# brass tube out through the chin, with the flutter valve below
s.path([(404,380),(440,415),(440,440)],stroke=BRASS,sw=12)
s.path([(432,440),(448,440),(450,478),(430,478)],fill=RUBBER,close=True,sw=2)    # flutter valve
# hose down to the haversack on the chest
s.raw_path("M 440,420 C 500,430 480,520 400,560",stroke="#6e6656",sw=16)
for k in range(9):
    u=k/8; x=(1-u)**3*440+3*(1-u)**2*u*500+3*(1-u)*u*u*480+u**3*400
    y=(1-u)**3*420+3*(1-u)**2*u*430+3*(1-u)*u*u*520+u**3*560
    s.circle(round(x,1),round(y,1),3,fill=INK,sw=0)
s.path([(250,550),(420,550),(420,670),(250,670)],fill=CANVAS,close=True,sw=3)     # haversack
s.line(250,580,420,580,sw=2)
s.text(330,725,"worn, with the box in a bag on the chest",anchor="middle",italic=True,fill=SOFT,size=18)

# ================= the box, cut open =================
BX0,BX1,BY0,BY1=900,1090,250,640
s.raw_path(f"M {BX0},{BY0+20} Q {BX0},{BY0} {BX0+20},{BY0} L {BX1-20},{BY0} Q {BX1},{BY0} {BX1},{BY0+20} L {BX1},{BY1-20} Q {BX1},{BY1} {BX1-20},{BY1} L {BX0+20},{BY1} Q {BX0},{BY1} {BX0},{BY1-20} Z",fill=TIN,sw=3)
def layer(y0,y1,fill,dots):
    s.path([(BX0+12,y0),(BX1-12,y0),(BX1-12,y1),(BX0+12,y1)],fill=fill,close=True,sw=2)
    for i in range(int((BX1-BX0-40)/22)):
        for j in range(int((y1-y0-10)/20)):
            s.circle(BX0+26+i*22+(j%2)*11,y0+14+j*20,4,fill=dots,sw=0)
layer(300,390,CHAR,"#3a3632")          # charcoal
layer(390,500,ACC,"#8e3b28")           # chemical granules
layer(500,580,CHAR,"#3a3632")          # charcoal
for y in (300,500,580): s.line(BX0+12,y,BX1-12,y,stroke="#e8e8e8",sw=3,dash="4 4")   # gauze
s.path([(985,BY0-34),(1005,BY0-34),(1005,BY0),(985,BY0)],fill=BRASS,close=True,sw=2)  # outlet to the hose
s.circle(995,BY1+2,9,fill=RUBBER,sw=2)                                                # inlet valve
s.arrow(995,705,995,BY1+18)
s.arrow(995,BY0-40,995,BY0-80)
s.text(1015,700,"air in",anchor="start",italic=True,fill=SOFT,size=18)
s.text(1015,205,"to the hose",anchor="start",italic=True,fill=SOFT,size=18)
s.text(995,150,"the box, cut open",anchor="middle",italic=True,fill=SOFT,size=18)

s.callout(1,416,330,560,215,"A clip pinches|the nose shut")
s.callout(2,410,372,560,330,"Air comes in through|a mouthpiece in the teeth")
s.callout(3,440,470,560,455,"Breath goes out|by a rubber flap")
s.callout(4,448,523,560,580,"A hose from a tin|box on the chest")
s.callout(5,BX0+40,445,860,690,"Layers of charcoal and lime|take the gas out of the air",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","72-gas-mask","gas-mask"))
