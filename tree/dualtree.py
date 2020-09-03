
class Node:
    def __init__(self,v):
        self.v=v
        self.left=self.right=None
root=None
def preorder(node):
    if node is not None :
        print(node.v)
        preorder(node.left)
        preorder(node.right)
    return

def double(node):
    if node is None:
        return 
    double(node.left)
    double(node.right)
    t=Node(node.v)
    t.left=node.left
    node.left=t
    return node



a=[2,7,4]
root=double(Node(a[0]))
for i in range(1,len(a)):

    if root is not None:
        if root.v<i:
            root.right=double(Node(i))
        else:
            root.left=double(Node(i))

preorder(root)




