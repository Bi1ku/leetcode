class Solution(object):
    def mergeAlternately(self, word1, word2):
        len_word1, len_word2 = len(word1), len(word2)
        res = ""

        for i in range(len_word1 if len_word1 > len_word2 else len_word2):
            if i < len_word1 and i < len_word2:
                res += word1[i] + word2[i]
            elif i < len_word2:
                res += word2[i]
            else:
                res += word1[i]

        return res



