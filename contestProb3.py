class TrieNode:
    def __init__(self):
        self.c = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def _insert(self,word):
        node = self.root
        for l in word:
            if l not in node.c:
                node.c[l] = TrieNode()
            node = node.c[l]
        node.end = True
    def _search(self,string,node):
        ans = []
        if node.end:
            ans.append(string)
        def dfs(node,path):
            nonlocal ans
            for l in node.c:
                if node.c[l].end:
                    ans.append(path+l)
                dfs(node.c[l],path+l)
        
        dfs(node,string)
        ans.sort()
        return ans
            
            
            
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        res = []
        for word in products:
            trie._insert(word)
        node = trie.root
        for ind,l in enumerate(searchWord):
            if l not in node.c:
                node.c[l] = TrieNode()
            node = node.c[l]
            res.append(trie._search(searchWord[:ind+1],node)[:3])
            
        return res
        