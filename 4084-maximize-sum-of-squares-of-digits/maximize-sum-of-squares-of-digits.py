class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > 9 * num:
            return ""
        q, r = divmod(sum, 9)
        if r > 0:
            return "9" * q + str(r) + "0" * (num - q - 1)
        else :
            return "9" * q + "0" * (num - q)