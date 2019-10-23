# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        ans = [[root.val]]
        start = 1
        while q:
            level = collections.deque()
            tmp = []
            start*=-1
            while q:
                cur = q.popleft()
                
                if cur.left:
                    level.append(cur.left)
                    tmp.append(cur.left.val)
                if cur.right:
                    tmp.append(cur.right.val)
                    level.append(cur.right)
            if level:
                q = level
                ans.append(tmp[::start])
        return ans
            