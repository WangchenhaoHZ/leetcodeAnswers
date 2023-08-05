from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0]* 2**31 + x[1])
        ans = 0
        former_shoot = - 2**31 -1
        for start, end in points:
            if start > former_shoot:
                ans +=1
                former_shoot = end
            # else:
            #     if end <former_shoot:
            #         former_shoot = end
        return ans


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the balloons by their end points in ascending order
        points.sort(key=lambda x: x[1])
        
        # Initialize the number of arrows needed and the end point of the last arrow
        arrows = 0
        last_end = float('-inf')
        
        # Iterate through the balloons
        for start, end in points:
            # If the current balloon starts after the end of the last arrow, shoot a new arrow
            if start > last_end:
                arrows += 1
                last_end = end
        
        return arrows

print(
    Solution().findMinArrowShots(
        [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
    )
)