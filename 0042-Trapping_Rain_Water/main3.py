from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # max height the water can reach at any given index
        l = []
        r = []

        lmax = 0
        for h in height:
            if h > lmax:
                lmax = h
            l.append(lmax)
        rmax = 0
        for h in height[::-1]:
            if h > rmax:
                rmax = h
            r.append(rmax)

        print(f"{l}\n{r}")

        vol = 0
        for i in range(len(l)):
            # print(min(l[i], r[len(r) - i - 1]) - height[i])
            vol += min(l[i], r[len(r) - i - 1]) - height[i]

        return vol
    
print(5*"\n")
print(Solution().trap([4,2,0,3,2,5]))
