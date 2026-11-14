class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        ans = float('inf')
        for i in range(len(nums)):
            s = 0
            for j in range(i, min(len(nums), i + r)):
                s += nums[j]
                if j - i + 1 >= l and s > 0:
                    ans = min (ans, s)
        return ans if ans != float('inf') else -1