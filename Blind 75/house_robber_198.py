class Solution:
    def rob(self, nums: list[int]) -> int:
        # if list has two elements or less, return the max of the two
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        arr = [0]*(len(nums))
        arr[0], arr[1] = nums[0], max(nums[:2])
        for i in range(2,len(nums)):
            arr[i] = max(nums[i] + arr[i-2], arr[i-1])
        return arr[len(nums)-1]
    
    def rob_opt(self, nums):
        # two pointers required only, rob1 and rob2
        # rob2 is 2 steps behind current pointer, and rob1 is one step behind current
        # initially, they are out of the array, hence 0,0
        rob1,rob2 = 0,0
        for i in range(len(nums)):
            current = max(nums[i] + rob2, rob1)
            # if you choose to steal the current house, add current house to the house two steps back
            # another one if you don't steal the current house, then you steal the house preceeding current
            # So the question is: steal current house or not, if yes, take rob2 with you since rob2 will have the last maximum cash grabbed two houses back
            # and if no, rob1 will have maxmoney from adjacent house, take max of both
            # now move the pointers a step ahead, rob2 becomes rob1, and rob1 becomes current
            rob2 = rob1
            rob1 = current
        return current

if __name__ == "__main__":
    S = Solution()
    nums = [2,7,9,3,1,4]
    print(S.rob(nums))
    print(S.rob_opt(nums))

