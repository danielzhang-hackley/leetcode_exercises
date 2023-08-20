class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = ""

        # if row to col is palindrome
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for j in range(len(dp)):
            for i in range(j+1):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

                if dp[i][j] and j - i + 1 > len(max_length):
                    max_length = s[i:j+1]
                
        return max_length
    
print('\033c')
print(Solution().longestPalindrome('cbbd'))