
from Traverse import ins
from collections import defaultdict
root=ins()
di=defaultdict(list)
def vert(root,d,l):
    # if root is None:
    #     return
    # di[l].append(root.v)

    # vert(root.left,l-1)
    # vert(root.right,l+1)

    if(root == None): 
        return
      
    if d not in di: 
        di[d] = [root.v,l] 
    elif(di[d][1] > l): 
        di[d] = [root.v,l] 
    vert(root.left, d - 1, l + 1) 
    vert(root.right, d + 1, l + 1) 
    




vert(root,0,0)
for i in sorted(di):
    print(di[i][0],end=" ")