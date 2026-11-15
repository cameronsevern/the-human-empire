import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The stirrup","Asia, reaching Europe by about the 700s")
HORSE="#d9c4a2"; HFAR="#c9b18c"; MAIL="#c3c5c0"; TACK="#9b7653"
G=712; D=-70                                  # D shifts the horse and rider left
def P(pts): return [(x+D,y) for x,y in pts]
def M(d):                                     # shift every x in an "x,y" path string
    out=[]
    for tok in d.split():
        if "," in tok:
            x,y=tok.split(","); out.append(f"{float(x)+D:.0f},{y}")
        else: out.append(tok)
    return " ".join(out)
s.line(60,G,880,G,stroke=SOFT,sw=1.5)
def leg(top,knee,hoof,fill=HORSE,w=13):
    (xt,yt),(xk,yk),(xf,yf)=[(x+D,y) for x,y in (top,knee,hoof)]
    s.path([(xt-w-6,yt),(xk-w,yk),(xf-w+4,G-16),(xf+w-2,G-16),(xk+w,yk),(xt+w+8,yt)],fill=fill,close=True,sw=2.5)
    s.path([(xf-w+2,G-16),(xf+w,G-16),(xf+w+3,G),(xf-w-1,G)],fill=INK,close=True,sw=2)
# the lance runs on the far side of the head
s.line(380+D,334,1150+D,286,stroke=INK,sw=9); s.line(380+D,334,1150+D,286,stroke=WOOD,sw=5)
s.path(P([(1144,280),(1186,284),(1146,293)]),fill=METAL,close=True,sw=2.5)
# far legs
leg((470,530),(452,620),(462,0),fill=HFAR); leg((800,530),(812,620),(806,0),fill=HFAR)
# the horse: rump at the left, neck and head at the right
s.raw_path(M("M 455,385 C 520,372 590,392 640,394 C 700,396 760,380 790,360 C 820,330 850,290 880,262 "
             "C 892,248 910,240 925,246 C 950,262 985,300 1002,330 C 1008,344 996,356 982,352 "
             "C 960,346 935,330 915,322 C 895,340 875,380 865,420 C 858,470 845,520 815,545 "
             "C 760,560 560,566 480,550 C 440,540 420,500 418,460 C 416,420 430,392 455,385 Z"),fill=HORSE,sw=3)
s.circle(930+D,268,3.5,fill=INK,sw=0)
s.raw_path(M("M 900,250 L 896,226 L 912,244"),fill=HORSE,sw=2.5)                   # ear
s.raw_path(M("M 795,356 C 820,326 850,288 884,256"),stroke=SOFT,sw=2)            # mane
s.raw_path(M("M 422,410 C 392,430 380,500 392,590"),sw=7)                        # tail
leg((500,535),(488,622),(496,0)); leg((830,520),(842,622),(836,0))
# bridle and rein
s.raw_path(M("M 925,248 L 975,340 M 912,322 L 990,330"),stroke=TACK,sw=3)
s.raw_path(M("M 978,336 C 880,350 760,348 712,330"),stroke=TACK,sw=2.5)
# saddle cloth, then the high back (cantle) behind the rider
s.raw_path(M("M 545,392 C 600,402 690,402 730,390 L 722,450 C 680,462 590,462 552,452 Z"),fill="#c8a982",sw=2.5)
s.raw_path(M("M 560,398 L 548,330 C 552,318 572,316 578,328 L 594,398 Z"),fill=WOOD,sw=3)
# the rider, in soft grey
R=SOFT
s.raw_path(M("M 590,404 C 610,384 660,384 676,396 L 704,470 L 686,552 L 664,552 L 676,474 L 640,420 Z"),fill=MAIL,stroke=R,sw=3)
s.path(P([(658,552),(700,552),(716,566),(658,568)]),fill=TACK,close=True,stroke=R,sw=2.5)  # foot
s.raw_path(M("M 596,400 C 590,340 592,292 606,262 L 658,260 C 666,300 668,350 664,400 Z"),fill=MAIL,stroke=R,sw=3)
s.circle(632+D,234,24,fill=PAPER,stroke=R,sw=3)
s.raw_path(M("M 606,228 C 610,198 654,198 658,228 Z"),fill=METAL,stroke=R,sw=2.5)
s.raw_path(M("M 640,272 C 628,300 630,320 650,322 L 712,318"),stroke=R,sw=10)      # arm over the lance
# the high front (pommel), in front of the rider's thigh
s.raw_path(M("M 700,396 L 712,344 C 718,334 734,336 734,348 L 724,398 Z"),fill=WOOD,sw=3)
# the stirrup leather and the stirrup
s.line(640+D,410,676+D,526,stroke=TACK,sw=5)
s.raw_path(M("M 676,524 C 648,526 642,560 652,574 L 702,574 C 712,560 704,526 676,524 Z"),stroke=ACC,sw=6)
s.line(644+D,574,714+D,574,stroke=ACC,sw=8)
# inset: an early iron stirrup seen from the front
CX,CY,RR=1060,520,100
s.inset(CX,CY,RR)
# an Avar-style stirrup: a round iron ring with an eye for the strap and a flattened tread
s.path([(CX-12,CY-86),(CX+12,CY-86),(CX+10,CY-56),(CX-10,CY-56)],fill=ACC,close=True,sw=2.5)
s.ellipse(CX,CY-74,5,6,fill="#ffffff",sw=1.5)
s.raw_path(f"M {CX},{CY-58} C {CX+52},{CY-58} {CX+62},{CY+10} {CX+44},{CY+44} L {CX-44},{CY+44} C {CX-62},{CY+10} {CX-52},{CY-58} {CX},{CY-58} Z",fill=ACC,sw=3)
s.raw_path(f"M {CX},{CY-46} C {CX+40},{CY-46} {CX+48},{CY+8} {CX+34},{CY+32} L {CX-34},{CY+32} C {CX-48},{CY+8} {CX-40},{CY-46} {CX},{CY-46} Z",fill="#ffffff",sw=2.5)
s.path([(CX-50,CY+34),(CX+50,CY+34),(CX+46,CY+50),(CX-46,CY+50)],fill=ACC,close=True,sw=2.5)
s.callout(1,CX+30,CY+46,1110,680,"An iron ring, flattened|where the foot rests",anchor="end")
s.callout(2,664+D,480,250,560,"A leather strap|from the saddle",anchor="end")
s.callout(3,552+D,340,400,175,"A high back to brace him|when the lance strikes",anchor="end")
s.callout(4,722+D,352,720,175,"A high front|to the saddle")
s.callout(5,1080+D,291,1150,175,"The lance, held|under the arm",anchor="end")
s.save(os.path.join(os.path.dirname(__file__),"..","37-stirrup","stirrup"))
