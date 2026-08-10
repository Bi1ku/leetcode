class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # nums = [1, 0, 3, 4, 0, 8]
        left  = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left] # skips the need for a temp variable
                left += 1
            
        # Runtime: O(n)
        # Spacetime: O(1)
