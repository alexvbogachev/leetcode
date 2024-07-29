class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # time and space complexity O(n)
        result = []
        for i in s:
            if i == '*':
                result.pop()
            else:
                result.append(i)
        return ''.join(result)
