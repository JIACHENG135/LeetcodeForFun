class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [1] + [0]*(arrLen-1)
        row = [0]*arrLen
        MOD = 10**9+7
        
        for i in range(1,steps+1):
            row[0] = dp[0] + dp[1]
            row[-1] = dp[-1]+dp[-2]
            for p in range(1,min(steps,arrLen-1)):
                row[p] = dp[p] + dp[p-1] + dp[p+1]
            dp,row = row,dp
            
                
        return dp[0]%MOD