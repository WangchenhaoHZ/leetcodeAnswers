class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        segment = ''
        maxlen = 0
        for index, char in enumerate(s):
            fomer_index_in_segment = segment.find(char)
            if fomer_index_in_segment == -1:
                segment += char
            else:
                segment = segment[fomer_index_in_segment+1:]+char
            if maxlen < len(segment):
                maxlen = len(segment)
        return maxlen

print(
    Solution().lengthOfLongestSubstring(s = "abcabcbb")
)