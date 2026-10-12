class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # create array one larger than the amount and populate with same value
        dp = [amount + 1] * (amount + 1)
        # set first value to zero
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                # for every amount up to the goal check if there's a coin bigger
                #   than the current amount
                if i - c >= 0:
                    # set the amount of ways to be for the largest possible coin
                    dp[i] = min(dp[i], 1 + dp[i - c])
        # can't have partial coins so checking amount + 1 tells if it's impossible
        return dp[amount] if dp[amount] != amount + 1 else -1
