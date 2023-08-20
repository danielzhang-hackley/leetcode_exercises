from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        procedure backtrack(P, c) is
        if reject(P, c) then return
        if accept(P, c) then output(P, c)
        s ← first(P, c)
        while s ≠ NULL do
            backtrack(P, s)
            s ← next(P, s)
        """
        candidates.sort()
        num_to_idx = {candidates[i]: i for i in range(len(candidates))}

        sol = []

        def backtrack(cur_sol):
            sum_sol = sum(cur_sol)
            if sum_sol > target:
                return
            if sum_sol == target:
                sol.append(cur_sol)
            for candidate in candidates[num_to_idx[cur_sol[-1]]:]:
                backtrack(cur_sol + [candidate])

        for candidate in candidates:
            backtrack([candidate])

        return sol
    
print('\033c')
print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))