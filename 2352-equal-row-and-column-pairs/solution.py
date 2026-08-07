class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = {}
        for  i in range(len(grid)):
            key = tuple([row[i] for row in grid])
            if key in columns: columns[key] += 1
            else: columns[key] = 1

        pairs = 0
        for row in grid:
            if tuple(row) in columns:
                pairs += columns[tuple(row)]
        
        return pairs

        # Runtime: O(n^2)
        # Spacetime: O(n^2)

'''
[3, 1, 2, 2]
[1, 4, 4, 4]
[2, 4, 2, 2]
[2, 5, 2, 2]

1: [3, 1, 2, 2]
2: [2, 4, 2, 2]
3:  [2, 4, 2, 2]

^ Double column edge case... needed to convert from set to hashmap
'''
