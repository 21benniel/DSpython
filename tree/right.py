from Traverse import ins
root=ins()
def rightview(root,l,maxlevel):
    if root is None:
        return
    if l>maxlevel[0]:
        print(l,maxlevel[0])
        print(root.v)
        maxlevel[0]=l
    rightview(root.right,l+1,maxlevel)
    rightview(root.left,l+1,maxlevel)
rightview(root,1,[0])