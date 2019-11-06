# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        def dfs(node,path):
            nonlocal res
            if not node.left and not node.right:
                res += int(path)
                return 
            if node.left:
                dfs(node.left,path+str(node.left.val))
            if node.right:
                dfs(node.right,path+str(node.right.val))
        if not root:
            return res
        dfs(root,str(root.val))
        return res