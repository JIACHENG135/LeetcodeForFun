class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid]<=nums[r]:# in the right range
                if target>nums[r]:
                    r = mid - 1
                elif nums[mid]<target:
                    l = mid + 1
                else:
                    r = mid
            else:# mid in the left part
                if target>nums[r]:
                    if nums[mid]<target:
                        l = mid + 1
                    else:
                        r = mid
                else:
                    l = mid + 1
        return l if nums[l]==target else -1