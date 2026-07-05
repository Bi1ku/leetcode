class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}

        if not s: return 0
        best, start, end = 0, 0, 0

        for i, char in enumerate(s):
            window = s[start:end]

            if char in window:
                start = hashmap[char] + 1
                del hashmap[char]

            end += 1
            hashmap[char] = i

            if end - start > best:
                best = end - start

        return best

sol = Solution()
print(sol.lengthOfLongestSubstring("bbtablud"))
