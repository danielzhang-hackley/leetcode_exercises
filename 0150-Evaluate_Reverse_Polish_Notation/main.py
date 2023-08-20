from typing import List
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expr = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }

        for token in tokens:
            if token in ops and expr[-2] not in ops:
                expr[-2] = ops[token](int(expr[-2]), int(expr[-1]))
                expr.pop()
            else:
                expr.append(token)

        return int(expr[0])
    
print('\033c')
solution = Solution()
print(solution.evalRPN(tokens = ["18"]))

