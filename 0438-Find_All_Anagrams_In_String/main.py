from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # look for anagrams of p in s
        ans = []
        p_freq = {}
        for char in p:
            if char in p_freq:
                p_freq[char] += 1
            else:
                p_freq[char] = 1

        s_freq = {}
        for char in s[:len(p)]:
            if char in s_freq:
                s_freq[char] += 1
            else:
                s_freq[char] = 1

        for i in range(len(s) - len(p)):
            if s_freq == p_freq:
                ans.append(i)

            s_freq[s[i]] -= 1
            if s_freq[s[i]] == 0:
                del s_freq[s[i]]

            if s[i+len(p)] in s_freq:
                s_freq[s[i+len(p)]] += 1
            else:
                s_freq[s[i+len(p)]] = 1
        
        if s_freq == p_freq: ans.append(len(s) - len(p))

        return ans
    
print('\033c')
print(Solution().findAnagrams(s = "cbaebabacd", p = "abc"))