class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0, 1, 1]
        for i in range(2, n+1):
            a[i % 3] = a[(i-1) % 3] + a[(i-2) % 3]
        return(a[n % 3])

print(
    Solution().fib(n=3)
)