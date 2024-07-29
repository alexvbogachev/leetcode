class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        # O(n^2) time complexity
        result, n = 0, len(rating)
        for i, b in enumerate(rating):
            l = sum(a<b for a in rating[:i])
            r = sum(c>b for c in rating[i+1:])
            result += l*r
            result += (i-l)*(n-1-i-r)
        return result
