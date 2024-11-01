from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        not_substring = [True for _ in range(2000)]
        words.sort(key= lambda x:len(x),reverse=True)
        for i_l, long_word in enumerate(words):
            for i_s in range(i_l+1, len(words)):
                if not not_substring[i_s]: continue
                short_word = words[i_s]
                if  len(short_word) > len(long_word):
                    continue
                if short_word == long_word[len(long_word)-len(short_word):]:
                    not_substring[i_s] = False
        ans = 0
        for i, word in enumerate(words):
            if not_substring[i]:
                ans += len(word) + 1
        return ans
                
print(
    Solution().minimumLengthEncoding(
        words = ["time", "me", "bell"]
    )
)