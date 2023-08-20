from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        temp_vol = 0

        l = r = 0
        # update l when there is a higher block?
        while l <= r < len(height):
            if height[r] <= height[r-1]:
                temp_vol += height[l]-height[r]
                r += 1
            else:
                pass



        return 0