class Node:
    def __init__(self,v):
        self.v=v
        self.left=self.right=None

def convert(pre,ino,s,e):

    if s>e:
        return None
    node=Node(pre[convert.preindex])
    convert.preindex+=1
    if s==e:
        return node
    inoindex=ino.index(node.v)
    node.left=convert(pre,ino,s,inoindex-1)
    node.right=convert(pre,ino,inoindex+1,e)
    return node
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.v)
        inorder(root.right)
    return

pre=[2,4,7,3,8]
ino=[7,4,3,2,8]
convert.preindex=0
root=convert(pre,ino,0,len(pre)-1)
inorder(root)