class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        longest_substring_common_prefix_suffix_lenth_list = [0] * len(needle)
        for index, present_char in enumerate(needle):
            if index == 0: continue
            prefix_lenth = longest_substring_common_prefix_suffix_lenth_list[index - 1]
            while (prefix_lenth>0) and (present_char != needle[prefix_lenth]):
                # needle[prefix_lenth]: next char of prefix
                # the index of end element of prefix is prefix_lenth -1
                # the index of next char of prefix is prefix_lenth
                prefix_lenth = \
                    longest_substring_common_prefix_suffix_lenth_list[prefix_lenth-1]
            if present_char == needle[prefix_lenth]:
                prefix_lenth += 1
            longest_substring_common_prefix_suffix_lenth_list[index] = prefix_lenth
        
        match_lenth = 0
        for index, present_char in enumerate(haystack):
            while (match_lenth>0) and (present_char != needle[match_lenth]):
                match_lenth = longest_substring_common_prefix_suffix_lenth_list[match_lenth - 1]
            if present_char == needle[match_lenth]: match_lenth += 1
            if match_lenth == len(needle): break
        if match_lenth< len(needle):
            return -1
        else:
            return index - match_lenth+1