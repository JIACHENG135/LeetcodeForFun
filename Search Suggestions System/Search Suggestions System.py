import collections
class TrieNode():
    def __init__(self):
        self.children = {}
        self.words = []

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def _build(self, word):
        root = self.root
        for ch in word.lower():
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root.children[ch].words.append(word)
            root = root.children[ch]

    def _search(self, word, N):
        root = self.root
        for ch in word.lower():
            if ch not in root.children:
                return []
            else:
                root = root.children[ch]
        return sorted(root.words)[:N]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        res = []
        for word in products:
            trie._build(word)
        for i in range(1, len(searchWord)+1):
            res.append( trie._search(searchWord[:i], 3) )
        return res