class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        bd = set()
        for i in range(r):
            if grid[i][0] == 0:
                bd.add((i,0))
            if grid[i][-1] == 0:
                bd.add((i,c-1))
        for j in range(c):
            if grid[0][j] == 0:
                bd.add((0,j))
            if grid[-1][j] == 0:
                bd.add((r-1,j))
        
        
        def expand(i,j):
            grid[i][j] = 1
            for x,y in [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]:
                if -1<x<r and -1<y<c and grid[x][y] == 0:
                    expand(x,y)
        for i,j in bd:
            expand(i,j)
        ccn = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    ccn += 1
                    expand(i,j)
        return ccn
            