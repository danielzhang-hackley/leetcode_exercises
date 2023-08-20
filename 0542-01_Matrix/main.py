from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = {}
        def get_dist(i, j):
            print('inspecting', (i, j))
            if (i, j) in dist:
                return dist[(i, j)]
            if i < 0 or i > len(mat) - 1 or j < 0 or j > len(mat[0]) - 1:
                return 10002
            if mat[i][j] == 0:
                dist[(i, j)] = 0
                return 0
            dist[(i, j)] = 1 + min(
                get_dist(i-1, j), get_dist(i+1, j), get_dist(i, j-1), get_dist(i, j+1)
            )
            return 1 + min(get_dist(i-1, j), get_dist(i+1, j), get_dist(i, j-1), get_dist(i, j+1))
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print((i, j), dist)
                mat[i][j] = get_dist(i, j)

        return mat

print('\033c')    
solution = Solution()
print(solution.updateMatrix([[0,0,0],[0,1,0],[0,1,0]]))
