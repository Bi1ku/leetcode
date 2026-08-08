class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr_ones = max_ones = left = right = 0
        thresh = k

        while right < len(nums):
            if nums[right] == 1: 
                curr_ones += 1
                
            elif thresh > 0: 
                thresh -= 1
                curr_ones += 1

            else:
                curr_ones = 0
                thresh = k
                left += 1
                right = left
                continue;

            if curr_ones > max_ones: max_ones = curr_ones
            right += 1

        return max_ones
