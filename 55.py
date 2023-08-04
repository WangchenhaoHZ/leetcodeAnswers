from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        end = len(nums) - 1
        for present , num in enumerate(nums):
            if max_reach < present: return False
            max_reach = max(max_reach, present + num)
            if max_reach >= end: return True

print(
    Solution().canJump(
        nums = [0]
    )
)