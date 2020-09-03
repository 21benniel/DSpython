from Traverse import ins
root=ins()


def diameter(root):
    if root is None:
        return -1
    
    l=diameter(root.left)
    r=diameter(root.right)
    diameter.d=max(diameter.d,(l+r+1))
    return max()
    if l==-1 or r==-1 or root
    


diameter.d=0
d=diameter(root)
print(d)