# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        g = collections.defaultdict(set)
        
        q = collections.deque([root])
        
        leaf = set()
        while q:
            cur = q.popleft()
            if not cur.left and not cur.right:
                leaf.add(cur.val)
                
            if cur.left:
                g[cur.val].add(cur.left.val)
                g[cur.left.val].add(cur.val)
                q.append(cur.left)
            if cur.right:
                g[cur.val].add(cur.right.val)
                g[cur.right.val].add(cur.val)
                q.append(cur.right)
        
        q = collections.deque([k])
        visited = set()
        while q:
            cur = q.popleft()
            visited.add(cur)
            if cur in leaf:
                return cur
            else:
                for nei in g[cur]:
                    if nei not in visited:
                        q.append(nei)
        
                
                
        
        