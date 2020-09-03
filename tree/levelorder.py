from Traverse import ins
from high import h
from givenlevel import level
root=ins()
l=h(root)
def levelorder(root):
    for i in range(l,0,-1):
        level(root,i)
        print()
   
levelorder(root)

