from typing import List
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        index_stack = deque()
        for index, temperature in enumerate(temperatures):
            while (len(index_stack) > 0) and (temperatures[index_stack[-1]] < temperature):
                answers[index_stack[-1]] = index - index_stack[-1]
                index_stack.pop()
            index_stack.append(index)
        return answers


print(Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))