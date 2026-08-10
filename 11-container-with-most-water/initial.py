class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                y = height[i] if height[i] < height[j] else height[j]
                x = j - i
                if x * y > max_area: max_area = x * y
        return max_area

        # Runtime: O(n^2)
        # Spacetime: O(1)
