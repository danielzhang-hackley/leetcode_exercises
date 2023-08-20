from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(dist, node):
            farthest_node = node
            max_dist = dist
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    cand = dfs(dist+1, neighbor)
                    if cand[0] > max_dist:
                        max_dist = cand[0]
                        farthest_node = cand[1]
            return max_dist, farthest_node
        
        def dfs_path(node):
            longest_path = []
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    cur_path = dfs_path(neighbor)
                    if len(cur_path) > len(longest_path):
                        longest_path = cur_path
            longest_path.append(node)

            return longest_path

        
        seen = {0}
        _, point1 = dfs(0, 0)
        seen = {point1}
        longest_path = dfs_path(point1)

        return longest_path[(len(longest_path)-1)//2:len(longest_path)//2+1]

print('\033c')
print(Solution().findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))