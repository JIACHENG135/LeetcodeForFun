class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        r,c = len(grid),len(grid[0])
        ccn,cc = 0,collections.defaultdict(int)
        ccnMap = {}
        
        ctv = set()
        def dfs(x,y,cnn):
            cc[ccn] += grid[x][y]
            ccnMap[(x,y)] = ccn
            tmp = grid[x][y]
            grid[x][y] = 0
            ctv.add((x,y))
            for i,j in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
                if -1<i<r and -1<j<c and grid[i][j]:
                    dfs(i,j,cnn)

            grid[x][y] = tmp

        ans = 0
        def maxPath(x,y,cur):
            nonlocal ans
            ans = max(ans,cur)
            tmp = grid[x][y]
            grid[x][y] = 0
            
            for i,j in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
                if -1<i<r and -1<j<c and grid[i][j]:
                    maxPath(i,j,cur+grid[i][j])
            grid[x][y] = tmp


        visited = set()

        for i in range(r):
            for j in range(c):
                if grid[i][j] and (i,j) not in ctv:
                    ccn += 1
                    dfs(i, j, 0)

        wait = sorted([[i,j] for i in range(r) for j in range(c) if grid[i][j]],key=lambda x:cc[ccnMap[(x[0],x[1])]],reverse=True)
        for i,j in wait:
            visited = set()
            if grid[i][j] and ccnMap[(i,j)] not in visited:
                if cc[ccnMap[(i,j)]]>ans:
                    maxPath(i, j, grid[i][j])
                visited.add(ccnMap[(i,j)])


        return ans

        