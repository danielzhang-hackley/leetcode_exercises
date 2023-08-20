from typing import List
from collections import deque

class Solution:
    dirs = ((0,1), (1,0), (0,-1), (-1,0))

    def exist(self, board: List[List[str]], word: str) -> bool:
        search_init = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    search_init.append((i, j, 0))

        # print(search_init)
        for start in search_init:
            s = deque([start])
            searched = set()
            # print(f'starting search with {(s[0][0], s[0][1])}')
            while s:
                i, j, idx = s.pop()
                searched.add((i, j))
                if idx == len(word) - 1:
                    return True
                for dx, dy in Solution.dirs:
                    # if 0 <= i+dx < len(board) and 0 <= j+dy < len(board[0]):
                        # print(f"board at {(i+dx, j+dy)} is {board[i+dx][j+dy]}")
                    if 0 <= i+dx < len(board) and 0 <= j+dy < len(board[0])\
                        and board[i+dx][j+dy] == word[idx+1] and (i+dx, j+dy) not in searched:
                        s.append((i+dx, j+dy, idx+1))
                        # print(f"above added (char at idx {idx+1})")

        return False
    
print('\033c')
print(Solution().exist(board = [["A","B","C","E"],
                                ["S","F","E","S"],
                                ["A","D","E","E"]], word = "ABCESEEEFS"))