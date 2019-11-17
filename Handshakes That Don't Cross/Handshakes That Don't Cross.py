class Solution {
public:
    unordered_map<int, long long> memo;
    const long long mod = 1e9+7;
    int numberOfWays(int n) {
        if(n == 0)
            return 1;
        if(memo.find(n) != memo.end())
            return memo[n];
        long long res = 0;
        for(int i = 0; i < n; i+=2) {
            res += ((long long) numberOfWays(i) * numberOfWays(n-2-i)) % mod;
        }
        return memo[n] = res%mod;
    }
};