class Solution:
    def rob(self, nums: List[int]) -> int:
        # start at $0 since no houses have been robbed
        sum1, sum2 = 0, 0

        # for each house $ amount
        for n in nums:
            # get highest of this house plus previous total or current total
            tmp = max(n + sum1, sum2)
            # set previous total to current total
            sum1 = sum2
            # set current total to highest value
            sum2 = tmp
        # return current total, which is now the highest value possible
        return sum2