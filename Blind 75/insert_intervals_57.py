class Solution:
    def insert(self, intervals, newInterval):
        # TC: O(n)
        # check if the newInterval is overlapping with anyone, if yes, then merge it with first overlapping interval
        # Keep merging it till we find an interval that is non-overlapping. Then only push the merged one into the output array
        output = []
        inserted = False # keep track of whether the merged interval has been inserted or not
        # if already inserted, we just take care of the rest of the array in the output
        def isOverlapping(newInterval, interval):
            if newInterval[1] >= interval[0] and newInterval[0] <= interval[1]:
                return True
            return False

        for interval in intervals:
            if isOverlapping(newInterval,interval):
                newInterval = [min(newInterval[0],interval[0]), max(newInterval[1], interval[1])]
                #print(newInterval[0], newInterval[1])
                continue
            # check to take care newInterval is merged at right place
            if not inserted and newInterval[0] < interval[0]:
                output.append(newInterval)
                inserted = True
            output.append(interval)
        
        # handle case where merged interval is the last interval in the input array
        if not inserted:
            output.append(newInterval)
        return output


S = Solution()
print(S.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
