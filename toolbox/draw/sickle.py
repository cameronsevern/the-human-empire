import sys,os
sys.path.insert(0,os.path.dirname(__file__)); from lib import *
s=Sheet("The sickle","about 23,000 years ago")
# The drawing itself (handle, flint blades, stalks, cut-through inset) is kept as SVG in sickle_art.txt.
for line in open(os.path.join(os.path.dirname(__file__),"sickle_art.txt")).read().split("\n"):
    if line.strip(): s.add(line)
s.text(1010,520,"Cut through the handle",anchor="middle",italic=True)
s.callout(1,234,563,80,250,"Handle of wood|or bone")
s.callout(2,476,286,580,150,"Blades of flint,|each as long as|a finger joint")
s.callout(3,289,419,300,640,"Glue holds the|blades in|a groove")
s.callout(4,724,560,900,640,"The curve gathers a|bunch of stalks, and|one pull cuts them")
s.save(os.path.join(os.path.dirname(__file__),"..","05-sickle","sickle"))
