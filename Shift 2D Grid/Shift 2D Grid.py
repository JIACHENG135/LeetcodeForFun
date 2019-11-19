class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r,c = len(grid),len(grid[0])
        res = [[0 for i in range(c)]for i in range(r)]
        
        for i in range(r):
            for j in range(c):
                waiti,waitj = ((i*c+j+k)%(r*c))//c,((i*c+j+k)%(r*c))%c
                res[waiti][waitj] = grid[i][j]
        return res