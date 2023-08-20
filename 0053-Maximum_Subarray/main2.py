from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum = -10001
        cand = 0

        for num in nums:
            cand += num
            if cand > msum:
                msum = cand
            if cand < 0:
                cand = 0

        return msum

print('\033c')
solution = Solution()
print(solution.maxSubArray([-3, -2, -1]))
