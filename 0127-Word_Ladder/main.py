from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def dist(s1, s2):
            res = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    res += 1
            return res

        graph = defaultdict(list)

        for i in range(len(wordList)):
            for j in range(i, len(wordList)):
                if dist(wordList[i], wordList[j]) == 1:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        visited = [False for _ in range(len(wordList))]
        q = deque([])


        return 0