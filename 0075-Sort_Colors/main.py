from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        val_to_idx = {0:-1, 1:-1, 2:-1}

        for i in range(len(nums)):
            nums[val_to_idx[nums[i]] + 1] = nums[i]
            val_to_idx[nums[i]] += 1
            for j in range(nums[i] + 1, 3):
                val_to_idx[j] += 1
                if val_to_idx[j] > val_to_idx[j-1]:
                    nums[val_to_idx[j]] = j

print('\033c')
x = [2,0,2,1,1,0]
print(Solution().sortColors(x))
print(x)