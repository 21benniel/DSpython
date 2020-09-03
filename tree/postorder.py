from Traverse import ins
root=ins()

def preorder(root):
    st=[]
    ans=[]
    st.append(root)
    while(len(st)>0):
        t=st.pop()
        ans.append(t)
        if t.left:
            st.append(t.left)
        if t.right:
            st.append(t.right)
    while ans:
        print(ans.pop().v)

# 2 stacks


preorder(root)