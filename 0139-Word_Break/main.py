from typing import List
from collections import defaultdict

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

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lengths = defaultdict(list)

        for word in wordDict:
            lengths[len(word)].append(word)

        sols = [False for _ in range(len(s)+1)]  # array of bool, indicating if lenght i is possible
        sols[0] = True

        for i in range(len(s)):
            for j in range(i+1):
                for word in lengths[i-j+1]:
                    if word == s[j:i+1] and sols[j]:
                        sols[i+1] = True
                        break
                else:
                    continue
                break
        return sols[-1]
    
print('\033c')
print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))