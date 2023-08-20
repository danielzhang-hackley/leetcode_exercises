from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_intervals = [intervals[0]]

        for interval in intervals[1:]:
            if new_intervals[-1][1] < interval[0]:
                new_intervals.append(interval)
            else:
                new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])

        return new_intervals
    
print('\033c')
print(Solution().merge([[1,4]]))