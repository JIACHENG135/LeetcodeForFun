class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        m = collections.defaultdict(int)
        m[0] = 0
        res = 0
        for i in nums:
            # print(m,i)
            if (3-i%3)%3 in m:
                res = max(res,m[(3-i%3)%3]+i)
            keys = list(m.keys())
            tmp = copy.deepcopy(m)
            for rem in keys: 
                m[(rem+i)%3] = max(m[(rem+i)%3],tmp[rem] + i)
            
        return res
            
            