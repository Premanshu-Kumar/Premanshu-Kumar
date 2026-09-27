class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            for a, b in ((i, i), (i, i + 1)):
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    a, b = a - 1, b + 1
                res = max(res, s[a + 1:b], key=len)
        return res