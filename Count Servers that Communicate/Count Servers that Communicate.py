class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = collections.Counter()
        col = collections.Counter()
        r,c = len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    if col[j]>1 or row[i]>1:
                        res += 1
        return res
        
#         m,n = len(grid),len(grid[0])
#         dad = [i for i in range(m*n*3)]
#         size = [1 for i in range(m*n*3)]
        
#         def root(x):
#             while dad[x]!=x:
#                 dad[x] = dad[dad[x]]
#                 x = dad[x]
#             return x
        
#         def union(x,y):
#             r1,r2 = map(root,[x,y])
#             if r1!=r2:
#                 size[r1] += size[r2]
#                 dad[r2] = r1
        
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]:
#                     union(i,251+j)
#                     union(j,251+i)
                    
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if size[251+i]>1 or size[251+j]>1:
#                     res += 1
#         return res
