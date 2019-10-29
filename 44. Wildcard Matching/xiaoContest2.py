class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.content = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def _build(self,word):
        node = self.root
        for ind,i in enumerate(word):
            if i not in node.child:
                node.child[i] = TrieNode()
            node = node.child[i]
        node.end = True
        node.content = "/".join(word)
        return "/".join(word)
    


class Solution:
    def __init__(self):
        self.ans = []
    def _dfs(self,node):
        # nonlocal ans
        for key in node.child:
            if node.child[key].end:
                self.ans.append(node.child[key].content)
            else:
                self._dfs(node.child[key])
        
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        trie = Trie()
        # ans = []
        for f in folder:
            wait = f.split("/")
            trie._build(wait)
        self._dfs(trie.root)
        return self.ans
        