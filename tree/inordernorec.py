from Traverse import ins
root=ins()
def inorderno(root):
    st=[]
    while(root):
        st.append(root)
        root=root.left
    while(len(st)>0):
        t=st.pop()
        print(t.v)
        if t.right is not None:
            t=t.right
            while(t):
                st.append(t)
                t=t.left

# using stack
#         push all left
#         while size>0
#             print and pop
#             if right iruntha 
#             t=t.right
#             while t:
#                 add all



inorderno(root)