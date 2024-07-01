# Space complexity O(1), time complexity O(mn) where m is the loger input string and n is the shorter one. Uses the euclidean approach, can also be approached recursively.
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # no GCD case
        if str1+str2 != str2+str1:
            return ""
        
        #GCD helper method
        def gcd(a,b):
            while b:
                a, b = b, a % b
            return a
        
        return str1[:gcd(len(str1), len(str2))]
