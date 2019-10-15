class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        prev = []
        ans = 0
        for i in nums:
            if not prev or i>prev[-1]:
                prev.append(i)
                
            else:
                ind = bisect.bisect_left(prev,i)
                prev[ind] = i
            ans = max(ans,len(prev))
        return ans