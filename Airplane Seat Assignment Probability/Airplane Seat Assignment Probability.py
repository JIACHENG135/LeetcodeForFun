class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        # return 0.5 if n > 1 else 1.0
        
        dp = [0] * n
        dp[0] = 1.0
        for i in xrange(1, n):
            dp[i] = 1.0 / (i+1) +  dp[i-1] * (i-1) / (i+1) 
        return dp[-1]