class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        
        for i in range(n):
            if i > max_reach: # cannot reach current index i
                return False
            max_reach = max(max_reach, i + nums[i])
        
        return True # all indices can be reached
S = Solution()
print(S.canJump([2,3,1,1,4])
