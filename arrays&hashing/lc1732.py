# Time complexity O(n)
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_val = 0
        alt = 0
        for i in gain:
            alt += i
            if alt > max_val:
                max_val = alt
        return max_val
