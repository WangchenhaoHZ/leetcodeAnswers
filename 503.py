from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lenth = len(nums)
        answer = [0] * lenth
        nums = nums * 2
        index_stack = []
        for index, num in enumerate(nums):
            while (index_stack != []) and (nums[index_stack[-1]]<num):
                if index_stack[-1]< lenth:
                    answer[index_stack[-1]] = nums[index]
                index_stack.pop()
            index_stack.append(index)
        while index_stack != []:
            if index_stack[-1]< lenth:
                answer[index_stack[-1]] = -1
            index_stack.pop()
        return answer

Solution().nextGreaterElements(nums = [3,1,2,3,4,])