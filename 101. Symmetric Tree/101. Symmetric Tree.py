# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True 
        q = collections.deque([root])
        while q:
            newt = collections.deque()
            num = []
            # tmp = q
            while q:
                cur = q.popleft()
                if cur.left:
                    newt.append(cur.left)
                    num.append(cur.left.val)
                else:
                    num.append("#")
                if cur.right:
                    newt.append(cur.right)
                    num.append(cur.right.val)
                else:
                    num.append("#")
            for i in range(len(num)//2):
                if num[i]!=num[-(i+1)]:
                    return False
            q = newt
        return True