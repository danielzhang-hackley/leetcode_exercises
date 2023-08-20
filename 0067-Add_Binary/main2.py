class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0

        for i in range(min(len(a), len(b)) - 1, -1, -1):
            bit_sum = carry
            if i < len(a):
                bit_sum += int(a[i])
            if i < len(b):
                bit_sum += int(b[i])

            if bit_sum >= 2:
                carry = 1
                bit_sum -= 2
            else:
                carry = 0

            ans = str(bit_sum) + ans

        if carry != 0:
            ans = str(carry) + ans

        return ans

solution = Solution()
a = "11"; b = "1"
print(solution.addBinary(a, b))
