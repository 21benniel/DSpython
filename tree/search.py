from Traverse import ins
root=ins()

def search(root,val):
    if root is not None:
        print(root.v)
        if root.v==val:
            return True
        return search(root.left,val) or search(root.right,val)
def help(root,val):
    if (search(root,val)):
        print("yes")
    else:
        print("no")
help(root,50)