from Traverse import ins
root=ins()
def level(root,l):
    if root is None:
        return
    if l==1:
        print(root.v,end=" ")
        return 
    level(root.left,l-1)
    level(root.right,l-1)
    
# level(root,3)