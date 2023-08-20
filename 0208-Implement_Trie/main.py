# first(?) leetcode problem where there were no bugs upon first run B)

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        ended = False
        for char in word:
            if ended or char not in cur:
                cur[char] = {}
                ended = True
            cur = cur[char]
        cur[" "] = {}

    def search(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if char in cur:
                cur = cur[char]
            else:
                return False
        return " " in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for char in prefix:
            if char in cur:
                cur = cur[char]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)