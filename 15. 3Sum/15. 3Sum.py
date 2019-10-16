class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        k,n = 0,len(nums)
        while k<n:
            l,r = k+1,n-1
            target = -nums[k]
            while l<r:
                if nums[l] + nums[r] == target:
                    cur = nums[l]
                    ans.append([nums[k],nums[l],nums[r]])
                    while l<r and nums[l]==cur:
                        l += 1
                elif nums[l]+nums[r]<target:
                    l += 1
                else:
                    r -= 1
            cur = nums[k]
            while k<n and nums[k] == cur:
                k += 1
        return ans