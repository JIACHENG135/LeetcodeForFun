class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        r,c = len(rooms),len(rooms[0])
        q = collections.deque()
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    q.append([i,j])
        while q:
            cx,cy = q.popleft()
            for i,j in [[cx+1,cy],[cx,cy+1],[cx-1,cy],[cx,cy-1]]:
                if -1<i<r and -1<j<c and rooms[i][j]==2**31-1:
                    rooms[i][j] = rooms[cx][cy] + 1
                    q.append([i,j])
        
                