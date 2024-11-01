class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i_head = 0
        cost = 0
        max_len = 0
        for i_tail in range(len(s)):
            cost += abs(ord(s[i_tail]) - ord(t[i_tail]))
            while cost > maxCost:
                cost -= abs(ord(s[i_head]) - ord(t[i_head]))
                i_head +=1
            max_len = max(max_len, i_tail - i_head + 1)
        return max_len

print(
    Solution().equalSubstring(s = "abcd", t = "bcdf", maxCost = 3)
)