from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check whether to start from left or right
        l = 0
        r = len(nums) - 1

        m = l if nums[l] <= target else r
        m_prev = m

        while l <= r:
            print(m, m_prev, l, r)
            input()
            if nums[m] == target:
                return m
            
            elif m_prev < m and nums[m_prev] > nums[m] and nums[m_prev] < target:
                # if we searched to the right while looking for larger than nums[m_prev]
                # and the numbers became smaller
                # then search back to the left (we passed the pivot)
                print('here 1')
                m_prev = m
                r = m-1
            elif m < m_prev and nums[m] > nums[m_prev] and nums[m_prev] > target:
                # if we searched to the left while looking for smaller than nums[m_prev]
                # and the numbers became larger
                # then search back to the right (we passed the pivot)
                print('here 2')
                m_prev = m
                l = m+1

            # standard binary search cases
            elif nums[m] < target:
                m_prev = m
                l = m+1
            elif nums[m] > target:
                m_prev = m
                r = m-1

            m = (l + r) // 2

        return -1


print('\033c')
print(Solution().search(nums = [4,5,6,7,8,9,1,2,3], target = 1))

nums = [4,5,6,7,8,9,1,2,3]
"""
for i in nums:
    print(Solution().search(nums, i))
# """
