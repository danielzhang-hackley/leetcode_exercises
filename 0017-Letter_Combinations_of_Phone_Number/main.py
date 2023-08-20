from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keys = {
            "1": " ",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n_trailing = 0
        while len(digits) < 4:
            digits += "1"
            n_trailing += 1
        
        ans = []
        # the number of nested loops is the number of digits
        for a in keys[digits[0]]:
            for b in keys[digits[1]]:
                for c in keys[digits[2]]:
                    for d in keys[digits[3]]:
                        if n_trailing:
                            ans.append((a + b + c + d)[:-n_trailing])
                        else:
                            ans.append(a + b + c + d)

        return ans

print('\033c')
print(Solution().letterCombinations("5678"))