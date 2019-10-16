class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        r,c = len(board),len(board[0])
        wait = collections.deque()
        for i in range(r):
            if board[i][0] == "O":
                wait.append([i,0])
            if board[i][-1] == "O":
                wait.append([i,c-1])
        for j in range(c):
            if board[0][j] == "O":
                wait.append([0,j])
            if board[-1][j] == "O":
                wait.append([r-1,j])
        visited = [[0 for i in range(c)]for j in range(r)]
        def dfs(x,y):
            nonlocal board
            board[x][y] = "Q"
            for i,j in [[x-1,y],[x,y-1],[x,y+1],[x+1,y]]:
                if -1<i<r and -1<j<c and board[i][j] == "O":
                    dfs(i,j)     
        while wait:
            x,y = wait.popleft()
            dfs(x,y)
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(r):
            for j in range(c):
                if board[i][j] == "Q":
                    board[i][j] = "O"