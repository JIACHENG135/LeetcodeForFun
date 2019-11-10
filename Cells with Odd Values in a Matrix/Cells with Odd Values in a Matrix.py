class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        r,c = collections.defaultdict(int),collections.defaultdict(int)
        for i,j in indices:
            r[i] += 1
            c[j] += 1
        odd = 0
        for i in range(n):
            for j in range(m):
                if (r[i] + c[j])%2:
                    odd += 1
        return odd