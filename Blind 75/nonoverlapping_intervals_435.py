class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))        
        output = 0
        if len(intervals) == 0:
            return output
        newInterval = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if newInterval[1] > interval[0] and newInterval[0] < interval[1]:
                output += 1 # remove current interval
                # Update newInterval to the one with smaller end point
                if newInterval[1] > interval[1]:
                    newInterval = interval
            else:
                # no overlap, modify newInterval
                newInterval = interval
        return output
