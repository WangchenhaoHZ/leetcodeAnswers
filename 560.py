from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        i_start = 0
        sum = 0
        for i_end, num in enumerate(nums):
            sum += num
            while sum > k:
                sum -= nums[i_start]
                i_start += 1
            if sum == k and (i_end>=i_start):
                answer += 1
        return answer

print(Solution().subarraySum(nums = [-1,-1,0], k = 0))