from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1 = [0 for _ in range(len(prices))]
        # the max income that buy and sell before or at day i
        # i.e. the best buy-sell pair before or at day i
        # equals i) sell at day_i = price_i = min
        # or 2) the best buy-sell pair before or at day i-1 = dp1[i-1]
        m = 1000000 
        # m = min_price before price_i
        for i, price in enumerate(prices):
            if i > 0:
                dp1[i] = price - m
                dp1[i] = max(dp1[i], dp1[i-1])
            m = min(price, m)
        m = 0
        dp2 = [0 for _ in range(len(prices))]
        # the max income that buy and sell after or ar day i
        # m = max_price after price_i
        for i in range(len(prices)-1,-1,-1):
            price = prices[i]
            if i < len(prices) -1:
                dp2[i] = m - price
                dp2[i] = max(dp2[i],dp2[i+1])
            m = max(price, m)
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, dp1[i]+dp2[i])
        return ans
    
print(
    Solution().maxProfit(
        [3,3,5,0,0,3,1,4]
    )
)
        
            
# f = open("user.out", 'w')
# for line in stdin:
#     s = list(map(int, line.rstrip()[1:-1].split(',')))
#     buy1 = buy2 = float("inf")
#     profit1 = profit2 = 0
    
#     for price in s:
#         buy1 = min(buy1, price)
#         profit1 = max(profit1, price - buy1)
# the equivalent price for buy = price - former profit
#         buy2 = min(buy2, price - profit1)
#         profit2 = max(profit2, price - buy2)
#     print(profit2, file=f)
# exit(0)