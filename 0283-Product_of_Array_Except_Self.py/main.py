from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1, nums[0]]
        suffix = [1, nums[-1]]
        for i in range(1, len(nums)-1):
            prefix.append(prefix[i] * nums[i])
            suffix.append(suffix[i] * nums[len(nums) - 1 - i])

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[len(nums) - 1 - i])

        return ans
    
print('\033c')
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
# [24,12,8,6]
# [1, 2, 6, 24]  [4, 12, 24, 24],[24, 24, 12, 4]
# for prefix, prefix starting at 0 and ending at i
# for suffix, suffix starting at i and ending at -1
# [(1) * 24, 1 * 12, 2 * 4, 6 * (1)]
# [(1), 1, 2, 6] * [24, 12, 4, (1)]
# [(1), 4, 12, 24]
# remove last prefix, remove first suffix
