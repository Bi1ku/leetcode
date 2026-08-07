class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = { "a", "e", "i", "o", "u"}

        def count_vowels(s: str) -> int:
            counter = 0

            for c in s:
                if c in vowels: counter += 1

            return counter

        curr_count = max_count = count_vowels(s[:k])

        for i in range(k, len(s)):
            if s[i-k] in vowels: curr_count -= 1
            if s[i] in vowels: curr_count += 1
            if curr_count > max_count: max_count = curr_count

        return max_count

        # Runtime: O(n)
        # Spacetime: O(1)
