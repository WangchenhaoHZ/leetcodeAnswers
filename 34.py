from typing import List

def strict_lower_bond(nums,h,t,target):
    if h==t:
        return h
    m = (h+t+1)//2
    if nums[m-1] >= target: return strict_lower_bond(nums,h,m-1,target)
    if (nums[m-1] < target) and (target <= nums[m]): return m-1
    if target > nums[m]: return strict_lower_bond(nums,m,t,target)
    
def strict_upper_bond(nums,h,t,target):
    if h==t:
        return h
    m = (h+t+1)//2
    if nums[m-1] > target: return strict_upper_bond(nums,h,m-1,target)
    if (nums[m-1] <= target) and (target < nums[m]): return m
    if target >= nums[m]: return strict_upper_bond(nums,m,t,target)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        if nums[0]>target: return [-1,-1]
        elif nums[0]==target: l=-1
        else: l = strict_lower_bond(nums,0,len(nums)-1,target)
        if nums[-1]<target: return [-1,-1]
        elif nums[-1]== target: u = len(nums)
        else: u = strict_upper_bond(nums,0,len(nums)-1,target)
        if u-1 >= l+1: return [l+1, u-1]
        else: return [-1,-1]

print(
    Solution().searchRange(
        nums = [], target = 8
    )
)