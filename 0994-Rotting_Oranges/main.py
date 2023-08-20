from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    if 0 <= x+dx < len(grid) and 0 <= y+dy< len(grid[0]) and grid[x+dx][y+dy] == 1:
                        q.append((x+dx, y+dy))
                        grid[x+dx][y+dy] = 2
            if q: time += 1

        for row in grid:
            for ele in row:
                if ele == 1:
                    return -1
                    
        return time

print('\033c')
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))