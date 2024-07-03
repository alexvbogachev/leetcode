# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(logn) time complexity, O(1) space complexity
        l,h = 1,n
        while True:
            m = (l+h)//2  
            res = guess(m)
            if res > 0:
                l = m + 1
            elif res < 0:
                h = m - 1
            else:
                return m

        #Recursive solution that has too much depth
        # high = n
        # low = 1
        # mid = (high+low)//2
        # pick = 0
        # def binarySearch(high, low, mid):
        #     if guess(mid) == 0:
        #         return mid
        #     if guess(mid) == 1:
        #         low = mid
        #         mid = (high + low)//2
        #         return binarySearch(high, low, mid)
        #     if guess(mid) == -1:
        #         high = mid
        #         mid = (high + low)//2
        #         return binarySearch(high, low, mid)
        # return binarySearch(high, low, mid)
