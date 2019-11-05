# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

    
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        res = 'z'*8500
        def dfs(node,path):
            nonlocal res
            if not node.left and not node.right:
                res = min(res,path[::-1])
                return 
            if node.left:
                dfs(node.left,path+chr(node.left.val+97))
            if node.right:
                dfs(node.right,path+chr(node.right.val+97))
        if not root:
            return ""
        dfs(root,str(chr(root.val+97)))
        return res