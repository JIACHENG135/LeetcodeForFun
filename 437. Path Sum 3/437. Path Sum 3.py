import collections
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        rec = collections.defaultdict(list)
        rec[0] = [[]]
        ans = 0
        mem = collections.defaultdict(list)
        
        def dfs(root,preSum,curPath,target,mem):
            nonlocal ans
            if target-root.val in mem:
                for tempPath in mem[target-root.val]:
                    ans.append(tempPath+[root.val])
            mem[preSum+root.val].append(curPath+[root.val])
            if root.left:
                dfs(root.left,preSum+root.val,curPath+[root.val],target-root.val,mem)
            if root.right:
                dfs(root.right,preSum+root.val,curPath+[root.val],target-root.val,mem)
        dfs(root,0,[[]],0,mem)
        return ans