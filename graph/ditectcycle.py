import sys
from collections import defaultdict
class g:
    def __init__(self,n):
        self.dict=defaultdict(list)
        self.flag=0
    def insert(self,u,v):
        self.dict[u].append(v)
        # self.dict[v].append(u)
    def dfs(self,visited,f,r):
        if r not in visited:
            print(r)
            visited.add(r)
            f[r]+=1
            for i in self.dict[r]:
                if f[i]==0:
                    self.flag=1
                self.dfs(visited,f,i)

        if self.flag==1:
            return True
        else:
            return False
    
n=4
t=g(n)
t.insert(0, 1) 
# t.insert(0, 2) 
t.insert(1, 2) 
# t.insert(2, 0) 
t.insert(2, 3) 
t.insert(3,0) 

print("----------")

visited=set()
q=[]
f=[-1]*5
sol=t.dfs(visited,f,1)
print(sol)