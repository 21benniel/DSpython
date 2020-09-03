
class Tree:
    def __init__(self,v):
        self.left=None
        self.right=None
        self.v=v
    
def insert(root,node):
    if root is None:
        root=node
    else:
        if root.v<node.v:
            if root.right is None:
                root.right =node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left =node
            else:
                insert(root.left,node)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.v)
        inorder(root.right)

