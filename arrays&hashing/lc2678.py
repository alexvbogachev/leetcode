class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        # Time complexity O(n), space complexity O(1)
        count = 0
        for passenger in details:
            if int(passenger[11:13]) > 60:
                count += 1
        return count
