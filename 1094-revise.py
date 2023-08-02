from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diffs = []
        for num_pass, start, end in trips:
            diffs.append([start, num_pass])
            diffs.append([end, -num_pass])
        diffs.sort(key = lambda x : x[0])
        last_stop = 0
        total_pass = 0
        for stop, delta_pass in diffs:
            if last_stop != stop:
                if total_pass > capacity: return False
            total_pass += delta_pass
            last_stop = stop
        return True
    
print(
    Solution().carPooling(trips = [[4,5,6],[6,4,7],[4,3,5],[2,3,5]], capacity = 13)
)