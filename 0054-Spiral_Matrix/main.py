from typing import List

class Solution:
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        if len(matrix) == 1: return [ele for ele in matrix[0]]
        if len(matrix[0]) == 1: return [row[0] for row in matrix]
        
        outer_order = []
        i = j = 0

        for dx, dy in Solution.dirs:
            while 0 <= i+dx < len(matrix) and 0 <= j+dy < len(matrix[0]):
                outer_order.append(matrix[i][j])
                i += dx; j += dy
        
        submatrix = [row[1:-1] for row in matrix[1:-1]]
        outer_order.extend(self.spiralOrder(submatrix))
        
        return outer_order
    
print('\033c')
print(Solution().spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))