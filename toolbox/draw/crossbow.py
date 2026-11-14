import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The crossbow","about 2,300 years ago")
BRONZE="#a8a070"
# stock, seen from above, pointing left
s.add(f'<rect x="250" y="400" width="520" height="40" rx="8" fill="{WOOD}" stroke="{INK}" stroke-width="3"/>')
bow="M 300,215 C 386,330 386,510 300,625"
s.raw_path(bow,stroke=INK,sw=17); s.raw_path(bow,stroke="#c9a56b",sw=12)
s.line(302,222,640,420,sw=2.5); s.line(302,618,640,420,sw=2.5)                     # the drawn string
s.line(330,420,636,420,sw=4); s.path([(330,412),(306,420),(330,428)],fill=METAL,close=True)   # the bolt
s.add(f'<rect x="628" y="404" width="34" height="32" rx="4" fill="{ACC}" stroke="{INK}" stroke-width="2.5"/>')
# the lock, from the side
ix,iy,r=960,225,118
s.inset(ix,iy,r,caption="The lock, from the side")
s.add(f'<rect x="{ix-100}" y="{iy-12}" width="200" height="34" fill="{WOOD}" stroke="{INK}" stroke-width="2.5"/>')
s.raw_path(f"M {ix-8},{iy-12} L {ix-8},{iy-44} L {ix+8},{iy-44} L {ix+8},{iy-30} L {ix+22},{iy-30} L {ix+22},{iy-12} Z",fill=ACC,sw=2.5)   # the catch
s.circle(ix-16,iy-26,6,fill=INK,sw=0)                                               # the string, held
s.raw_path(f"M {ix+10},{iy+22} L {ix+34},{iy+78} L {ix+48},{iy+72} L {ix+28},{iy+22} Z",fill=BRONZE,sw=2.5)   # the trigger
s.callout(1,352,300,480,160,"A short, stiff bow fixed|across a wooden stock")
s.callout(2,470,520,480,690,"The string is drawn back with|the whole body, and hooked")
s.callout(3,645,420,800,560,"A bronze catch holds it,|so the archer can|wait and aim")
s.callout(4,ix+40,iy+70,1150,470,"Squeezing the trigger|lets the string go",anchor="end")
s.callout(5,400,420,120,690,"A short bolt lies|in a groove")
s.save(os.path.join(os.path.dirname(__file__),"..","21-crossbow","crossbow"))
