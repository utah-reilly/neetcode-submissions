class Solution:
    def rob(self, nums: List[int]) -> int:

        # edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(nums[0], self.rob_original(nums[1:]), self.rob_original(nums[:-1]))
    
    def rob_original(self, nums):
            sum1, sum2 = 0, 0

            for n in nums:
                temp = max(n + sum1, sum2)
                sum1 = sum2
                sum2 = temp
            
            return sum2