class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        maxH = height.index(max(height))
        h = 0
        res = 0
        for i in range(maxH):
            h = max(h,height[i])
            if height[i]<h:
                res += h - height[i]
        h = 0
        for i in range(len(height)-1,maxH,-1):
            h = max(h,height[i])
            if height[i]<h:
                res += h-height[i]
        
        return res
            