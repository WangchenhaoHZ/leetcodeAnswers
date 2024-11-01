from typing import List

def pivot(nums, h, t):
    if h == t: return h
    m = (h+t+1)//2
    if nums[m-1] > nums[m]: return m
    if (nums[h] > nums[m-1]): return pivot(nums, h, m-1)
    if nums[m] > nums[t]: return pivot(nums, m, t)

def find(nums, h, t, target): 
    if h == t:
        if (nums[h]==target): return h
        else: return -1
    m = (h+t+1)//2
    # when h<=t-1, this division ensures h<=m-1 and m<=t
    # which means [h..t] can always be divide into two part [h..m-1] amd [m..t]
    
    # the left case
    if nums[m-1] >= target: return find(nums, h, m-1, target)
    # the middle case
    if (nums[m-1] < target) and (target < nums[m]): return -1
    # the right case
    if target >= nums[m]: return find(nums, m, t, target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot(nums, 0, len(nums)-1)
        if nums[0]< nums[-1]:
            p = 0
        else:
            p = pivot(nums, 0, len(nums)-1)
        sorted_nums = nums[p:]
        for i in range(p):
            sorted_nums.append(nums[i])        
        index = find(sorted_nums, 0, len(nums)-1, target)
        if index == -1: return -1
        else: return (index + p) % len(nums)


print(
    Solution().search(
        nums = [1,3], target = 1
    )
)