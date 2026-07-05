class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""

        others = 0
        if len(s) > 1: 
            others = self.lengthOfLongestSubstring(s[1:])

        for char in s:
            if char not in substr: substr += char
            else: break

        return others if others > len(substr) else len(substr)

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
