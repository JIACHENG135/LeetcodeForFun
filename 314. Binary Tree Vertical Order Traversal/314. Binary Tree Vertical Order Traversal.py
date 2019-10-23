# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        def helper(root,depth=0):
            if not root:
                return depth
            return max(helper(root.left,depth+1),helper(root.right,depth+1))
        depth = helper(root)
        q = collections.deque([[root,depth]])
        res = collections.defaultdict(list)
        while q:
            cur,pos = q.popleft()
            res[pos].append(cur.val)
            if cur.left:
                q.append([cur.left,pos-1])
            if cur.right:
                q.append([cur.right,pos+1])
        ans = []
        for key in sorted(res.keys()):
            ans.append(res[key])
        return ans