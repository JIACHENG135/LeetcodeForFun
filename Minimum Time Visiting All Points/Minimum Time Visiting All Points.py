class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        prevx,prevy = points[0][0],points[0][1]
        for x,y in points[1:]:
            res += max(map(abs,[x-prevx,y-prevy]))
            prevx,prevy = x,y
        return res
        