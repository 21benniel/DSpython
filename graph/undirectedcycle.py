import sys
from collections import defaultdict
class g:
    def __init__(self,n):
        self.dict=defaultdict(list)
    def insert(self,u,v):
        self.dict[u].append(v)
        self.dict[v].append(u)

    
    def bfs(self,visited,q,f,r):
        q.append(r)
        visited.add(r)
        f[r]+=1
        flag=0
        while(len(q)>0):
            t=q.pop()
            f[t]+=1
            
            for i in self.dict[t]:
                if f[i]==0:
                    
                    flag=1
                if i not in visited:
                    
                    
                    q.append(i)
                    visited.add(i)
                    f[i]+=1
        if flag==1:
            return "True"
        
        return "False"
n=4
t=g(n)
t.insert(0, 1) 
# t.insert(0, 2) 
t.insert(1, 2) 
# t.insert(2, 0) 
t.insert(2, 3) 
t.insert(0,2) 

print("----------")

visited=set()
q=[]
f=[-1]*5
sol=t.bfs(visited,q,f,1)
print(sol)