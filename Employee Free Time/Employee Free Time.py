"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import functools
class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: list<list<Interval>>
        :rtype: list<Interval>
        """
        intervalsMap = {}
        for intervals in schedule:
            for i in intervals:
                if i.start in intervalsMap:
                    intervalsMap[i.start] = Interval(i.start,max(i.end,intervalsMap[i.start].end))
                else:
                    intervalsMap[i.start] = i
                    
        def getFree(inters):
            free = []
            if len(inters)>0:
                start = inters[0].end
                for i in inters[1:]:
                    free.append(Interval(start,i.start))
                    start = i.end
            return free
        
        def merge(intervals):
            res = []
            for i in intervals:
                if not res:
                    res.append(i)
                else:
                    ma,mi = max(res[-1].start,i.start),min(res[-1].end,i.end)
                    if ma<=mi:
                        res[-1].end = max(res[-1].end,i.end)
                    else:
                        res.append(i)
            return getFree(res)
        
        return merge([intervalsMap[key] for key in sorted(intervalsMap.keys())])
        