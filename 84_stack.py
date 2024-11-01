from collections import deque

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        secesive_not_lower_number = [0] * len(heights)
        
        stack = deque()
        for index, height in enumerate(heights):
            while stack and (heights[stack[-1]] > height):
                former_lower_index = stack.pop()
                secesive_not_lower_number[former_lower_index] = index - former_lower_index - 1
            stack.append(index)
        while stack:
            index = stack.pop()
            secesive_not_lower_number[index] = len(heights) - 1 - index

        former_not_lower_number = [0] * len(heights)
        for index in range(len(heights)-1,-1,-1):
            height = heights[index]
            while stack and (heights[stack[-1]] > height):
                later_lower_index = stack.pop()
                former_not_lower_number[later_lower_index] = later_lower_index - index - 1
            stack.append(index)
        while stack:
            index = stack.pop()
            former_not_lower_number[index] = index
        ans = 0
        for index, number in enumerate(secesive_not_lower_number):
            ans = max(ans, heights[index]*(1+number + former_not_lower_number[index]))
        return ans
    
print(Solution().largestRectangleArea([2,1,2]))