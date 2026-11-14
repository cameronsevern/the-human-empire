"""Shared drawing helpers for toolbox diagrams. House style is in ../design.md."""
import subprocess
INK="#2f2a26"; PAPER="#faf6ee"; SOFT="#8a8178"; ACC="#b5523b"
WOOD="#e6d6b8"; STONE="#cdc6ba"; CLAY="#d9b08c"; METAL="#b9c0c4"; BONE="#efe6d0"; HIDE="#d8b995"
W,H=1200,760

class Sheet:
    def __init__(self,title,date):
        self.title=title; self.date=date; self.e=[]
    def add(self,s): self.e.append(s); return self
    def path(self,pts,fill="none",stroke=INK,sw=3,close=False,extra=""):
        d="M "+" L ".join(f"{x:.1f},{y:.1f}" for x,y in pts)+(" Z" if close else "")
        return self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>')
    def raw_path(self,d,fill="none",stroke=INK,sw=3,extra=""):
        return self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>')
    def circle(self,x,y,r,fill="none",stroke=INK,sw=3):
        return self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def ellipse(self,x,y,rx,ry,fill="none",stroke=INK,sw=3,rot=0):
        return self.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" transform="rotate({rot} {x} {y})"/>')
    def line(self,x1,y1,x2,y2,stroke=INK,sw=3,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        return self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"{d}/>')
    def text(self,x,y,s,size=21,anchor="start",italic=False,bold=False,fill=INK,halo=PAPER):
        st=(' font-style="italic"' if italic else "")+(' font-weight="bold"' if bold else "")
        for j,l in enumerate(s.split("|")):
            self.add(f'<text x="{x}" y="{y+j*27}" text-anchor="{anchor}" font-size="{size}" fill="{fill}" stroke="{halo}" stroke-width="7" paint-order="stroke" stroke-linejoin="round"{st}>{l}</text>')
        return self
    def callout(self,n,x,y,tx,ty,label,anchor="start",halo=PAPER):
        """Dot on the part at (x,y), ringed number at (tx,ty), label beside the ring."""
        self.line(x,y,tx,ty,sw=1.5); self.circle(x,y,4,fill=INK,sw=0)
        self.circle(tx,ty,19,fill=PAPER,sw=2)
        self.text(tx,ty+7,str(n),anchor="middle",bold=True)
        self.text(tx+30 if anchor=="start" else tx-30, ty+7, label, anchor=anchor, halo=halo)
        return self
    def inset(self,x,y,r,caption=None):
        self.circle(x,y,r,fill="#ffffff",sw=2.5)
        if caption: self.text(x,y+r+40,caption,anchor="middle",italic=True)
        return self
    def arrow(self,x1,y1,x2,y2):
        import math
        a=math.atan2(y2-y1,x2-x1); L=16
        self.line(x1,y1,x2,y2,sw=2.5)
        for da in (2.6,-2.6):
            self.line(x2,y2,x2+L*math.cos(a+da),y2+L*math.sin(a+da),sw=2.5)
        return self
    def person(self,x,y,lean=0.35,scale=1.0,arm_to=None):
        """Simple soft-grey figure standing at foot point (x,y), leaning forward (to the right)."""
        import math
        s=scale; hipx,hipy=x-10*s,y-70*s
        shx,shy=hipx+70*s*math.sin(lean),hipy-70*s*math.cos(lean)
        hx,hy=shx+16*s*math.sin(lean),shy-20*s*math.cos(lean)
        for (a,b,c,d) in ((x-28*s,y,hipx,hipy),(x+14*s,y,hipx,hipy),(hipx,hipy,shx,shy)):
            self.line(round(a,1),round(b,1),round(c,1),round(d,1),stroke=SOFT,sw=5)
        self.circle(round(hx,1),round(hy,1),round(13*s,1),fill=PAPER,stroke=SOFT,sw=4)
        if arm_to: self.line(round(shx,1),round(shy+8*s,1),arm_to[0],arm_to[1],stroke=SOFT,sw=4)
        return (shx,shy)
    def save(self,stem):
        # Text stays crisp on top; everything else gets the hand-drawn treatment.
        shapes="\n".join(x for x in self.e if not x.startswith("<text"))
        texts="\n".join(x for x in self.e if x.startswith("<text"))
        svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Georgia, 'Noto Serif', serif">
<defs>
<!-- paper: fine grain plus slow blotches -->
<filter id="paper" x="0" y="0" width="100%" height="100%">
<feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" seed="3" result="grain"/>
<feColorMatrix in="grain" type="matrix" values="0 0 0 0 0.45  0 0 0 0 0.36  0 0 0 0 0.24  0 0 0 0.9 -0.42" result="g2"/>
<feTurbulence type="fractalNoise" baseFrequency="0.006" numOctaves="2" seed="8" result="blot"/>
<feColorMatrix in="blot" type="matrix" values="0 0 0 0 0.55  0 0 0 0 0.42  0 0 0 0 0.25  0 0 0 0.55 -0.2" result="b2"/>
<feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="b2"/><feMergeNode in="g2"/></feMerge>
</filter>
<!-- ink: a slight wobble in every line, a soft bleed of colour under it, and mottling inside the washes -->
<filter id="ink" x="-5%" y="-5%" width="110%" height="110%">
<feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="5" result="warp"/>
<feDisplacementMap in="SourceGraphic" in2="warp" scale="5" xChannelSelector="R" yChannelSelector="G" result="drawn"/>
<feGaussianBlur in="drawn" stdDeviation="7" result="bleed0"/>
<feComponentTransfer in="bleed0" result="bleed"><feFuncA type="linear" slope="0.38"/></feComponentTransfer>
<feTurbulence type="fractalNoise" baseFrequency="0.011" numOctaves="2" seed="11" result="wash"/>
<feColorMatrix in="wash" type="matrix" values="0 0 0 0 0.35  0 0 0 0 0.25  0 0 0 0 0.15  0 0 0 0.75 -0.3" result="w2"/>
<feComposite in="w2" in2="drawn" operator="in" result="mottle"/>
<feMorphology in="drawn" operator="erode" radius="2.5" result="inner"/>
<feComposite in="drawn" in2="inner" operator="out" result="rim0"/>
<feColorMatrix in="rim0" type="matrix" values="0 0 0 0 0.3  0 0 0 0 0.22  0 0 0 0 0.15  0 0 0 0.16 0" result="rim"/>
<feOffset in="drawn" dx="5" dy="7" result="off"/>
<feGaussianBlur in="off" stdDeviation="5" result="sh0"/>
<feColorMatrix in="sh0" type="matrix" values="0 0 0 0 0.25  0 0 0 0 0.2  0 0 0 0 0.15  0 0 0 0.22 0" result="shadow"/>
<feMerge><feMergeNode in="shadow"/><feMergeNode in="bleed"/><feMergeNode in="drawn"/><feMergeNode in="mottle"/><feMergeNode in="rim"/></feMerge>
</filter>
<radialGradient id="vig" cx="50%" cy="50%" r="75%"><stop offset="60%" stop-color="#6b4a2a" stop-opacity="0"/><stop offset="100%" stop-color="#6b4a2a" stop-opacity="0.22"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" fill="{PAPER}" filter="url(#paper)"/>
<rect width="{W}" height="{H}" fill="url(#vig)"/>
<rect x="14" y="14" width="{W-28}" height="{H-28}" fill="none" stroke="{INK}" stroke-width="2"/>
<rect x="20" y="20" width="{W-40}" height="{H-40}" fill="none" stroke="{INK}" stroke-width="0.7"/>
<text x="44" y="64" font-size="30" font-weight="bold" fill="{INK}" letter-spacing="3">{self.title.upper()}</text>
<line x1="44" y1="76" x2="104" y2="76" stroke="{ACC}" stroke-width="3"/>
<text x="44" y="104" font-size="20" font-style="italic" fill="{SOFT}">{self.date}</text>
<g filter="url(#ink)">
{shapes}
</g>
{texts}
</svg>'''
        open(stem+".svg","w").write(svg)
        subprocess.run(["rsvg-convert","-w","1600",stem+".svg","-o",stem+".png"],check=True)
