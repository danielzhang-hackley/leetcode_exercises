from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True

        # keys are courses, values are the prequisites for that course
        parents = defaultdict(set)

        for prereq in prerequisites:
            parents[prereq[0]].add(prereq[1])
            parents[prereq[0]] |= parents[prereq[1]]
        
        rec_stack = deque()
        visited = set()

        # print(parents)
        
        def dfs(node):
            # print(node, rec_stack)
            for neighbor in parents[node]:
                # print(node, neighbor)
                if neighbor in rec_stack:
                    return False
                if neighbor not in visited:
                    rec_stack.append(neighbor)
                    visited.add(neighbor)
                    if not dfs(neighbor):
                        return False
            if len(rec_stack) > 0: rec_stack.pop()
            return True
        
        for node in parents:
            if not dfs(node):
                return False
            
        return True
                



print('\033c')
solution = Solution()
print(solution.canFinish(numCourses = 3, prerequisites = [[1,0],[2,2],[2,1]]))