from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0 
        cnt = [0] * 5000
        cnt[0] = 1
        total_odd_num = 0
        # cnt[k] denotes the counts of proper initail segment has k odd nums
        for num in nums:
            if num % 2 == 1: total_odd_num +=1
            ans += cnt[total_odd_num - k]
            cnt[total_odd_num] += 1
        return ans
    
    
print(Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))