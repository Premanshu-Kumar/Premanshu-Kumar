class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, depth = [], 0
        for c in s:
            if c == '(' and depth > 0:
                res.append(c)
            elif c == ')' and depth > 1:
                res.append(c)
            depth += 1 if c == '(' else -1
        return "".join(res)
        