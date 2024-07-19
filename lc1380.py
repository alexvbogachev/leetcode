class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = {min(row) for row in matrix}
        cols = {max(col) for col in zip(*matrix)}
        return list(rows & cols)
