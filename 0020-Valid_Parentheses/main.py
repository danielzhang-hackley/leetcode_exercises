class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            '(': (0, 1), ')': (0, -1),
            '{': (1, 1), '}': (1, -1),
            '[': (2, 1), ']': (2, -1)
        }

        balance = [0, 0, 0]
        classes = [0, 1, 2]

        for char in s:
            if key[char][1] == -1:
                remain_classes = list(set(classes) - set([key[char][0]]))
                print(remain_classes)
                if balance[remain_classes[0]] != 0 or balance[remain_classes[1]] != 0:
                    return False

            balance[key[char][0]] += key[char][1]

            if balance[key[char][0]] < 0:
                return False

        return balance[0] == balance[1] and balance[1] == balance[2] and balance[2] == 0


solution = Solution()
print(solution.isValid("([)]"))
