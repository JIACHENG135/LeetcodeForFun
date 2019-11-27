class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0
        target = len(t)
        tcounter = collections.Counter(t)
        window = collections.Counter()
        ct = 0
        ans = s
        flag = False
        while r<len(s):
            
            while r<len(s) and ct<target:
                if window[s[r]]<tcounter[s[r]]:
                    ct += 1
                window[s[r]] += 1
                r += 1

            while l<r and ct == target:
                flag = True
                ans = min(ans,s[l:r],key=lambda x:len(x))
                if window[s[l]] == tcounter[s[l]]:
                    ct -= 1
                window[s[l]] -= 1
                l += 1
        if flag:
            return ans
        else:
            return ""
                
                    