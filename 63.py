from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0: dp[i][0] = 1
            else: break
        for i in range(n):
            if obstacleGrid[0][i] == 0: dp[0][i] = 1
            else: break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1: continue
                if obstacleGrid[i-1][j] == 0: dp[i][j] += dp[i-1][j] 
                if obstacleGrid[i][j-1] == 0: dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]
    
print(
    Solution().uniquePathsWithObstacles(
        obstacleGrid = [[1,0]]
    )
)