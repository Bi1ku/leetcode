class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        desires = {} # key: desired number, value: [indices]
        pointer, operations = 0, 0

        while pointer < len(nums):
            if nums[pointer] in desires:
                partner = desires[nums[pointer]].pop()
                if not desires[nums[pointer]]: del desires[nums[pointer]]

                nums.pop(partner)
                nums.pop(pointer - 1) # items shifted one to the left
                operations += 1
                pointer -= 1 # - 2 + 1 = -1
            
            else:
                target = k - nums[pointer]
                if target in desires: desires[target].append(pointer)
                else: desires[target] = [pointer]
                pointer += 1

        return operations

        # Runtime: O(n^2) .pop() operation is O(n)
        # Spacetime: O(n) => O(n) + O(n) + O(1) = O(n)
        # Solution doesn't exactly work because you don't account for shifts after storing in indices

# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         desires = {} # key: desired number, value: [indices]
#         pointer, operations = 0, 0
# 
#         while pointer < len(nums):
#             if nums[pointer] in desires:
#                 desires[nums[pointer]].pop() # Will always be at the end, doesn't matter the number
#                 if not desires[nums[pointer]]: del desires[nums[pointer]]
#                 operations += 1
#                 pointer += 1
#             
#             else:
#                 target = k - nums[pointer]
#                 if target in desires: desires[target].append(pointer)
#                 else: desires[target] = [pointer]
#                 pointer += 1
# 
#         return operations
# 
#         # Runtime: O(n)
#         # Spacetime: O(n) => O(n) + O(n) + O(1) = O(n)
#         # This version actually works
