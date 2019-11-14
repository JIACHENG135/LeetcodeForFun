from collections import defaultdict 
import random
class Test:
    def __init__(self,vertices,numComp):
        self.edges = []
        self.
        cc = 0
        while cc<numComp:
            verticesSet = set()
            while len(vertices)<vertices:
                randomU = random.randint(1+vertices*cc,vertices**(cc+1))
                randomV = random.randint(1+vertices*cc,vertices**(cc+1))
                if randomU!=randomV:
                    verticesSet |= set([randomU,randomV])
                    self.edges.append([randomU,randomU])

class Graph: 
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
        self.Time = 0
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 
    def APUtil(self,u, visited, ap, parent, low, disc): 
        children =0
        visited[u]= True
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
        for v in self.graph[u]: 
            if visited[v] == False : 
                parent[v] = u 
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc) 
                low[u] = min(low[u], low[v]) 
                if parent[u] == -1 and children > 1: 
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]: 
                    ap[u] = True    
            elif v != parent[u]:  
                low[u] = min(low[u], disc[v]) 
    def AP(self): 
        visited = [False] * (self.V) 
        disc = [float("Inf")] * (self.V) 
        low = [float("Inf")] * (self.V) 
        parent = [-1] * (self.V) 
        ap = [False] * (self.V) 
        for i in range(self.V): 
            if visited[i] == False: 
                self.APUtil(i, visited, ap, parent, low, disc) 
        for index, value in enumerate (ap): 
            if value == True: print(index)

def criticalRounters(numRouters,numLinks,links):
    g = Graph(numRouters+1)
    for u,v in links:
        g.addEdge(u,v)
    g.AP()

criticalRounters(6+1,5,[[1,2],[2,3],[3,4],[4,5],[6,3]])