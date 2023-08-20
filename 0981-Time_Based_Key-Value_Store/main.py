class TimeMap:

    def __init__(self):
        # rows are keys, columns are times
        self.times = []
        self.key_to_idx = {}
        self.table = [[]]

    def binary_search(self, x):
        """
        binary search, but return idx of largest element that is smaller than target
        if target is not in the array

        array is strictly increasing
        """
        
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
        self.times.append(timestamp)
        # add new timestamp
        for row in self.table:
            row.append(False)

        if key not in self.key_to_idx:
            self.table.append([False for _ in range(len(self.table[0]))])
            self.key_to_idx[key] = len(self.table)-1
        
        self.table[self.key_to_idx[key]][-1] = value


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_idx:
            return ""
        
        time_idx = self.binary_search(timestamp)

        return self.table[self.key_to_idx[key]][time_idx] if self.table[self.key_to_idx[key]][time_idx] else ""
    

print('\033c')
timeMap = TimeMap()
print(timeMap.set("foo", "bar", 1))  # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))         # return "bar"
print(timeMap.get("foo", 3))         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
print(timeMap.set("foo", "bar2", 4)) # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))         # return "bar2"
print(timeMap.get("foo", 5))         # return "bar2"

print(timeMap.table)
            
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)