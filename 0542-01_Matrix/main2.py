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

            if (not (0 <= i <= len(mat) - 1)) or (not (0 <= j <= len(mat[0]) - 1)):
                continue

            parents = []
            for (a, b) in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
                if (a, b) in updated:
                    parents.append(mat[a][b])
                else:
                    if (a, b) not in queue:
                        queue.append((a, b))

            if mat[i][j] == 1:
                mat[i][j] = min(parents) + 1
            else:
                mat[i][j] = 0

            updated.add((i, j))

            print((i, j))
            print(mat)
            print(queue)
            print(updated)

            print("**************")

        return mat

print('\033c')    
solution = Solution()
print(solution.updateMatrix([[0,0,0],
                             [0,1,0],
                             [1,1,1]]))