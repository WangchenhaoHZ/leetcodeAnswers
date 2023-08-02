from typing import List
import time

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # t0=time.time()
        lenth =  len(heights)
        larger_prior_number_list = [0]
        for i in range(1,lenth,1):
            larger_prior_number = 0
            while heights[i] <= heights[i-larger_prior_number-1]:
                larger_prior_number += larger_prior_number_list[i-larger_prior_number-1] + 1
                if i-larger_prior_number-1 < 0: break
            larger_prior_number_list.append(larger_prior_number)
        # print(heights)
        # print(larger_prior_number_list)
        # t1= time.time()
        # print(t1-t0)
        larger_post_number_list:List[int] = [0] * lenth
        for i in range(lenth-2, -1, -1):
            larger_post_number = 0
            while heights[i] <= heights[i+larger_post_number+1]:
                larger_post_number += larger_post_number_list[i+larger_post_number+1] + 1
                if i+larger_post_number+1 > lenth-1: break
            larger_post_number_list[i] = larger_post_number
        # print(larger_post_number_list)
        # t2= time.time()
        # print(t2-t1)
        max = 0
        for i in range(lenth):
            present = heights[i] * (1 + larger_post_number_list[i]+larger_prior_number_list[i])
            if present > max:
                max = present
        return max


print(Solution().largestRectangleArea([2,1,5,6,2,3]))