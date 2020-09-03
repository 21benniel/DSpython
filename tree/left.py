from Traverse import ins
root=ins()
def leftview(root,l,maxlevel):
    if root is None:
        return
    if l>maxlevel[0]:
        print(l,maxlevel[0])
        print(root.v)
        maxlevel[0]=l
    leftview(root.left,l+1,maxlevel)
    leftview(root.right,l+1,maxlevel)
leftview(root,1,[0])