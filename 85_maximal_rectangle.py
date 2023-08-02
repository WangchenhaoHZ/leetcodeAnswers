from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        lined_upper_block_table = []
        for _ in range(len(matrix)):
            lined_upper_block_table.append([0] * len(matrix[0]))
        for line_index, line in enumerate(matrix):
            for row_index, indicator in enumerate(line):
                if line_index == 0: 
                    lined_upper_block_table[0][row_index] = int(matrix[0][row_index])
                else:
                    if matrix[line_index][row_index] == '0': 
                        lined_upper_block_table[line_index][row_index] = int(indicator)
                    else:
                        lined_upper_block_table[line_index][row_index] = int(indicator) + lined_upper_block_table[line_index-1][row_index] 
        max = 0
        for  heights in lined_upper_block_table:
            lenth =  len(heights)
            larger_prior_number_list = [0]
            for i in range(1,lenth,1):
                larger_prior_number = 0
                while heights[i] <= heights[i-larger_prior_number-1]:
                    larger_prior_number += larger_prior_number_list[i-larger_prior_number-1] + 1
                    if i-larger_prior_number-1 < 0: break
                larger_prior_number_list.append(larger_prior_number)
            larger_post_number_list:List[int] = [0] * lenth
            for i in range(lenth-2, -1, -1):
                larger_post_number = 0
                while heights[i] <= heights[i+larger_post_number+1]:
                    larger_post_number += larger_post_number_list[i+larger_post_number+1] + 1
                    if i+larger_post_number+1 > lenth-1: break
                larger_post_number_list[i] = larger_post_number
            for i in range(lenth):
                present = heights[i] * (1 + larger_post_number_list[i]+larger_prior_number_list[i])
                if present > max:
                    max = present
        return max
print(
    Solution().maximalRectangle([["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]])
)