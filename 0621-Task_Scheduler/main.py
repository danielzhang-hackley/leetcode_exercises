from typing import List
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {char: 0 for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        max_freq = 0

        for task in tasks:
            freqs[task] += 1
            if freqs[task] > max_freq:
                max_freq = freqs[task]
                
        n_max = 0
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if freqs[char] == max_freq:
                n_max += 1
        
        if (max_freq-1)*(n - n_max + 1) <= len(tasks) - max_freq*n_max:
            return len(tasks)
        
        return (max_freq-1)*(n+1) + n_max

print('\033c')
print(Solution().leastInterval(["A","B","C","D","A","B","V"], n = 3))