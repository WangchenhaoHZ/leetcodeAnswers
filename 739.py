from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        index_stack = []
        for index, temperature in enumerate(temperatures):
            while (index_stack != []) and (temperatures[index_stack[-1]] < temperature):
                answers[index_stack[-1]] = index - index_stack[-1]
                index_stack.pop()
            index_stack.append(index)
        return answers


Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70])