class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        if not envelopes:
            return 0
        
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        res = []
        
        for envelope in envelopes:
            height = envelope[1]
            if not res or height > res[-1]:
                res.append(height)
            else:
                idx = self.find_upper_place(res, height)
                res[idx] = height
        
        return len(res)
    
    def find_upper_place(self, res, height):
        start, end = 0, len(res) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if res[mid] > height:
                end = mid
            else:
                start = mid
        
        if res[start] >= height:
            return start
        if res[end] >= height:
            return end
        return len(res)