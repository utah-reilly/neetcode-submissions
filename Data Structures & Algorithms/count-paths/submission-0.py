class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # can do recursive with base case of hitting last row/column
        # store previously computed values for memo
        # how to do bottom up?
        # uses extra row of zeros to offset for addition
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]