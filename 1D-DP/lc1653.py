class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time complexity O(n), space complexity O(1)
        total = 0
        count = 0
        for c in s:
            if c == 'a':
                total = min(total+1, count)
            else:
                count += 1
        return total
