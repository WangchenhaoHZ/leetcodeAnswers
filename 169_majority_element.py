# 从别人那里抄的o(n)算法

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = None
        counter = 0
        for num in nums:
            if counter == 0: answer = num
            if num == answer: counter +=1
            else: counter -= 1
        return answer
    
print(Solution().majorityElement(
    nums = [1,2,2,2,3,3,1,2]
))