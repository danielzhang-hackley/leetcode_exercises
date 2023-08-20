from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        fix = 1
        for num in nums[:-1]:  
            fix *= num
            ans.append(fix)

        fix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= fix
            fix *= nums[i]

        return ans
    
print('\033c')
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
# [24,12,8,6]
