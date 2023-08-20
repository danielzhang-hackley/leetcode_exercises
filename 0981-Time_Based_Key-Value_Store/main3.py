from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def binary_search(self, arr, x):
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            if arr[m][0] == x:
                return m
            if arr[m][0] > x:
                r = m-1
            else:
                l = m+1

        return r

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        time_idx = self.binary_search(self.data[key], timestamp)

        if self.data[key][time_idx][0] <= timestamp:
            return self.data[key][time_idx][1]
        
        return ""


print('\033c')

# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

timeMap = TimeMap()
print(None)
print(timeMap.set("love", "high", 10))
print(timeMap.set("love", "low", 20))
print(timeMap.get("love", 5))
print(timeMap.get("love", 10))
print(timeMap.get("love", 15))
print(timeMap.get("love", 20))
print(timeMap.get("love", 25))