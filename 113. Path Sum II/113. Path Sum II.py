# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def dfs(node,preSum,path):
            nonlocal ans
            if not node.left and not node.right:
                if preSum == sum:
                    ans.append(path)
            if node.left:
                dfs(node.left,preSum+node.left.val,path+[node.left.val])
            if node.right:
                dfs(node.right,preSum+node.right.val,path+[node.right.val])
        if not root:
            return ans
        dfs(root,root.val,[root.val])
        return ans