from functools import cache

class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            # base case:
            if i >= len(nums): 
                return 0 if must_pick else -float('inf')
            
            # recursive case
            include_cur =     nums[i] + solve(i+1, True)
            not_include_cur = 0 if must_pick else solve(i+1, False)
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        
        return solve(0, False)
    
print('\033c')
solution = Solution()
print(solution.maxSubArray([5,4,-1,7,8]))