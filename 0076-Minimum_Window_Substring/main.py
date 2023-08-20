from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s is big string, t is requirements for substring of s
        """

        # s = bab______aba
        # t = aab

        s_freqs = defaultdict(int)
        t_freqs = defaultdict(int)  # first is spec, second is observed

        start_idx = -1

        for char in t:
            t_freqs[char] += 1

        for i in range(len(s)):
            s_freqs[s[i]] += 1
            if t_freqs[s[i]] != 0:
                start_idx = i
                break

        ans = s
        i = j = start_idx
        wind_freq = defaultdict(int)
        wind_freq[s[i]] = 1
        while i <= j < len(s):
            
            # increment j if wind_freq[s[i]] < max
            
            # increment i if wind_freq[s[i]] >= max


        return ans