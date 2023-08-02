from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        total_passengers_at_locations = [0] * 1001
        for num_passengers, start, end in trips:
            for location in range(start, end):
                total_passengers_at_locations[location] += num_passengers
        for total_passengers in total_passengers_at_locations:
            if total_passengers > capacity:
                return False
        return True

print(
    Solution().carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4)
)