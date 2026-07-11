class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key, self.val, self.next, self.prev = key, val, next, prev

class LRUCache:
    def __init__(self, cap):
        self.cap  = cap 
        self.cache = {} # key: {key: (...), val: (...), next: (...), prev: (...)}

        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key):
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1

    def put(self, key, value):
        if len(self.cache) + 1 > self.cap:
            temp = self.left.next
            self.remove(temp)
            del self.cache[temp.key]

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

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
