class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        
        # sort all intervals by start time
        intervals = []
        for timeSlots in schedule:
            for timeSlot in timeSlots:
                intervals.append(timeSlot)
        
        intervals.sort(key= lambda x: x.start)
        
        # Maintain left and right pointer pointing to the interval
        left = right = 0
        commonFree = []
        
        # iterate through intervals with left pointer
        # if left.start > right.end, append the common free time to the ans
        # else, assign right to the lastest-ended intervals we heve visited so far.
        while left < len(intervals) - 1:
            left += 1
            if intervals[left].start > intervals[right].end:
                commonFree.append(Interval(intervals[right].end,intervals[left].start))
                right = left
            else:
                if intervals[left].end > intervals[right].end:
                    right = left
        return commonFree