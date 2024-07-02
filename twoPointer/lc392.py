#Time complexity O(n), space complexity O(1)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        j = 0
        for l in t:
            if j == n:
                return True
            if l == s[j]:
                j += 1
        return j == n
