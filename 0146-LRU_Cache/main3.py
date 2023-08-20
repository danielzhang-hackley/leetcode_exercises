class ListNode:
    def __init__(self, val, key, mr=None, lr=None) -> None:
        self.val = val
        self.key = key
        self.mr = mr
        self.lr = lr

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.cache = {}

        self.mr_key = None
        self.lr_key = None
        # hash map where keys are keys and values are nodes in a doubly linked list, with values of value

    def __str__(self):
        return str({key: self.cache[key].val for key in self.cache})

    def update_lr(self, delete=False):
        """
        Turn the 2nd lr node into the lr node and delete original lr if necessary
        """
        old_lr_key = self.lr_key
        self.lr_key = self.cache[self.lr_key].mr.key
        self.cache[self.lr_key].lr = None

        if delete:
            del self.cache[old_lr_key]

    def update_mr(self, new_mr_key):
        """
        Set the new mr node AND update attributes of old mr node
        """
        self.cache[self.mr_key].mr = self.cache[new_mr_key]
        self.cache[new_mr_key].lr = self.cache[self.mr_key]
        self.cache[new_mr_key].mr = None
        self.mr_key = new_mr_key

    def contract(self, key):
        """
        For a the node associated with key, connect the nodes surrounding it
        """
        self.cache[key].lr.mr = self.cache[key].mr
        self.cache[key].mr.lr = self.cache[key].lr

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        if key == self.mr_key:
            return self.cache[key].val
        
        # attach the nodes to the left and right of the one associated with key
        if key == self.lr_key:
            self.update_lr()
        else:
            self.contract(key)

        self.update_mr(key)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:     
        if key == self.mr_key:
            self.cache[key].val = value
            return
        
        if key not in self.cache:
            self.cache[key] = ListNode(value, key, mr=None)
            if len(self.cache) == 1:
                self.cache[key].lr = None
                self.lr_key = key
            else:
                self.cache[key].lr = self.cache[self.mr_key]
                self.cache[key].lr.mr = self.cache[key]

            if len(self.cache) > self.capacity:
                self.update_lr(delete=True)

            self.mr_key = key
            
        else:
            self.cache[key].val = value
            if key == self.lr_key:
                self.update_lr()
            else:
                self.contract(key)

            self.update_mr(key)



print('\033c')

# '''
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
for i in range(len(vals)):
    if len(vals[i]) == 1:
        print(f"get {vals[i]} gives", calls[i](vals[i][0]))
    else:
        print(f"put {vals[i]}")
        calls[i](vals[i][0], vals[i][1])
    print(f"cache is {lrucache}, mr = {lrucache.mr_key}, lr = {lrucache.lr_key}")
    cur = lrucache.cache[lrucache.lr_key]
    while cur:
        print(cur.key, end=', ')
        cur = cur.mr
    print('\n')
# '''

'''
lrucache = LRUCache(2)

print(lrucache.put(2, 1))
print(f'cache is {lrucache}\n')

print(lrucache.put(2, 2))
print(f'cache is {lrucache}\n')

print(lrucache.get(2), end='\n\n')
# print(lrucache.highest)
# print(lrucache.pos_to_key)

print(lrucache.put(1, 1))
print(f'cache is {lrucache}\n')

print(lrucache.put(4, 1))
print(f'cache is {lrucache}\n')

print(lrucache.get(2), end='\n\n')

# '''

'''
lRUCache = LRUCache(2)

print(lRUCache.put(10, 1))  # cache is {10=1}
print(f'cache is {lRUCache}\n')

print(lRUCache.put(20, 2))  # cache is {10=1, 20=2}
print(f'cache is {lRUCache}\n')

print(lRUCache.get(10), end='\n')     # return 1
print(f'cache is {lRUCache}\n')

print(lRUCache.put(30, 3))  # LRU key was 20, evicts key 20, cache is {10=1, 30=3}
print(f'cache is {lRUCache}\n')

print(lRUCache.get(20), end='\n')     # returns -1 (not found)

print(lRUCache.put(40, 4))  # LRU key was 10, evicts key 10, cache is {40=4, 30=3}
print(f'cache is {lRUCache}\n')

print(lRUCache.get(10), end='\n\n')     # return -1 (not found)

print(lRUCache.get(30), end='\n\n')     # return 3

print(lRUCache.get(40), end='\n\n')     # return 4
print(lRUCache)
# '''