class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        def getProduct(nums):
            prod = 1
            for i in range(len(nums)):
                prod *= nums[i]
            return prod
                
        for i in range(len(nums)):
            removed = nums.pop(i)
            prod = getProduct(nums)
            output.append(prod)
            # put it back in (thats what she said)
            nums.insert(i, removed)
        return output
