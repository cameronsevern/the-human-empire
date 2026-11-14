import math,sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The layered bow","about 2,200 years ago")
HORN="#6b5a4a"
bow="M 240,150 C 272,180 272,204 250,232 C 176,300 176,540 250,608 C 272,636 272,660 240,690"
s.raw_path(bow,stroke=INK,sw=19); s.raw_path(bow,stroke="#c9a56b",sw=14)
s.line(256,160,256,680,sw=2)                       # string
s.raw_path("M 196,395 L 196,445",stroke=ACC,sw=22)   # grip
# cut through one limb
ix,iy,r=800,330,150
s.inset(ix,iy,r)
s.add(f'<rect x="710" y="250" width="42" height="160" fill="{HIDE}" stroke="{INK}" stroke-width="2.5"/>')
s.add(f'<rect x="752" y="250" width="78" height="160" fill="{WOOD}" stroke="{INK}" stroke-width="2.5"/>')
s.add(f'<rect x="830" y="250" width="60" height="160" fill="{HORN}" stroke="{INK}" stroke-width="2.5"/>')
s.text(731,438,"target side",anchor="middle",italic=True,size=17); s.text(868,438,"archer's side",anchor="middle",italic=True,size=17)
s.text(ix,iy+r+36,"Cut through one limb",anchor="middle",italic=True)
s.callout(1,790,330,900,130,"A thin core of wood")
s.callout(2,860,372,1150,600,"Horn on the archer's side|can take the squeezing",anchor="end")
s.callout(3,731,300,570,170,"Sinew on the far side|stretches and springs back",anchor="end")
s.callout(4,246,160,400,330,"The tips curve away|from the archer")
s.callout(5,200,420,400,560,"Short enough to swing|across a horse's neck")
s.save(os.path.join(os.path.dirname(__file__),"..","22-layered-bow","layered-bow"))
