# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        node,st = root,[]
        while node or st:
            while node:
                st.append(node)
                node = node.left
            node = st.pop()
            ans.append(node.val)
            node = node.right
        return ans