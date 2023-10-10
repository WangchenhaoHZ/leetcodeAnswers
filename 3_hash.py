class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        index_start = 0
        last_appear_lookup = dict()
        # hash table
        for index_end, char in enumerate(s):
            last_appear_index = last_appear_lookup.get(char, -1)
            if last_appear_index != -1: index_start = max(index_start, last_appear_index + 1)
            ans = max(ans, index_end-index_start + 1)
            last_appear_lookup[char] = index_end
        return ans

print(
    Solution().lengthOfLongestSubstring(s = "abba")
)

# intuition: the foremr substring of a sting without reapting, is the string without repeating

# in the loop we are try to figure out the index_s of each index_e
# base case: at the first letter, it is the longgest substring without reapting end at index_e = index_s = 0

# induction step: when we try to figure out if a next character at index_e +1 can be put into a former substring as a end
# there are two cases:

# 1: if the character does not appear after former index_start, the new character can be put in directly

# we claim the s[index_s, index_e +1] is the longest substring ends at index_e +1
# 
# proof: if the longest substring ends at index_e -1 and starts at index_s is the longgest unreaping string end at index_e -1
# the substring ended at index_e - 1 and starts at index_s -1 is not the longgest unreaping string end at index_e -1
# so character at index_s -1 must repeat betwen index_s and index_e -1
# or it does not exist as index_S is the first letter
# so character at index_s -1 must repeat betwen index_s and index_e or not exist
# so s[index_s, index_e +1] is the longest substring ends at index_e +1

# 2: if the character appears between index_s and index_e, at index_last_appear
# the substring of string without repeating characters has not repeating characters

# we claim the substring between index_s and index_e has no 2 same that character
# and thus s[index_last_appear+1, index_e +1] is the longest substring ends at index_e +1

# proof: s[index_s, index_e] is a string without repeating characters
# therefore s[index_last_appear+1, index_e +1] is a substring without repeating characters
# further s[index_last_appear, index_e +1] has two repeat character at begin and end,
# so it is not a substring without repeating characters
# therefore s[index_last_appear+1, index_e +1] is longest substring without repeating characters ends at index_e +1