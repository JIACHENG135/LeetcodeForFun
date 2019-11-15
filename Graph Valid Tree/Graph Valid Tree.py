class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ccn = 0
        color = [0 for i in range(n)]
        g = collections.defaultdict(set)
        dad = {}
        def dfs(n):
            color[n] = 1
            for i in g[n]:
                if color[i] == 0:
                    dad[i] = n 
                    if not dfs(i):
                        return False
                elif i!=dad[n]:
                    return False
            color[n] = 2
            return True
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        
        for i in range(n):
            if color[i] == 0:
                ccn += 1
                if not dfs(i):
                    return False
        return ccn == 1
            
        
        