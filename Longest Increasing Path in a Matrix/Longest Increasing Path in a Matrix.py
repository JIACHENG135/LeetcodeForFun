class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        mem = collections.defaultdict(int)
        r,c = len(matrix),len(matrix[0])
        ans = 0
        def dfs(x,y,cur):
            
            if (x,y) in mem:
                
                return mem[(x,y)]
            tmp = matrix[x][y]
            matrix[x][y] = -float("inf")
            s = 1
            for i,j in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
                if -1<i<r and -1<j<c and matrix[i][j]>tmp:
                    s = max(s,1+dfs(i,j,cur+1))
            matrix[x][y] = tmp
            mem[(x,y)] = s
            return s
            
        for i in range(r):
            for j in range(c):
                dfs(i,j,1)
        
        return max(mem.values())
                
        