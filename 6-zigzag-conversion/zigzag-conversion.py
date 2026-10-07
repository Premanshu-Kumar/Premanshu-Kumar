class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        rows, i, d =[''] * numRows, 0, -1
        for c in s:
            rows[i] += c
            if i in (0, numRows - 1): d = -d
            i += d
        return ''.join(rows)
