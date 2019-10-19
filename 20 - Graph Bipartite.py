class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        colors = [0] * len(graph)
        
        from collections import deque
        for i in range(len(graph)):
            if colors[i] != 0 :
                continue
            
            q = deque([i])
            colors[i] = 1
            
            while q:
                size = len(q)
                for _ in range(size):
                    curNode = q.popleft()
                    for nei in graph[curNode]:
                        if colors[nei] == 0:
                            colors[nei] = -colors[curNode]
                            q.append(nei)
                        else:
                            if colors[nei] != -colors[curNode]:
                                return False
        
        return True