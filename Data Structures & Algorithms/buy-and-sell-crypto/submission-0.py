class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = prices[0]

        for r in prices:
            profit = max(profit, r - l)
            l = min(l, r)
            
        return profit