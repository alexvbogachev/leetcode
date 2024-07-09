class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def helper(n,k):
            if n == 1:
                return 0
            return (helper(n-1,k)+k) % n

        return helper(n,k)+1
