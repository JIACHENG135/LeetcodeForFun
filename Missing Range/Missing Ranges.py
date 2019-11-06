class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower==upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
            
        else:
            if nums[0]!=lower:
                nums = [lower-1] + nums
            if nums[-1]!=upper:
                nums = nums + [upper+1]
            ans = []
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1]>2:
                    ans.append(str(nums[i-1]+1) + "->" + str(nums[i]-1))
                elif nums[i] - nums[i-1]==2:
                    ans.append(str(nums[i]-1))
            return ans