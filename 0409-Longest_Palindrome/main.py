class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        counts = {}

        for char in s:
            try:
                counts[char] += 1
            except:
                counts[char] = 1

            if counts[char] % 2 == 0:
                length += 2

        if len(s) > length:
            length += 1

        return length

solution = Solution()
print(solution.longestPalindrome("a"))