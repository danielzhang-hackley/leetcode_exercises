from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def binary_search(arr: List[List[int]], x: int):
            # """
            # returns (idx, in) where idx is the index where x would fit, and in is if
            # x is in any of the existing intervals
            # """
            l = 0
            r = len(arr) - 1
            mid = (l + r) // 2
            while l <= r:
                if arr[mid][0] <= x <= arr[mid][1]:
                    return mid, True
                if arr[mid][0] > x:
                    if mid > 0 and arr[mid - 1][1] < x:
                        return mid, False
                    r = mid - 1
                else:
                    if mid < len(arr) - 1 and arr[mid + 1][0] > x:
                        return mid + 1, False
                    l = mid + 1
                mid = (l + r) // 2
            return l, False

        l, l_in = binary_search(intervals, newInterval[0])
        r, r_in = binary_search(intervals, newInterval[1])

        to_ins = [newInterval[0] if not l_in else intervals[l][0],
                  newInterval[1] if not r_in else intervals[r][1]]
        
        if r_in:
            intervals = intervals[:l] + intervals[r+1:]
        else:
            intervals = intervals[:l] + intervals[r:]

        intervals.insert(l, to_ins)

        return intervals

print('\033c')
solution = Solution()
print(solution.insert(intervals = [[1,2]], newInterval = [0,0]))
