from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(dist, node):
            neighbors = []
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    neighbors.append(dfs(dist+1, neighbor))

            if len(neighbors) == 0:
                return dist, node

            return max(neighbors)
        
        def dfs_path(dist, path, node):
            neighbors = []
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    neighbors.append(dfs_path(dist+1, path + [neighbor], neighbor))

            if len(neighbors) == 0:
                return dist, path, node
            
            return max(neighbors)

        
        seen = {0}
        _, point1 = dfs(0, 0)
        seen = {point1}
        _, longest_path, _ = dfs_path(0, [point1], point1)

        return longest_path[(len(longest_path)-1)//2:len(longest_path)//2+1]

print('\033c')
print(Solution().findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))