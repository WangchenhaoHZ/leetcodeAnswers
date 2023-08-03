class Trie:

    def __init__(self):
        self.children = {}
        self.string = ""
        self.is_word = False
        
    def set_string(self, string):
        self.string = string

    def insert(self, word: str) -> None:
        if word:
            next_node:Trie = self.children.get(word[0], False)
            if next_node:
                next_node.insert(word[1:])
            else:
                next_node = Trie()
                next_node.set_string(self.string + word[0])
                self.children[word[0]] = next_node
                next_node.insert(word[1:])
        else:
            self.is_word = True
        

    def search(self, word: str) -> bool:
        if word:
            next_node:Trie = self.children.get(word[0], False)
            if next_node:
                return next_node.search(word[1:])
            else:
                return False
        else:
            return self.is_word
        

    def startsWith(self, prefix: str) -> bool:
        if prefix:
            next_node:Trie = self.children.get(prefix[0], False)
            if next_node:
                return next_node.startsWith(prefix[1:])
            else:
                return False
        else:
            return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))