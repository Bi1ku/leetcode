class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = left = 0
        right = len(height) - 1

        while left != right:
            x, y = right - left, height[left]

            if height[right] < height[left]: 
                y = height[right]
                right -= 1
            else: left += 1

            if x * y > max_area: max_area = x * y
        
        return max_area

        # Runtime: O(n)
        # Spacetime: O(1)
