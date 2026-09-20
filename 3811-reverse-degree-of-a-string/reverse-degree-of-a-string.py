class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum((ord('z') - ord(char) + 1) * i for i, char in enumerate(s, 1))