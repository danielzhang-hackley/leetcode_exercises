from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        checked = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in checked:
                    n_islands += 1
                    s = deque([(i, j)])
                    while s:
                        node = s.pop()
                        for dx, dy in dirs:
                            if 0 <= node[0]+dx < len(grid) and \
                               0 <= node[1]+dy < len(grid[0]) and \
                               grid[node[0]+dx][node[1]+dy] == "1" and \
                               (node[0]+dx, node[1]+dy) not in checked:
                                checked.add((node[0]+dx, node[1]+dy))
                                s.append((node[0]+dx, node[1]+dy))
        return n_islands
    
print('\033c')
print(Solution().numIslands([["1","1","0","0","0"],
                             ["1","1","0","0","0"],
                             ["0","0","1","0","0"],
                             ["0","0","0","1","1"]]))