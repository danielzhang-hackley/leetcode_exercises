class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0, 0]

        # if row to col is palindrome
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(dp)):
            dp[i][i] = True

        for i in range(len(dp) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]
        
        for diff in range(2, len(dp)):
            for i in range(len(s)-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]

        return s[ans[0]:ans[1]+1]
    
print('\033c')
print(Solution().longestPalindrome('babad'))