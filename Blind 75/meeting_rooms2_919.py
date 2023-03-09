import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort(key=lambda x: x[0]) # sort the intervals by start time
        heap = [] # use a heap to keep track of the end times of meetings
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                # if the start time of the current interval is greater than or equal to the
                # end time of the earliest meeting that is still ongoing, then we can reuse that
                # meeting room and remove it from the heap
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        
        return len(heap) # the size of the heap corresponds to the number of meeting rooms needed

S = Solution()
print(S.minMeetingRooms([[0,30],[5,10],[15,20],[17,21],[31,33]]))
