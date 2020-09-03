from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.graph=[]
        self.v=n
    def addEdge(self,a,b,w):
        self.graph.append([a,b,w])
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
    def union(self,parent,rank,x,y):
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
    def KruskalMST(self):
        res=[]
        i=0
        e=0
        self.graph=sorted(self.graph,key= lambda item:item[2])
        print(self.graph)
        parent=[]
        rank=[]
        for node in range(self.v):
            parent.append(node)
            rank.append(0)
        print(parent)
        while e<self.v-1:
            u,v,w=self.graph[i]
            i+=1
            x=self.find(parent,u)
            y=self.find(parent,v)

            if x!=y:
                e+=1
                res.append([u,v,w])
                self.union(parent,rank,x,y)
        print("Following are the edges in the constructed MST")
        for u,v,weight  in res: 
            #print str(u) + " -- " + str(v) + " == " + str(weight) 
            print ("%d -- %d == %d" % (u,v,weight)) 
    

g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

g.KruskalMST()