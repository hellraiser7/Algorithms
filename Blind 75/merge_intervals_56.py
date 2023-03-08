class Solution:
    def merge(self, intervals):
        # intervals = sorted(intervals, key = lambda x: x[0])
        # O(nlogn)
        output = []
        def isOverlapping(interval1, interval2):
            if interval2[0] <= interval1[1] and interval2[1]>=interval1[0]:
                return True
            return False
        newInterval = intervals[0]

        for interval in intervals[1:]:
            if isOverlapping(newInterval, interval):
                newInterval = [min(newInterval[0],interval[0]), max(newInterval[1],interval[1])]
            if newInterval[1] < interval[0]:
                output.append(newInterval)
                newInterval = interval
        if newInterval[0] == intervals[-1][0] and newInterval[1] == intervals[-1][1]:
            # coming out of the loop, we have to check if last element got appended or not
            output.append(intervals[-1])
        else:
            # if last element also was part of an overlap, we have not yet appended it
            # so consider that
            output.append(newInterval)
        return output
    def merge1(self, intervals):
        # same TC, just cleaner code
        # ONly 
        intervals.sort(key=lambda x: x[0])  # in-place sorting
        output = []
        for interval in intervals:
            if not output or output[-1][1] < interval[0]:
                # no overlap with previous interval, add new interval to output
                output.append(interval)
            else:
                # overlap with previous interval, merge current interval with previous interval
                output[-1][1] = max(output[-1][1], interval[1])
        return output

S = Solution()
print(S.merge1([[1,3],[3,5],[6,9],[9,10]]))

output = [[1,2],[3,4],[6,7],[9,10]]
