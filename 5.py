class Solution:
    def longestPalindrome(self, s: str) -> str:
        # greedy strategy: if s[i:j] is palindrom, s[i+1:j-1] must be
        max = 1
        argmax = s[0:1]
        for i_mid in range(len(s)):
            for half_len in range(1, i_mid+1):
                i_start= i_mid - half_len
                i_end = i_mid + half_len
                if i_end > len(s): break
                if (2*half_len>max) and (s[i_start:i_mid] == s[i_end-1:i_mid-1:-1]) :
                    argmax = s[i_start:i_end]
                    max = 2*half_len
                if (2*half_len+1>max) and (s[i_start:i_mid] == s[i_end:i_mid:-1]) :
                    argmax = s[i_start:i_end+1]
                    max = 2*half_len +1
        return argmax
                


print (
    Solution().longestPalindrome(
        "bbb"
    )
) 
