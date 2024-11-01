from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums == []: return -1
        head = 0
        total = 0
        min_len = 1000000
        for tail, num in enumerate(nums):
            total += num
            while total >= target:
                if min_len> tail - head + 1:
                    min_len = tail - head + 1
                total -= nums[head]
                head += 1
        if min_len == 1000000: return 0
        return min_len

print(    
Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3,100])
)