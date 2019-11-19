# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        q = collections.deque([root])
        self.value = set()
        while q:
            cur = q.popleft()
            self.value.add(cur.val)
            if cur.left:
                cur.left.val = 2*cur.val+1
                q.append(cur.left)
            if cur.right:
                cur.right.val = 2*cur.val+2
                q.append(cur.right)
                

    def find(self, target: int) -> bool:
        return target in self.value


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)