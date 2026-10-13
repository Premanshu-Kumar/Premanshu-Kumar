class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sq = sorted(x * x for x in nums)
        m = len(nums) // 2
        return sum(sq[m:]) - sum(sq[:m])