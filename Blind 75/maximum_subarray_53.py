class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadanes: max(currentElement, previousMaxSum + currentElement)
        max1 = nums[0]
        maxArray = [0]*len(nums)
        maxArray[0] = nums[0]
        for i in range(1, len(nums)):
            # do I extend the previous answer or take a new subarray starting at current element
            maxArray[i] = max(nums[i], maxArray[i-1] + nums[i])
            if maxArray[i] >= max1:
                max1 = maxArray[i]
        return max1
            
        
                
        
