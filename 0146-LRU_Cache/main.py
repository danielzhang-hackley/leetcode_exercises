from collections import defaultdict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.cache = defaultdict(lambda: -1)

        self.highest = 0
        self.lowest = 0
        self.key_to_pos = {}
        self.pos_to_key = {}  # position 0 is most recent

    def get(self, key: int) -> int:
        if self.cache[key] == -1:
            del self.cache[key]
            return -1

        if self.key_to_pos[key] != self.highest:    
            self.highest += 1

            del self.pos_to_key[self.key_to_pos[key]]  # delete position currently associated with key
            self.pos_to_key[self.highest] = key
            self.key_to_pos[key] = self.highest
        
        return self.cache[key]

    def put(self, key: int, value: int) -> None:     
        if self.cache[key] != -1 and self.key_to_pos[key] == self.highest:
            self.cache[key] = value
        else:
            if self.cache[key] != -1:
                del self.pos_to_key[self.key_to_pos[key]]  # delete position currently associated with key
            del self.cache[key]

            self.highest += 1

            self.pos_to_key[self.highest] = key
            self.key_to_pos[key] = self.highest

            self.cache[key] = value

            # print(self.pos_to_key, len(self.cache), self.cache)
            if len(self.cache) > self.capacity:
                del self.cache[self.pos_to_key[self.highest - self.capacity]]
                del self.key_to_pos[self.pos_to_key[self.highest - self.capacity]]
                del self.pos_to_key[self.highest - self.capacity]


print('\033c')

lrucache = LRUCache(10)
calls = [lrucache.put,lrucache.put,lrucache.put,lrucache.put,lrucache.put,lrucache.get,
         lrucache.put,lrucache.get,lrucache.get,lrucache.put,lrucache.get,lrucache.put,
         lrucache.put,lrucache.put,lrucache.get,lrucache.put,lrucache.get,lrucache.get,
         lrucache.get,lrucache.get,lrucache.put,lrucache.put,lrucache.get,lrucache.get,
         lrucache.get,lrucache.put,lrucache.put,lrucache.get,lrucache.put,lrucache.get,
         lrucache.put,lrucache.get,lrucache.get,lrucache.get,lrucache.put,lrucache.put,
         lrucache.put,lrucache.get,lrucache.put,lrucache.get,lrucache.get,lrucache.put,
         lrucache.put,lrucache.get,lrucache.put,lrucache.put,lrucache.put,lrucache.put,
         lrucache.get,lrucache.put,lrucache.put,lrucache.get,lrucache.put,lrucache.put,
         lrucache.get,lrucache.put,lrucache.put,lrucache.put,lrucache.put,lrucache.put,
         lrucache.get,lrucache.put,lrucache.put,lrucache.get,lrucache.put,lrucache.get,
         lrucache.get,lrucache.get,lrucache.put,lrucache.get,lrucache.get,lrucache.put,
         lrucache.put,lrucache.put,lrucache.put,lrucache.get,lrucache.put,lrucache.put,
         lrucache.put,lrucache.put,lrucache.get,lrucache.get,lrucache.get,lrucache.put,
         lrucache.put,lrucache.put,lrucache.get,lrucache.put,lrucache.put,lrucache.put,
         lrucache.get,lrucache.put,lrucache.put,lrucache.put,lrucache.get,lrucache.get,
         lrucache.get,lrucache.put,lrucache.put,lrucache.put,lrucache.put,lrucache.get,
         lrucache.put,lrucache.put,lrucache.put,lrucache.put,lrucache.put,lrucache.put,
         lrucache.put]
vals = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],
        [7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],
        [12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],
        [5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],
        [3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],
        [2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],
        [9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
for i in range(len(calls)):
    try:
        print(f"put {vals[i]}", calls[i](vals[i][0], vals[i][1]))
    except IndexError:
        print(f"get {vals[i]}", calls[i](vals[i][0]))
    print(str(lrucache.cache)[75:-1], lrucache.key_to_pos, lrucache.pos_to_key)
    print()

'''
lrucache = LRUCache(2)

print(lrucache.put(2, 1))
print(f'cache is {lrucache.cache}\n')

print(lrucache.put(2, 2))
print(f'cache is {lrucache.cache}\n')

print(lrucache.get(2), end='\n\n')
# print(lrucache.highest)
# print(lrucache.pos_to_key)

print(lrucache.put(1, 1))
print(f'cache is {lrucache.cache}\n')

print(lrucache.put(4, 1))
print(f'cache is {lrucache.cache}\n')

print(lrucache.get(2), end='\n\n')

# '''

'''
lRUCache = LRUCache(2)

print(lRUCache.put(10, 1))  # cache is {10=1}
print(f'cache is {lRUCache.cache}\n')

print(lRUCache.put(20, 2))  # cache is {10=1, 20=2}
print(f'cache is {lRUCache.cache}, pos -> key is {lRUCache.pos_to_key}\n')

print(lRUCache.get(10), end='\n')     # return 1
print(f'cache is {lRUCache.cache}, pos -> key is {lRUCache.pos_to_key}\n')

print(lRUCache.put(30, 3))  # LRU key was 20, evicts key 20, cache is {10=1, 30=3}
print(f'cache is {lRUCache.cache}, pos -> key is {lRUCache.pos_to_key}\n')

print(lRUCache.get(20), end='\n')     # returns -1 (not found)
print(lRUCache.pos_to_key, end='\n\n')

print(lRUCache.put(40, 4))  # LRU key was 10, evicts key 10, cache is {40=4, 30=3}
print(f'cache is {lRUCache.cache}\n')

print(lRUCache.get(10), end='\n\n')     # return -1 (not found)

print(lRUCache.get(30), end='\n\n')     # return 3

print(lRUCache.get(40), end='\n\n')     # return 4
print(lRUCache.cache)
print(lRUCache.key_to_pos)
print(lRUCache.pos_to_key)
# '''