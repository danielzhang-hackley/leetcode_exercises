class Solution:
    def isValid(self, s: str) -> bool:
        convert = {
            '(': 0, ')': 3,
            '[': 1, ']': 4,
            '{': 2, '}': 5
        }

        open_idx = {0: [-1], 1: [-1], 2: [-1]}

        for i, brac in enumerate(s):
            char = convert[brac]
            if char < 3:
                open_idx[char].append(i)
            else:
                others = list({3, 4, 5} - {char})
                if open_idx[others[0] - 3][-1] >= open_idx[char - 3][-1] or \
                   open_idx[others[1] - 3][-1] >= open_idx[char - 3][-1]:
                    return False
                else:
                    open_idx[char - 3].pop(-1)

        return open_idx == {0: [-1], 1: [-1], 2: [-1]}

solution = Solution()
print(solution.isValid(")(){}"))