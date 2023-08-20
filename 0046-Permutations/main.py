from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def solve(nums, n_perm):
            # n_perm = number of spots permuted
            if n_perm == 0:
                sol.append(nums)
                print(n_perm, nums)
                return [nums]
            
            prev = solve(nums, n_perm - 1)
            print(n_perm, prev)
            new = []
            next_idx = n_perm  # the idx of the element to be moved around
            for perm in prev:
                for i in range(n_perm):
                    new.append(perm[:i] + perm[i:n_perm+1] + perm[n_perm+2:])
            
            sol.extend(new)
            print(n_perm, new)
            return new
        
        solve(nums, len(nums))
        

        return sol
        
print('\033c')
print(Solution().permute([1, 2, 3]))

            