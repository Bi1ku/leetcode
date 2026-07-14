class Solution:
    def uniqueOccurrences(self, arr):
        hashmap = {}

        for num in arr:
            if num in hashmap: hashmap[num] += 1
            else: hashmap[num] = 1

        temp = hashmap.values()
        return len(temp) == len(set(temp))
