class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}

        for char in s:
            try:
                chars[char] += 1
            except:
                chars[char] = 1

        for char in t:
            try:
                if chars[char] == 0:
                    return False
                chars[char] -= 1
            except:
                return False

        for count in chars.values():
            if count != 0:
                return False

        return True

solution = Solution()
s = "rat"; t = "car"
print(solution.isAnagram(s, t))