class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = []
        for i in nums:
            res.append(i%2)
            
        m = {0:1}
        ans,ps = 0,0
        for i in res:
            ps += i
            if ps-k in m:
                ans += m[ps-k]
            m[ps] = m.get(ps,0) + 1
        return ans