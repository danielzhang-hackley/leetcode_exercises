class TimeMap:
    def __init__(self):
        # rows are times, columns are keys
        self.times = []
        self.key_to_idx = {}
        self.table = [[]]

    def binary_search(self, x):
        l = 0
        r = len(self.times) - 1

        while l <= r:
            m = (l + r) // 2
            if self.times[m] == x:
                return m
            if self.times[m] > x:
                r = m-1
            else:
                l = m+1

        return r

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add new key if needed
        if key not in self.key_to_idx:
            for row in self.table:
                row.append(False)
            self.key_to_idx[key] = len(self.table[0]) - 1

        # add new timestamp
        self.times.append(timestamp)
        if not (len(self.table) == 1 and not self.table[0][0]):
            self.table.append([False for _ in range(len(self.table[0]))])
        
        self.table[-1][self.key_to_idx[key]] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_idx:
            return ""
        
        time_idx = self.binary_search(timestamp)

        if self.times[time_idx] <= timestamp:
            return self.table[time_idx][self.key_to_idx[key]] if self.table[time_idx][self.key_to_idx[key]] else ""
        
        return ""


print('\033c')

# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

timeMap = TimeMap()
print(None)
print(timeMap.set("love", "high", 10))
print(timeMap.set("love", "low", 20))
print(timeMap.get("love", 5))
print(timeMap.table, timeMap.times)
# print(timeMap.get("love", 10))
# print(timeMap.get("love", 15))
# print(timeMap.get("love", 20))
# rint(timeMap.get("love", 25))