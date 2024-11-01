from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pair_index_list: list[list] = [[] for i in range(len(wordList))]
        i_endword = -1
        for i, word in enumerate(wordList):
            if word == endWord:
                i_endword = i
                break
        if i_endword == -1: return 0
        for i, word_a in enumerate(wordList):
            for j_, word_b in enumerate(wordList[i+1:]):
                j = j_ + i + 1
                n_diff = 0
                for char1,char2 in zip(word_a,word_b):
                    if char1 != char2: 
                        n_diff += 1
                    if n_diff > 1: break
                if n_diff == 1:
                    pair_index_list[i].append(j)
                    pair_index_list[j].append(i)
        
        queue = []
        ans = 2
        for i, word in enumerate(wordList):
            n_diff = 0
            for char1, char2 in zip(word, beginWord):
                if char1 != char2: 
                    n_diff += 1
                if n_diff > 1: break
            if n_diff == 1:
                if i == i_endword: return ans
                queue.append(i)
        i_start = 0
        i_end = len(queue) - 1
        while i_start<= i_end:
            ans +=1
            for i_present in queue[i_start:i_end+1]:
                for i_next in pair_index_list[i_present]:
                    if not (i_next in queue):
                        if i_next == i_endword: return ans
                        queue.append(i_next)
            i_start = i_end+1
            i_end = len(queue) - 1
        return 0
                
print(
    Solution().ladderLength(
        beginWord = "a", endWord = "c", wordList = ["a","b","c"]
    )
)