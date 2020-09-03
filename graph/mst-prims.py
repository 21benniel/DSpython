from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.graph=[]
        self.vis=[False]*n
        self.q=[]
        self.v=n
    def addEdge(self,a,b,w):
        self.graph.append([a,b,w])
    def relax(self,s):
        self.vis[s]=True
        edges=self.graph[s]
        for edge in edges:
            dest=edge
            if self.vis[dest]==False:
                if dict not in self.q:
                    self.q.append(dest,edge)
                else:
                    self.q.remove(dest,edge)

    def Prims(self,s):
        m=self.v-1
        
        edgecount,mstcost=0,0
        msted=[False]*self.m
        self.relax(s)
        while(q and edgecount!=m):
            dest,edge=q.pop()
            msted[edgecount]=edge
            edgecount+=1
            mstcost+=
            


    

g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

g.Prims(0)