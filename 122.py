from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        former_local_low = 9999999
        former_price = -1
        for price in prices:
            if price < former_price:
                if former_price > former_local_low:
                    ans += (former_price - former_local_low)
                    former_local_low = price
            if former_local_low>price:
                former_local_low = price
            former_price = price
        
        if former_price > former_local_low:
            ans += (former_price - former_local_low)

        return ans
    

print(
    Solution().maxProfit(
        [1,2,3,4,5]
    )
)