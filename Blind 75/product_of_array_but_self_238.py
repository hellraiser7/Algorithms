class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1 = []
        prod, zeroCount, zeroIndex = 1,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
                zeroIndex = i
            else:
                prod *= nums[i]
        
        if zeroCount == 1:
            nums1 = [0]*len(nums)
            nums1[zeroIndex] = prod
            return nums1
        elif zeroCount > 1:
            return [0]*len(nums)
        
        for ele in nums:
            #remove element
            nums1.append(prod//ele)
        return nums1
