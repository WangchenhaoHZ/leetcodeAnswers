from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        stack = []
        for interval in intervals:
            if stack:
                new_start, new_end = interval
                last_start, last_end = stack[-1]
                if new_start >= last_end:
                    stack.append(interval)
                else:
                    if new_end >= last_end:
                        continue
                    else:
                        stack.pop()
                        stack.append(interval)
            else:
                stack.append(interval)
        return len(intervals) - len(stack)

print(
    Solution().eraseOverlapIntervals(
        intervals = [[1,2],[1,2],[1,2]]
    )
)