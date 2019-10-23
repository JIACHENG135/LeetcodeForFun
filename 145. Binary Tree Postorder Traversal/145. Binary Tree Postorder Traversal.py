# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        st1,st2= [root],[]
        ans = []
        while st1:
            cur = st1.pop()
            st2.append(cur)
            if cur.left:
                st1.append(cur.left)
            if cur.right:
                st1.append(cur.right)
        while st2:
            ans.append(st2.pop().val)
        return ans