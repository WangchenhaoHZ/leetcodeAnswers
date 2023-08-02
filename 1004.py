from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i_head = 0
        num_zero = 0
        max_len = 0
        for i_tail, tail, in enumerate(nums):
            if tail == 0: num_zero += 1
            while num_zero > k:
                if nums[i_head] == 0:
                    num_zero -= 1
                i_head += 1
            max_len = max(max_len, i_tail - i_head + 1)
        return max_len


print(
    Solution().longestOnes(nums = [0,1,1,0,0,0,1,1,1,1,0], k = 0)
)