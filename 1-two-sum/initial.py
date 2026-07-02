from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try: found = nums.index(target - nums[i])
            except: found = -1
            if found != -1 and found != i:
                return [i, found]
        return []

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
