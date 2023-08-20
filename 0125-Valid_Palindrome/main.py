class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].casefold() != s[r].casefold():
                return False
            else:
                l += 1
                r -= 1

        return True

solution = Solution()
s = ""
print(solution.isPalindrome(s))