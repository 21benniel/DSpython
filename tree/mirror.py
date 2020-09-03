from Traverse import ins
from Tree import inorder
root=ins()

def mirror(root):
    if root is None:
        return None
    t=root.left
    root.left=root.right
    root.right=t
    mirror(root.left)
    mirror(root.right)
    return root
root =mirror(root)
inorder(root)