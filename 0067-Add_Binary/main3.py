class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 and j >= 0:
            bit_sum = carry + int(a[i]) + int(b[j])

            if bit_sum >= 2:
                carry = 1
                bit_sum -= 2
            else:
                carry = 0

            ans = str(bit_sum) + ans
            i -= 1
            j -= 1

        remain, idx = (b, j) if j >= 0 else (a, i)
        while idx >= 0:
            bit_sum = carry + int(remain[idx])

            if bit_sum >= 2:
                carry = 1
                bit_sum -= 2
            else:
                carry = 0

            ans = str(bit_sum) + ans
            idx -= 1

        if carry != 0:
            ans = str(carry) + ans

        return ans


print('\033c')
solution = Solution()
a = "11"; b = "11"
print(solution.addBinary(a, b))
