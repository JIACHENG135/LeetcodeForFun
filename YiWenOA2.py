import copy
def alive_count(self, grid, x, y):
    n, m = len(grid), len(grid[0])
    dir_x = [0,0,1,1,1,-1,-1,-1]
    dir_y = [1,-1,0,1,-1,0,1,-1]
    count = 0
    
    for i in range(len(dir_x)):
        tempx = dir_x[i] + x
        tempy = dir_y[i] + y
        if tempx >= 0 and tempx < n and tempy >= 0 and tempy < m and grid[tempx][tempy] == 1:
            count += 1
    return count

# Simulate K turns
def GridGame(self, grid, rules, k):
    n, m = len(grid), len(grid[0])
    def reverse(l):
        nonlocal grid

    
    return grid