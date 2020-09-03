
from Traverse import ins
from collections import defaultdict
root=ins()

def printbound(root):
    if root is not None:
        print(root.v,end=" ")
        printbl(root.left)
        printleve(root.left)
        printleve(root.right)
        printbr(root.right)
def printbl(root):
    if root is None:
        return
    if root.left is not None:
        print(root.v,end=" ")
        printbl(root.left)
    elif root.right is not None:
        print(root.v,end=" ")
        printbl(root.right)
    
def printbr(root):
    if root is None:
        return
    if root.right is not None:
        printbr(root.right)
        print(root.v,end=" ")
    elif root.left is not None:
        printbl(root.left)
        print(root.v,end=" ")
def printleve(root):
    if root is None:
        return
    printleve(root.left)
    if root.left is None and root.right is None:
        print(root.v,end=" ")
    printleve(root.right)
    








printbound(root)