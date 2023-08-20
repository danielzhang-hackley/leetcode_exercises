class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        incu = []
        cand = []
        for char in s:
            if char in cand:
                cand = cand[cand.index(char)+1:]
            
            cand.append(char)
            if len(cand) > len(incu):
                incu = cand

        return len(incu)
    
print('\033c')
solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))

"""

            print(char)
            print(incu)
            print(cand)
            print("*************")
"""