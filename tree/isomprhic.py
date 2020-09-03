from Traverse import ins
from Tree import inorder
root=ins()


def isomor(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.v!=root2.v:
        return False
    return (isomor(root1.left,root2.left) and isomor(root1.right,root2.right) )or (isomor(root1.left,root2.right) and isomor(root1.right,root2.left))


print(isomor(root,root))