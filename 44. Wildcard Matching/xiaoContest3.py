import copy
class Solution:
    def balancedString(self, s: str) -> int:
        counter = collections.Counter()
        for l in s:
            counter[l] += 1
        
        missing = collections.Counter()
        avg = len(s)//4
        for l in "QWER":
            missing[l] = counter[l] - avg
        
        for key in missing:
            if missing[key]<0:
                missing[key] = 0

            
        l,r = 0,0
        target = sum(missing.values())
        if target == 0:
            return 0
        tcounter = missing
        window = collections.Counter()
        ct = 0
        ans = len(s)
        flag = False
        while r<len(s):
            while r<len(s) and ct<target:
                if window[s[r]]<tcounter[s[r]]:
                    ct += 1
                window[s[r]] += 1
                r += 1

            while l<r and ct == target:
                flag = True
                ans = min(ans,r-l)
                if window[s[l]] == tcounter[s[l]]:
                    ct -= 1
                window[s[l]] -= 1
                l += 1
        if flag:
            return ans
        else:
            return 0