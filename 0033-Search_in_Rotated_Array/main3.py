from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check whether to start from left or right
        l = 0
        r = len(nums) - 1
        m = l if nums[l] <= target else r

        start = m

        # search towards the direction you started if you are past the pivot
        while l <= r:
            # print(f"nums[{m}] = {nums[m]}", (l, r))

            if nums[m] == target:
                return m
            
            elif start == len(nums) - 1 and nums[m] > nums[start]:
                l = m+1
            elif start == 0 and nums[start] > nums[m]:
                r = m-1
            
            elif nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1

            m = (l + r) // 2

        return -1


print('\033c')
# print(Solution().search(nums = [4,5,6,7,8,9,1,2,3], target = 9))

nums = [4,5,6,7,8,9,1,2,3]
# """
for i in nums:
    print(Solution().search(nums, i))
# """
