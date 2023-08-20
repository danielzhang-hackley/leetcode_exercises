from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0; r = len(height) - 1

        # for whichever side is shorter, find the next tallest
        # if both sides are the same height, the 

        area = 0
        while l < r:
            area_temp = min(height[l], height[r]) * (r - l)
            if area_temp > area:
                area = area_temp
            
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1; r -= 1
            
        return area
    

print('\033c')
print(Solution().maxArea([1,1]))