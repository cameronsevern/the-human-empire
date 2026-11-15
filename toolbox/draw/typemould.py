import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The type mould","Mainz, by about 1450")
STEEL="#b9c0c4"; COPPER="#c98a5a"; LEAD="#aeb3b6"; MOLTEN="#e8b04a"; WOODD="#b08a5e"
def glyph(x,y,ch,size,flip=False,fill=INK):
    tr=f' transform="translate({2*x},0) scale(-1,1)"' if flip else ""
    s.add(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" font-weight="bold" fill="{fill}"{tr}>{ch}</text>')
# ---- 1. the punch: a steel rod, the letter cut on its tip back to front
PX=130
s.path([(PX-20,190),(PX+20,190),(PX+20,410),(PX+14,440),(PX-14,440),(PX-20,410)],fill=STEEL,close=True,sw=3)
s.line(PX-20,206,PX+20,206,stroke=SOFT,sw=1.5)
glyph(PX,432,"a",26,flip=True)
s.arrow(PX,452,PX,500)
# ---- 2. the matrix: a copper bar with the letter struck into it
s.path([(PX-62,512),(PX+62,512),(PX+62,552),(PX-62,552)],fill=COPPER,close=True,sw=3)
s.path([(PX-14,512),(PX+14,512),(PX+12,524),(PX-12,524)],fill="#8f5a35",close=True,sw=1.5)
s.raw_path(f"M {PX+70},532 C 240,560 300,560 370,520",stroke=INK,sw=2.5)
s.arrow(352,532,372,518)
# ---- 3. the mould, cut open from the front: two halves, a channel between, the matrix closing the bottom
CL,CR,TOP,BOT=566,604,262,500
s.path([(380,230),(430,230),(430,560),(380,560)],fill=WOODD,close=True,sw=2.5)        # wooden grips
s.path([(740,230),(790,230),(790,560),(740,560)],fill=WOODD,close=True,sw=2.5)
s.path([(430,230),(530,230),(CL,TOP),(CL,BOT),(430,BOT)],fill=ACC,close=True,sw=3)      # left half
s.path([(430,BOT),(CL-30,BOT),(CL-30,BOT+60),(430,BOT+60)],fill=ACC,close=True,sw=3)
s.path([(740,230),(640,230),(CR,TOP),(CR,BOT),(740,BOT)],fill=ACC,close=True,sw=3)      # right half
s.path([(740,BOT),(CR+30,BOT),(CR+30,BOT+60),(740,BOT+60)],fill=ACC,close=True,sw=3)
# the matrix, clamped across the bottom of the channel, its letter facing up
s.path([(CL-30,BOT),(CR+30,BOT),(CR+30,BOT+40),(CL-30,BOT+40)],fill=COPPER,close=True,sw=2.5)
# the channel, filling with metal
s.path([(CL,TOP+30),(CR,TOP+30),(CR,BOT),(CL,BOT)],fill=MOLTEN,close=True,sw=2)
# the ladle pouring into the mouth
s.raw_path("M 560,196 C 556,170 600,164 610,180 L 616,196 Z",fill=STEEL,sw=2.5)
s.line(560,182,452,112,stroke=INK,sw=6); s.line(560,182,452,112,stroke=STEEL,sw=3)
s.raw_path("M 600,196 C 598,214 588,236 585,292",stroke=MOLTEN,sw=6)
# the halves slide sideways: closer for a narrow letter, wider for a broad one
s.arrow(520,604,470,604); s.arrow(650,604,700,604)
# ---- 5. two cast letters, the same height, different widths
GY,TY=590,330
for (x,w,ch) in ((900,44,"i"),(1050,124,"m")):
    s.path([(x-w/2,TY),(x+w/2,TY),(x+w/2,GY),(x-w/2,GY)],fill=LEAD,close=True,sw=3)
    s.path([(x-w/2,TY),(x-w/2+20,TY-26),(x+w/2+20,TY-26),(x+w/2,TY)],fill="#c8ccce",close=True,sw=2.5)
    s.line(x-w/2,GY-60,x+w/2,GY-60,stroke=SOFT,sw=2)                                  # the nick
    glyph(x+10,TY-6,ch,24,flip=True)
s.line(860,TY-34,1140,TY-34,stroke=SOFT,sw=1.5,dash="6 6")
s.line(860,GY,1130,GY,stroke=SOFT,sw=1.5)
# ---- labels
s.callout(1,PX+20,300,240,170,"The punch: steel, the|letter cut back to front")
s.callout(2,PX-40,540,110,680,"The matrix: copper, with|the letter struck into it")
s.callout(3,470,380,560,680,"Two halves slide: close|for an i, apart for an m")
s.callout(4,585,262,790,150,"Molten metal poured|into the mouth")
s.callout(5,1050,460,1160,680,"The same height,|whatever the width",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","45-type-mould","type-mould"))
