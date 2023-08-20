from typing import List
from heapq import heappush, heappushpop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = -(point[0]**2 + point[1]**2)
            if len(heap) >= k and dist > heap[0][0]:
                heappushpop(heap, (dist, point))
            elif len(heap) < k:
                heappush(heap, (dist, point))
        
        return [point for _, point in heap]
    

print('\033c')
solution = Solution()
print(solution.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))