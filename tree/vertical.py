from Traverse import ins
from Tree import inorder
from collections import defaultdict
root=ins()
di=defaultdict(list)
def vert(root,hd):
    # if root is None:
    #     return
    # di[l].append(root.v)

    # vert(root.left,l-1)
    # vert(root.right,l+1)

    if root is None: 
        return

    try: 
        di[hd].append(root.v) 
    except: 
        di[hd] = [root.v] 
    vert(root.left, hd-1) 
    vert(root.right, hd+1) 
    




vert(root,0)

for index, value in enumerate(sorted(di)): 
        for i in di[value]: 
            print (i,end=" ") 
        print()
# 1 2 4 14 23 37 108 111 115 116 83 84 85 
