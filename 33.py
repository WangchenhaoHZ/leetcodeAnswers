from typing import List

def pivot(nums, h, t):
    m = (h+t)//2
    if nums[m-1] > nums[m]: return m
    if h == t: return h
    if nums[h] > nums[m-1]: return pivot(nums, h, m-1)
    if nums[m] > nums[t]: return pivot(nums, m, t)

def find(nums, h, t, target):
    m = (h+t)//2
    if (h ==t) and (nums[h]==target): return h
    if nums[m-1] >= target: return find(nums, h, m-1, target)
    if (nums[m-1] < target) and (target < nums[m-1])

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = pivot(nums, 0, len(nums)-1)
        sorted_nums = nums[p:]
        for i in range(p):
            sorted_nums.append(nums[i])
        print(sorted_nums)


print(
    Solution().search(
        nums = [4,5,6,7,0,1], target = 0
    )
)