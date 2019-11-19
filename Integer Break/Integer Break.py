class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        rec = [1]*(n+1)
        rec[2] = 1
        for i in range(3, n+1):
            maximum = 0
            for j in range(1, i / 2 + 1):
                maximum = max(maximum, j * max(rec[i-j], i-j))
            rec[i] = maximum
        return rec[n]