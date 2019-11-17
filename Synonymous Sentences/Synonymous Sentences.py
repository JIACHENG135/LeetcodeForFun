class Solution:
    def generateSentences(self, s: List[List[str]], text: str) -> List[str]:
        g = collections.defaultdict(set)
        words = set()
        for u,v in s:
            words |= set([u,v])
            g[u].add(v)
            g[v].add(u)
        
        cc = collections.defaultdict(set)
        ccnMap = collections.defaultdict(int)
        visited = set()
        def dfs(w,ccn):
            cc[ccn].add(w)
            ccnMap[w] = ccn
            visited.add(w)
            for nei in g[w]:
                if nei not in visited:
                    dfs(nei,ccn)
        ccn = 0
        for w in words:
            if w not in visited:
                ccn += 1
                dfs(w,ccn)
        # print(ccnMap,cc)
        sent = text.split(" ")
        wait = []
        for ind,w in enumerate(sent):
            # print(w,ind,w in ccnMap,ccnMap)
            # print(w,ind,words,w in words)
            if w in words:
                # print("inmap")
                wait.append(ind)
        res = [sent]
        # print(wait)
        for i in wait:
            cur = []
            for s in res:
                for word in sorted(cc[ccnMap[s[i]]]):
                    tmp = list(s)
                    tmp[i] = word
                    cur.append(tmp)
            res = cur
        res = [" ".join(s) for s in res]
        return res
        
            
            