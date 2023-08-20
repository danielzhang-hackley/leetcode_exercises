class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = 0
        length = min(len(a), len(b))
        for i in range(length):
            pos = length - i - 1
            ans += (int(a[pos]) + int(b[pos])) * 2**i
        return ans

print('\033c')
solution = Solution()
a = "1010"
b = "1011"
ans = solution.addBinary(a, b)
print(ans)
print(0b10101)