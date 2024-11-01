from typing import List

class Solution:
    def search(self,row_index,collumn_index, grid: List[List[str]]):
        grid[row_index][collumn_index] = "0"
        if (row_index>0) and (grid[row_index-1][collumn_index] == "1"):
            self.search(row_index-1,collumn_index, grid)
        if (collumn_index>0) and (grid[row_index][collumn_index-1] == "1"):
            self.search(row_index,collumn_index-1, grid)
        if (row_index < len(grid) - 1) and (grid[row_index+1][collumn_index] == "1"):
            self.search(row_index+1,collumn_index, grid)
        if (collumn_index < len(grid[0]) - 1) and (grid[row_index][collumn_index+1] == "1"):
            self.search(row_index,collumn_index+1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        island_num = 0
        for row_index in range(len(grid)):
            for collumn_index in range(len(grid[0])):
                if grid[row_index][collumn_index] == "1":
                    self.search(row_index, collumn_index, grid)
                    island_num += 1
        return(island_num)
    
print(
    Solution().numIslands( grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
)