from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lenth = len(nums)
        left_sum = [0] * lenth
        right_sum = [0] * lenth
        for index in range(1,lenth):
            left_sum[index] = left_sum[index-1] + nums[index -1]
        for index in range(lenth-2, -1, -1):
            right_sum[index] = right_sum[index+1] + nums[index +1]
        for index in range(lenth):
            if left_sum[index] == right_sum[index]:
                return index
        return -1

print(
    Solution().pivotIndex(nums = [1,7,3,6,5,6])
)