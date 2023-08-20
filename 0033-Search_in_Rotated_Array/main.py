from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        save checkpoints in relation to pivot:
        if you move left and numbers increase, 
            then you have crossed pivot; save previous idx
        if you move right and numbers decrease
            then you have crossed pivot; save previous idx


        searched an idx and need a higher number:
            search to right
            if too low, 
                if standard
                    search right
                if passed pivot
                    search back left
            if too high,
                search back left (standard binary)
            
            search to left only if reached rightmost
            and still need higher (roll back to checkpoint,
            or to leftmost if none)


        searched an idx and need a lower number:
            search to left
            if too low,
                search back right (standard binary)
            if too high,
                if standard
                    search left
                if passed pivot
                    search back right

            search to right only if reached leftmost
            and still need lower (roll back to checkpoint,
            or rightmost if none)                             
        """

        # check whether to start from left or right.

        l = 0
        r = len(nums) - 1
        m = (l + r) // 2

        m_prev = m

        while l <= r:
            m = (l + r) // 2

            print(m, m_prev, l, r)
            input()
            if nums[m] == target:
                return m
            
            elif m_prev < m and nums[m_prev] > nums[m]:
                # if we searched to the right (looking for larger than nums[m_prev]) 
                # and the numbers became smaller
                # then search back to the left (we passed the pivot)
                m_prev = m
                r = m-1
            elif m < m_prev and nums[m] > nums[m_prev]:
                # if we searched to the left (looking for smaler than nums[m_prev]) 
                # and the numbers became larger
                # then search back to the right (we passed the pivot)
                m_prev = m
                l = m+1

            elif nums[m] < target:
                m_prev = m
                l = m+1
            elif nums[m] > target:
                m_prev = m
                r = m-1

        return -1


print('\033c')
print(Solution().search(nums = [17,18,19,20,21,0,1,2,3,4,5,6,7,8,9,10,11,12], target = 0))
