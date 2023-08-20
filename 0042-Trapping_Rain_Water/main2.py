from typing import List
from collections import defaultdict

class Solution:
    def trap(self, height: List[int]) -> int:
        def binary_search(arr, x, offset=None):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = (l + r) // 2

                if arr[m] == x:
                    return m
                elif arr[m] < x:
                    l = m + 1
                elif arr[m] > x:
                    r = m - 1

            if not offset:
                return -1
            elif offset == 'left':
                return r
            else:
                return l

        max_height = 0
        h_to_i = defaultdict(list)
        for i in range(len(height)):
            if height[i] > max_height:
                max_height = height[i]
            h_to_i[height[i]].append(i)

        vol = 0
        n_high = 0
        l = len(height) - 1
        r = 0
        for h in range(max_height, 0, -1):
            if h_to_i[h]:
                if h_to_i[h][0] < l: 
                    l = h_to_i[h][0]
                if h_to_i[h][-1] > r: 
                    r = h_to_i[h][-1]
            
            n_high += binary_search(h_to_i[h], r, offset='left' )+1 - \
                      binary_search(h_to_i[h], l, offset='right')

            if n_high > 1:
                vol += r - n_high - l + 1

        return vol
    
print('\n\n\n\n\n\n')
print(Solution().trap([4,2,0,3,2,5]))
#                      0  1  2  3  4  5  6  7  8  9 10 11