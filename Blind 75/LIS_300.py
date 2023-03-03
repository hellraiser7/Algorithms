class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            # from end to beginning
            for j in range(i+1, len(nums)):
            # check for each element, if the next element(s) are bigger or not
            # if bigger, then we can extend the LIS by one
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
