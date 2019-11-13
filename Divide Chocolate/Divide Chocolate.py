class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def helper(arr,K,S):
            state = 0
            for ind in range(len(arr)):
                if state<S:
                    state += arr[ind]
                    if state>=S:
                        state = 0
                        K -= 1
                        if K<=0:
                            return True
            return K <= 0
        
        if K==0:
            return sum(sweetness)
        
        l,r = 0,sum(sweetness)/K+1
        
        ans = 0
        while l<r:
            mid = (l+r)//2
            if helper(sweetness,K+1,mid):
                ans = max(ans,mid)
                l = mid + 1
            else:
                r = mid
        return int(ans)
            