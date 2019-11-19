# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -float("inf")
        def helper(node):
            nonlocal res
            if not node:
                return -float("inf")
            else:
                l = helper(node.left)
                r = helper(node.right)
                res = max(res,node.val+max(0,l)+max(0,r))
                return max(node.val,node.val+l,node.val+r)
        helper(root)
        return res