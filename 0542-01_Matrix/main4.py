from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        updated = set()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    updated.add((i, j))

        while len(queue) > 0:
            (i, j) = queue.popleft()
            if (i-1, j) not in updated and i > 0:
                updated.add((i-1, j))
                mat[i-1][j] = mat[i][j] + 1 if mat[i-1][j] == 1 else 0
                queue.append((i-1, j))
            if (i+1, j) not in updated and i < len(mat) - 1:
                updated.add((i+1, j))
                mat[i+1][j] = mat[i][j] + 1 if mat[i+1][j] == 1 else 0
                queue.append((i+1, j))
            if (i, j-1) not in updated and j > 0:
                updated.add((i, j-1))
                mat[i][j-1] = mat[i][j] + 1 if mat[i][j-1] == 1 else 0
                queue.append((i, j-1))
            if (i, j+1) not in updated and j < len(mat[0])-1:
                updated.add((i, j+1))
                mat[i][j+1] = mat[i][j] + 1 if mat[i][j+1] == 1 else 0
                queue.append((i, j+1))

        return mat

print('\033c')    
solution = Solution()
print(solution.updateMatrix([[0,0,0],
                             [0,1,0],
                             [1,1,1]]))