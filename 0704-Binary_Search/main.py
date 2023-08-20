from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)

    def binary_search(self, nums: List[int], target: int, l: int = 0) -> int:
        mid_idx = len(nums) // 2

        if len(nums) <= 1:
            return l if nums[0] == target else -1

        if target == nums[mid_idx]:
            return l + mid_idx
        elif target < nums[mid_idx]:
            return self.binary_search(nums[:mid_idx], target, l)
        else:
            return self.binary_search(nums[mid_idx:], target, l + mid_idx)
