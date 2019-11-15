class Solution:
    def numDecodings(self, s: str) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1
        for ind,i in enumerate(s,1):
            if i!="0":
                dp[ind] += dp[ind-1]
            if "09"<s[ind-2:ind]<"27":
                dp[ind] += dp[ind-2]
        return dp[len(s)]