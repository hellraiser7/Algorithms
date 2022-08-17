def longestConsecutive_Sort(nums):
    # first solution: sorting nums and iterating through set
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    ####
    longestStreak = 1
    currentStreak = 1
    nums1 = list(set(nums))
    nums1.sort()

    for i in range(len(nums1)-1):
        if nums1[i] == nums1[i+1] - 1:
            currentStreak += 1
        else:
            longestStreak = max(currentStreak, longestStreak) # get new max if streak ends
            currentStreak = 1 # reinitialize to prepare for the next sequence
    
    # to take care of a corner case where the current streak goes on till end of the loop
    # and that streak is greater than the curren longest streak since it doesn't go to the else part for the last element
    # hence we need to return maximum of those two in order to eliminate any ambiguity
    return max(longestStreak, currentStreak)

# Time: O(n) | Space: O(n)
def longestConsecutiveOptimized(nums):
    # use numsSet, but check the starting element for the sequence
    # iterate, and if the element does not have a number at the left which is one lesser than itself, it is a starting element
    # then iterate from this starting element, keep checking if next consecutive element exists or not
    # if it does, then keep incrementing local length
    numsSet = set(nums)
    longestStreak = 0
    for i in range(len(nums)):
        # check if starting ele
        if (nums[i]-1) not in numsSet:
            currentStreak = 0
            while (nums[i] + currentStreak) in numsSet:
                currentStreak += 1
            longestStreak = max(longestStreak, currentStreak)

    return longestStreak
if __name__ == "__main__":
    nums = [100,200,4,300,7,6,5]
    print("longest consecutive sequence: ", longestConsecutive_Sort(nums))
    print("longest consecutive sequence with optimization: ", longestConsecutiveOptimized(nums))
