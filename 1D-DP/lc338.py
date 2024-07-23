class Solution(object):
    def countBits(self, n):
        # O(n) space and time complexity
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i & 1)

        return ans
