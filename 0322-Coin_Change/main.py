from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = []  # index is amount, value is number of coins

        for i in range(amount + 1):
            cands = [10001]
            for coin in coins:
                if coin == len(dp):
                    dp.append(1)
                    break
                elif coin < len(dp):
                    cands.append(dp[i - coin] + 1)
            else:
                dp.append(min(cands))
                
        return dp[-1] if dp[-1] < 10001 else -1
    
print('\033c')
solution = Solution()
print(solution.coinChange(coins = [1], amount = 0))