from Traverse import ins
from Tree import inorder
root=ins()
from high import h
ans=[]
def level(root,l,a):
    if root is None:
        return
    if l==1:
        a.append(root.v)
        return 
    level(root.left,l-1,a)
    level(root.right,l-1,a)


def spiral(root):
    he=h(root)
    for i in range(1,he+1):
        a=[]
        level(root,i,a)
        if(i%2==0):
            ans.append(a[::-1])
        else:
            ans.append(a)





spiral(root)
print(ans)
print(len(max(ans,key=len)))