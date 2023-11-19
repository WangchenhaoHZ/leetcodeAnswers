from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1):
            steal = nums[i]
            if i-2 >= 0: steal += dp[i-2]
            not_steal = 0
            if i-1 >= 0: not_steal += dp[i-1]
            dp[i] = max(steal, not_steal)
        max_first = dp[len(nums)-2]
        dp = [0 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            steal = nums[i]
            if i-2 >= 1: steal += dp[i-2]
            not_steal = 0
            if i-1 >= 1: not_steal += dp[i-1]
            dp[i] = max(steal, not_steal)
        max_no_first = dp[len(nums)-1]
        return max(max_first, max_no_first)

print(
    Solution().rob( [1,2,3,1])
    )