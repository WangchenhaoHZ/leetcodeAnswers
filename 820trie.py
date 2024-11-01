from typing import Optional, List

class Trie_node():
    
    def __init__(self, char, level: Optional[str]) -> None:
        self.char = char
        self.next_node = {}
        self.level = level
        
    def add_next(self, next_chr, next_node):
        self.next_node[next_chr] = next_node    
        
    def search(self):
        if self.next_node:
            ans = 0
            for chr, next_one in self.next_node.items():
                ans += next_one.search()
            return ans
        else:
            return 1 + self.level
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Trie_node("",0)
        for word in words:
            node = root
            for i_chr in range(len(word)-1,-1,-1):
                chr = word[i_chr]
                next_node = node.next_node.get(chr, False)
                if next_node:
                    node = next_node
                else:
                    next_node = Trie_node(chr + node.char, node.level+1)
                    node.add_next(chr, next_node)
                    node = next_node
        return root.search()
                
print(
    Solution().minimumLengthEncoding(
        words = ["time", "me", "bell", "atime", "btime"]
    )
)                