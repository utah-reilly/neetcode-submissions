class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))

        # edge case
        if len(nums) == 1:
            return 1

        # check every int starting at end
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # check if current is less than any previous
                # add the previous LIS + 1 if it is
                # get max of possible LIS
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)