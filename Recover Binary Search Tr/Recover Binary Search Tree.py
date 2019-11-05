# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        it = self.isValidBST(root)
        a, b = next(it)
        c = next(it, None)
        if c:
            _, c = c
            a.val, c.val = c.val, a.val
        else:
            a.val, b.val = b.val, a.val
        return root

    def isValidBST(self, root):
        pre, cur, stack = None, root, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            s = stack.pop()
            if pre and s.val <= pre.val:
                yield pre, s
            pre, cur = s, s.right
        