from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        for index, word in enumerate(words):
            for root in dictionary:
                if (len(root)<len(words[index])) and (word[:len(root)] == root):
                     words[index] = root
        new_sentence = ''
        for index, word in enumerate(words):
            new_sentence += word
            new_sentence += ' '
        return new_sentence[:len(new_sentence)-1]

print(        
Solution().replaceWords(dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa")
)