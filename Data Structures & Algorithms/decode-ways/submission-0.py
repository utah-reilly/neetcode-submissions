class Solution:
    def numDecodings(self, s: str) -> int:
        # 0 needs to have prefix
        # prefix has to be 1, or 2 for 0-6 suffix
        # 12720425
        # A B G T D B E
        # A B G T D Y
        # L G T D B E
        # L G T D Y

        dp = [1] * (len(s) + 1)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i + 1 < len(s) and (s[i] == '1' or 
                s[i] == '2' and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]

        return dp[0]
