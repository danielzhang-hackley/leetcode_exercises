# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1

        l = 1
        r = n

        while l <= r:
            mid = (l + r) // 2

            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                r = mid - 1
            else:  #  not isBadVersion()
                l = mid + 1

        return -1