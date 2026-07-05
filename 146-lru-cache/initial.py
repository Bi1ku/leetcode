class LRUCache:
    def __init__(self, capacity: int):
        # track the key
        # track a number to see most recently performed operation
        # max number of keys/elements = capacity
        self.operation = 1
        self.lru_tracker = {} 

        self.values = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.values: return -1
        self.operation += 1
        self.lru_tracker[key] = self.operation
        return self.values[key]
        
    def put(self, key: int, value: int) -> None:
        if len(self.lru_tracker) + 1 > self.capacity and key not in self.lru_tracker:
            minimum = 999
            min_key = 0
            for k, v in self.lru_tracker.items():
                if minimum > v:
                    minimum = v
                    min_key = k

            del self.lru_tracker[min_key]
            del self.values[min_key]

        self.values[key] = value
        self.lru_tracker[key] = self.operation
        self.operation += 1

lRUCache = LRUCache(2);
lRUCache.put(1, 1);
lRUCache.put(2, 2); 
print(lRUCache.get(1));    
lRUCache.put(3, 3); 
print(lRUCache.get(2));    
lRUCache.put(4, 4); 
print(lRUCache.get(1));    
print(lRUCache.get(3));    
print(lRUCache.get(4));    

