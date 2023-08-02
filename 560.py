from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        sum = 0
        cnt = {}
        cnt[0] = 1 
        # cnt_k denotes the count of the proper inital segment has sum = k
        for num in nums:
            sum += num 
            # sum denote summation of proper all element including the present one
            if sum-k in cnt.keys():
                answer += cnt[sum - k]
                # count of the subarry sum = k, the last element of which must be present scaning one
                # which ensure there exists at least one element in the subarray
                # which equals to the count of the proper inital segment has a summation = sum - k
                
                #      sum
                # /-----^-----\
                # a  b  c  d  e
                # \--v--/ \-v-/
                # sum - k   k
                
            if sum in cnt.keys():
                cnt[sum] +=1
            else:
                cnt[sum] = 1
        return answer
    
print(
    Solution().subarraySum(
        [1], 0
    )
)