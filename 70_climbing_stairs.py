class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 0: return 1
        # if n == 1: return 1
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        a = [1, 1, 2]
        for i in range(2, n+1):
            a[i % 3] = a[(i-1) % 3] + a[(i-2) % 3]
        return(a[n % 3])

print(
    Solution().climbStairs(n=38)
)