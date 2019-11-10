class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        price = collections.defaultdict(int)
        ans = 0
        ltp = collections.Counter(letters)
        def dfs(ltCt,res,start):
            
            nonlocal ans
            word = words[start]
            tmpct = collections.Counter(word)
            flag = False
            init = int(res)
            for l in tmpct:
                if ltCt[l]<tmpct[l]:
                    flag = True
                    break
                else:
                    ltCt[l] -= tmpct[l]
            
            if not flag:
                res += price[word]
                ans = max(ans,res)
                for i in range(start+1,len(words)):
                    nextCt = copy.deepcopy(ltCt)
                    nextRes = int(res)
                    dfs(nextCt,nextRes,i)
                    
        for word in words:
            ct = collections.Counter(word)
            res = 0
            flag = True
            for l in ct:
                if ct[l]<=ltp[l]:
                    res += ct[l]*score[ord(l)-ord("a")]
                else:
                    flag = False
            if flag:
                price[word] = res
        for i in range(len(words)):
            tmpCt = copy.deepcopy(ltp)
            dfs(tmpCt,0,i)
        return ans
            
            
        