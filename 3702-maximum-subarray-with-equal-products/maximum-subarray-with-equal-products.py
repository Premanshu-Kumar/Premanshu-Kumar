from fractions import gcd
class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        for i in range(len(nums)):
            p = g = l = nums[i]
            for j in range(i + 1, len(nums)):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = l * nums[j] // gcd(l, nums[j])
                if p == l * g:
                    ans = max(ans, j - i + 1)
        return ans