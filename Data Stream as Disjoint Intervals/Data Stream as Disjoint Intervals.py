class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heap = []
    def addNum(self, val: int) -> None:
        self.heap.append((val,[val,val]))
        
    def getIntervals(self) -> List[List[int]]:
        
        stack = []
        heapq.heapify(self.heap) 
        while self.heap:
            idx, cur = heapq.heappop(self.heap)
            if not stack:
                stack.append((idx,cur))
            else:
                _,prev = stack[-1]
                
                if prev[1] +1 >= cur[0]:
                    prev[1] = max(cur[1],prev[1])
                else:
                    stack.append((idx,cur))
        self.heap = stack
        return list(map(lambda x:x[1],self.heap))