class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        best, start, end = 0, 0, 0

        for char in s:
            window = s[start:end]

            if char in window:
                start += window.index(char) + 1

            end += 1

            if end - start > best:
                best = end - start

        return best

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))
