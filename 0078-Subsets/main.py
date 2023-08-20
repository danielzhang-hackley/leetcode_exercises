from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        new_subsets = self.subsets(nums[:-1])
        for i in range(len(new_subsets)):
            new_subsets.append(new_subsets[i] + [nums[-1]])
        return new_subsets

print('\033c')
print(Solution().subsets([1, 2, 3]))