# state extension
# O(n)
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        INF = 1000000000
        dp = [[0  for _ in range(len(prices))] for _ in range(4)]
        sign = 1
        ans = 0
        for transaction in range(min(4, len(prices))):
            sign *= -1
            former_max = - INF
            if transaction == 0:
                for i in range(len(prices)):
                    dp[transaction][i] = - prices[i]
            else:
                former_max = dp[transaction-1][transaction-1]
                for i in range(transaction, len(prices)):
                    dp[transaction][i] = sign*prices[i] + former_max
                    former_max = max(former_max, dp[transaction-1][i])
                    if sign == 1: ans = max(ans, dp[transaction][i])
        return ans

print(
    Solution().maxProfit(
        [7,6,4,3,1]
    )
)