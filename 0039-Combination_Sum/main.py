# O(n^m) where n is the length of the array and m is the target value

from collections import defaultdict
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sols = defaultdict(list)

        # i is the intermediate target
        for i in range(2, target + 1):
            # j is the candidate we want to inspect for the current intermediate target
            for j in candidates:
                new_sols = []
                # k is are the solutions that we can add j to to make a solution for the intermediate target
                if i == j:
                    new_sols.append([j])
                else:
                    for k in sols[i - j]:
                        if j >= k[-1]:
                            new_sols.append(k + [j])
                if len(new_sols) > 0:
                    sols[i].extend(new_sols)
                
        return sols[target]
    
print('\033c')
print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))