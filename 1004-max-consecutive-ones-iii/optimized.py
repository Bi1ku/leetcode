# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         curr_ones = max_ones = left = right = 0
#         thresh = k
# 
#         while right < len(nums):
#             if nums[right] == 1: 
#                 curr_ones += 1
#                 
#             elif thresh > 0: 
#                 thresh -= 1
#                 curr_ones += 1
# 
#             else:
#                 curr_ones -= 1
#                 if nums[left] == 0: thresh += 1
#                 left += 1
#                 continue;
# 
#             if curr_ones > max_ones: max_ones = curr_ones
#             right += 1
# 
#         return max_ones

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr_ones = max_ones = num_zeros = left = right = 0

        while right < len(nums):
            if nums[right] == 1:
                curr_ones += 1

            elif nums[right] == 0 and num_zeros < k:
                curr_ones += 1
                num_zeros += 1

            else:
                if nums[left] == 0: num_zeros -= 1; curr_ones -= 1
                elif nums[left] == 1: curr_ones -= 1
                left += 1
                continue
            
            if curr_ones > max_ones: max_ones = curr_ones
            right += 1

        return max_ones

    # Runtime: O(n)
    # Spacetime: O(1)
