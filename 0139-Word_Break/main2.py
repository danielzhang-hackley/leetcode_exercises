from typing import List

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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)

        dp = [False for _ in range(len(s)+1)]  # array of bool, indicating if length i is possible
        dp[0] = True

        for i in range(len(s)):
            for j in range(i+1):
                if trie.search(s[j:i+1]) and dp[j]:
                    dp[i+1] = True
                    break
        return dp[-1]
    
print('\033c')
print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))