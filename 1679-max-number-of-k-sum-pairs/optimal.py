class Solution:
    # This problem is a lot like Two Sum
    def maxOperations(self, nums: List[int], k: int) -> int:
        desires = {} # key: desired number, value: counting number
        operations = 0

        for num in nums:
            if num in desires:
                desires[num] -= 1 # Will always be at the end, doesn't matter the number
                if not desires[num]: del desires[num]
                operations += 1
            
            else:
                target = k - num
                if target in desires: desires[target] += 1
                else: desires[target] = 1

        return operations

        # Runtime: O(n)
        # Spacetime: O(n)
