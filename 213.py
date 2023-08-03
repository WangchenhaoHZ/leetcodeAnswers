from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        ans =0
        for i_forbid in [0, len(nums)-1]:
            no_forbid = nums[i_forbid+1:]
            no_forbid.extend(nums[:i_forbid])
            dp = [ [0 for _ in range(len(nums)-1)] for _ in range(2)]
            # dp[times][i_target] : choose at most #times# numbers and the last choice is nums[i_target]
            for times in range(len(nums)//2):
                for i_target, num in enumerate(no_forbid):
                    max_former = 0
                    if (times>0) and (i_target -2>=0):
                        for i_former in range(i_target -2 +1):
                            max_former = max(max_former, dp[(times-1)%2][i_former])
                    dp[(times)%2][i_target] = max(num + max_former, dp[(times-1)%2][i_target])
                    ans = max(ans, dp[times%2][i_target])
        return ans
    
print(
    Solution().rob(
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    )
)
                    