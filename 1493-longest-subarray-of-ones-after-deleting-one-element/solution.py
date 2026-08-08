class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = max_ones = curr_ones = 0
        deleted = False

        for right in range(len(nums)):
            if nums[right] == 1:
                curr_ones += 1
            
            elif nums[right] == 0 and not deleted:
                deleted = True
            
            else:
                while nums[left] == 1: curr_ones -= 1; left += 1 # O(2n)
                if nums[left] == 0: left += 1
            
            if curr_ones > max_ones: max_ones = curr_ones

        return max_ones if deleted else max_ones - 1

        # Runtime: O(n)
        # Spacetime: O(1)
