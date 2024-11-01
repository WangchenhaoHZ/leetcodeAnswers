class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_start = 0
        max_end = 0
        # dp[start][end]: length of Palindromic string of s[start][end]
        # if not the palindrome lenth dp[start][end] = 0
        # this solution can be modified to solve subsequence problem
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        # topological order: increasing substring length,
        # claim: if s[start][end] is palindromic only 
        # depend on if substring with shorter length is palindromic
        # proof: if s[start][end] is Palindromic, s[start+1][end-1] also is ▪️
        for length in range(len(s)+1):
            for start in range(len(s)+1 - length):
                end = start + length
                if length == 0:
                    dp[start][end] = 0
                elif length == 1:
                    dp[start][end] = 1
                else:
                    if (s[start] == s[end - 1]) and (dp[start+1][end-1] == end - start - 2):
                        dp[start][end] = dp[start+1][end-1] + 2
                # output updata
                if max_len < dp[start][end]:
                    max_len = dp[start][end]
                    max_start = start
                    max_end = end
        return s[max_start:max_end]
    
print (
    Solution().longestPalindrome(
        "aacabdkacaa"
    )
) 