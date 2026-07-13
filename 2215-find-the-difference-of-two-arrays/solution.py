class Solution:
    def findDifference(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        output = [set(), set()]

        for num in nums1:
            if num not in set2:
                output[0].add(num)

        for num in nums2:
            if num not in set1:
                output[1].add(num)

        return [list(output[0]), list(output[1])]

sol = Solution()
print(sol.findDifference([1, 2, 3], [2, 4, 6]))
