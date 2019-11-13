class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:return 0
        parent = {}
        size = {}
        def root(v):
            while parent[v]!=v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v
        for i in nums:
            parent[i] = i
            parent[i+1] = i+1
            size[i] = 1
            size[i+1] = 1
        for i in nums:
            root2,root1 = map(root,[i,i+1])
            if root2!=root1:
                size[root1] += size[root2]
                parent[root2] = root1

        return max(size.values())-1