from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        for char in t:
            if char in t_freq:
                t_freq[char] += 1
            else:
                t_freq[char] = 1

        ans = s + " "
        n_satisfied = 0
        wind_freq = defaultdict(int)

        wind_freq[s[0]] += 1
        if wind_freq[s[0]] == t_freq.get(s[0], 0):
            n_satisfied += 1

        i = j = 0
        while i < len(s) - 1 and not (n_satisfied < len(t_freq) and j >= len(s) - 1):
            # string from i to j, inclusive both
            if n_satisfied < len(t_freq):
                j += 1
                wind_freq[s[j]] += 1
                if wind_freq[s[j]] == t_freq.get(s[j], 0):
                    n_satisfied += 1
            else:
                # check if the new string is optimal, find more optimal
                if len(s[i:j+1]) < len(ans):
                    ans = s[i:j+1]
                i += 1
                wind_freq[s[i-1]] -= 1
                if wind_freq[s[i-1]] == t_freq.get(s[i-1], 0) - 1:
                    n_satisfied -= 1
        
        if n_satisfied == len(t_freq) and len(s[i:j+1]) < len(ans):
            ans = s[i:j+1]

        if len(ans) < len(s) + 1:
            return ans

        return ans if n_satisfied == len(t_freq) else ""
    
print('\033c')
print('buffer')
print(Solution().minWindow(s = "abc", t = "abc"))