class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        def expand(ind,direct):
            nonlocal ans
            if direct == 1:
                l,r = ind,ind+1
            else:
                l,r = ind,ind
            while l>-1 and r<len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            expand(i,1)
            expand(i,0)
        return ans
            
            