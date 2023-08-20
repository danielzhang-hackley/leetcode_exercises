from math import sqrt

class Solution:
    def climbStairs(self, n: int) -> int:
        r5 = sqrt(5)
        return round(((r5 + 1) / (2*r5)) * ((1 + r5) / 2)**n + \
                     ((r5 - 1) / (2*r5)) * ((1 - r5) / 2)**n)
    
solution = Solution()
print(solution.climbStairs(2))