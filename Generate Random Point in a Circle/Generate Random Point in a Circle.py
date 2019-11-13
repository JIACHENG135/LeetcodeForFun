import math
class Solution:

    def __init__(self, radius: float, x: float, y: float):
        self.r = radius
        self.x = x
        self.y = y
        

    def randPoint(self) -> List[float]:
        r = random.random()**0.5*self.r
        angle = random.uniform(0,math.pi*2)
        
        x = r*math.cos(angle)
        y = r*math.sin(angle)
        return [self.x+x,self.y+y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()