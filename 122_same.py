INF = 1000000
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find out all the monotonic increasing interval
        ans = 0
        local_min = INF
        min_index = -1
        local_max = -INF
        for index, price in enumerate(prices):
            if price < local_min:
                local_min = price
                min_index = index
            if  (price > local_max) and (index > min_index):
                local_max = price
            else:
                if (local_min < local_max):
                    ans += local_max -local_min
                    local_min = price
                    min_index = index
                    local_max = -INF
                    
        if local_min < local_max:
            ans += local_max -local_min
        return ans
print(
    Solution().maxProfit(
        [7,1,5,3,6,4]
    )
)