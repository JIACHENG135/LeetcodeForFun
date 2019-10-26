import collections

def _copy(root, offset=0):
    if not root:
        return None
    node = TreeNode(root.val + offset)
    node.left= _copy(root.left, offset=offset)
    node.right =_copy(root.right, offset=offset)
    return node


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return None
        d = collections.defaultdict(list)
        d[0] = [None]
        for i in range(1, n+1):
            for k in range(1, i+1):
                for l in d[k-1]:
                    for r in d[i-k]:
                        root = TreeNode(k)
                        root.left = _copy(l)
                        root.right = _copy(r, offset=k)
                        d[i].append(root)
        return  d[n]
        