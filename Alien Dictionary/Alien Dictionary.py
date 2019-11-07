class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = collections.defaultdict(set)
        ls = set()
        for w1,w2 in zip(words,words[1:]):
            ls |= set(w1)
            ls |= set(w2)
            for u,v in zip(w1,w2):
                if u!=v:
                    g[u].add(v)
                    break
        
        T = []
        visited = collections.defaultdict(int)
        
        def dfs(u):
            visited[u] = 1
            for nei in g[u]:
                if visited[nei] ==0 :
                    if not dfs(nei):
                        return False
                elif visited[nei] == 1:
                    return False
            visited[u] = 2
            T.append(u)
            return True
        
        for l in ls:
            if not visited[l]:
                if not dfs(l):
                    return ""
        if not ls:
            return words[0]
        return "".join(T[::-1])
        