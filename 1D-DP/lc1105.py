class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        # Time complexity O(n^2), space complexity O(n)
        dp = [0] + [float('inf')] * len(books)
        for i in range(len(books)):
            sumT = 0
            maxH = 0
            for j in range(i, -1, -1):
                t, h = books[j]
                sumT += t
                if sumT > shelfWidth:
                    break
                maxH = max(maxH, h)
                dp[i + 1] = min(dp[i + 1], dp[j] + maxH)
        return dp[-1]
