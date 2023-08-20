class MedianFinder:
    def __init__(self):
        self.arr = []

    def binary_search(self, x, offset=None):
            l = 0
            r = len(self.arr) - 1

            while l <= r:
                m = (l + r) // 2
                # print((l, m, r), (arr[m], x))

                if self.arr[m] == x:
                    return m
                elif self.arr[m] < x:
                    l = m + 1
                elif self.arr[m] > x:
                    r = m - 1


            if not offset:
                return None
            elif offset == 'left':
                return r
            else:
                return l

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
            return
        
        self.arr.insert(self.binary_search(num, offset='right'), num)


    def findMedian(self) -> float:
        if len(self.arr) % 2 != 0:
            return self.arr[(len(self.arr) - 1) // 2]
        return (self.arr[(len(self.arr) - 1) // 2] + self.arr[len(self.arr) // 2]) / 2