class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()

# 插入单词
words = ["apple", "app", "banana", "book", "books"]
for word in words:
    trie.insert(word)

# 搜索单词
print(trie.search("apple"))   # True
print(trie.search("app"))     # True
print(trie.search("grape"))   # False

# 查找以特定前缀开头的单词
print(trie.startsWith("app"))   # True
print(trie.startsWith("boo"))   # True
print(trie.startsWith("car"))   # False