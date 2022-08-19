# Time: O(n^2) | Space: O(1)
def threeSum(nums):
    # 2 pointer approach just like 2 sum II
    # sort and fix first element
    # go through with 2 pointers l and r for the next two elements that satisfy the zero sum
    nums.sort()
    output = []
    for i,num in enumerate(nums):
        # eliminate duplicates with first number
        if i > 0 and num == nums[i-1]:
            # check if previous number was same
            continue
        left = i + 1
        right = len(nums) - 1
        # prepare for left and right pointer implementation
        while left < right:
            threeSum = num + nums[left] + nums[right]
            if threeSum < 0:
                # if sum < 0, since array is sorted, we need to inc left ptr
                # to make the sum bigger i.e., closer to target
                left += 1
            elif threeSum > 0:
                # similarly, decrement right ptr
                right -= 1
            else:
                # get candidate in output
                output.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                # this is to take care of duplicate left pointers in list
                # duplicate right pointers will already be taken care of in the logic above as it goes into the elif part
        return output

if __name__ == "__main__":
    nums = [-3,3,4,-3,1,2]
    print("3 Sum is: ", threeSum(nums)) 
