from collections import defaultdict
class g:
    def __init__(self,n):
        self.dict=defaultdict(list)
       
    def insert(self,u,v,n):
        self.dict[u].append((v,n))
        self.dict[v].append((u,n))
       


    # def dij(self,root,n,s):
    #     vis=set()
    #     dist=[1000]*n
    #     dist[s]=0
    #     prev=[-1]*n
    #     q=[]
    #     q.append((s,0))

    #     while(q):
    #         ind,mi=q.pop()
    #         vis.add(ind)
    #         for i in self.dict[ind]:
    #             if i in vis:
    #                 continue
    #             newt=dist[ind]+i[1]
    #             print(newt)
    #             print(dist[ind])
    #             if newt<dist[i[0]]:
    #                 prev[i[0]]=ind
    #                 dist[i[0]]=newt
    #                 print(dist[ind])
    #                 q.append((i[0],newt)) 
    #     print(dist)
    #     print(prev)
    def dij(self,root,n,s):
        vis=set()
        dist=[1000]*n
        dist[s]=0
        # prev=[-1]*n
        q=[]
        q.append((s,0))

        while(q):
            ind,mi=q.pop()
            vis.add(ind)
            if dist[ind]<mi:
                continue
            for i in self.dict[ind]:
                if i in vis:
                    continue
                newt=dist[ind]+i[1]
                print(newt)
                print(dist[ind])
                if newt<dist[i[0]]:
                    # prev[i[0]]=ind
                    dist[i[0]]=newt
                    print(dist[ind])
                    if i[0] not in q:
                        q.append((i[0],newt)) 
                    else:
                        q.remove((i[0],newt))
        print(dist)
        # print(prev)

def add():

    n=5
    t=g(n)
    t.insert(0, 1,2) 
    t.insert(0, 2,6) 
    t.insert(2, 4,3)
    t.insert(1,4,2)
    
    t.dij(t,n,0)
    # visited=set()
    # t.dfs(visited,2)
    # print("----------")
    # visited=set()
    # q=[]
    # t.bfs(visited,q,2)
    # return t
t=add()


