from collections import defaultdict
class g:
    def __init__(self,n):
        self.dict=defaultdict(list)
    def insert(self,u,v):
        self.dict[u].append(v)
        self.dict[v].append(u)

    
    def dfs(self,visited,r):
        if r not in visited:
            print(r)
            visited.add(r)
            for i in self.dict[r]:
                self.dfs(visited,i)

    def bfs(self,visited,q,r):
        q.append(r)
        visited.add(r)
        while(len(q)>0):
            t=q.pop()
            print(t)
            for i in self.dict[t]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)
def add():

    n=5
    t=g(n)
    t.insert(0, 1) 
    t.insert(0, 2) 
    t.insert(1, 2) 
    t.insert(2, 0) 
    t.insert(2, 3) 
    t.insert(3, 3) 
    visited=set()
    t.dfs(visited,2)
    print("----------")
    visited=set()
    q=[]
    t.bfs(visited,q,2)
    return t
t=add()


