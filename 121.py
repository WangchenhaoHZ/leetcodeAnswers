from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        former_min = list(prices)
        later_max = list(prices)
        for i in range(1, len(prices)):
            former_min[i] =  min(former_min[i], former_min[i-1])
        for i in range(len(prices)-2,-1,-1):
            later_max[i] = max(later_max[i], later_max[i+1])
        for low, high in zip(former_min, later_max):
            ans = max(ans, high - low)
        return ans

print(
    Solution().maxProfit(
        [7,1,5,3,6,4]
    )
)