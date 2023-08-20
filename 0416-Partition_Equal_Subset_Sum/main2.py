from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        
        target //= 2

        # each element is a sequence of indices, index of element is sum value
        dp = {0: set()}

        # i is the intermediate target value
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i - nums[j] in dp and j not in dp[i - nums[j]]:
                    dp[i] = (dp[i - nums[j]] | {j})
                    break
        return target in dp
    
print('\033c')
print(Solution().canPartition(nums = [1,5,11,5]))