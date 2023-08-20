import heapq

class MedianFinder:
    def __init__(self):
        self.lower = []  # max heap (need to negate values)
        self.upper = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.lower:
            self.lower.append(-num)
            return
        
        if len(self.lower) <= len(self.upper):
            if num <= self.upper[0]:
                heapq.heappush(self.lower, -num)
            else:
                heapq.heappush(self.lower, -heapq.heappushpop(self.upper, num))
        else:
            if num >= -self.lower[0]:
                heapq.heappush(self.upper, num)
            else:
                heapq.heappush(self.upper, -heapq.heappushpop(self.lower, -num))


    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper):
            return (-self.lower[0] + self.upper[0]) / 2
        else:
            return -self.lower[0]
        
print(5*"\n")
mf = MedianFinder()
print(mf.addNum(5))
print()
print(mf.addNum(6))
print()
print(mf.findMedian())
print()
print(mf.addNum(7))
print()
print(mf.findMedian())
print()
print(mf.addNum(4))
print(mf.findMedian())
