from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        
        target //= 2

        # each element is a sequence of indices, index of element is sum value
        dp = [set()]

        # i is the intermediate target value
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if 0 <= i - nums[j] < len(dp) and (len(dp[i - nums[j]]) > 0 or i - nums[j] == 0) and \
                   j not in dp[i - nums[j]]:
                    dp.append(dp[i - nums[j]] | {j})
                    break
            else:
                dp.append(set())
        print(dp)
        return len(dp[-1]) > 0
    
print('\033c')
print(Solution().canPartition(nums = [1,5,11,5]))