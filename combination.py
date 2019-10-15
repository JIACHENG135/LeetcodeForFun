class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        mi,ma = min(candidates),max(candidates)
        ans = set()
        def dfs(cur,path):
            nonlocal ans
            for i in candidates:
                if not cur%i:
                    wait = ",".join([str(i) for i in sorted(path+(cur//i)*[i])])
                    ans.add(wait)
                if cur - i >= mi:
                    dfs(cur-i,path+[i])
        dfs(target,[])
        res = []
        for s in ans:
            res.append([int(i) for i in s.split(",")])
        return res