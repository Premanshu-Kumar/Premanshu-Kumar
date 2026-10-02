class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return [""]
        return [
            "(" + a + ")" + b
            for i in range(n)
            for a in self.generateParenthesis(i)
            for b in self.generateParenthesis(n-1-i)
        ]