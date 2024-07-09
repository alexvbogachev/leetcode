class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        curr = 0
        delta = 1

        for _ in range(time):
            curr += delta
            if curr == n:
                curr = n-2
                delta = -1
            elif curr == -1:
                curr = 1
                delta = 1
        return curr + 1
