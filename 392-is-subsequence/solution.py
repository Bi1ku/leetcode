# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         for right in range(len(t)):
#             if not s: return True
# 
#             if s[0] == t[right]:
#                 s = s[1:] this is O(k) and creates new string each time... inefficient
# 
#         return True if not s else False
# 
#         # Runtime: O(n)
#         # Spacetime: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i == len(s): return True
            
            if s[i] == t[j]:
                i += 1

        return True if i == len(s) else False

        # Runtime: O(n)
        # Spacetime: O(1)
