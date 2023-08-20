from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # recurrence:
        # max(
        #     existing solution (up until first neg after existing solution),
        #     sum of the existing solution plus num with negs in between end of existing solution and num,
        #     the sum of everything after the streak of negs immediately after the existing solution,
        # )

        msum = -float('inf')
        negs = pos = 0

        for num in nums:
            print(msum, '\t', num, '\t', negs, '\t', pos, end='\n')
            if num < 0:
                if num > msum:
                    msum = num
                    continue
                negs += num
                pos = 0
            else:
                pos += num
                temp_max = max(msum, msum + negs + pos, pos)
                if temp_max != msum:
                    negs = pos = 0
                    msum = temp_max
        
        return msum

        
solution = Solution()
print(solution.maxSubArray([8,-19,5,-4,20]))
