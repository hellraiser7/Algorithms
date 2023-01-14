class Solution:
    def rob(self, nums: List[int]) -> int:
        # use house robber 1 twice and calculate max of the two cases
        if len(nums) == 1:
            return nums[0]
        def house_robber1(nums):
            rob1, rob2 = 0,0 # max money to the house 1 step back, and 2 steps back
            for i in range(len(nums)):
                #include or don't include
                current = max(nums[i] + rob2, rob1)
                rob2 = rob1
                rob1 = current
            return current
        return max(house_robber1(nums[:-1]), house_robber1(nums[1:]))
