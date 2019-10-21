class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        return self.bfs_sol(words)
        
        word_set = set()
        words.sort()
        res = ''
        
        for word in words:
            if len(word) == 1 or word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(res):
                    res = word
        
        return res
     
     
    def bfs_sol(self, words):
        from collections import deque
        words = set(words)
        
        q = deque()
        for word in words:
            if len(word) == 1:
                q.append(word)
        
        res = ''
        maxLen = 0
        
        while q:
            cur_word = q.popleft()
            
            if len(cur_word) > maxLen:
                res = cur_word
                maxLen = len(cur_word)
            elif len(cur_word) == maxLen:
                res = min(res, cur_word)
            
            for next_word in self.gen_next_word(cur_word):
                if next_word in words:
                    q.append(next_word)
        
        return res
    
    def gen_next_word(self, cur_word):
        res = []
        for c in "qwertyuiopasdfghjklzxcvbnm":
            res.append(cur_word + c)
        return res
    
    def lw(self, words):
        word_set = set()
        words.sort()
        res = ''

        for word in words:
            if len(word) == 1 or word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(res):
                    res = word
        return res


test1 = ['w', 'wo', 'wor', 'word', 'wa', 'wan', 'caked']

def lwd(word_list):
    word_list.sort()
    word_set = set()
    res = ''
    
    print(test1)
    # a, ab, ad, ac
    # a, ab, ac, ad
    for word in word_list:
        if len(word) == 1 or word[:-1] in word_set:
            word_set.add(word)
            if len(res) < len(word):
                res = word

    return res

print(lwd(test1))
