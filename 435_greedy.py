# greedy strategy: always pick the interval with earliest end
# The proof is in 6.046 L1, which is most obvious

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        INF = 100000
        ans = 0
        intervals.sort(key = lambda x:x[1])
        latest_end_time_selected = -INF
        for interval in intervals:
            start, end = interval
            if start >= latest_end_time_selected:
                latest_end_time_selected = end
                ans += 1
        return len(intervals) -  ans
    
print(
Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
)