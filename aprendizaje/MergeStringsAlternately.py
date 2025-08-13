class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        word =""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            word += word1[i] + word2[j]
            i += 1
            j += 1
        word += word1[i:] + word2[j:]
        return word

print(Solution().mergeAlternately("abc","pqr"))