class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        mi = min(candidates)
        ans = set()
        def dfs(cur,state,path):
            nonlocal ans
            for ind,i in enumerate(candidates):
                
                if not (1<<ind)&state:
                    if cur == i:
                        ans.add(",".join(sorted(path+[str(i)])))
                    if cur - i>=mi:
                        dfs(cur-i,state|(1<<ind),path+[str(i)])
        dfs(target,0,[])
        res = []
        for s in ans:
            res.append([int(i) for i in s.split(",")])
        return res