class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = set()
        for  i in range(len(grid)):
            columns.add(tuple([row[i] for row in grid]))

        pairs = 0
        for row in grid:
            if tuple(row) in columns: pairs += 1
        
        return pairs

        # Runtime: O(n^2)
        # Spacetime: O(n^2)
