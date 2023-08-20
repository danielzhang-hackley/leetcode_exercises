from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    root = (i, j)
                    break
            else:
                continue
            break

        queue = deque([root])
        parents = {root: set()}
        while len(queue) > 0:
            print(queue)
            (i, j) = queue.popleft()
            if mat[i][j] == 1:
                min_val = mat[parents[(i, j)][0][0]][parents[(i, j)][0][1]]
                for k in range(1, len(parents[(i, j)])):
                    if mat[parents[(i, j)][k][0]][parents[(i, j)][k][1]] < min_val:
                        min_val = mat[parents[(i, j)][k][0]][parents[(i, j)][k][1]]
                mat[i][j] = min_val + 1
            
            if i > 0:
                try:    parents[(i-1, j)].add((i, j))
                except: parents[(i-1, j)] = [(i, j)]
                queue.append((i-1, j))
            if i < len(mat) - 1:
                try:    parents[(i+1, j)].add((i, j))
                except: parents[(i+1, j)] = [(i, j)]
                queue.append((i+1, j))
            if j > 0:
                try:    parents[(i, j-1)].add((i, j))
                except: parents[(i, j-1)] = [(i, j)]
                queue.append((i, j-1))
            if j < len(mat[0]) - 1:
                try:    parents[(i, j+1)].add((i, j))
                except: parents[(i, j+1)] = [(i, j)]
                queue.append((i, j+1))

        return mat
    
print('\033c')    
solution = Solution()
print(solution.updateMatrix([[0,0,0],
                             [0,1,0],
                             [0,1,0]]))
