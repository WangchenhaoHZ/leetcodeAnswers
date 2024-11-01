from typing import List
INF = 1000000
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        former_min = INF
        for price in prices:
            ans = max(ans, price - former_min)
            former_min = min(former_min, price)
        return ans
    
print(
    Solution().maxProfit(
        [7,1,5,3,6,4]
    )
)