class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(x, y): 
            while(y): 
                x, y = y, x % y 
            return x 
        init = nums[0]
        for i in range(1,len(nums)):
            init = gcd(init,nums[i])
        return init == 1