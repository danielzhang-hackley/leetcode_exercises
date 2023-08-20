from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = set()
        for num in nums:
            if num in found:
                return True
            found.add(num)
        return False
