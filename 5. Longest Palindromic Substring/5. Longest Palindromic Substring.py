class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0,0]
        def expand(ind,direc):
            nonlocal ans
            if direc == 1:
                l,r = ind,ind
            else:
                l,r = ind,ind+1
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            ans = max(ans,[l+1,r],key = lambda x:x[1]-x[0])
                
        for i in range(len(s)):
            expand(i,1)
            expand(i,-1)
        
        return s[ans[0]:ans[1]]