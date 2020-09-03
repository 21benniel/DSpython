from Traverse import ins
root=ins()

def preorder(root):
    st=[]
    st.append(root)
    while(len(st)>0):
        t=st.pop()
        print(t.v)
        if t.right:
            st.append(t.right)
        if t.left:
            st.append(t.left)

# add to stack
#   while size!=0
#      pop and print
#            right
#            thrn left



preorder(root)