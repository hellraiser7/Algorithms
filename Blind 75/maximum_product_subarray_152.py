class Solution:
    # O(n) Time, O(1) Space
    def maxProduct(self, nums) -> int:
        curmax = curmin = res = nums[0]
        for num in nums[1:]:
            # include num, so we can reset when a 0 is encountered
            # when 0 is encountered, value of num will determine the next curMax or curMin as a 0 kills our streak
            curmax, curmin = max(curmax * num, curmin * num, num), min(curmax * num, curmin * num, num)
            res = max(res, curmax)
        return res

S = Solution()
print(S.maxProduct([-1,-2,-3]))
