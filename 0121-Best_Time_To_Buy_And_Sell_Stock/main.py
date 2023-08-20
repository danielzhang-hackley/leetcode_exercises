from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        f is the max profit for x, a subsequnce of prices
        f(x) = max(f(x[:-1]), x[-1] - max(x[:-1]))
        """

        a = [0]
        min_prev = prices[0]

        for i in range(1, len(prices)):
            if prices[i-1] < min_prev:
                min_prev = prices[i-1]
            a.append(max(a[-1], prices[i] - min_prev))

        return a[-1]

solution = Solution()

prices = [7,6,4,3,1]
print(solution.maxProfit(prices))
