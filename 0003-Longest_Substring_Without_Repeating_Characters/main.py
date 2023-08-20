class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        incu = set()
        cand = set()
        for char in s:
            if char in cand:
                cand = set(char)
            else:
                cand.add(char)

            if len(cand) > len(incu):
                incu = cand

            print(char)
            print(incu)
            print(cand)
            print("*************")

        return len(incu)
    
print('\033c')
solution = Solution()
print(solution.lengthOfLongestSubstring("dvdf"))
