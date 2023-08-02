from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return False
        dp = [False for i in range(400)]
        for i in range(len(s)):
            for word in wordDict:
                if (i >= len(word) -1) and (word == s[i+1-len(word):i+1]):
                    if (i-len(word) == -1) or (dp[i-len(word)]):
                        dp[i] = True
        return dp[len(s)-1]
    
print(
    Solution().wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
    )
)