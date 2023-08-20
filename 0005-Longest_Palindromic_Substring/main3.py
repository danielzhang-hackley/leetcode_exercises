class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(idx):
            # returns length and is_even
            i = idx - 1; j = idx + 1
            len_odd = 1
            while 0 <= i and j < len(s) and s[i] == s[j]:
                len_odd += 2
                i -= 1; j += 1

            i = idx; j = idx + 1
            len_even = 0
            while 0 <= i and j < len(s) and s[i] == s[j]:
                len_even += 2
                i -= 1; j += 1

            if len_odd > len_even:
                return len_odd, False
            else:
                return len_even, True
        
        ans = [0, 0]

        for i in range(len(s) - 1):
            length, is_even = expand(i)
            if length > ans[1] - ans[0] + 1:
                radius = length // 2
                if is_even:
                    ans = [i - radius + 1, i + radius]
                else:
                    ans = [i - radius, i + radius]

        return s[ans[0]: ans[1] + 1]
    
print('\033c')
print(Solution().longestPalindrome('ccc'))
