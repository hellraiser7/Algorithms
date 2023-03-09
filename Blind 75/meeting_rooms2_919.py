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
    def minMeetingRooms1(self, intervals) -> int:
        # Using a normal list, now append and push towards back of array
        intervals = sorted(intervals, key=lambda x: x[0])  # sort intervals by start time
        rooms = []  # list of current meeting end times
        
        for interval in intervals:
            if rooms and rooms[-1] <= interval[0]:
                # if the earliest ending meeting ends before the current interval starts, reuse that room
                rooms.pop()
            rooms.append(interval[1])  # add the current meeting end time to the list of rooms
            
        return len(rooms)

S = Solution()
print(S.minMeetingRooms([[0,30],[5,10],[15,20],[17,21],[31,33]]))
