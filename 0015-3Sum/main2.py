from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        idx_map = defaultdict(set)
        ans = []
        used = set()
        for i in range(len(nums)):
            idx_map[nums[i]].add(i)
            for j in range(i+1, len(nums)):
                cand_idx = idx_map[-(nums[i] + nums[j])]
                trip = tuple(sorted([nums[i], nums[j], -(nums[i] + nums[j])]))
                print((i, j), cand_idx)
                if trip not in used and len(cand_idx - {i, j}) == len(cand_idx) > 0:
                    ans.append([nums[i], nums[j], -(nums[i] + nums[j])])
                    used.add(trip)
        print(idx_map)
        return ans
    
print('\033c')
solution = Solution()
print(solution.threeSum([0,0,0]))


