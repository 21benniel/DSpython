from Traverse import ins

root=ins()

def h(root):
    if root is None:
        return 0
    return 1+(max(h(root.left),h(root.right)))
# print(h(root))