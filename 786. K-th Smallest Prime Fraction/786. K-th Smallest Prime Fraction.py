import bisect as bi
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        l, r, n = 0.0, 1.0, len(A)
        while True:
            m = (l+r)/2
            border = [bi.bisect(A, A[i]*m) for i in xrange(n)]            
            cur = sum(border)
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                return max([[A[j-1], A[i]] for i, j in enumerate(border) if j > 0], key=lambda x: float(x[0])/x[1])