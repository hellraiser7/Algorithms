def missingNumber(nums):
    # here, we can sort the array and then when we iterate
    # return the element if not present
    nums.sort()
    for i in range(len(nums)):
        if (i != nums[i]):
            return i
    return

def missingNumberGenius(nums):
    # even better, to reduce the time complexity
    # we can calculate sum of all elements
    # and subtract this value from the natural number sum till n
    # we get the missing number
    n = len(nums)
    naturalSum = n*(n+1)//2 
    sum1 = sum(nums)
    return naturalSum - sum1

if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print("O(nlogn) solution: ", missingNumber(nums))
    print("O(n) solution: ", missingNumberGenius(nums))