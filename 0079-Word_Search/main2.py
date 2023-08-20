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

        def dfs(node, searched):
            i, j, idx = node
            if idx == len(word) - 1:
                print(f'{(i, j, idx)} returns True')
                return True
            recs = []
            for dx, dy in Solution.dirs:
                if 0 <= i+dx < len(board) and 0 <= j+dy < len(board[0]):
                    print(f"board at {(i+dx, j+dy, idx+1)} is {board[i+dx][j+dy]}")
                if 0 <= i+dx < len(board) and 0 <= j+dy < len(board[0])\
                    and board[i+dx][j+dy] == word[idx+1] and (i+dx, j+dy) not in searched:
                    print('searching above')
                    recs.append(dfs((i+dx, j+dy, idx+1), searched | {(i+dx, j+dy)}))
            return any(recs)

        for node in search_init:
            if dfs(node, {node[:-1]}):
                return True

        return False
    
print('\033c')
print(Solution().exist(board = [["A","B","C","E"],
                                ["S","F","E","S"],
                                ["A","D","E","E"]], word = "ABCESEEEFS"))
print()
print(Solution().exist(board=[['a', 'a']], word='aaa'))