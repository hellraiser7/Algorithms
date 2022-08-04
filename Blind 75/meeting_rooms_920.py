# leetcode premium, solved on lintcode

from calendar import c


def can_attend_meetings(intervals):
    intervals.sort(key=lambda i:i[0])
    # end time of current meeting must be lesser than the next start time
    for i in range(len(intervals)-1):
        # check for each meeting
        current_end_time = intervals[i][1]
        next_start_time = intervals[i+1][0]
        if (current_end_time > next_start_time):
            return False
    return True

if __name__ == "__main__":
    intervals = [(5,8),(9,15)]
    print(can_attend_meetings(intervals))